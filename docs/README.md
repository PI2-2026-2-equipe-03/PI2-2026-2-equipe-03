# Governança de Artefatos de Requisitos — TaGravado

> **Versão:** 0.1 (rascunho) · **Última atualização:** 18/10/2026
> **Escopo:** artefatos de requisitos do projeto TaGravado (sistema web de replays e, futuramente, reserva de horários para quadras de areia).

Este documento define **quais artefatos de requisitos existem, quem cuida de cada um, como são nomeados, revisados, alterados e rastreados**. Ele também registra as inconsistências e lacunas encontradas na análise dos documentos atuais, para que a equipe possa corrigi-las de forma organizada.

---

## Sumário

1. [Objetivo](#1-objetivo)
2. [Inventário de artefatos](#2-inventário-de-artefatos)
3. [Papéis e responsabilidades](#3-papéis-e-responsabilidades)
4. [Glossário padronizado](#4-glossário-padronizado)
5. [Convenções de identificação e prioridade](#5-convenções-de-identificação-e-prioridade)
6. [Estrutura padrão de um requisito funcional](#6-estrutura-padrão-de-um-requisito-funcional)
7. [Ciclo de vida de um requisito](#7-ciclo-de-vida-de-um-requisito)
8. [Controle de mudanças (Git)](#8-controle-de-mudanças-git)
9. [Matriz de rastreabilidade](#9-matriz-de-rastreabilidade)
10. [Checklist de qualidade e revisão](#10-checklist-de-qualidade-e-revisão)
11. [Inconsistências identificadas](#11-inconsistências-identificadas)
12. [Lacunas de cobertura](#12-lacunas-de-cobertura)
13. [Histórico de versões](#13-histórico-de-versões)

---

## 1. Objetivo

- Garantir que os requisitos sejam **únicos, identificáveis, rastreáveis e revisados** antes de virarem código.
- Manter **consistência** entre o Plano de Projeto, os Perfis de Usuário e os Requisitos Funcionais.
- Padronizar a ligação entre requisito → Issue → Pull Request → teste (Gherkin), conforme o acordo de trabalho da equipe e o manual de rastreabilidade do professor Bruno Riccelli.

---

## 2. Inventário de artefatos

| # | Artefato | Arquivo atual | Conteúdo | Responsável (sugerido) |
|---|----------|---------------|----------|------------------------|
| A1 | Plano de Projeto | `plano-de-projeto.md` | Contexto do cliente (Arena Dunnas Beach), problema, solução em duas fases, objetivos, equipe, impacto social e governança Git | Analistas de Requisitos e Design |
| A2 | Perfis de Usuário | `perfis_de_usuario.md` | Tipos de usuário (Usuário, Cliente/Dono de Quadra, Administrador) e suas permissões | Analistas de Requisitos e Design |
| A3 | Requisitos Funcionais + Gherkin | `requisitos_funcionais_gherkin (1).md` | RF-01 a RF-12 com descrição, atores, fluxos, prioridade e cenários Gherkin | Analistas de Requisitos e Design |
| A4 | Regras de Negócio | **não existe** | RN-01, RN-04 e RN-05 são citadas nos RFs, mas não estão documentadas | A definir (ver seção 12) |
| A5 | Requisitos Não Funcionais | **não existe** | Previsto como objetivo específico da Sprint 1 no Plano de Projeto | A definir (ver seção 12) |

**Recomendação de nomes de arquivo:** padronizar em `kebab-case`, sem espaços ou sufixos como `(1)`:

```
docs/
├── plano-de-projeto.md
├── perfis-de-usuario.md
├── requisitos-funcionais.md
├── regras-de-negocio.md          
├── requisitos-nao-funcionais.md  
└── matriz-de-rastreabilidade.md
 viver na seção 9
```

---

## 3. Papéis e responsabilidades

Papéis conforme a divisão de equipe do Plano de Projeto. A atribuição por artefato abaixo é uma **proposta** a ser validada pela equipe.

| Papel | Integrantes | Responsabilidade sobre os requisitos |
|-------|-------------|--------------------------------------|
| Analistas de Requisitos e Design | Kauan, Laryssa | **Donos** dos artefatos A1–A5: elicitar, redigir, priorizar e manter a consistência |
| Desenvolvedores Backend e Infraestrutura | Pedro, Lucas, Pablo | Revisar viabilidade técnica (armazenamento, rotinas automáticas, microcontroladores, Docker) |
| Desenvolvedores Frontend | Alan, Kaik | Revisar clareza de fluxos e mensagens de interface |
| QA / Testes | Rick | Validar que cada RF é testável e que os cenários Gherkin estão completos e executáveis |

### Matriz RACI simplificada

| Atividade | Analistas | Backend | Frontend | QA |
|-----------|:---------:|:-------:|:--------:|:--:|
| Criar/alterar requisito | **R/A** | C | C | C |
| Revisar viabilidade técnica | I | **R** | C | I |
| Escrever/revisar Gherkin | **R** | C | C | **A** |
| Aprovar requisito para desenvolvimento | **A** | R | R | R |
| Manter matriz de rastreabilidade | **R/A** | C | C | C |

> R = Responsável · A = Aprovador · C = Consultado · I = Informado

---

## 4. Glossário padronizado

Os documentos atuais usam "Cliente" e "Usuário" com significados diferentes (ver [inconsistência I-01](#11-inconsistências-identificadas)). Propõe-se adotar os termos abaixo em **todos** os artefatos:

| Termo | Definição | Fonte |
|-------|-----------|-------|
| **Usuário** | Jogador comum que busca quadras e visualiza/baixa gravações. Acessa apenas o próprio perfil e dados | Perfis de Usuário |
| **Cliente / Dono de Quadra** | Usuário cuja solicitação foi aprovada por um Administrador. Gerencia exclusivamente as quadras de sua propriedade | Perfis de Usuário |
| **Administrador** | Equipe/desenvolvedores responsáveis pela operação. Acesso irrestrito a quadras e usuários | Perfis de Usuário |
| **Quadra / Arena** | Espaço esportivo cadastrado no sistema (ex.: Arena Dunnas Beach). *A definir: "quadra" e "arena" são sinônimos ou a arena agrupa quadras?* | Plano de Projeto / RFs |
| **Replay / Vídeo** | Clipe dos últimos 30 segundos gerado pelo acionamento da botoeira | RF-05 |
| **Botoeira** | Botão físico instalado na quadra, ligado a microcontrolador | Plano de Projeto |
| **Patrocinador** | Marca vinculada a uma quadra, aplicada como marca d'água nos replays | RF-07 |

---

## 5. Convenções de identificação e prioridade

### 5.1 Identificadores

| Prefixo | Tipo | Exemplo | Observação |
|---------|------|---------|------------|
| `RF-NN` | Requisito Funcional | `RF-06` | Dois dígitos, sequencial, **nunca reaproveitado** |
| `RNF-NN` | Requisito Não Funcional | `RNF-01` | A criar |
| `RN-NN` | Regra de Negócio | `RN-01` | Referenciada nos RFs; documento a criar |
| `EC-NN` | Label de rastreabilidade do manual do professor | `EC-04` | Usar conforme o manual; confirmar significado e escopo com o professor |

Regras:
- Um ID, depois de criado, **não muda de significado**. Se o requisito for descartado, marca-se como `Cancelado` (não se apaga nem se reutiliza o número).
- Referências cruzadas devem usar o ID (ex.: "conforme RN-05"), nunca descrições soltas.

### 5.2 Escala de prioridade

Os RFs já usam três níveis. Fica oficializada a seguinte escala:

| Prioridade | Significado |
|------------|-------------|
| **Essencial** | Sem ele o sistema não cumpre seu propósito; entra no escopo mínimo |
| **Importante** | Agrega valor significativo; entra no escopo planejado, mas pode ser adiado se necessário |
| **Desejável** | Melhoria; entregue se houver capacidade |

---

## 6. Estrutura padrão de um requisito funcional

Todo RF deve seguir o modelo abaixo. Campos obrigatórios estão marcados com `*`.

```markdown
**RF-NN: Título curto no infinitivo ou substantivo***

**Descrição:*** O que o sistema deve fazer e para quê.
**Atores:*** Usuário | Cliente | Administrador | Sistema   (usar o glossário)
**Objetivos:** (opcional) Resultados esperados.
**Pré-condições:** (opcional) O que precisa ser verdade antes.
**Fluxo principal:*** Passos numerados.
**Fluxos alternativos / exceções:*** Passos numerados, cada um com cenário Gherkin correspondente.
**Regras de negócio relacionadas:** RN-NN, ...
**Prioridade:*** Essencial | Importante | Desejável
**Versão Gherkin:*** Cenários cobrindo o fluxo principal e cada fluxo alternativo.
**Status:*** Rascunho | Em revisão | Aprovado | Implementado | Cancelado
```

### Padrão para cenários Gherkin

- Todo cenário deve ter `Dado`, `Quando` e `Então`, mesmo que `Dado` seja um estado inicial simples.
- Mensagens exibidas ao usuário devem aparecer **entre aspas e idênticas** às da interface.
- Um cenário = um comportamento. Evitar misturar fluxos (ex.: login dentro do RF de dashboard).
- Todo fluxo alternativo listado no RF deve ter ao menos um cenário.
- Usar dados fictícios coerentes (e-mails, IDs, datas) e **não dados reais de pessoas**.

---

## 7. Ciclo de vida de um requisito

```
Rascunho ──► Em revisão ──► Aprovado ──► Em desenvolvimento ──► Implementado ──► Validado (QA)
                 │              │
                 ▼              ▼
             Rejeitado      Cancelado
```

| Status | Condição de entrada | Quem decide |
|--------|---------------------|-------------|
| Rascunho | Requisito proposto | Analistas |
| Em revisão | Estrutura completa (seção 6) | Analistas |
| Aprovado | Checklist da seção 10 cumprido + revisão de Backend, Frontend e QA | Analistas (aprovador) |
| Em desenvolvimento | Issue criada e vinculada à milestone da Sprint | Dev responsável |
| Implementado | PR aprovado e integrado | Revisor do PR |
| Validado | Cenários Gherkin executados com sucesso | QA |

---

## 8. Controle de mudanças (Git)

Aplica-se o **Acordo de Trabalho da Equipe** do Plano de Projeto aos artefatos de requisitos:

1. **Nenhuma alteração direta em `main`/`master`**: toda mudança em requisito entra por Pull Request.
2. **Todo PR exige revisão de pelo menos um colega** antes do merge. Para mudanças em requisitos, recomenda-se que o revisor seja de papel diferente do autor (ex.: Analista altera, QA revisa).
3. **Toda tarefa nasce como Issue**, com:
   - um único responsável;
   - vínculo à milestone da Sprint vigente;
   - label de rastreabilidade (ex.: `RF-01`, `EC-04`) conforme o manual do professor Bruno Riccelli.
4. Tarefas fora das regras do manual de rastreabilidade podem ser **canceladas ou reestruturadas**, impactando a pontuação quinzenal de todos.

### Fluxo para alterar um requisito

1. Abrir Issue descrevendo a mudança (qual RF/RN, por quê, impacto).
2. Criar branch a partir de `main` (sugestão: `req/rf-06-ajuste-busca`).
3. Editar o artefato e atualizar a **matriz de rastreabilidade** e o **histórico de versões**.
4. Abrir PR referenciando a Issue (`Closes #NN`) e marcar revisores.
5. Após aprovação, fazer o merge e comunicar a equipe se o requisito já estiver em desenvolvimento.

### Convenção de commits (sugestão)

```
docs(req): RF-06 inclui cenário de quadra indisponível
docs(req): cria regras-de-negocio.md com RN-01, RN-04 e RN-05
docs(req): padroniza termo "Cliente" em todos os artefatos
```

---

## 9. Matriz de rastreabilidade

Rastreia cada requisito até seu ator, perfil e regras de negócio. As colunas **Issue**, **PR** e **Teste** devem ser preenchidas conforme o trabalho avança.

| RF | Título | Ator(es) | Perfil de acesso | Prioridade | RN | Gherkin | Issue | PR | Teste |
|----|--------|----------|------------------|------------|----|:-------:|-------|----|-------|
| RF-01 | Cadastro de usuário | Usuário | Usuário | Essencial | — | ✅ | | | |
| RF-02 | Login de usuário | Usuário | Todos | Essencial | — | ⚠️ incompleto | | | |
| RF-03 | Métricas para o administrador | Administrador | Administrador | Importante | — | ⚠️ | | | |
| RF-04 | Métricas para o cliente | Cliente | Cliente | Importante | — | ⚠️ | | | |
| RF-05 | Gravar vídeo | Usuário (jogador) | Usuário | Essencial | — | ✅ | | | |
| RF-06 | Baixar vídeo | Usuário | Usuário | Essencial | — | ⚠️ | | | |
| RF-07 | Cadastrar patrocinadores | Cliente | Cliente | Importante | RN-05 | ⚠️ | | | |
| RF-08 | Tempo de disponibilidade dos vídeos | Sistema | — | Importante | RN-01 | ✅ | | | |
| RF-09 | Associar informações ao replay | Sistema | — | Essencial | — | ✅ | | | |
| RF-10 | Exclusão de vídeos | Cliente, Administrador | Cliente, Administrador | Desejável | RN-04 | ✅ | | | |
| RF-11 | Recuperação de senha | Usuário | Todos | Importante | — | ✅ | | | |
| RF-12 | Solicitação de cadastro como gestor de quadra | Cliente, Administrador | Usuário → Cliente | Essencial | — | ✅ | | | |

Legenda: ✅ cenários cobrem os fluxos descritos · ⚠️ há fluxos sem cenário ou cenários com problema (ver seção 11).

### Rastreabilidade entre Perfis de Usuário e RFs

| Permissão (Perfis de Usuário) | RF que a implementa |
|-------------------------------|---------------------|
| Usuário: visualizar e editar o próprio perfil | ❌ sem RF |
| Usuário: buscar, visualizar e baixar gravações | RF-06 |
| Usuário/Cliente/Administrador: recuperar ou alterar senha | RF-11 |
| Usuário: solicitar cadastro como Cliente | RF-12 |
| Cliente: criar, editar e excluir as próprias quadras | ❌ sem RF |
| Cliente: dashboard de métricas das próprias quadras | RF-04 |
| Administrador: criar, editar e excluir quadras de qualquer Cliente | ❌ sem RF |
| Administrador: avaliar, aprovar ou indeferir solicitações | RF-12 |
| Administrador: dashboard consolidado | RF-03 |
| Excluir vídeos (Cliente/Administrador) | RF-10 (⚠️ não consta em Perfis de Usuário) |
| Cadastrar patrocinadores (Cliente) | RF-07 (⚠️ não consta em Perfis de Usuário) |

---

## 10. Checklist de qualidade e revisão

Um requisito só passa para **Aprovado** se todos os itens forem atendidos:

**Clareza e consistência**
- [ ] Possui ID único e título claro
- [ ] Usa os termos do glossário (seção 4)
- [ ] Ator coincide com o perfil que, em *Perfis de Usuário*, tem a permissão correspondente
- [ ] Prioridade definida na escala oficial
- [ ] Sem texto solto, bullets vazios ou frases incompletas

**Completude**
- [ ] Fluxo principal e fluxos alternativos descritos
- [ ] Toda regra de negócio citada (`RN-NN`) existe em `regras-de-negocio.md`
- [ ] Mensagens de erro e sucesso definidas

**Testabilidade**
- [ ] Cada fluxo tem cenário Gherkin com `Dado`/`Quando`/`Então`
- [ ] Resultados verificáveis (sem termos vagos como "rápido" ou "intuitivo" sem métrica)
- [ ] QA revisou os cenários

**Rastreabilidade**
- [ ] Linha atualizada na matriz (seção 9)
- [ ] Issue criada com label do RF e vínculo à milestone da Sprint

---

## 11. Inconsistências identificadas

Levantamento feito sobre os três documentos atuais. Sugere-se abrir **uma Issue por item** (ou agrupar por afinidade).

### Alta severidade (afetam o significado ou a implementação)

| ID | Artefato | Problema | Ação sugerida |
|----|----------|----------|---------------|
| I-01 | Perfis × RFs | **Termo "Cliente" com dois sentidos.** Em *Perfis de Usuário*, Cliente = dono de quadra. Nos RF-05 e RF-06, "cliente" é o jogador que aperta o botão e baixa o vídeo (no Plano de Projeto também: "clientes da arena") | Adotar o glossário da seção 4 e revisar RF-05, RF-06 e Plano |
| I-02 | RF-12 × Perfis | RF-12 chama o resultado da aprovação de **"administrador de quadra"**, mas Perfis define **"Cliente/Dono de Quadra"** e reserva "Administrador" à equipe do sistema. O ator do RF-12 também é "Cliente", mas quem solicita é o **Usuário** | Renomear para "Cliente/Dono de Quadra" e corrigir o ator para Usuário |
| I-03 | RF-01 | Fluxo e Gherkin divergem: o fluxo pede nome, telefone, e-mail e senha, mas o cenário de erro usa **CPF**, que não está nos campos do formulário. Também fala "cliente é cadastrado" em vez de "usuário" | Decidir se CPF é campo do cadastro; alinhar fluxo, cenário e mensagens |
| I-04 | RN-01, RN-04, RN-05 | **Regras de negócio citadas nos RFs (RF-07, RF-08, RF-10) não estão documentadas** em nenhum artefato | Criar `regras-de-negocio.md` |
| I-05 | RF-05 | Descrição diz "aperta um botão"; Gherkin exige **segurar por 2 segundos**. Ator é "Usuário", mas os cenários falam "cliente". Descrição diz "banco de dados"; RF-08 fala em "storage" | Padronizar regra do botão, ator e local de armazenamento |
| I-06 | Perfis × RFs | Permissões **sem RF correspondente** (ver tabela da seção 9): editar perfil, CRUD de quadras (Cliente e Administrador) | Criar RFs ou revisar o escopo dos perfis |

### Média severidade (cenários incompletos ou fluxos sem cobertura)

| ID | Artefato | Problema | Ação sugerida |
|----|----------|----------|---------------|
| I-07 | RF-01 | Segundo bullet em *Fluxo alternativo* está vazio; **falta cenário** para campo obrigatório não preenchido e para e-mail duplicado | Remover bullet vazio e adicionar cenários |
| I-08 | RF-02 | Cenário "senha incorreta" **não tem `Então`**. Falta cenário para campos obrigatórios vazios | Completar cenários |
| I-09 | RF-03 / RF-04 | Cenário "Login com credenciais inválidas" é cópia do RF-02, sem `Dado`, e no RF-04 falta a aspa de fechamento da mensagem. Duplica comportamento já coberto | Remover e referenciar RF-02, ou completar |
| I-10 | RF-06 | Fluxo alternativo "Quadras indisponíveis" **sem cenário Gherkin**. O fluxo principal diz "Quadra", mas os cenários usam "arena" | Adicionar cenário e unificar termo |
| I-11 | RF-07 | Fluxos alternativos "Patrocinador já existe" e "Total de patrocinadores já preenchido" **sem cenário**. Limite de patrocinadores **não está definido** | Definir o limite (RN) e escrever cenários |
| I-12 | RF-09 | Gherkin registra `patrocinador id: 5` nos metadados, mas a descrição e os objetivos citam só quadra, data e horário. Fluxo alternativo (falha ao salvar) sem cenário | Alinhar descrição aos metadados; adicionar cenário de falha |
| I-13 | RF-08 | Sem seção de fluxo principal, apesar de ser um RF. Prazo de 7 dias deveria constar em RN-01 | Completar o RF e a RN |
| I-14 | RF-10 | Gherkin exige "informar o motivo" e gerar log de auditoria, o que **não consta no fluxo principal**. Perfis de Usuário não menciona exclusão de vídeos | Alinhar fluxo, cenário e perfis |
| I-15 | RF-11 | No fluxo alternativo, o código incorreto volta ao "passo 2"; no Gherkin, volta à "escolha do meio de recebimento" (passo 3). **Critérios mínimos de senha** não estão definidos | Padronizar o retorno e definir a política de senha (RNF/RN) |
| I-16 | RF-12 | Cenário "e-mail já existente" é conceitualmente estranho, pois quem solicita já é um usuário cadastrado. Gherkin fala em "cadastro", mas o fluxo é **solicitação de upgrade de perfil** | Reavaliar o cenário e o vocabulário |
| I-17 | Perfis | Frase "Surge a partir da aprovação de uma solicitação feita por um administrador" é ambígua: a solicitação é feita pelo Usuário e **aprovada** por um Administrador | Reescrever |

### Baixa severidade (forma e padronização)

| ID | Artefato | Problema |
|----|----------|----------|
| I-18 | Todos | Nome de arquivo com sufixo `(1)` e espaços |
| I-19 | RFs | Formatação inconsistente: alguns RFs têm "Objetivos", outros não; prioridade e rótulos variam (`Fluxos alternativos`/`Fluxo alternativo`); ator citado como "Atores"/"Ator" |
| I-20 | Perfis | Falta de vírgula em "Buscar visualizar e baixar gravações" |
| I-21 | RF-03 | Cabeçalho sem os dois-pontos padrão (`**RF-03:** Métricas...` vs. `**RF-01: ...**`) |

---

## 12. Lacunas de cobertura

| Lacuna | Origem | Ação sugerida |
|--------|--------|---------------|
| **Módulo de Reserva de Horários** (2ª parte do projeto) não possui nenhum RF | Plano de Projeto, seção 1.3 | Levantar RFs ou declarar explicitamente que está fora do escopo da versão atual |
| **Requisitos Não Funcionais** não documentados (desempenho, segurança de senha, retenção, disponibilidade, usabilidade, deploy via Docker) | Plano de Projeto, seção 2 (objetivos específicos) | Criar `requisitos-nao-funcionais.md` |
| **Hardware** (botoeira, fiação, microcontroladores, integração com a câmera) sem requisito formal | Plano de Projeto, seção 1.3 | Definir RFs/RNFs de integração e instalação |
| **Marca d'água** de patrocinadores (RN-05) aparece só como referência no RF-07 | RF-07 | Documentar em RN e, se for processamento, criar RF próprio |
| **Notificações** (aprovação/reprovação no RF-12, novas solicitações para o Administrador) sem definição de canal | RF-12 | Definir canal (e-mail, SMS, interno) |
| **Continuidade pós-semestre** com estudo pendente | Plano de Projeto, seção 4 | Registrar como risco e acompanhar |
| **Desafios de implantação** (fluxo não intuitivo, instalação) sem critérios de aceitação | Plano de Projeto, seção 4 | Converter em RNFs de usabilidade e critérios de teste |
| **Logs de auditoria** citados no RF-10 sem requisito próprio | RF-10 | Definir escopo do log (o que, por quanto tempo, quem acessa) |

---

## 13. Histórico de versões

| Versão | Data | Autor | Descrição |
|--------|------|-------|-----------|
| 0.1 | 18/10/2026 | Equipe TaGravado | Criação do documento de governança com inventário, convenções, matriz de rastreabilidade e levantamento de inconsistências |

---

> **Manutenção deste documento:** qualquer alteração em um artefato de requisitos deve atualizar a matriz de rastreabilidade (seção 9) e o histórico de versões (seção 13) **no mesmo Pull Request**.
