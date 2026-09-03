# TaGravado — Sistema de Replay para Quadras Esportivas

> Repositório principal do projeto **TaGravado** — concentra a documentação, o planejamento e os links para os repositórios técnicos (frontend e backend). Trabalho de conclusão do **Projeto Integrador 2 (2026/2) — Equipe 03**, sob orientação do professor Bruno Riccelli.

---

## Sobre o projeto

Nas quadras de esportes de areia, um pedido recorrente dos jogadores é ter acesso aos **replays das câmeras de segurança** para reviver os melhores momentos das partidas. Hoje esse fluxo é manual: o funcionário precisa abrir os arquivos da câmera, localizar o horário do clipe e enviá-lo ao cliente.

**TaGravado** resolve isso com uma aplicação web conteinerizada que, ao pressionar um botão físico instalado na quadra, gera e disponibiliza automaticamente o clipe para download pelo cliente da arena. Numa segunda etapa, o sistema também oferecerá **reserva de horários** das quadras pela mesma plataforma.

**Cliente/Parceiro:** Rennan — Arena Dunnas Beach.

Detalhes completos (requisitos, arquitetura, impacto social, governança) em [`plano-de-projeto.md`](./plano-de-projeto.md).

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
    <td align="center"><a href="https://github.com/CristianoGolDeBiciclceta2018"><img src="https://github.com/CristianoGolDeBiciclceta2018.png" width="80" alt="Kauan"/><br/><sub><b>Kauan</b></sub></a><br/>Análise & Design</td>
    <td align="center"><a href="https://github.com/laryssaszz"><img src="https://github.com/laryssaszz.png" width="80" alt="Laryssa"/><br/><sub><b>Laryssa</b></sub></a><br/>Análise & Design</td>
    <td align="center"><a href="https://github.com/Rickfarias"><img src="https://github.com/Rickfarias.png" width="80" alt="Rick"/><br/><sub><b>Rick</b></sub></a><br/>QA / Testes</td>
  </tr>
</table>

---

## Roadmap

Milestones acompanhados em [milestones do repositório](https://github.com/PI2-2026-2-equipe-03/PI2-2026-2-equipe-03/milestones).

| Sprint | Foco | Status |
|---|---|---|
| **Sprint 0** | Setup dos repositórios, plano de projeto e governança Git | Em andamento |
| **Sprint 1** | Levantamento de requisitos e prototipação inicial | A iniciar |
| Sprints seguintes | Implementação (backend + frontend), integração com hardware, testes e deploy | A definir |

Acordos de governança (PRs, revisão obrigatória, rastreabilidade de issues) descritos em [`plano-de-projeto.md` §5](./plano-de-projeto.md).

---

## Documentação

- [Plano de Projeto](./plano-de-projeto.md) — contexto, objetivos, papéis e governança.
- [Documentação técnica](./documentacao-tecnica.md) — arquitetura e decisões técnicas (a preencher nas próximas sprints).
- [Guia de instalação](./instalacao.md) — pré-requisitos e passo a passo (a preencher nas próximas sprints).

---

## Licença

Distribuído sob a licença [MIT](./LICENSE).
