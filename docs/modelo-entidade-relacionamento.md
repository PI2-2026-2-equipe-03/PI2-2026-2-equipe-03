# Modelo Entidade-Relacionamento (MER) — TaGravado

**Projeto:** TaGravado — plataforma de captura e download de replays esportivos
**Sprint:** 1
**Fonte dos requisitos:** [`requisitos_funcionais.md`](./requisitos_funcionais.md), [`casos-de-uso.md`](./casos-de-uso.md), [`diagrama-casos-de-uso.md`](./diagrama-casos-de-uso.md)

## Entidades

| Entidade | Descrição |
|---|---|
| **usuario** | Conta única para os perfis Usuário, Cliente e Administrador (`tipo_perfil` discrimina o papel). |
| **arena** | Estabelecimento esportivo, pertencente a um Cliente. |
| **quadra** | Quadra dentro de uma arena. |
| **camera** | Câmera vinculada a uma quadra, responsável pelo buffer de gravação. |
| **replay** | Vídeo gerado a partir do acionamento da botoeira, associado a quadra/data/hora. |
| **patrocinador** | Patrocinador cadastrado por um Cliente. |
| **quadra_patrocinador** | Associativa N:N entre quadra e patrocinador. |

## Diagrama

```mermaid
erDiagram
    USUARIO ||--o{ ARENA : possui
    ARENA ||--o{ QUADRA : contem
    QUADRA ||--o{ CAMERA : possui
    QUADRA ||--o{ REPLAY : gera
    QUADRA }o--o{ PATROCINADOR : anuncia

    USUARIO {
        int id_usuario PK
        string nome
        string email UK
        string senha_hash
        string telefone
        string tipo_perfil
        int tentativas_login
        datetime bloqueado_ate
    }
    ARENA {
        int id_arena PK
        int id_cliente FK
        string nome
        string cidade
        string endereco
    }
    QUADRA {
        int id_quadra PK
        int id_arena FK
        string nome
        bool disponivel
    }
    CAMERA {
        int id_camera PK
        int id_quadra FK
        string identificador
        string status
    }
    REPLAY {
        int id_replay PK
        int id_quadra FK
        string arquivo_url
        date data_geracao
        time hora_geracao
        string status
        datetime criado_em
        datetime expira_em
    }
    PATROCINADOR {
        int id_patrocinador PK
        string nome
        string foto_url
        int duracao
        decimal valor
    }
```

## Atributos, chaves e regras

### usuario
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_usuario | int | PK | |
| nome | string | | |
| email | string | UK | RF-01, RF-02 |
| senha_hash | string | | nunca armazenar em texto plano |
| telefone | string | | |
| tipo_perfil | enum | | `usuario`, `cliente`, `administrador` |
| tentativas_login | int | | RNF-04 — bloqueio após 5 tentativas |
| bloqueado_ate | datetime | | RNF-04 — bloqueio de 15 min |

### arena
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_arena | int | PK | |
| id_cliente | int | FK → usuario | dono da arena |
| nome | string | | |
| cidade | string | | usada na busca (fluxo de navegação) |
| endereco | string | | |

### quadra
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_quadra | int | PK | |
| id_arena | int | FK → arena | |
| nome | string | | |
| disponivel | bool | | RF-06, fluxo alternativo "quadra indisponível" |

### camera
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_camera | int | PK | |
| id_quadra | int | FK → quadra | |
| identificador | string | | |
| status | string | | |

### replay
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_replay | int | PK | |
| id_quadra | int | FK → quadra | RF-09 |
| arquivo_url | string | | |
| data_geracao | date | | RF-09 |
| hora_geracao | time | | RF-09 |
| status | enum | | `pendente`, `disponivel`, `excluido` — RF-09 (falha), RF-10 (exclusão manual) |
| criado_em | datetime | | |
| expira_em | datetime | | RF-08 — `criado_em` + 7 dias |

### patrocinador
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_patrocinador | int | PK | |
| nome | string | | RF-07 — unicidade validada por quadra |
| foto_url | string | | |
| duracao | int | | |
| valor | decimal | | |

### quadra_patrocinador
| Atributo | Tipo | Chave | Observação |
|---|---|---|---|
| id_quadra | int | PK, FK → quadra | |
| id_patrocinador | int | PK, FK → patrocinador | RF-07 — limite de patrocinadores por quadra controlado na aplicação |

## Cardinalidades

| Relacionamento | Cardinalidade |
|---|---|
| usuario (cliente) — arena | 1:N |
| arena — quadra | 1:N |
| quadra — camera | 1:N |
| quadra — replay | 1:N |
| quadra — patrocinador | N:N (via quadra_patrocinador) |

## Pontos em aberto

1. **RF-10 (exclusão de replay)** — modelo não registra quem excluiu (Cliente ou Administrador). Se necessário rastrear, adicionar `excluido_por FK → usuario` em `replay`.
2. **RF-08 (expiração)** — `status = excluido` cobre tanto soft delete automático quanto manual; purge físico do arquivo é decisão de infraestrutura, fora do escopo do MER.

## Referências

- [`requisitos_funcionais.md`](./requisitos_funcionais.md)
- [`casos-de-uso.md`](./casos-de-uso.md)
- [`diagrama-casos-de-uso.md`](./diagrama-casos-de-uso.md)