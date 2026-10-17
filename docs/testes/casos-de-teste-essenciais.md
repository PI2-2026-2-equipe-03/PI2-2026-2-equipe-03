# Especificação e Execução de Casos de Teste — Requisitos Essenciais (Sprint 2 / Q2-01)

## 1. Plano de Teste
| Campo | Informação |
| :--- | :--- |
| **Projeto** | Sistema de Captura e Gestão de Replays Esportivos |
| **Equipe** | Projeto Integrador UFC Campus Crateús |
| **Responsável (QA)** | Rick Farias |
| **Sprint** | Sprint 3 |
| **Data de Execução** | 17/10/2026 |

---

## 2. Suítes de Teste

| Código | Suíte de Teste | Requisitos Cobertos | Descrição |
| :---: | :--- | :---: | :--- |
| **ST-01** | Gestão de Acesso e Contas | `RF-01`, `RF-02`, `RNF-04` | Testes de cadastro de atleta, login, emissão de JWT e controle de acesso. |
| **ST-02** | Captura e Processamento de Replay | `RF-05`, `RF-09`, `RN-02` | Testes de acionamento de botão, gravação do buffer de 30s e vínculo de metadados. |
| **ST-03** | Consulta, Download e Manutenção | `RF-06`, `RF-08`, `RN-01`, `RNF-03` | Testes de busca por filtros, download em tempo hábil e rotina de limpeza de 7 dias. |

---

## 3. Especificação e Execução dos Casos de Teste (RFs Essenciais)

### CT-001 — Cadastro de Novo Atleta com Dados Válidos

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-001 |
| **Suíte de Teste** | ST-01 Gestão de Acesso e Contas |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-01` (Cadastro de Usuário / Atleta) |
| **Importância** | Essencial |

* **Resumo:** Validar o cadastro de um novo atleta/usuário na plataforma fornecendo nome, e-mail único, telefone e senha válida.
* **Pré-condições:** Aplicação Frontend e Backend rodando em contêineres Docker; Banco de dados ativo sem registro prévio do e-mail `atleta.teste@email.com`.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a tela de cadastro na rota `/cadastro`. | Formulário de cadastro exibido com campos Nome, E-mail, Telefone e Senha. |
| **2** | Preencher: Nome "Carlos Eduardo", E-mail "atleta.teste@email.com", Telefone "(88) 99888-7766" e Senha "Senha@123". | Todos os campos preenchidos corretamente sem erros de validação sintática. |
| **3** | Clicar no botão "Cadastrar". | O sistema processa o cadastro, retorna HTTP 201 Created, redireciona para `/login` e exibe o alerta "Conta criada com sucesso!". |
| **4** | Verificar a persistência no banco de dados. | Registro criado na tabela `usuarios` com a senha devidamente criptografada (hash BCrypt). |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Aprovado** | — | Cadastro concluído com sucesso e hash de senha verificado no banco. |

---

### CT-002 — Autenticação de Usuário e Geração de Token JWT

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-002 |
| **Suíte de Teste** | ST-01 Gestão de Acesso e Contas |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-02` (Autenticação e Login) e `RNF-04` (Segurança) |
| **Importância** | Essencial |

* **Resumo:** Verificar se o sistema autentica um usuário ativo, gera o token de sessão JWT e permite o acesso ao painel do atleta.
* **Pré-condições:** Usuário `atleta.teste@email.com` previamente cadastrado e ativo com a senha `Senha@123`.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a tela de login na rota `/login`. | Tela de login exibida com os campos de E-mail e Senha. |
| **2** | Informar E-mail "atleta.teste@email.com" e Senha "Senha@123". | Campos preenchidos corretamente. |
| **3** | Clicar no botão "Entrar". | A API valida as credenciais e retorna HTTP 200 contendo o `token` Bearer JWT no payload. |
| **4** | Validar o redirecionamento. | O Frontend armazena o token de forma segura e redireciona o atleta para a tela de dashboard/replays. |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Reprovado** | Issue #20 | Autenticação realizada, porém token JWT sem retorno no cabeçalho das requisições. |

---

### CT-003 — Acionamento e Gravação de Replay de 30 Segundos

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-003 |
| **Suíte de Teste** | ST-02 Captura e Processamento de Replay |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-05` (Acionamento e Gravação de Replay) e `RN-02` (Buffer de 30s) |
| **Importância** | Essencial |

* **Resumo:** Validar o corte do buffer circular de vídeo dos últimos 30 segundos na quadra após o acionamento do botão físico ou virtual.
* **Pré-condições:** Câmera da "Quadra 1 - Arena Crateús" ativa transmitindo para o buffer em memória; Atleta conectado.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Pressionar o botão de acionamento do replay para a "Quadra 1". | O sinal de acionamento é enviado ao serviço de captura. |
| **2** | Aguardar o processamento do clipe pelo Backend. | O sistema extrai exatamente os 30 segundos anteriores do buffer e encoda o arquivo `.mp4`. |
| **3** | Checar a geração do arquivo de mídia no storage. | O clipe de vídeo é salvo no volume configurado do container. |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Bloqueado** | — | Sem as condições necessárias para realizar Caso de Teste até o momento. Necessita da instalação física. |

---

### CT-004 — Vinculação Automática de Metadados ao Replay

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-004 |
| **Suíte de Teste** | ST-02 Captura e Processamento de Replay |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-09` (Associar Metadados ao Replay) |
| **Importância** | Essencial |

* **Resumo:** Verificar se o sistema associa automaticamente os metadados de localização, quadra, data/hora e id do patrocinador ativo ao registro do vídeo recém-gerado.
* **Pré-condições:** Replay acionado na "Quadra 1" da cidade "Crateús" com patrocinador ativo ID #3.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Finalizar o salvamento do clipe gerado no CT-003. | O serviço do Backend grava o registro no banco de dados. |
| **2** | Consultar no banco de dados a tabela `replays` referente ao vídeo gerado. | O registro contém os campos: `cidade="Crateús"`, `quadra="Quadra 1"`, `data_hora` atual e `patrocinador_id=3`. |
| **3** | Realizar requisição `GET /api/replays/{id}` via API. | O JSON retornado traz a estrutura completa de metadados vinculados ao replay. |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Bloqueado** | — | Pendente de implementação |

---

### CT-005 — Busca de Vídeos e Download de MP4 dentro do Limite de Tempo

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-005 |
| **Suíte de Teste** | ST-03 Consulta, Download e Manutenção |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-06` (Buscar e Baixar Vídeos) e `RNF-03` (Tempo de resposta < 10s) |
| **Importância** | Essencial |

* **Resumo:** Testar o filtro de replays por cidade/quadra/data e validar o download do arquivo de vídeo respeitando a métrica de desempenho de menos de 10 segundos.
* **Pré-condições:** Mídia gravada no CT-003 disponível e associada à cidade "Crateús" e quadra "Quadra 1".

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a tela de busca de vídeos no Frontend. | Formulário com filtros de Cidade, Quadra e Data exibido. |
| **2** | Selecionar Cidade "Crateús", Quadra "Quadra 1" e a Data de hoje. Clicar em "Buscar". | A API retorna a lista com a miniatura, horário e o botão de download do vídeo. |
| **3** | Clicar no botão "Baixar Vídeo" e cronometrar o tempo até o início da transferência do arquivo `.mp4`. | O download inicia no navegador em tempo inferior a 10 segundos (atendendo ao `RNF-03`). |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Bloqueado** | — | Pedente de implementação |

---

### CT-006 — Execução da Rotina de Exclusão Automática por Expiração (7 Dias)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-006 |
| **Suíte de Teste** | ST-03 Consulta, Download e Manutenção |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-08` (Exclusão Automática) e `RN-01` (Prazo de Retenção de 7 Dias) |
| **Importância** | Essencial |

* **Resumo:** Verificar se a rotina automática (cronjob) remove do storage e do banco de dados os replays cuja data de criação ultrapassar 168 horas (7 dias).
* **Pré-condições:** Vídeo de teste ID #999 inserido no banco com `data_hora` modificada para 8 dias atrás (192 horas) e arquivo mantido no storage.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Executar o comando da rotina de limpeza de mídias expiradas no Backend (`npm run cron:cleanup`). | A rotina é iniciada, varre os registros de mídia com mais de 7 dias e executa a limpeza. |
| **2** | Verificar a remoção do arquivo no volume/storage do container. | O arquivo de vídeo físico do ID #999 é deletado do disco. |
| **3** | Consultar a busca de vídeos no Frontend para a quadra do vídeo expirado. | O vídeo ID #999 não é mais retornado no resultado das buscas. |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Reprovado** | Issue #21 | Rotina de exclusão não adicionada no banco de dados. Script não existe. |

---

## 4. Evidências de Teste de Falhas

### CT-006-E1 — Falha na Remoção Física do Arquivo no Storage (Issue #20)
* **Caminho da Evidência:** `/docs/testes/evidencias/CT-006-E1.png`
* **Descrição do Erro:** Ao executar a rotina de expiração (RF-08 / RN-01), o script executou a query `UPDATE replays SET status='expirado'` no banco de dados, porém isso não garante a exclusão do vídeo. Script de limpeza não existe.

### CT-002-E1: Token JWT não gerado ao realizar login na sessão (Issue #21)
**Caminho da Imagem:** `docs/testes/evidencias/CT-002-E1.png`, `docs/testes/evidencias/CT-002-E1-1.png` e `docs/testes/evidencias/CT-002-E1-2.png`
* **Descrição da falha:** Ao realizar o login, no cabeçalho de resposta deveria ser gerado um Token Temporário, o que não acontece.