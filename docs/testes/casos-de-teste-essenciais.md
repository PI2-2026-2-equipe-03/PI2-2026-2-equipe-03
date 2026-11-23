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
 **ST-04** | Gestão e Solicitação de Perfil Gestor | `RF-12`, `RF-13`, `RNF-04` | Testes de solicitação de perfil gestor de quadra pelo cliente/atleta e fluxo de moderação (aprovação/reprovação) pelo Administrador. |

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

### CT-007 — Envio de Solicitação de Cadastro como Gestor de Quadra com Dados Válidos

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-007 |
| **Suíte de Teste** | ST-04 Gestão e Moderação de Gestores de Quadra |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-12` (Solicitação de Cadastro como Gestor de Quadra) |
| **Importância** | Essencial |

* **Resumo:** Validar se um usuário autenticado com perfil Atleta (USR) consegue enviar uma solicitação completa para se tornar gestor de quadra, gerando registro pendente de análise no sistema.
* **Pré-condições:** Usuário com perfil Atleta (USR) devidamente autenticado e logado no sistema; nenhuma solicitação anterior pendente vinculada a este usuário.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar o menu de navegação e clicar em "Solicitar Gestor" (rota `/app/solicitar-gestor`). | Formulário exibido contendo campos de identificação: CPF, CNPJ, Razão Social / Nome da Arena, Quantidade de Quadras e Endereço. |
| **2** | Preencher todos os campos com dados válidos: CPF "123.456.789-00", CNPJ "12.345.678/0001-99", Razão Social "Arena Crateús Beach Sports LTDA", Quantidade de Quadras "2" e Endereço comercial completo. | Campos preenchidos sem mensagens de erro de formato ou validação sintática. |
| **3** | Clicar no botão "Enviar Solicitação". | O sistema processa o pedido, retorna HTTP 201 Created e exibe a mensagem: "Solicitação enviada. Aguarde a análise dos administradores.". |
| **4** | Consultar a persistência da solicitação no banco de dados. | Registro criado com status `"PENDING"` associado ao ID do usuário solicitante. |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 08/11/2026 | Aprovado | - | Solicitação devidamente registrada no banco de dados com o status correto. |

---

### CT-008 — Bloqueio de Solicitação de Gestor em Duplicidade

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-008 |
| **Suíte de Teste** | ST-04 Gestão e Moderação de Gestores de Quadra |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-12` (Solicitação de Cadastro como Gestor de Quadra) |
| **Importância** | Essencial |

* **Resumo:** Garantir que o sistema rejeite uma nova solicitação de gestor caso o usuário já possua uma solicitação com status pendente de análise.
* **Pré-condições:** Usuário autenticado que já concluiu com sucesso o envio do CT-007 (solicitação pendente ativa no sistema).

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Tentar acessar novamente a tela de solicitação de gestor em `/app/solicitar-gestor`. | O sistema identifica o pedido existente e desabilita o formulário ou exibe status "Em análise". |
| **2** | Submeter uma nova requisição via interface ou chamada direta `POST /api/manager-requests`. | A API barra a criação, retornando HTTP 409 Conflict (ou 400 Bad Request). |
| **3** | Verificar a mensagem de feedback na tela. | Mensagem exibida: "Já existe uma solicitação pendente para este usuário.". |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 08/11/2026 | Aprovado | - | Mensagem de "já existe uma solicitação pendente" está sendo aplicada corretamente. |

---

### CT-009 — Aprovação de Solicitação de Gestor pelo Administrador

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-009 |
| **Suíte de Teste** | ST-04 Gestão e Moderação de Gestores de Quadra |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-13` (Confirmação de Cadastro como Gestor de Quadra) e `RF-12` |
| **Importância** | Essencial |

* **Resumo:** Validar a aprovação da solicitação por um Administrador (ADM) e garantir a elevação imediata do perfil do solicitante de Atleta (USR) para Gestor/Cliente (CLI), liberando o acesso ao painel `/admin`.
* **Pré-condições:** Usuário Administrador (ADM) autenticado no sistema; solicitação pendente gerada no CT-007.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar o painel administrativo na rota `/admin` e abrir a listagem de solicitações de gestores. | A solicitação pendente do CT-007 é listada com os dados da arena e do solicitante. |
| **2** | Clicar na ação "Aprovar Solicitação" referente ao solicitante. | O sistema envia a requisição de atualização (`PATCH /api/manager-requests/{id}` com payload `{ status: "APPROVED" }`). |
| **3** | Validar o retorno do sistema e o banco de dados. | Retorno HTTP 200 OK com mensagem de confirmação; o campo `role` do usuário no banco passa de `'USR'` para `'CLI'`. |
| **4** | Realizar login com as credenciais do usuário recém-aprovado e tentar acessar a rota `/admin`. | O usuário tem o acesso liberado ao painel administrativo de quadras e patrocinadores (`<RequireRole roles={['ADM', 'CLI']}>`). |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 08/11/2026 | Bloqueado | - | Como todas as senhas de admin no seed estão em hash, nao consigo entrar numa conta admin. |

---

### CT-010 — Reprovação / Indeferimento de Solicitação de Gestor pelo Administrador

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-010 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-04 Gestão e Moderação de Gestores de Quadra |
| **Autor** | Rick |
| **Requisito Coberto** | `RF-13` (Confirmação de Cadastro como Gestor de Quadra) e `RF-12` |
| **Importância** | Essencial |

* **Resumo:** Verificar se a rejeição de uma solicitação por dados incorretos ou não comprovação de posse da quadra mantém o usuário no perfil Atleta (USR) sem conceder permissões administrativas.
* **Pré-condições:** Usuário Administrador (ADM) logado; usuário comum com solicitação cadastrada com dados inconsistentes.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a listagem de solicitações pendentes no painel administrativo. | Solicitação inconsistente exibida para análise. |
| **2** | Clicar na opção "Reprovar / Indeferir" informando o motivo da recusa. | O sistema envia a atualização com `status: "REJECTED"`. |
| **3** | Validar a persistência do status no sistema. | O registro tem o status atualizado para rejeitado e o perfil do usuário permanece estritamente como Atleta (`USR`). |
| **4** | Tentar acessar diretamente a URL `/admin` com a conta do usuário reprovado. | O sistema barra a navegação com tela de acesso negado / Forbidden ou redireciona para `/app`. |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 08/11/2026 | Bloqueado | - | Como todas as senhas de admin no seed estão em hash, nao consigo entrar numa conta admin. |

---

## 4. Evidências de Teste de Falhas

### CT-006-E1 — Falha na Remoção Física do Arquivo no Storage (Issue #20)
* **Caminho da Evidência:** `/docs/testes/evidencias/CT-006-E1.png`
* **Descrição do Erro:** Ao executar a rotina de expiração (RF-08 / RN-01), o script executou a query `UPDATE replays SET status='expirado'` no banco de dados, porém isso não garante a exclusão do vídeo. Script de limpeza não existe.

### CT-002-E1: Token JWT não gerado ao realizar login na sessão (Issue #21)
**Caminho da Imagem:** `docs/testes/evidencias/CT-002-E1.png`, `docs/testes/evidencias/CT-002-E1-1.png` e `docs/testes/evidencias/CT-002-E1-2.png`
* **Descrição da falha:** Ao realizar o login, no cabeçalho de resposta deveria ser gerado um Token Temporário, o que não acontece.