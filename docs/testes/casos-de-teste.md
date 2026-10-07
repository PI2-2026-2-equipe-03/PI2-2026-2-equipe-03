# Especificação e Execução de Testes

## 1. Plano de Teste
* **Projeto:** Plataforma de Captura e Gestão de Replays Esportivos
* **Equipe:** Equipe de Projeto Integrador II - UFC Campus Crateús
* **Responsável (QA):** Rick Farias
* **Data do Documento:** 20/09/2026 (Fechamento da Sprint 1)

---

## 2. Suítes de Teste
Agrupamento de casos de teste por funcionalidade e conjunto de requisitos associados.

| Código | Suíte | Descrição | Requisitos Relacionados |
| :--- | :--- | :--- | :--- |
| **ST-01** | Autenticação e Gestão de Contas | Testes de cadastro, autenticação, controle de sessão e bloqueio de segurança. | RF-01, RF-02, RNF-04 |
| **ST-02** | Captura e Associação de Replays | Testes de acionamento do botão físico/virtual, gravação de 30s e vinculação de metadados. | RF-05, RF-09 |
| **ST-03** | Busca, Visualização e Download | Testes de navegação por cidade, quadra, horário, streaming e download de vídeo. | RF-06, RNF-03 |
| **ST-04** | Gestão de Patrocinadores e Exclusão | Testes de cadastro de patrocinadores pelo cliente e exclusão manual/automática de replays. | RF-07, RF-08, RF-10 |
| **ST-05** | Dashboards e Métricas | Testes de exibição de painéis analíticos para administradores e clientes. | RF-03, RF-04 |

---

## 3. Casos de Teste

### CT-001 — Cadastro de Novo Usuário com Dados Válidos

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-001 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-01 Autenticação e Gestão de Contas |
| **Autor** | Rick |
| **Requisito Coberto** | RF-01 (Cadastro de usuário) |
| **Importância** | Alta |

* **Resumo:** Verifica se o sistema permite que um novo jogador crie sua conta preenchendo todos os dados obrigatórios no formulário.
* **Pré-condições:** Usuário não cadastrado previamente no banco de dados. Sistema e banco de dados operacionais no container.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a tela de cadastro da aplicação. | O formulário de cadastro é exibido contendo campos para Nome, E-mail, Senha e Confirmação de Senha. |
| **2** | Preencher Nome "João Silva", E-mail `joao.silva@exemplo.com` e Senha `Senha#2026`. | Os dados são inseridos corretamente nos campos correspondentes. |
| **3** | Clicar no botão "Cadastrar". | O sistema registra o usuário no banco de dados e exibe a mensagem de sucesso: "Cadastro realizado com sucesso!". |
| **4** | Tentar realizar o login com as credenciais recém-criadas. | O login é efetuado com sucesso e o usuário é direcionado para a tela principal. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Aprovado** | — | Cadastro e login subsequente executados sem falhas. |

---

### CT-002 — Bloqueio de Cadastro para E-mail Já Existente

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-002 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-01 Autenticação e Gestão de Contas |
| **Autor** | Rick |
| **Requisito Coberto** | RF-01 (Cadastro de usuário) |
| **Importância** | Média |

* **Resumo:** Verifica se o sistema impede a criação de duplicidade de contas informando que o e-mail já está em uso.
* **Pré-condições:** Usuário `joao.silva@exemplo.com` já cadastrado no banco de dados.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar o formulário de cadastro. | Formulário exibido. |
| **2** | Preencher o formulário utilizando o e-mail `joao.silva@exemplo.com`. | Campos preenchidos. |
| **3** | Clicar em "Cadastrar". | O sistema recusa o cadastro e exibe a mensagem de alerta: "E-mail já cadastrado no sistema". |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Aprovado** | — | Validação de unicidade de e-mail operando conforme o esperado. |

---

### CT-003 — Autenticação de Usuário e Redirecionamento

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-003 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-01 Autenticação e Gestão de Contas |
| **Autor** | Rick |
| **Requisito Coberto** | RF-02 (Login de usuário) |
| **Importância** | Alta |

* **Resumo:** Valida a autenticação de credenciais válidas e o correto direcionamento para a tela principal da aplicação.
* **Pré-condições:** Usuário `joao.silva@exemplo.com` com senha `Senha#2026` cadastrado.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Navegar até a tela de login. | Tela de login exibida com os campos de e-mail e senha. |
| **2** | Digitar `joao.silva@exemplo.com` e a senha `Senha#2026`. | Dados inseridos nos campos. |
| **3** | Clicar no botão "Entrar". | O sistema autentica o usuário e redireciona para o Dashboard principal. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Aprovado** | — | Sessão iniciada com sucesso. |

---

### CT-004 — Bloqueio de Acesso Após 5 Tentativas Incorretas de Login

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-004 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-01 Autenticação e Gestão de Contas |
| **Autor** | Rick |
| **Requisito Coberto** | RNF-04 (Segurança em Acesso) |
| **Importância** | Alta |

* **Resumo:** Valida se a política de segurança bloqueia temporariamente a conta após 5 tentativas consecutivas de senha inválida.
* **Pré-condições:** Usuário `joao.silva@exemplo.com` cadastrado e ativo.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Tentar realizar login com e-mail `joao.silva@exemplo.com` e senha errada por 4 vezes consecutivas. | O sistema exibe a mensagem "E-mail ou senha inválidos" a cada tentativa. |
| **2** | Realizar a 5ª tentativa com senha errada. | O sistema exibe o aviso: "Conta temporariamente bloqueada por motivo de segurança. Tente novamente mais tarde". |
| **3** | Tentar uma 6ª vez com a senha correta `Senha#2026`. | O sistema impede o login e mantém a mensagem de bloqueio por tempo determinado. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Reprovado** | CT-004-E1 | Falhou no passo 3: O sistema aceitou a senha correta na 6ª tentativa sem aplicar o bloqueio temporal exigido no RNF-04. Evidência registrada em `CT-004-E1`. |

---

### CT-005 — Gravação de Replay de 30 Segundos via Acionamento de Botão

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-005 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-02 Captura e Associação de Replays |
| **Autor** | Rick |
| **Requisito Coberto** | RF-05 (Gravar Vídeo) e RF-09 (Associar informações ao replay) |
| **Importância** | Alta |

* **Resumo:** Verifica se o acionamento do botão armazena os últimos 30 segundos do fluxo de vídeo e vincula os metadados de quadra, data e hora.
* **Pré-condições:** Câmera de vídeo ativa na quadra "Arena Crateús - Quadra 01" e serviço de gravação de buffer ativo.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Pressionar o botão de captura de jogada na quadra. | O sinal de acionamento é enviado ao servidor de mídia. |
| **2** | Aguardar o processamento do vídeo no backend. | O arquivo de vídeo dos últimos 30 segundos é gerado no banco de dados/storage. |
| **3** | Consultar o registro do vídeo recém-criado no banco/API. | O vídeo consta com as informações associadas: ID da quadra, Data atual e Hora do acionamento. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Bloqueado** | — | Teste depende de instalação física ainda pendente |

---

### CT-006 — Exclusão Automática de Vídeos Atingindo 7 Dias de Armazenamento

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-007 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-04 Gestão de Patrocinadores e Exclusão |
| **Autor** | Rick |
| **Requisito Coberto** | RF-08 (Tempo de disponibilidade dos vídeos) |
| **Importância** | Alta |

* **Resumo:** Verifica se a rotina do sistema remove automaticamente vídeos cuja data de criação ultrapasse 7 dias.
* **Pré-condições:** Registro de vídeo no banco com `data_criacao` ajustada para 8 dias atrás em ambiente de staging.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Executar a rotina agendada de limpeza de mídia (cron job). | O script de expiração varre o banco de dados identificando mídias > 7 dias. |
| **2** | Consultar a presença do vídeo no banco de dados e no storage de arquivos. | O registro e o arquivo físico de vídeo foram removidos permanentemente. |
| **3** | Tentar buscar o vídeo pela interface do usuário. | O vídeo não aparece nos resultados e a busca informa que o registro não está disponível. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Bloqueado** | — | Armazenamento de vídeos ainda pendente de ser implementado no sistema |

---

### CT-008 — Cadastro e Vinculação de Patrocinador por Cliente da Quadra

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-008 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-04 Gestão de Patrocinadores e Exclusão |
| **Autor** | Rick |
| **Requisito Coberto** | RF-07 (Cadastrar patrocinadores) |
| **Importância** | Média |

* **Resumo:** Valida o cadastro de patrocinadores pelo cliente dono de quadra e a associação às suas respectivas arenas.
* **Pré-condições:** Cliente autenticado com perfil de gestor de quadra.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar o menu "Patrocinadores" no painel do cliente. | A tela de gestão de patrocinadores é exibida. |
| **2** | Preencher Nome "Patrocinador X", foto da marca, duração de exibição "10s" e valor investido. | Os dados e a imagem são carregados no formulário. |
| **3** | Selecionar as quadras "Quadra 01" e "Quadra 02" e clicar em "Salvar". | O patrocinador é cadastrado e associado às quadras selecionadas. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Bloqueado** | — | Impossibilitado de testar pois telas ainda a serem implementadas |

---

### CT-009 — Exibição do Dashboard de Métricas do Administrador e do Cliente

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-009 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-05 Dashboards e Métricas |
| **Autor** | Rick |
| **Requisito Coberto** | RF-03 e RF-04 (Métricas para Admin e Cliente) |
| **Importância** | Média |

* **Resumo:** Verifica se o painel inicial exibe os indicadores consolidados de uso e replays ao realizar login como administrador/cliente.
* **Pré-condições:** Usuário com perfil de Administrador autenticado no sistema.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a tela inicial (Dashboard) com conta de Administrador. | Os cartões de métricas (total de replays gerados, downloads efetuados e quadras ativas) são carregados. |
| **2** | Verificar a presença de dados numéricos nos gráficos e indicadores. | Os valores refletem os registros presentes no banco de dados. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Aprovado** | — | Painéis de métricas carregados com dados agregados. |

---

### CT-010 — Alternância de Tema Claro / Escuro na Interface

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-010 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-06 Usabilidade, Interface e Desempenho |
| **Autor** | Rick |
| **Requisito Coberto** | RNF-01 (Tema escuro e Tema claro) |
| **Importância** | Baixa |

* **Resumo:** Valida a alternância dinâmica entre os modos visual claro e escuro sem perda de usabilidade ou contraste de elementos.
* **Pré-condições:** Usuário navegando em qualquer tela da aplicação.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Clicar no botão de alternância de tema no cabeçalho da página. | A interface altera imediatamente sua paleta de cores para o modo escuro (Dark Mode). |
| **2** | Clicar novamente no botão de alternância. | A interface retorna à paleta de cores clara (Light Mode). |
| **3** | Recarregar a página e verificar a preferência salva. | O tema selecionado permanece salvo nas preferências do navegador/usuário. |

#### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 06/10/2026 | **Aprovado** | — | Alternância e persistência de tema funcionando conforme RNF-01. |

---

## 4. Evidências de Teste
As capturas de tela e registros de falhas são armazenados na pasta `/docs/testes/evidencias/` seguindo o padrão de nomenclatura `CT-XXX-En`.

### CT-004-E1 — Falha no bloqueio temporal após 5 tentativas incorretas de login
* **Caminho da imagem:** `/docs/testes/evidencias/CT-004-E1.png`
* **Descrição da falha:** Na 6ª tentativa de login realizada imediatamente após 5 erros, o sistema aceitou a senha válida sem aplicar o bloqueio temporário exigido pela política de segurança (RNF-04).
* **Issue de Defeito Vinculada:** `#18` no GitHub Projects.

---

## 5. Legendas e Regras de Qualidade

### Status da Execução
* **Aprovado:** Todos os passos foram executados exatamente conforme o resultado esperado.
* **Reprovado:** Qualquer passo divergiu do resultado esperado (exige obrigatoriamente a abertura de uma Issue de defeito no GitHub e registro da evidência).
* **Bloqueado:** Impossibilidade de execução devido à indisponibilidade de ambiente, container ou dependência de caso reprovado.
* **Não executado:** Caso especificado, mas ainda pendente de execução no ciclo.

### Status do Caso de Teste
* **Rascunho** · **Em revisão** · **Final** · **Obsoleto**

> **Regra Obrigatória do Manual:** Todo caso marcado como **Reprovado** deve gerar imediatamente uma Issue no GitHub Projects com a label de defeito. O número da issue deve ser inserido na coluna *Defeito* da tabela de execução e a captura do erro deve ser armazenada na pasta `/docs/testes/evidencias/`.
