# Relatório de Análise e Qualidade dos Requisitos (QA / Testes)

**Projeto:** Plataforma de Captura e Gestão de Replays Esportivos  
**Disciplina:** CRT0432/CRT0428 - Projeto Integrador II / IV  
**Curso:** Sistemas de Informação / Ciência da Computação (UFC Campus Crateús)  
**Autor (QA):** Responsável de QA / Testes  
**Data da Análise:** 13/09/2026  
**Sprint:** Sprint 1  
**Documento Analisado:** `Requisitos Funcionais e NFuncionais.pdf` e `Documento Integrador.pdf`  

---

## 1. Resumo Executivo

Este relatório apresenta a avaliação crítica de qualidade, clareza, testabilidade e coerência dos **Requisitos Funcionais (RFs)** e **Requisitos Não Funcionais (RNFs)** elicitados para o sistema. 

A análise foi conduzida segundo os critérios de validação da Seção 4.2 do Documento Integrador da UFC Campus Crateús, que orienta a checagem de:
1. **Clareza e Compreensão** (O que pode ser aprimorado?);
2. **Verificabilidade e Testabilidade** (O requisito é mensurável/testável?);
3. **Ausência de Conflitos** (Existe colisão ou ambiguidade com outros requisitos?).

### Diagnóstico Geral
* **Total de Requisitos Funcionais Analisados:** 10 (RF-01 a RF-09, incluindo a duplicação do código RF-09 no documento original).
* **Total de Requisitos Não Funcionais Analisados:** 5 (RNF-01 a RNF-05).
* **Ponto Crítico Identificado:** Erro de duplicação do identificador `RF-09` no documento original (atribuído tanto a "Associar informações ao replay" quanto a "Exclusão de vídeos"), além de termos vagos nos dashboards de métricas (RF-03 e RF-04).

---

## 2. Análise Detalhada dos Requisitos Funcionais (RFs)

### 🔹 RF-01: Cadastro de Usuário
* **Prioridade:** Essencial | **Ator:** Usuário
* **Descrição do Documento:** Permite que novos usuários realizem seu cadastro para acessar as funcionalidades relacionadas aos replays disponíveis na plataforma.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Parcialmente claro.* O fluxo principal e alternativos estão definidos, mas não especifica quais campos são obrigatórios (ex: Nome, E-mail, Senha, CPF/Telefone). **Melhoria:** Detalhar a lista de campos obrigatórios e regras de validação (ex: formato de e-mail e requisitos de senha).
  * **2. É verificável e testável?**  
    *Sim.* É possível criar casos de teste automatizados ou manuais enviando dados válidos, dados incompletos e e-mails duplicados para validar as mensagens de erro.
  * **3. Possui conflito com outro requisito?**  
    *Não.* Alinha-se perfeitamente com o RF-02 (Login de Usuário).

---

### 🔹 RF-02: Login de Usuário
* **Prioridade:** Essencial | **Ator:** Usuário
* **Descrição do Documento:** Permite que usuários cadastrados realizem login informando e-mail e senha para acessar a área principal.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Sim, claro.* O fluxo de autenticação e validação está adequado. **Melhoria:** Especificar a permanência da sessão (token JWT/cookies) e se haverá fluxo de "Esqueci minha senha".
  * **2. É verificável e testável?**  
    *Sim.* Testável com combinações de credenciais válidas, inválidas e campos em branco.
  * **3. Possui conflito com outro requisito?**  
    *Não.* Integra-se diretamente ao RNF-04 (bloqueio por tentativas incorretas).

---

### 🔹 RF-03: Métricas para o Administrador
* **Prioridade:** Importante | **Ator:** Administrador
* **Descrição do Documento:** Exibe informações relevantes para o administrador em um dashboard na tela inicial.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Não.* O termo "informações relevantes" é extremamente vago e contraria a boa prática de levantamento. **Melhoria:** Listar exatamente quais métricas o Administrador deve ver (ex: total de replays gerados no mês, quantidade de clientes ativos, total de downloads e quadras cadastradas).
  * **2. É verificável e testável?**  
    *Não na forma atual.* Como as métricas não estão especificadas, o teste fica subjetivo. Só se tornará testável após a definição explícita dos indicadores.
  * **3. Possui conflito com outro requisito?**  
    *Possível sobreposição com o RF-04.* É necessário definir claramente a separação de escopo entre o Dashboard do Admin e o Dashboard do Cliente.

---

### 🔹 RF-04: Métricas para o Cliente
* **Prioridade:** Importante | **Ator:** Cliente (Dono de Quadra/Arena)
* **Descrição do Documento:** Exibe informações relevantes para o cliente em um dashboard na tela inicial.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Não.* Apresenta a mesma fragilidade do RF-03. **Melhoria:** Especificar os indicadores de interesse do cliente (ex: horários de pico de gravação da sua quadra, visualizações dos patrocinadores cadastrados, histórico de downloads dos replays da sua arena).
  * **2. É verificável e testável?**  
    *Não na forma atual.* Requer especificação concreta dos campos para elaboração dos critérios de aceite de QA.
  * **3. Possui conflito com outro requisito?**  
    *Não conflita*, mas exige controle estrito de permissões (RBAC) para impedir que um cliente veja métricas de quadras pertencentes a outros clientes.

---

### 🔹 RF-05: Gravar Vídeo (Acionamento do Replay)
* **Prioridade:** Essencial | **Ator:** Usuário / Cliente
* **Descrição do Documento:** Acionamento de botão no qual a câmera da quadra armazena os últimos 30 segundos gravados.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Parcialmente claro.* Há ambiguidade de atores (o texto diz "Cliente aperta o botão", mas a tabela indica "Usuário"). **Melhoria:** Esclarecer se o botão é físico (na quadra) ou virtual (no aplicativo móvel/web), além de definir um tempo mínimo de intervalo (cooldown) entre dois acionamentos consecutivos.
  * **2. É verificável e testável?**  
    *Sim.* Testável acionando o botão e verificando a geração de um arquivo de vídeo com duração de exatamente 30 segundos e seu salvamento.
  * **3. Possui conflito com outro requisito?**  
    *Não.* Depende diretamente do RF-09 (Associar informações ao replay).

---

### 🔹 RF-06: Baixar Vídeo
* **Prioridade:** Essencial | **Ator:** Usuário
* **Descrição do Documento:** Permite que o usuário acesse o site, busque por Cidade -> Quadra -> Horário, visualize o vídeo e realize o download.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Sim, muito claro.* O fluxo de navegação e busca está bem encadeado. **Melhoria:** Especificar o formato do arquivo para download (ex: `.mp4`) e a necessidade de login prévio.
  * **2. É verificável e testável?**  
    *Sim.* Testável realizando buscas com filtros existentes/inexistentes e executando o download (conectado ao RNF-03: tempo < 10s).
  * **3. Possui conflito com outro requisito?**  
    *Comportamento de exceção com RF-08 e Exclusão Manual:* Caso um vídeo tenha sido excluído por ultrapassar 7 dias (RF-08) ou manualmente (exclusão pelo cliente), o sistema deve tratar graciosamente a busca sem quebrar a tela.

---

### 🔹 RF-07: Cadastrar Patrocinadores
* **Prioridade:** Importante | **Ator:** Cliente
* **Descrição do Documento:** O cliente cadastra os patrocinadores da sua quadra em específico (Nome, Foto, Duração, Valor).
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Sim, claro.* Os campos estão bem especificados. **Melhoria:** Detalhar onde e como a marca do patrocinador é exibida (ex: marca d'água inserida no vídeo gerado ou banner na tela de visualização do replay).
  * **2. É verificável e testável?**  
    *Sim.* Testável através da inclusão, edição e associação de patrocinadores às quadras do cliente.
  * **3. Possui conflito com outro requisito?**  
    *Não.*

---

### 🔹 RF-08: Tempo de Disponibilidade dos Vídeos (Exclusão Automática)
* **Prioridade:** Importante | **Ator:** Sistema
* **Descrição do Documento:** Após 7 dias, os vídeos armazenados serão excluídos automaticamente pelo sistema.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Sim, claro.* **Melhoria:** Especificar o horário de execução da rotina automática (cron job) de limpeza e se a exclusão é física (remoção do disco) ou lógica (soft delete).
  * **2. É verificável e testável?**  
    *Sim.* Testável simulando registros com data de gravação superior a 7 dias e verificando a rotina de exclusão.
  * **3. Possui conflito com outro requisito?**  
    *Não.* Complementa a exclusão manual de vídeos pelo cliente.

---

### 🔹 RF-09 (Versão A): Associar Informações ao Replay
* **Prioridade:** Essencial | **Ator:** Sistema
* **Descrição do Documento:** O sistema associa cada replay gerado às informações da quadra, data e horário da solicitação.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Sim, excelente.* É o requisito mais completo do documento, possuindo objetivos e fluxo de exceção para falha de persistência.
  * **2. É verificável e testável?**  
    *Sim.* Testável inspecionando os metadados gravados na tabela de vídeos após a geração do replay.
  * **3. Possui conflito com outro requisito?**  
    *Conflito de Identificador:* O código `RF-09` foi reutilizado no documento original. **Ação do QA:** Manter este como `RF-09`.

---

### 🔹 RF-09 (Versão B / Sugestão RF-10): Exclusão Manual de Vídeos
* **Prioridade:** Desejável | **Ator:** Cliente
* **Descrição do Documento:** Permite que o cliente exclua manualmente um vídeo específico a qualquer momento.
* **Análise de QA:**
  * **1. É claro? O que pode melhorar?**  
    *Parcialmente claro.* Há uma inconsistência no texto ("cliente com sua conta de administrador loga em sua conta"). **Melhoria:** Esclarecer se a permissão é do Cliente (dono da quadra) ou do Administrador geral. Renomear o código para `RF-10`.
  * **2. É verificável e testável?**  
    *Sim.* Testável executando a exclusão manual e confirmando que o vídeo deixa de ser listado na busca do usuário (RF-06).
  * **3. Possui conflito com outro requisito?**  
    *Conflito Crítico de Rastreabilidade:* Possui o mesmo identificador do requisito anterior (`RF-09`). **Recomendação imediata:** Alterar este requisito para **`RF-10`** para não quebrar o script de coleta do professor no GitHub.

---

## 3. Análise Detalhada dos Requisitos Não Funcionais (RNFs)

### 🔸 RNF-01: Tema Escuro e Tema Claro
* **Métrica do Documento:** Usuário ou Admin podem mudar o tema do site para tema claro ou tema escuro.
* **Análise de QA:**
  * **É claro e testável?** *Sim.* **Melhoria:** Especificar a persistência da escolha no navegador (`localStorage`) ou perfil do usuário.
  * **Conflitos:** Nenhum.

---

### 🔸 RNF-02: Responsividade
* **Métrica do Documento:** As telas do sistema se adaptam ao dispositivo que o usuário utiliza (mobile, desktop e tablet).
* **Análise de QA:**
  * **É claro e testável?** *Sim.* **Melhoria:** Definir os *breakpoints* exatos em pixels (ex: Mobile < 768px, Tablet 768px-1024px, Desktop > 1024px).
  * **Conflitos:** Nenhum.

---

### 🔸 RNF-03: Tempo de Resposta
* **Métrica do Documento:** Tempo de resposta < 2 segundos para telas e < 10 segundos para download de vídeos.
* **Análise de QA:**
  * **É claro e testável?** *Sim, excelente.* Apresenta métricas numéricas objetivas e altamente testáveis através das ferramentas do navegador ou testes de carga.
  * **Conflitos:** Nível de exigência que deve ser monitorado em conjunto com o RNF-04.

---

### 🔸 RNF-04: Segurança em Acesso e Desempenho
* **Métrica do Documento:** Até 5 tentativas de login incorretas antes do bloqueio por tempo determinado; suporte a 20 usuários simultâneos sem degradação perceptível.
* **Análise de QA:**
  * **É claro e testável?** *Parcialmente claro.* A expressão "tempo determinado" deve ser quantificada (ex: bloqueio de 15 minutos). A métrica de 20 usuários simultâneos é testável com ferramentas como Apache JMeter ou K6.
  * **Conflitos:** Requer implementação de rotina de desbloqueio automático ou via e-mail.

---

### 🔸 RNF-05: Usabilidade
* **Métrica do Documento:** Interface intuitiva sem necessidade de treinamento prévio; mensagens de erro claras orientando a correção.
* **Análise de QA:**
  * **É claro e testável?** *Parcialmente.* "Interface intuitiva" é subjetivo. Contudo, a exigência de "mensagens de erro claras" é perfeitamente testável via testes de validação de formulário.
  * **Conflitos:** Nenhum.

---

## 4. Plano de Ação e Recomendações para a Equipe

1. **Correção Imediata de Rastreabilidade no GitHub:**
   * Ajustar a duplicação do `RF-09` criando a label **`RF-10`** no repositório para a funcionalidade de "Exclusão Manual de Vídeos".
2. **Refinamento dos Dashboards (RF-03 e RF-04):**
   * Reunir a equipe de Analistas com o cliente para detalhar os campos exatos dos dashboards de Admin e Cliente antes da codificação do Backend.
3. **Parametrização do RNF-04:**
   * Definir que o tempo de bloqueio após 5 tentativas incorretas será de **15 minutos**.
4. **Vínculo das Issues da Sprint 1:**
   * Vincular cada nova issue do quadro a um identificador validado (`RF-01` a `RF-10` e `RNF-01` a `RNF-05`) para garantir o cômputo integral da pontuação da equipe pelo script automático do professor.
