# Matriz de Rastreabilidade Multidimensional — TaGravado

> **Versão:** 0.1 (rascunho) · **Data:** 18/10/2026
> **Objetivo:** cruzar, em um único lugar, todas as dimensões dos artefatos de requisitos (Plano → Perfis → RF → RN → RNF → Gherkin → execução) para permitir **análise de cobertura** (o que está sem vínculo) e **análise de impacto** (o que muda quando algo muda).

---

## Sumário

1. [Fontes e dimensões](#1-fontes-e-dimensões)
2. [Matriz mestre (visão consolidada por RF)](#2-matriz-mestre-visão-consolidada-por-rf)
3. [RF × RN](#3-rf--rn)
4. [RF × RNF](#4-rf--rnf)
5. [RN × RNF](#5-rn--rnf)
6. [Perfil × RF](#6-perfil--rf)
7. [Permissões dos Perfis → RF](#7-permissões-dos-perfis--rf)
8. [Plano de Projeto → Requisitos](#8-plano-de-projeto--requisitos)
9. [Cobertura Gherkin](#9-cobertura-gherkin)
10. [Índices reversos (análise de impacto)](#10-índices-reversos-análise-de-impacto)
11. [Achados da consolidação](#11-achados-da-consolidação)
12. [Como manter esta matriz](#12-como-manter-esta-matriz)
13. [Histórico de versões](#13-histórico-de-versões)

---

## 1. Fontes e dimensões

### 1.1 Artefatos consolidados

| ID | Artefato | Arquivo | Itens |
|----|----------|---------|-------|
| A1 | Plano de Projeto | `plano-de-projeto.md` | Objetivos, solução em 2 fases, equipe, impacto social, governança Git |
| A2 | Perfis de Usuário | `perfis_de_usuario.md` | 3 perfis (Usuário, Cliente/Dono de Quadra, Administrador) e suas permissões |
| A3 | Requisitos Funcionais + Gherkin | `requisitos_funcionais_gherkin (1).md` | RF-01 a RF-12 · 33 cenários |
| A4 | Regras de Negócio | `regrasDeNegocioRF (1).md` | RN-01 a RN-10 |
| A5 | Requisitos Não Funcionais | `requisitos-nao-funcionais.md` | RNF-01 a RNF-05 |

### 1.2 Dimensões da matriz

| Dim. | Dimensão | Origem | Valores |
|------|----------|--------|---------|
| D1 | Objetivo / Fase do projeto | A1 | Fase 1 (replays), Fase 2 (reserva de horários), objetivos específicos |
| D2 | Perfil / Ator | A2, A3 | Visitante, Usuário, Cliente, Administrador, Sistema |
| D3 | Requisito Funcional | A3 | RF-01 … RF-12 |
| D4 | Regra de Negócio | A4 | RN-01 … RN-10 |
| D5 | Requisito Não Funcional | A5 | RNF-01 … RNF-05 |
| D6 | Cenário de teste (Gherkin) | A3 | 33 cenários |
| D7 | Execução | Git | Issue · PR · Teste · Status |

### 1.3 Legenda geral

| Símbolo | Significado |
|---------|-------------|
| ● | Vínculo **bilateral**: um lado cita o outro, e vice-versa (ou ator declarado no RF) |
| ◐ | Vínculo **unilateral**: declarado apenas por um dos lados (o outro não cita) |
| △ | Vínculo **sugerido**: não declarado nos documentos; inferência desta matriz, **a validar pela equipe** |
| ○ | Aplicação **transversal** ou por herança de perfil |
| ✅ | Cobertura adequada |
| ⚠️ | Cobertura parcial ou com problema |
| ❌ | Sem cobertura |
| · | Sem vínculo |

> **Suposição assumida:** o Plano de Projeto não atribui fase a cada RF. Considerou-se que os RF-01 a RF-12 pertencem à **Fase 1**, pois o módulo de Reserva de Horários (Fase 2) não possui nenhum RF.

---

## 2. Matriz mestre (visão consolidada por RF)

Cada linha cruza as dimensões D1–D7 de um requisito funcional. Os detalhes de cada cruzamento estão nas seções seguintes.

| RF | Título | Fase | Prioridade | Ator(es) no RF | Perfis com acesso | RN vinculadas | RNF aplicáveis | Cenários | Issue | PR | Teste | Status |
|----|--------|:----:|------------|----------------|-------------------|---------------|----------------|:--------:|:-----:|:--:|:-----:|:------:|
| RF-01 | Cadastro de usuário | 1 | Essencial | Usuário | Visitante | RN-09 ◐, RN-10 ◐ | RNF-01 a 05 | 2 ⚠️ | | | | |
| RF-02 | Login de usuário | 1 | Essencial | Usuário | Usuário, Cliente, Administrador | RN-03 ◐, RN-06 ◐ | RNF-01 a 05 (RNF-04 ●) | 2 ⚠️ | | | | |
| RF-03 | Métricas para o administrador | 1 | Importante | Administrador | Administrador | — | RNF-01 a 05 | 3 ⚠️ | | | | |
| RF-04 | Métricas para o cliente | 1 | Importante | Cliente | Cliente | — | RNF-01 a 05 | 3 ⚠️ | | | | |
| RF-05 | Gravar vídeo | 1 | Essencial | Usuário (jogador) | Qualquer pessoa na arena | RN-02 ◐, RN-08 △ | RNF-04 | 3 ⚠️ | | | | |
| RF-06 | Baixar vídeo | 1 | Essencial | Usuário | Usuário, Cliente | RN-08 ◐, RN-01 △, RN-05 △ | RNF-01 a 05 (RNF-03 ●) | 4 ⚠️ | | | | |
| RF-07 | Cadastrar patrocinadores | 1 | Importante | Cliente | Cliente | RN-05 ● | RNF-01 a 05 | 1 ⚠️ | | | | |
| RF-08 | Tempo de disponibilidade dos vídeos | 1 | Importante | Sistema | — (automático) | RN-01 ● | — | 1 ✅ | | | | |
| RF-09 | Associar informações ao replay | 1 | Essencial | Sistema | — (automático) | RN-05 ◐, RN-02 △ | RNF-04 | 1 ⚠️ | | | | |
| RF-10 | Exclusão de vídeos | 1 | Desejável | Cliente, Administrador | Cliente (proprietário), Administrador | RN-04 ● | RNF-01 a 05 | 1 ⚠️ | | | | |
| RF-11 | Solicitação de recuperação de senha | 1 | Importante | Usuário | Usuário, Cliente, Administrador | RN-07 ◐, RN-10 △ | RNF-01 a 05 | 6 ⚠️ | | | | |
| RF-12 | Solicitação de cadastro como gestor de quadra | 1 | Essencial | Cliente*, Administrador | Usuário (solicita), Administrador (avalia) | RN-09 △ | RNF-01 a 05 | 6 ✅ | | | | |

\* O RF-12 cita "Cliente" como ator, mas pelos Perfis quem solicita é o **Usuário** (ver I-02).

**Resumo de cobertura:** 12 RFs · 10 RNs · 5 RNFs · 33 cenários. Apenas **3 vínculos RF↔RN são bilaterais** (RF-07/RN-05, RF-08/RN-01, RF-10/RN-04). Os RF-03 e RF-04 não têm nenhuma RN associada.

---

## 3. RF × RN

Quem declarou o vínculo está explicado na legenda geral (●, ◐, △). **Em todos os casos ◐, é a RN que cita o RF**: os RFs só citam RN-01, RN-04 e RN-05.

| RF \ RN | RN-01 | RN-02 | RN-03 | RN-04 | RN-05 | RN-06 | RN-07 | RN-08 | RN-09 | RN-10 |
|---------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| RF-01 | · | · | · | · | · | · | · | · | ◐ | ◐ |
| RF-02 | · | · | ◐ | · | · | ◐ | · | · | · | · |
| RF-03 | · | · | · | · | · | · | · | · | · | · |
| RF-04 | · | · | · | · | · | · | · | · | · | · |
| RF-05 | · | ◐ | · | · | · | · | · | △ | · | · |
| RF-06 | △ | · | · | · | △ | · | · | ◐ | · | · |
| RF-07 | · | · | · | · | ● | · | · | · | · | · |
| RF-08 | ● | · | · | · | · | · | · | · | · | · |
| RF-09 | · | △ | · | · | ◐ | · | · | · | · | · |
| RF-10 | · | · | · | ● | · | · | · | · | · | · |
| RF-11 | · | · | · | · | · | · | ◐ | · | · | △ |
| RF-12 | · | · | · | · | · | · | · | · | △ | · |
| **Nº de RFs** | 2 | 2 | 1 | 1 | 3 | 1 | 1 | 2 | 2 | 2 |

**Justificativa dos vínculos sugeridos (△):**

| Vínculo | Motivo |
|---------|--------|
| RF-05 → RN-08 | A **descrição** da RN-08 trata do intervalo mínimo de 30 s entre acionamentos do botão (comportamento do RF-05), embora o título e a política falem de login (ver I-22) |
| RF-06 → RN-01 | A RN-01 determina que vídeos expirados não podem ser listados nem baixados |
| RF-06 → RN-05 | A RN-05 exige marca d'água em todo vídeo disponibilizado para visualização e download |
| RF-09 → RN-02 | A RN-02 diz que o buffer é "associado à quadra/horário", que é exatamente o objeto do RF-09 |
| RF-11 → RN-10 | A RN-10 trata de **nova senha** (diferente da anterior e com complexidade mínima); isso é troca/recuperação de senha, não cadastro (ver I-23) |
| RF-12 → RN-09 | O RF-12 tem fluxo alternativo de "e-mail já cadastrado", regra definida pela RN-09 |

> **Regra transversal:** a **RN-06** (logout por inatividade de 30 min) se aplica a toda tela autenticada (RF-03, 04, 06, 07, 10, 12), mas está vinculada apenas ao RF-02. Tratada aqui como transversal, sem marcar célula.

---

## 4. RF × RNF

Nenhum RNF cita RFs e nenhum RF cita RNFs. Todos os vínculos abaixo são **sugestões (△)**, classificados como:

- **●** aplicação direta e medível no RF;
- **○** aplicação transversal (o RF tem tela ou interação que cai sob o RNF).

| RF \ RNF | RNF-01 Tema | RNF-02 Responsividade | RNF-03 Tempo de resposta | RNF-04 Segurança de acesso | RNF-05 Usabilidade |
|----------|:----------:|:--------------------:|:------------------------:|:-------------------------:|:------------------:|
| RF-01 | ○ | ○ | ○ | ○ | ● |
| RF-02 | ○ | ○ | ○ | ● | ● |
| RF-03 | ○ | ○ | ○ | ○ | ○ |
| RF-04 | ○ | ○ | ○ | ○ | ○ |
| RF-05 | · | · | · | ○ | · |
| RF-06 | ○ | ○ | ● | ○ | ● |
| RF-07 | ○ | ○ | ○ | ○ | ○ |
| RF-08 | · | · | · | · | · |
| RF-09 | · | · | · | ○ | · |
| RF-10 | ○ | ○ | ○ | ○ | ○ |
| RF-11 | ○ | ○ | ○ | ○ | ○ |
| RF-12 | ○ | ○ | ○ | ○ | ○ |

**Observações:**
- **RF-05, RF-08 e RF-09** não têm tela, então RNF-01, 02 e 05 não se aplicam. Nenhum RNF define, porém, o **tempo máximo para o replay ficar disponível** após o acionamento do botão.
- **RNF-03 (download < 10 s)** tem aplicação direta apenas no RF-06.
- **RNF-04 (20 usuários simultâneos)** é uma exigência do sistema inteiro. A parte de tentativas de login (5) aplica-se diretamente ao RF-02.

---

## 5. RN × RNF

| RN | RNF | Tipo | Observação |
|----|-----|:----:|------------|
| RN-01 | RNF-03 | ◐ | A RN-01 cita o RNF-03 como "métricas de armazenamento/desempenho", mas o RNF-03 trata de tempo de resposta e download, **não de armazenamento** (ver I-24) |
| RN-03 | RNF-04 | ◐ | Ambos definem **5 tentativas**. O valor está duplicado nos dois documentos (ver I-29) |
| RN-06 | RNF-04 | △ | Logout por inatividade é segurança de acesso, mas o RNF-04 não o menciona |
| RN-07, RN-10 | — | ❌ | Segurança de **credenciais** (código de recuperação, complexidade de senha) não tem RNF correspondente |
| RN-02, RN-04, RN-05, RN-08, RN-09 | — | · | Sem relação direta com RNFs |

---

## 6. Perfil × RF

Perfis conforme A2, com o acréscimo de **Visitante** (não autenticado) e **Sistema** (rotinas automáticas), que aparecem nos RFs mas não nos Perfis de Usuário.

| RF | Visitante | Usuário | Cliente | Administrador | Sistema |
|----|:---------:|:-------:|:-------:|:-------------:|:-------:|
| RF-01 Cadastro | ● | | | | |
| RF-02 Login | | ● | ○ | ○ | |
| RF-03 Métricas (admin) | | | | ● | |
| RF-04 Métricas (cliente) | | | ● | | |
| RF-05 Gravar vídeo | | ● | ○ | | |
| RF-06 Baixar vídeo | | ● | ○ | | |
| RF-07 Patrocinadores | | | ● | △ | |
| RF-08 Expiração de vídeos | | | | | ● |
| RF-09 Metadados do replay | | | | | ● |
| RF-10 Exclusão de vídeos | | | ● | ● | |
| RF-11 Recuperação de senha | | ● | ○ | ○ | |
| RF-12 Solicitação de gestor | | ● | | ● | |

Legenda desta matriz: ● ator no RF · ○ permitido pelos Perfis (herança do Cliente ou "todos os perfis solicitam senha") mas não citado no RF · △ **indefinido** nos Perfis (o Administrador gerencia quadras de qualquer Cliente, mas nada diz sobre patrocinadores).

---

## 7. Permissões dos Perfis → RF

Cobertura de cada permissão de A2 por RFs, e as regras associadas.

| Perfil | Permissão (A2) | RF | RN | RNF | Cobertura |
|--------|----------------|----|----|-----|:---------:|
| Usuário | Visualizar e editar o próprio perfil | — | — | — | ❌ |
| Usuário | Buscar, visualizar e baixar gravações | RF-06 | RN-08, RN-01, RN-05 | RNF-03 | ✅ |
| Todos | Solicitar recuperação ou alteração de senha | RF-11 | RN-07, RN-10 | RNF-04 | ⚠️ (só recuperação; falta alteração com sessão ativa) |
| Usuário | Solicitar cadastro como Cliente | RF-12 | RN-09 △ | — | ✅ |
| Cliente | Criar, editar e excluir as próprias quadras | — | — | — | ❌ |
| Cliente | Dashboard de métricas das próprias quadras | RF-04 | — | — | ⚠️ (métricas indefinidas) |
| Administrador | Criar, editar e excluir quadras de qualquer Cliente | — | — | — | ❌ |
| Administrador | Avaliar, aprovar ou indeferir solicitações | RF-12 | — | — | ✅ |
| Administrador | Dashboard consolidado | RF-03 | — | — | ⚠️ (métricas indefinidas) |
| *(só nos RFs)* Cliente, Administrador | Excluir vídeos | RF-10 | RN-04 | — | ⚠️ (não consta em A2) |
| *(só nos RFs)* Cliente | Cadastrar patrocinadores | RF-07 | RN-05 | — | ⚠️ (não consta em A2) |

---

## 8. Plano de Projeto → Requisitos

| Item do Plano (A1) | RF | RN | RNF | Cobertura |
|--------------------|----|----|-----|:---------:|
| 1.3 Fase 1 — software web com highlights e download | RF-05, RF-06, RF-08, RF-09 | RN-01, RN-02, RN-05, RN-08 | RNF-03 | ✅ |
| 1.3 Fase 1 — instalação da botoeira, fiação e microcontroladores | RF-05 (apenas o acionamento) | RN-02 | — | ⚠️ sem requisito de hardware/instalação |
| 1.3 Fase 2 — **Reserva de Horários** | — | — | — | ❌ |
| 2 Objetivo geral — aplicação conteinerizada | — | — | — | ❌ sem RNF de deploy |
| 2 Específico 1 — levantamento de RF e RNF na Sprint 1 | RF-01 a RF-12 | RN-01 a RN-10 | RNF-01 a RNF-05 | ✅ |
| 2 Específico 2 — banco de dados relacional | RF-09 (metadados), RF-08 (status expirado) | RN-01, RN-04 (log de auditoria) | — | ⚠️ sem modelo de dados |
| 2 Específico 3 — protótipo de alta fidelidade no Figma | RF-01 a RF-12 (telas) | — | RNF-01, RNF-02, RNF-05 | ⚠️ |
| 2 Específico 4 — deploy simplificado com Docker | — | — | — | ❌ |
| 4.2 Impacto — fluxo automático (botão → site) | RF-05, RF-09, RF-06 | RN-02, RN-05 | RNF-03 | ✅ |
| 4.3 Desafio — instalação de microcontroladores e botões | — | — | — | ❌ |
| 4.3 Desafio — fluxo não intuitivo | RF-06 (jornada) | — | RNF-05 | ✅ |
| 4.4 Continuidade pós-semestre | — | — | — | ❌ (ainda em estudo) |
| 5 Governança Git | — (processo) | — | — | ✅ ver README de Governança |

---

## 9. Cobertura Gherkin

### 9.1 Cenários por RF

| RF | Nº de cenários | Fluxos alternativos sem cenário ou cenários com problema |
|----|:--------------:|-----------------------------------------------------------|
| RF-01 | 2 | Campo obrigatório vazio; e-mail ou telefone duplicado (RN-09). O cenário de duplicidade usa **CPF**, que não é campo do cadastro |
| RF-02 | 2 | Cenário "senha incorreta" **sem `Então`**; campos obrigatórios vazios |
| RF-03 | 3 | Cenário de login inválido duplica o RF-02 e não tem `Dado` |
| RF-04 | 3 | Idem RF-03; aspa de fechamento ausente na mensagem |
| RF-05 | 3 | Intervalo mínimo de 30 s entre acionamentos (RN-08) |
| RF-06 | 4 | "Quadras indisponíveis" |
| RF-07 | 1 | "Patrocinador já existe"; "Total de patrocinadores preenchido" |
| RF-08 | 1 | — (✅) |
| RF-09 | 1 | Falha ao armazenar metadados (replay pendente para nova tentativa) |
| RF-10 | 1 | Tentativa de exclusão sem permissão (RN-04) |
| RF-11 | 6 | Código expirado e limites de tentativas/reenvios (RN-07); senha igual à anterior (RN-10) |
| RF-12 | 6 | — (✅; ver I-16 sobre o cenário de e-mail) |
| **Total** | **33** | |

### 9.2 Cobertura das regras de negócio por cenários

| RN | Cenário existente | Cobertura | Cenário que falta |
|----|-------------------|:---------:|-------------------|
| RN-01 | RF-08 "Quadra com vídeos relacionados" | ✅ | — |
| RN-02 | RF-05 "câmera em perfeito estado" | ⚠️ | Clipe com exatamente 30 s |
| RN-03 | — | ❌ | Bloqueio após 5 falhas; desbloqueio após 15 min |
| RN-04 | RF-10 "Exclusão manual autorizada" | ⚠️ | Usuário comum tenta excluir; registro de auditoria |
| RN-05 | RF-07 "Vinculação de patrocinador" | ⚠️ | Múltiplos patrocinadores; quadra sem patrocinador |
| RN-06 | — | ❌ | Logout após 30 min de inatividade; renovação por atividade |
| RN-07 | RF-11 "Código de verificação incorreto" | ⚠️ | Código expirado (10 min); 3 tentativas; 3 reenvios/hora; uso único |
| RN-08 | — | ❌ | Segundo acionamento antes de 30 s |
| RN-09 | RF-01 "CPF já existente" | ⚠️ | E-mail ou telefone duplicado |
| RN-10 | RF-11 "Nova senha não atende aos critérios" | ⚠️ | Nova senha igual à anterior; cada critério de complexidade |

**Resultado:** 1 de 10 RNs com cobertura completa · 6 parcial · 3 sem cenário.

### 9.3 Cobertura dos RNFs por testes

| RNF | Como é verificável | Teste previsto |
|-----|--------------------|:--------------:|
| RNF-01 | Alternar tema e verificar todas as telas | ❌ |
| RNF-02 | Conferir resoluções mobile, tablet e desktop | ❌ |
| RNF-03 | Medir resposta < 2 s e download < 10 s | ❌ |
| RNF-04 | 5 falhas bloqueiam; 20 usuários simultâneos (teste de carga) | ❌ |
| RNF-05 | Teste de usabilidade com ≥ 80% de sucesso sem auxílio | ❌ |

> RNFs não têm Gherkin. Sugere-se registrar o plano de teste de cada um (carga, usabilidade, responsividade) na coluna **Teste** da matriz mestre.

---

## 10. Índices reversos (análise de impacto)

Use para responder: **"se eu mudar X, o que precisa ser revisado?"**

### 10.1 Por Regra de Negócio

| RN | Tema | RF afetados | RNF | Perfis | Cenários a revisar |
|----|------|-------------|-----|--------|--------------------|
| RN-01 | Retenção de 7 dias | RF-08 ●, RF-06 △ | RNF-03 ◐ | Sistema, Usuário | RF-08 (1); RF-06 "horário sem vídeos" |
| RN-02 | Buffer de 30 s | RF-05 ◐, RF-09 △ | — | Usuário (jogador) | RF-05 (3) |
| RN-03 | Bloqueio por tentativas | RF-02 ◐ | RNF-04 ◐ | Todos que fazem login | RF-02 (2) |
| RN-04 | Exclusão manual | RF-10 ● | — | Cliente, Administrador | RF-10 (1) |
| RN-05 | Patrocinador / marca d'água | RF-07 ●, RF-09 ◐, RF-06 △ | — | Cliente | RF-07 (1); RF-09 (1) |
| RN-06 | Sessão de 30 min | RF-02 ◐ + todas as telas autenticadas | RNF-04 △ | Todos | — |
| RN-07 | Código de recuperação | RF-11 ◐ | — | Todos | RF-11 (3 primeiros cenários) |
| RN-08 | Intervalo de 30 s / login obrigatório | RF-06 ◐, RF-05 △ | — | Usuário | RF-06 (1); RF-05 (3) |
| RN-09 | E-mail e telefone únicos | RF-01 ◐, RF-12 △ | — | Visitante, Usuário | RF-01 (2); RF-12 "e-mail já existente" |
| RN-10 | Senha nova e complexa | RF-01 ◐, RF-11 △ | — | Visitante, Todos | RF-11 "senha não atende" |

### 10.2 Por Requisito Não Funcional

| RNF | RF afetados | RN relacionadas | Perfis citados no RNF | Observação |
|-----|-------------|-----------------|------------------------|------------|
| RNF-01 Tema | RF-01, 02, 03, 04, 06, 07, 10, 11, 12 (todas as telas) | — | Usuários e administradores (**Cliente omitido**) | Não há RF para a tela/preferência de tema |
| RNF-02 Responsividade | Todas as telas | — | Todos | — |
| RNF-03 Tempo de resposta | RF-06 ●, todas as telas | RN-01 ◐ | Todos | Condições normais e tamanho do vídeo indefinidos |
| RNF-04 Segurança | RF-02 ●, sistema inteiro | RN-03 ◐, RN-06 △ | Todos | Mistura segurança e capacidade |
| RNF-05 Usabilidade | RF-01 ●, RF-02 ●, RF-06 ●, demais telas ○ | — | Todos | Mensagens de erro claras ligam-se às mensagens dos Gherkin |

---

## 11. Achados da consolidação

A numeração continua a do README de Governança (I-01 a I-21). Sugere-se abrir uma Issue por item.

### 11.1 Situação dos achados anteriores após os novos documentos

| ID | Achado anterior | Situação |
|----|-----------------|----------|
| I-01 | Termo "Cliente" com dois sentidos | **Agravado**: RN-02, RN-08, RN-09 e RN-10 usam "cliente" para o jogador; RN-04 usa "Cliente Proprietário" para o dono |
| I-03 | CPF no Gherkin do RF-01 | **Esclarecido**: a RN-09 define unicidade por e-mail e telefone, não CPF. O Gherkin do RF-01 precisa ser reescrito |
| I-04 | RN-01, RN-04 e RN-05 não documentadas | **Resolvido**: agora existem em A4 |
| I-05 | Botão: "apertar" × "segurar 2 s" | **Aberto**: RN-02 confirma os 30 s, mas os 2 s seguem só no Gherkin do RF-05 |
| I-06 | Permissões sem RF (editar perfil, CRUD de quadras) | **Aberto** |
| I-11 | Limite de patrocinadores indefinido | **Aberto**: a RN-05 não define o limite |
| I-12 | `patrocinador_id` nos metadados do RF-09 | **Esclarecido**: a RN-05 vincula RF-09 ao patrocinador. Atualizar a descrição do RF-09 |
| I-13 | Prazo de 7 dias do RF-08 | **Resolvido** na RN-01. O RF-08 ainda não tem fluxo principal |
| I-14 | Motivo e log de auditoria no RF-10 | **Sustentado** pela RN-04. Falta refletir no fluxo do RF-10 e nos Perfis |
| I-15 | Critérios mínimos de senha | **Resolvido** na RN-10 (8 caracteres, maiúscula, minúscula, número e especial). Falta vincular ao RF-11 |
| — | Lacuna: RNFs não documentados | **Parcialmente resolvida**: RNF-01 a 05 criados. Seguem faltando Docker, privacidade de dados pessoais, disponibilidade/backup e capacidade de armazenamento |

### 11.2 Novos achados

| ID | Severidade | Artefatos | Problema | Ação sugerida |
|----|:----------:|-----------|----------|---------------|
| I-22 | Alta | RN-08 | **Título, descrição e política divergem.** O título fala de visualização/download só por cadastrados; a descrição trata do intervalo de 30 s entre acionamentos do botão; a política trata de criar conta e login (o item 3 é ininteligível) | Separar em duas RNs: (a) acesso a vídeos apenas para cadastrados (RF-06); (b) intervalo mínimo entre acionamentos (RF-05) |
| I-33 | Alta | RF-01, RF-05, RF-09, RF-06 | **Associação replay ↔ usuário indefinida.** O RF-01 tem como objetivo "associar os replays aos respectivos usuários", mas o RF-05 é um acionamento por botão físico sem identificação, o RF-09 não registra usuário e o RF-06 busca por cidade/quadra/horário | Decidir se replays são associados a usuários. Se sim, definir como; se não, remover o objetivo do RF-01 |
| I-26 | Alta | RN-09, RF-01 | A RN-09 (item 2) **permite várias contas para a mesma pessoa** com e-mails e telefones diferentes, o que conflita com a ideia de "identificar os usuários" (RF-01) e com a unicidade por CPF do Gherkin | Alinhar: definir qual é o identificador único do usuário |
| I-23 | Média | RN-10 | Vinculada ao RF-01 (cadastro), mas trata de "nova senha diferente da anterior", que é troca/recuperação de senha | Vincular ao RF-11 (e ao RF-01 apenas quanto à complexidade) |
| I-24 | Média | RN-01, RNF-03 | A RN-01 cita o RNF-03 como "métricas de armazenamento/desempenho", mas o RNF-03 só cobre tempo de resposta e download | Corrigir o vínculo ou criar RNF de capacidade de armazenamento |
| I-25 | Média | RN-05 | Contradição interna: a descrição diz que **todo** vídeo tem marca do patrocinador, mas o item 3 mantém a marca padrão quando não há patrocinador. O item 2 é ambíguo ("rodízio **ou** marca principal") | Definir uma única política e o limite de patrocinadores |
| I-27 | Média | RN-07, RF-11 | RN-07 ambígua: a descrição fala em 3 tentativas **e** 3 reenvios por hora; a política fala em "mais três tentativas em uma hora". O RF-11 não cita a RN-07 e não tem cenários de código expirado ou limites | Reescrever a RN-07 e criar os cenários |
| I-28 | Média | RN-06 | "Token de acesso é criado automaticamente após alguma atividade": o token deveria ser criado **no login** (RF-02) e renovado por atividade. Sem cenário nem RNF | Corrigir a política e criar cenário no RF-02 |
| I-30 | Média | RN-02, RF-05 | A RN-02 fala em botão "físico ou virtual"; o RF-05 só prevê o físico. O "segurar 2 s" está só no Gherkin | Alinhar a definição do botão e a RN |
| I-34 | Média | RF-01 a RF-12 | **Rastreabilidade unilateral:** os RFs citam só RN-01, 04 e 05. As RN-02, 03, 06, 07, 08, 09 e 10 não aparecem em nenhum RF | Adicionar o campo "Regras de negócio relacionadas" nos RFs (seção 6 do README) |
| I-29 | Baixa | RN-03, RNF-04 | Valor "5 tentativas" duplicado em dois documentos, com risco de divergência | O RNF-04 deve **referenciar** a RN-03, que fica como fonte única |
| I-31 | Baixa | RNF-01 | Cita "usuários e administradores" e omite o **Cliente** | Incluir o Cliente |
| I-32 | Baixa | RNF-04 | Mistura segurança de acesso e capacidade (20 usuários simultâneos) | Separar em dois RNFs |
| I-35 | Baixa | RNF-03, RNF-05 | Métricas sem condição de teste: "condições normais" e tamanho do vídeo/rede (RNF-03); número de participantes e tarefas do teste (RNF-05) | Definir ambiente e protocolo de medição |
| I-36 | Baixa | RN (arquivo) | Nomenclatura: título "Plataforma de Replays Esportivos" (projeto é TaGravado); "Administrador do Sistema" e "Matriz de Perfis de Acesso" não existem em A2; arquivo `regrasDeNegocioRF (1).md`; RN-06 a RN-10 fora do padrão de formatação (cabeçalhos e listas); erros de digitação ("popderá", "maiúsculo") | Padronizar |

### 11.3 Lacunas que continuam abertas

| Lacuna | Origem |
|--------|--------|
| Módulo de Reserva de Horários sem RF | A1 (Fase 2) |
| Hardware (botoeira, microcontroladores, integração com câmera) sem requisito | A1 |
| RF-03 e RF-04 não definem **quais métricas** exibir, e nenhuma RN as define | A3 |
| Aplicação da marca d'água (processamento do vídeo) sem RF próprio | RN-05, RF-07 |
| Notificações do RF-12 sem canal definido | A3 |
| Alteração de senha com sessão ativa (permitida em A2) sem RF | A2 |
| CRUD de quadras e edição de perfil sem RF | A2 |
| RNF de deploy (Docker), privacidade de dados pessoais, disponibilidade/backup | A1, A4, A5 |
| Tempo máximo para o replay ficar disponível após o clique | RF-05, RF-09 |

---

## 12. Como manter esta matriz

1. **Todo novo RF, RN ou RNF** entra primeiro na matriz mestre (seção 2) e na matriz cruzada correspondente (3, 4 ou 5), **no mesmo Pull Request** que cria o requisito.
2. **Vínculos devem ser bilaterais (●).** Ao criar um vínculo, citar a RN/RNF no RF **e** o RF na RN/RNF. Vínculos ◐ e △ são dívida de rastreabilidade a ser quitada.
3. **Colunas de execução** (Issue, PR, Teste, Status) são preenchidas pela pessoa responsável pela tarefa, usando a label do requisito (ex.: `RF-06`, `RN-05`) conforme o manual de rastreabilidade do professor.
4. **Antes de aprovar** uma mudança, consultar a seção 10 para identificar RFs, cenários e perfis afetados.
5. **Ao fechar uma Sprint**, revisar a coluna "Cenários" (seção 9) e atualizar a coluna "Teste".
6. Mudanças de glossário (ex.: resolução do I-01) devem ser aplicadas em A2, A3, A4 e A5 de uma só vez.

---

## 13. Histórico de versões

| Versão | Data | Descrição |
|--------|------|-----------|
| 0.1 | 18/10/2026 | Primeira consolidação: A1–A5, 12 RFs, 10 RNs, 5 RNFs, 33 cenários Gherkin; achados I-22 a I-36 |
