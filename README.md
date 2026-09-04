# PI2 — Sistema de Replay para Quadras Esportivas

Atletas amadores, treinadores e gestores de quadras esportivas enfrentam dificuldades para registrar e reviver momentos importantes de partidas e treinos.

Com esse sistema, propomos um SaaS White-Label de Replay** que permite:

1. **Gravação automática** de partidas e treinos em quadras esportivas
2. **Replay instantâneo** acessível via aplicativo mobile
3. **Compartilhamento** de melhores momentos em redes sociais
4. **Transmissão ao vivo** para familiares e torcedores
5. **Identidade visual personalizada** para cada arena (White-Label)
2
## Repositórios

| Camada | Repositório | Stack |
|---|---|---|
| Frontend (SPA) | https://github.com/PI2-2026-2-equipe-03/pi2-frontend | React 19 · Vite · Tailwind CSS 4 |
| Backend (API REST) | https://github.com/PI2-2026-2-equipe-03/pi2-backend | Fastify 5 · Prisma 7 · TypeScript |

## Modelo de dados (MER)

![Diagrama Entidade-Relacionamento do TNY](./)

Entidades centrais: `...`.

## Arquitetura

**a montar**

## Como rodar (resumo)

Requer Node.js 22+. Rode backend e frontend em terminais separados:

```bash
# Backend — API em http://localhost:3000 (Swagger em /docs)
git clone https://github.com/PI2-2026-2-equipe-03/pi2-backend
cd pi2-backend
cp .env.example .env      # defina JWT_SECRET e DATABASE_URL
npm install
npm run db:migrate
npm run db:seed           # opcional: dados de exemplo
npm run dev

# Frontend — SPA em http://localhost:5173
git clone https://github.com/PI2-2026-2-equipe-03/pi2-frontend
cd pi2-frontend
cp .env.example .env      # VITE_API_URL aponta para o backend
npm install
npm run dev
```

Para o ambiente de produção com Docker (PostgreSQL + API) e detalhes de configuração,
veja a documentação abaixo.

## Documentação

- **[Documentação técnica detalhada](documentacao-tecnica.md)** — arquitetura,
  banco de dados, referência de rotas da API, testes, containerização e deploy.
- **[Guia de instalação](instalacao.md)** — passo a passo de pré-requisitos, instalação e
  variáveis de ambiente.
- **[Design no Figma](./)** — protótipos e identidade visual do projeto.

## Stack

- **Frontend:** --.
- **Backend:** --.
- **Banco:** SQLite (dev/testes) · PostgreSQL 16 (produção/Docker).

## Licença

[MIT](LICENSE)
