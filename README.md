<p align="center">
  <img src="docs/marca/social/readme-banner.png" alt="Repeteco — esse lance merece repeteco" width="640">
</p>

# Repeteco - Sistema de Replay para Quadras Esportivas

> Repositório de documentação do projeto **Repeteco** - reúne o planejamento, a identidade visual e os links para os repositórios técnicos (frontend e backend), onde vivem o código e a execução da aplicação. Trabalho de conclusão do **Projeto Integrador 2 (2026/2) - Equipe 03**, sob orientação do professor Bruno Riccelli.

---

## Sobre o projeto

Nas quadras de esportes de areia, um pedido recorrente dos jogadores é ter acesso aos **replays das câmeras de segurança** para reviver os melhores momentos das partidas. Hoje esse fluxo é manual: o funcionário precisa abrir os arquivos da câmera, localizar o horário do clipe e enviá-lo ao cliente.

**Repeteco** resolve isso com uma aplicação web conteinerizada que, ao pressionar um botão físico instalado na quadra, gera e disponibiliza automaticamente o clipe para download pelo cliente da arena. Numa segunda etapa, o sistema também oferecerá **reserva de horários** das quadras pela mesma plataforma.

**Cliente/Parceiro:** Rennan - Arena Dunnas Beach.

Detalhes completos (requisitos, arquitetura, impacto social, governança) em [`plano-de-projeto.md`](./docs/plano-de-projeto.md).

---

## Repositórios

| Camada | Repositório | Stack |
|---|---|---|
| Frontend (SPA) | [pi2-frontend](https://github.com/PI2-2026-2-equipe-03/pi2-frontend) | React 19 · Vite · Tailwind CSS 4 |
| Backend (API REST) | [pi2-backend](https://github.com/PI2-2026-2-equipe-03/pi2-backend) | Fastify 5 · Prisma 7 · TypeScript |
| Documentação | [PI2-2026-2-equipe-03](https://github.com/PI2-2026-2-equipe-03/PI2-2026-2-equipe-03) | (você está aqui) |

---

## Equipe

<table>
  <tr>
    <td align="center"><a href="https://github.com/KaikMcpe12"><img src="https://github.com/KaikMcpe12.png" width="80" alt="Kaik"/><br/><sub><b>Kaik</b></sub></a><br/>Frontend</td>
    <td align="center"><a href="https://github.com/alanbfx-dev"><img src="https://github.com/alanbfx-dev.png" width="80" alt="Alan"/><br/><sub><b>Alan</b></sub></a><br/>Frontend</td>
    <td align="center"><a href="https://github.com/pedroolivsz"><img src="https://github.com/pedroolivsz.png" width="80" alt="Pedro"/><br/><sub><b>Pedro</b></sub></a><br/>Backend / Infra</td>
    <td align="center"><a href="https://github.com/lucasrds401"><img src="https://github.com/lucasrds401.png" width="80" alt="Lucas"/><br/><sub><b>Lucas</b></sub></a><br/>Backend / Infra</td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/pablocosme"><img src="https://github.com/pablocosme.png" width="80" alt="Pablo"/><br/><sub><b>Pablo</b></sub></a><br/>Backend / Infra</td>
    <td align="center"><a href="https://github.com/CristianoGolDeBiciclceta2018"><img src="https://github.com/CristianoGolDeBiciclceta2018.png" width="80" alt="Kauan"/><br/><sub><b>Anthony</b></sub></a><br/>Análise de requisitos</td>
    <td align="center"><a href="https://github.com/laryssaszz"><img src="https://github.com/laryssaszz.png" width="80" alt="Laryssa"/><br/><sub><b>Laryssa</b></sub></a><br/>Design</td>
    <td align="center"><a href="https://github.com/Rickfarias"><img src="https://github.com/Rickfarias.png" width="80" alt="Rick"/><br/><sub><b>Rick</b></sub></a><br/>QA / Testes</td>
  </tr>
</table>

---

## Roadmap

Milestones acompanhados em [milestones do repositório](https://github.com/PI2-2026-2-equipe-03/PI2-2026-2-equipe-03/milestones).

| Sprint | Foco | Status |
|---|---|---|
| **Sprint 0** | Setup dos repositórios, plano de projeto e governança Git | Concluída |
| **Sprint 1** | Levantamento de requisitos e prototipação inicial | Concluída |
| **Sprint 2** | Implementação inicial do frontend e backend; integração do SPA com a API | Concluída |
| **Sprint 3** | Expansão da API, persistência em Postgres e integração ponta-a-ponta | Concluída |
| **Sprint 4** | Autenticação (Better Auth), matriz de autorização e telas de erro/sem permissão | Concluída |
| **Sprint 5** | Sessão de testes com o cliente, ajustes de UX e priorização dos requisitos restantes | Em andamento |
| **Fase 1 - Planejamento** | Especificação técnica da botoeira física, captura de vídeo (RTSP/DVR) e arquitetura do servidor local | A definir |
| **Fase 2 - Implementação** | Infraestrutura física, cabeamento estruturado e instalação dos painéis na Arena Dunnas Beach | A definir |
| **Fase 3 - Testes** | Testes funcionais, de resiliência e homologação final em campo | A definir |

Acordos de governança (PRs, revisão obrigatória, rastreabilidade de issues) descritos em [`plano-de-projeto.md` §5](./docs/plano-de-projeto.md).

---

## Instalação e execução

Este repositório é só documentação — não há código nem `docker-compose.yml` central aqui. Cada camada vive no seu próprio repositório, com seu próprio Docker Compose, e roda de forma independente.

### Pré-requisitos

- [Docker Engine](https://docs.docker.com/engine/install/) 24+ e [Docker Compose plugin](https://docs.docker.com/compose/install/) v2+ (já vem com Docker Desktop) — se for usar containers
- Node.js 22+ e PostgreSQL 16+ — se for rodar algum dos repositórios nativamente, sem Docker
- Git

### 1. Clonar os repositórios

Cada repositório é autossuficiente, não é mais necessário cloná-los lado a lado:

```bash
git clone https://github.com/PI2-2026-2-equipe-03/pi2-backend.git
git clone https://github.com/PI2-2026-2-equipe-03/pi2-frontend.git
```

### 2. Backend ([pi2-backend](https://github.com/PI2-2026-2-equipe-03/pi2-backend))

```bash
cd pi2-backend
cp .env.example .env
```

Preencha `BETTER_AUTH_SECRET`, que vem vazio. Sem ela, o `docker compose up` falha. Se for expor fora de `localhost`, ajuste também `CORS_ORIGINS` e `BETTER_AUTH_URL`. A referência de todas as variáveis é o `.env.example` do backend.

**Opção A — Docker** (sobe Postgres **e** a API, ambos em containers):

```bash
docker compose up --build
```

**Opção B — Local** (a API roda fora do Docker e lê o `.env`; o `DATABASE_URL` precisa apontar para um PostgreSQL 16+):

```bash
npm ci
docker compose up -d db   # opcional: só o Postgres do compose, em localhost:${POSTGRES_PORT}
npm run dev
```

API em `http://localhost:3000` (no Docker, a porta publicada vem de `BACKEND_PORT`). Health check em `/api/health`.

### 3. Frontend ([pi2-frontend](https://github.com/PI2-2026-2-equipe-03/pi2-frontend))

```bash
cd pi2-frontend
cp .env.example .env
```

**Opção A — Docker:**

```bash
docker compose up --build
```

**Opção B — Local** (requer Node.js 22+):

```bash
npm install
npm run dev
```

Interface em `http://localhost:5173`. O Vite proxia as chamadas `/api` para o backend — por padrão para `http://localhost:3000` (fora de container) ou `http://backend:3000` (quando os dois sobem juntos na mesma rede Docker); ajuste em `API_PROXY_TARGET` se o backend estiver em outro host/porta.

### Troubleshooting

| Sintoma | Causa provável | Ação |
|---|---|---|
| `port is already allocated` em 5173/3000/5432 | Processo do host ocupando a porta | Trocar a porta no `.env` do repositório correspondente (`FRONTEND_PORT`, `BACKEND_PORT`, `POSTGRES_PORT`) |
| Frontend abre mas requests dão CORS error | Chamada direta a `http://localhost:3000` no browser, sem passar pelo proxy do Vite | Garanta `VITE_API_URL=/api` no `.env` do `pi2-frontend` |
| Páginas continuam exibindo dados mock mesmo com a API no ar | `VITE_USE_MOCKS` ficou em `true` | Ajuste para `false` no `.env` do `pi2-frontend` e recrie o container (`docker compose up --build`) |
| API responde mas DB diz "relation does not exist" | Volume do Postgres já existia sem schema | No `pi2-backend`: `docker compose down -v && docker compose up --build` — os scripts em `src/db/init/` só rodam na primeira inicialização do volume |
| Alterações no código não refletem (Docker) | Watcher não detecta mudança | Confirmar bind mount e `CHOKIDAR_USEPOLLING=true` (frontend); reiniciar o serviço |
| Backend reclama de `DATABASE_URL` não definida | `.env` sem o bloco de banco | Copie novamente o `.env.example` do `pi2-backend` |
| `docker compose up` falha com `required variable … is missing a value` | Variável obrigatória ausente ou vazia no `.env` do `pi2-backend` | Preencha a variável indicada na mensagem (ver `.env.example`) |
| Backend não conecta no DB (modo Docker) | Serviço `db` ainda inicializando | O compose usa `depends_on: service_healthy`; se persistir, `docker compose logs db` |
| Precisa resetar tudo | Volumes/imagens corrompidos | `docker compose down -v && docker compose build --no-cache`, no repositório afetado |

Notas de arquitetura de cada serviço (dev/prod, hot reload, etc.) estão como comentários nos respectivos `docker-compose.yml` de cada repositório.

---

## Documentação

- [Plano de Projeto](./docs/plano-de-projeto.md) - contexto, objetivos, papéis e governança.
- [Identidade visual (marca)](./docs/marca/README.md) - logo, cores, tipografia, ícones, ilustrações, mascote e motion graphics do Repeteco.
- [Design no Figma](https://www.figma.com/design/zLz9JwG8iKX8twcxCNoUO2/TaGravado?node-id=0-1&t=fCiQqqUcCPDcxCEy-1) - protótipo visual das telas.
- [Documentação técnica](./docs/documentacao-tecnica.md) - arquitetura e decisões técnicas (a preencher nas próximas sprints).
- [Guia de instalação](./docs/instalacao.md) - pré-requisitos e passo a passo (a preencher nas próximas sprints).

---

## Licença

Distribuído sob a licença [MIT](./LICENSE).
