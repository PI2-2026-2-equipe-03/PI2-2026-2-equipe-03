# TaGravado - Sistema de Replay para Quadras Esportivas

> Repositório principal do projeto **TaGravado** - concentra a documentação, o planejamento e os links para os repositórios técnicos (frontend e backend). Trabalho de conclusão do **Projeto Integrador 2 (2026/2) - Equipe 03**, sob orientação do professor Bruno Riccelli.

---

## Sobre o projeto

Nas quadras de esportes de areia, um pedido recorrente dos jogadores é ter acesso aos **replays das câmeras de segurança** para reviver os melhores momentos das partidas. Hoje esse fluxo é manual: o funcionário precisa abrir os arquivos da câmera, localizar o horário do clipe e enviá-lo ao cliente.

**TaGravado** resolve isso com uma aplicação web conteinerizada que, ao pressionar um botão físico instalado na quadra, gera e disponibiliza automaticamente o clipe para download pelo cliente da arena. Numa segunda etapa, o sistema também oferecerá **reserva de horários** das quadras pela mesma plataforma.

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
| Sprints seguintes | Implementação (backend + frontend), integração com hardware, testes e deploy | A definir |

Acordos de governança (PRs, revisão obrigatória, rastreabilidade de issues) descritos em [`plano-de-projeto.md` §5](./docs/plano-de-projeto.md).

---

## Executando a aplicação completa

Este repositório contém um `docker-compose.yml` central que orquestra frontend, backend e banco em conjunto. Os três repositórios devem ficar **lado a lado** no mesmo diretório-pai.

### Pré-requisitos

- [Docker Engine](https://docs.docker.com/engine/install/) 24+
- [Docker Compose plugin](https://docs.docker.com/compose/install/) v2+ (já vem com Docker Desktop)
- Git

### 1. Clonar os três repositórios lado a lado

O `docker-compose.yml` central referencia os outros repos por caminhos relativos (`../pi2-frontend`, `../pi2-backend`). Escolha um diretório-pai e clone os três:

```bash
mkdir tagravado && cd tagravado

git clone https://github.com/PI2-2026-2-equipe-03/PI2-2026-2-equipe-03.git
git clone https://github.com/PI2-2026-2-equipe-03/pi2-frontend.git
git clone https://github.com/PI2-2026-2-equipe-03/pi2-backend.git
```

Estrutura resultante:

```
tagravado/
├── PI2-2026-2-equipe-03/    ← docs + docker-compose.yml central
├── pi2-frontend/
└── pi2-backend/
```

### 2. Configurar variáveis de ambiente

```bash
cd PI2-2026-2-equipe-03
cp .env.example .env
```

O `.env.example` traz defaults funcionais. Ajuste `JWT_SECRET` e senhas antes de qualquer uso além do ambiente local.

### 3. Subir tudo

```bash
docker compose up --build
```

Serviços disponíveis:

| Serviço | URL / Porta | Descrição |
|---|---|---|
| Frontend (Vite dev) | http://localhost:5173 | Interface React com hot reload |
| Backend (Fastify) | http://localhost:3000 | API REST |
| Health check | http://localhost:3000/health | Sanity check da API |
| Postgres | localhost:5432 | Banco (usuário/senha do `.env`) |

Para encerrar:

```bash
docker compose down          # para os containers, mantém volumes
docker compose down -v       # remove também o volume do banco
```

### Execução individual (sem o compose central)

Cada repositório também roda isoladamente pelo seu próprio compose, útil quando você está mexendo em apenas uma camada:

```bash
# Só frontend
cd pi2-frontend && docker compose up

# Só backend (sobe apenas o Postgres — a API roda via `npm run dev` local)
cd pi2-backend && docker compose up
```

### Troubleshooting

| Sintoma | Causa provável | Ação |
|---|---|---|
| `port is already allocated` em 5173/3000/5432 | Processo do host ocupando a porta | Trocar a porta no `.env` (`FRONTEND_PORT`, `BACKEND_PORT`, `POSTGRES_PORT`) |
| Frontend abre mas requests dão CORS error | Backend sem `@fastify/cors` liberando `http://localhost:5173` | Configurar CORS no `pi2-backend` |
| Alterações no código não refletem | Watcher não detecta mudança | Confirmar bind mount e `CHOKIDAR_USEPOLLING=true` (frontend); reiniciar o serviço |
| `build: ../pi2-frontend: no such file` | Repos não estão lado a lado | Ver estrutura no passo 1 |
| Backend não conecta no DB | `db` ainda inicializando | O compose usa `depends_on: service_healthy`; se persistir, `docker compose logs db` |
| Precisa resetar tudo | Volumes/imagens corrompidos | `docker compose down -v && docker compose build --no-cache` |

Notas de arquitetura (dev/prod, alternativa de proxy, etc.) estão como comentários no próprio [`docker-compose.yml`](./docker-compose.yml).

---

## Documentação

- [Plano de Projeto](./docs/plano-de-projeto.md) - contexto, objetivos, papéis e governança.
- [Design no Figma](https://www.figma.com/design/zLz9JwG8iKX8twcxCNoUO2/TaGravado?node-id=0-1&t=fCiQqqUcCPDcxCEy-1) - protótipo visual das telas.
- [Documentação técnica](./docs/documentacao-tecnica.md) - arquitetura e decisões técnicas (a preencher nas próximas sprints).
- [Guia de instalação](./docs/instalacao.md) - pré-requisitos e passo a passo (a preencher nas próximas sprints).

---

## Licença

Distribuído sob a licença [MIT](./LICENSE).
