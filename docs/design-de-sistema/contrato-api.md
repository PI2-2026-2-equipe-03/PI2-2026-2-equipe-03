# Contrato da API

Contrato do backend do TaGravado, alinhado à implementação atual (Fastify + Better Auth + PostgreSQL). A documentação interativa (OpenAPI 3.1) está em `/api-docs` e o JSON em `/api/openapi.json`.

## Mapeamento entre rotas e requisitos funcionais

| Método | Endpoint | Requisito | Acesso | Descrição |
|---|---|---|---|---|
| POST | `/auth/register` | RF-01 | Público | Cadastro de usuário |
| POST | `/auth/login` | RF-02 | Público | Login |
| GET | `/me` | RF-02 | Autenticado | Usuário autenticado e perfil |
| GET | `/admin/metrics` | RF-03 | ADM | Métricas do administrador |
| GET | `/manager/metrics` | RF-04 | CLI/ADM (gestor) | Métricas do gestor |
| POST | `/replays` | RF-05 / RF-09 | CLI/ADM (dono da quadra) | Gera replay e associa quadra, data e horário |
| GET | `/arenas` | RF-06 | Público | Busca de arenas por cidade/nome |
| GET | `/quadras` | RF-06 | Público | Lista de quadras |
| GET | `/replays` | RF-06 | Autenticado | Lista de replays disponíveis |
| GET | `/replays/{id}` | RF-06 | Autenticado | Detalhes do replay |
| GET | `/replays/{id}/download` | RF-06 | Autenticado | Link de download MP4 |
| POST | `/sponsors` | RF-07 | CLI/ADM (gestor) | Cadastro de patrocinador |
| DELETE | `/replays/{id}` | RF-10 | CLI/ADM | Exclusão manual |
| POST | `/auth/forgot-password` | RF-11 | Público | Solicita recuperação de senha |
| POST | `/auth/reset-password` | RF-11 | Público | Redefine a senha |
| POST | `/manager-requests` | RF-12 | Autenticado | Solicita perfil de gestor |
| PATCH | `/manager-requests/{id}` | RF-12 | ADM | Aprova ou rejeita solicitação |

RF-08 (exclusão automática após 7 dias) é executado internamente: rotina diária que marca replays vencidos (`expira_em`, 168 h) como `excluido` e enfileira a exclusão da mídia. Na Vercel, é disparado por `GET /api/cron/expire-replays` (cron às 03:00, protegido por `Authorization: Bearer <CRON_SECRET>`); fora dela, por agendamento interno a cada 24 h.

## Convenções

Todas as rotas usam JSON. Não há prefixo `/api`, exceto as rotas nativas do Better Auth (`/api/auth/*`), `/api/health` e `/api/openapi.json`.

Identificadores são UUID (string), exceto `manager-requests`, cujo `id` é numérico.

Rotas protegidas aceitam token Bearer ou cookie de sessão do Better Auth:

```text
Authorization: Bearer <token>
```

A sessão expira após 30 minutos de inatividade (1800 s); cada requisição autenticada renova o prazo.

Perfis de acesso (`/me`): `ADM` (administrador), `CLI` (cliente/gestor de arena) e `USR` (usuário). Nas respostas de cadastro e login, o campo `role` usa `USER`, `MANAGER` e `ADMIN`.

Formato de erro:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "email: Informe um e-mail válido"
  }
}
```

Códigos usados: `VALIDATION_ERROR`, `UNAUTHENTICATED`, `INCOMPLETE_ACCOUNT`, `FORBIDDEN`, `NOT_FOUND`, `CONFLICT`, `ACCOUNT_LOCKED`, `INVALID_RECOVERY_CODE`, `INTERNAL_ERROR`, `REQUEST_ERROR`.

Erros comuns a rotas protegidas: `401` (sessão ausente, inválida ou expirada por inatividade), `403` (cadastro incompleto, `INCOMPLETE_ACCOUNT`, ou perfil sem permissão, `FORBIDDEN`).

## 1. Cadastrar usuário

### POST /auth/register

Entrada:

```json
{
  "name": "João da Silva",
  "email": "joao@email.com",
  "phone": "85999999999",
  "password": "Senha@2026",
  "confirmPassword": "Senha@2026"
}
```

`confirmPassword` é opcional. E-mail e telefone são normalizados (telefone: 10 a 15 dígitos, sem máscara) e devem ser únicos.

Senha: 8 a 72 caracteres, com maiúscula, minúscula, número e caractere especial.

Sucesso: `201 Created`

```json
{
  "id": "uuid",
  "name": "João da Silva",
  "email": "joao@email.com",
  "emailVerified": false,
  "image": null,
  "createdAt": "2026-09-24T14:00:00Z",
  "updatedAt": "2026-09-24T14:00:00Z",
  "role": "USER"
}
```

Erros: `400` (campos ausentes ou JSON malformado), `409` (e-mail ou telefone já vinculado a uma conta), `422` (senha fraca ou senhas não coincidem).

## 2. Login

### POST /auth/login

Entrada:

```json
{
  "email": "joao@email.com",
  "password": "Senha@2026"
}
```

Sucesso: `200 OK`

```json
{
  "token": "token-de-autenticacao",
  "expiresIn": 1800,
  "user": {
    "id": "uuid",
    "name": "João da Silva",
    "email": "joao@email.com",
    "emailVerified": false,
    "image": null,
    "createdAt": "2026-09-24T14:00:00Z",
    "updatedAt": "2026-09-24T14:00:00Z",
    "role": "USER"
  }
}
```

Erros:

`401`: `E-mail ou senha inválidos`.

`429`: após 5 falhas consecutivas para o mesmo e-mail e IP, o login é bloqueado por 15 minutos, mesmo com a senha correta. A resposta inclui o cabeçalho `Retry-After: 900`.

```json
{
  "error": {
    "code": "ACCOUNT_LOCKED",
    "message": "Conta temporariamente bloqueada por 15 minutos"
  }
}
```

## 3. Usuário autenticado

### GET /me

Requer autenticação.

Sucesso: `200 OK`

```json
{
  "data": {
    "id": "uuid",
    "name": "João da Silva",
    "email": "joao@email.com",
    "role": "USR"
  }
}
```

## 4. Solicitar recuperação de senha

### POST /auth/forgot-password

Entrada:

```json
{ "email": "joao@email.com" }
```

Sucesso: `200 OK` (resposta idêntica para e-mails cadastrados e não cadastrados)

```json
{ "message": "Se o e-mail estiver cadastrado, uma mensagem de recuperação será enviada." }
```

O e-mail contém um token no formato `<uuid>.<código de 6 dígitos>`, válido por 10 minutos. Solicitar novo token invalida os anteriores.

Erros: `400` (e-mail inválido), `429` (limite de 3 solicitações por e-mail e 20 por IP por hora), `503` (serviço de e-mail não configurado ou indisponível).

## 5. Redefinir senha

### POST /auth/reset-password

Entrada:

```json
{
  "token": "uuid.123456",
  "password": "NovaSenha@2026",
  "passwordConfirmation": "NovaSenha@2026"
}
```

Sucesso: `200 OK`

```json
{ "message": "Senha redefinida com sucesso" }
```

Todas as sessões do usuário são encerradas e o contador de falhas de login é zerado.

Erros:

`400`: token ou corpo em formato inválido.

`401`: token inválido, expirado ou já utilizado; ou código incorreto (`INVALID_RECOVERY_CODE`).

`422`: senha fraca, senhas não coincidem ou nova senha igual à anterior.

`429`: após 3 códigos incorretos o token é bloqueado.

As rotas nativas `/api/auth/request-password-reset` e `/api/auth/reset-password` retornam `404` para impedir o contorno desses limites.

## 6. Listar arenas

### GET /arenas

Público. Filtros opcionais: `cidade` e `q` (nome), ambos por correspondência parcial, sem diferenciar maiúsculas/minúsculas.

```text
GET /arenas?cidade=Fortaleza&q=Mendes
```

Sucesso: `200 OK`

```json
{
  "data": [
    {
      "id": "uuid",
      "clienteId": "uuid",
      "nome": "Arena Mendes",
      "cidade": "Fortaleza",
      "endereco": "Av. Nazaré, 100",
      "fotoUrl": null
    }
  ]
}
```

Erro: `400` (parâmetro inválido ou desconhecido).

## 7. Listar quadras

### GET /quadras

Público. Filtros opcionais: `arenaId` (UUID) e `disponivel` (`true` ou `false`).

Sucesso: `200 OK`

```json
{
  "data": [
    {
      "id": "uuid",
      "arenaId": "uuid",
      "nome": "Quadra 01",
      "disponivel": true
    }
  ]
}
```

Erro: `400` (`arenaId` ou `disponivel` inválido).

## 8. Listar replays

### GET /replays

Requer autenticação (qualquer perfil). Retorna apenas replays com status `disponivel` e ainda não expirados, ordenados do mais recente para o mais antigo.

Filtros opcionais: `courtId` (UUID), `city` (parcial), `date` (`AAAA-MM-DD`) e `time` (`HH:MM`).

```text
GET /replays?city=Fortaleza&courtId=<uuid>&date=2026-09-24&time=18:30
```

Sucesso: `200 OK`

```json
{
  "data": [
    {
      "id": "uuid",
      "courtId": "uuid",
      "courtName": "Quadra 01",
      "arenaName": "Arena Mendes",
      "city": "Fortaleza",
      "downloadUrl": "https://.../replay.mp4",
      "recordingDate": "2026-09-24",
      "recordingTime": "18:30:00",
      "status": "disponivel",
      "duration": 30,
      "sponsors": [{ "id": "uuid", "name": "Empresa Exemplo", "imageUrl": "/uploads/p.png" }],
      "createdAt": "2026-09-24T18:30:00Z",
      "expiresAt": "2026-10-01T18:30:00Z"
    }
  ]
}
```

Erro: `400` (filtro inválido).

## 9. Consultar replay específico

### GET /replays/{id}

Requer autenticação. Retorna somente replays `disponivel` e não expirados.

Sucesso: `200 OK`

```json
{
  "data": {
    "id": "uuid",
    "court": { "id": "uuid", "name": "Quadra 01" },
    "city": "Fortaleza",
    "recordedAt": "2026-09-24T21:30:00.000Z",
    "duration": 30,
    "videoUrl": "https://.../replay.mp4",
    "expiresAt": "2026-10-01T21:30:00.000Z"
  }
}
```

Erros: `400` (ID inválido), `401`, `404` (inexistente, expirado, excluído ou ainda pendente).

## 10. Gerar replay

### POST /replays

Requer perfil `CLI` ou `ADM`. Somente o gestor dono da quadra pode acionar a geração (a autorização é por propriedade da quadra, inclusive para administradores).

Entrada:

```json
{ "courtId": "uuid" }
```

Sucesso: `201 Created`

```json
{
  "data": {
    "id": "uuid",
    "courtId": "uuid",
    "downloadUrl": null,
    "recordingDate": "2026-09-24",
    "recordingTime": "18:30:00",
    "status": "pendente",
    "duration": 30,
    "sponsors": [{ "id": "uuid", "name": "Empresa Exemplo", "imageUrl": "/uploads/p.png" }],
    "createdAt": "2026-09-24T18:30:00Z",
    "expiresAt": "2026-10-01T18:30:00Z"
  }
}
```

O replay nasce `pendente`, com `duration` fixa de 30 s, `expiresAt` 168 h após a criação e um snapshot dos patrocinadores da quadra. Ele passa a `disponivel` (com `downloadUrl`) quando o processamento da mídia é concluído.

Status possíveis: `pendente`, `disponivel`, `excluido`.

Erros: `400` (`courtId` inválido ou campos extras, como `duration`), `401`, `403` (quadra de outro gestor), `404` (quadra não encontrada), `409` (menos de 30 s desde o último replay da quadra; acionamentos simultâneos são serializados), `422` (quadra indisponível).

## 11. Baixar replay

### GET /replays/{id}/download

Requer autenticação. Registra um evento de download usado nas métricas.

Sucesso: `200 OK`

```json
{
  "data": {
    "id": "uuid",
    "downloadUrl": "https://.../replay.mp4",
    "fileName": "replay-<id>.mp4",
    "format": "MP4"
  }
}
```

Erros: `400` (ID inválido), `401`, `404` (inexistente, excluído ou expirado), `422` (replay ainda pendente).

## 12. Excluir replay

### DELETE /replays/{id}

Requer perfil `CLI` ou `ADM`. Permitido ao gestor dono da quadra ou a qualquer administrador.

Entrada:

```json
{ "reason": "Solicitação do proprietário" }
```

`reason`: 3 a 500 caracteres.

Sucesso: `200 OK`

```json
{ "message": "Replay excluído com sucesso" }
```

A exclusão é lógica: o status passa a `excluido`, `arquivo_url` é zerado, a mídia entra na fila de exclusão do storage e a ação é registrada em auditoria (usuário e motivo), tudo na mesma transação.

Erros: `400` (ID ou motivo inválido), `401`, `403` (sem permissão), `404` (inexistente, já excluído ou expirado).

## 13. Cadastrar patrocinador

### POST /sponsors

Requer perfil `CLI` ou `ADM` e vínculo com gestor de arena. Só é possível vincular o patrocinador às quadras do próprio gestor.

Entrada:

```json
{
  "name": "Empresa Exemplo",
  "imageUrl": "/uploads/patrocinador.png",
  "duration": 10,
  "value": 500.0,
  "courtIds": ["uuid", "uuid"]
}
```

`name`: 2 a 150 caracteres. `imageUrl`: URL http(s) ou caminho `/uploads/...`. `duration`: inteiro de 1 a 30. `value`: não negativo, até 2 casas decimais. `courtIds`: 1 a 100 UUIDs, sem repetição.

Sucesso: `201 Created`

```json
{
  "id": "uuid",
  "name": "Empresa Exemplo",
  "imageUrl": "/uploads/patrocinador.png",
  "duration": 10,
  "value": 500.0,
  "courtIds": ["uuid", "uuid"]
}
```

Erros: `400` (dados inválidos), `401`, `403` (usuário não é gestor ou quadra de outro gestor), `404` (quadra não encontrada), `409` (patrocinador com o mesmo nome já cadastrado para o gestor, sem diferenciar maiúsculas/minúsculas).

## 14. Métricas do administrador

### GET /admin/metrics

Requer perfil `ADM`.

Sucesso: `200 OK`

```json
{
  "activeUsers": 125,
  "totalCourts": 18,
  "totalReplays": 842,
  "mostAccessedCourts": [
    { "courtId": "uuid", "name": "Quadra 01", "accesses": 320 }
  ]
}
```

`activeUsers`: usuários com sessão válida. `totalReplays`: replays não excluídos e não expirados. `mostAccessedCourts`: até 5 quadras, ordenadas por downloads.

Erros: `401`, `403`.

## 15. Métricas do gestor

### GET /manager/metrics

Requer perfil `CLI` ou `ADM` e vínculo com gestor de arena.

Sucesso: `200 OK`

```json
{
  "totalReplays": 186,
  "totalSponsors": 5,
  "peakHours": [
    { "hour": "19:00", "accesses": 72 }
  ],
  "courts": [
    { "id": "uuid", "name": "Quadra 01", "replays": 120 }
  ]
}
```

`peakHours`: até 5 horários com mais downloads (fuso America/Fortaleza).

Erros: `401`, `403`.

## 16. Solicitar cadastro como gestor

### POST /manager-requests

Requer autenticação.

Entrada:

```json
{
  "cpf": "12345678900",
  "cnpj": "12345678000199",
  "companyName": "Arena Exemplo LTDA",
  "courtQuantity": 2,
  "address": {
    "street": "Rua Principal, 100",
    "neighborhood": "Centro",
    "zipCode": "60000000",
    "city": "Fortaleza",
    "state": "CE"
  }
}
```

`cpf`: 11 dígitos. `cnpj`: opcional, 14 dígitos. `courtQuantity`: inteiro de 1 a 1000. `zipCode`: 8 dígitos. `state`: sigla de 2 letras. Campos extras são rejeitados. A validação é de formato, sem verificação de dígitos.

Sucesso: `201 Created`

```json
{
  "id": 15,
  "userId": "uuid",
  "status": "PENDING",
  "message": "Solicitação enviada. Aguarde a análise dos administradores."
}
```

Erros: `400` (dados inválidos), `401`, `409` (usuário ou documento já vinculado a um gestor, ou solicitação pendente existente).

## 17. Analisar solicitação de gestor

### PATCH /manager-requests/{id}

Requer perfil `ADM`.

Entrada:

```json
{ "status": "APPROVED" }
```

Valores aceitos: `APPROVED` ou `REJECTED`.

Sucesso: `200 OK`

```json
{
  "id": 15,
  "userId": "uuid",
  "status": "APPROVED",
  "message": "Solicitação aprovada com sucesso."
}
```

Na rejeição, a mensagem é `Solicitação rejeitada com sucesso.` A aprovação cria o registro de gestor de arena e promove o perfil do usuário a `CLI`.

Erros: `400` (ID ou status inválido), `401`, `403` (não é administrador), `404` (solicitação não encontrada), `409` (solicitação já analisada).

## Rotas nativas do Better Auth

Expostas em `/api/auth/*` e usadas pelo frontend: `POST /api/auth/sign-in/email`, `POST /api/auth/sign-up/email` (mesmas validações e limites de `/auth/register` e `/auth/login`), `POST /api/auth/sign-out` e `GET /api/auth/get-session`. A alteração de telefone via `update-user` retorna `400`.

## Códigos HTTP utilizados

| Código | Significado |
|---|---|
| 200 | Requisição realizada com sucesso |
| 201 | Recurso criado com sucesso |
| 400 | Dados inválidos, JSON malformado ou campos obrigatórios ausentes |
| 401 | Não autenticado, sessão expirada ou token inválido |
| 403 | Autenticado, mas sem permissão |
| 404 | Recurso não encontrado (inclui expirado ou excluído) |
| 409 | Conflito (duplicidade ou intervalo mínimo entre replays) |
| 422 | Regra de negócio violada (senha, quadra indisponível, replay pendente) |
| 429 | Limite de tentativas ou solicitações excedido |
| 500 | Erro interno do servidor |
| 503 | Serviço dependente não configurado (e-mail) |

## Observações

Os replays permanecem disponíveis por 7 dias (168 h). Após esse prazo, a rotina de retenção marca o replay como `excluido`, zera a URL e enfileira a exclusão do arquivo no storage, com novas tentativas em caso de falha.

Cada replay é vinculado à quadra de origem e registra data e horário da geração.

Rotas auxiliares fora do contrato de negócio: `GET /health` e `GET /api/health`.