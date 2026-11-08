# Especificação e Execução de Testes — Regras de Negócio (RN)

## 1. Plano de Teste
| Campo | Informação |
| :--- | :--- |
| **Projeto** | Repeteco |
| **Responsável (QA)** | Rick |
| **Data da Execução** | 17/10/2026 |
| **Ambiente de Teste** | Docker |

---

## 2. Suítes de Teste (Regras de Negócio)

| Código | Suíte de Teste | Regras de Negócio Associadas | Descrição |
| :---: | :--- | :---: | :--- |
| **ST-RN-01** | Retenção e Expiração de Mídias | `RN-01` | Testes da rotina automática de exclusão após 7 dias (168h). |
| **ST-RN-02** | Captura e Buffer de Vídeo | `RN-02` | Testes do buffer circular da câmera e gravação dos 30s. |
| **ST-RN-03** | Segurança e Controle de Acesso | `RN-03` | Testes do bloqueio temporário após 5 tentativas incorretas de login. |
| **ST-RN-04** | Permissões e Perfil de Acesso | `RN-04` | Testes de restrição de exclusão manual por tipo de perfil (`CLI`, `ADM`). |
| **ST-RN-05** | Marca d'Água e Patrocinadores | `RN-05` | Testes de vinculação e exibição de patrocinadores ativados na quadra. |

---

## 3. Estrutura dos Casos de Teste das Regras de Negócio

### CT-RN-001 — Validação da Retenção Automática de 7 Dias (RN-01)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-RN-001 |
| **Suíte de Teste** | ST-RN-01: Retenção e Expiração de Mídias |
| **Autor** | Rick |
| **Regra Coberta** | RN-01 (Retenção de 7 dias / 168 horas) |
| **Requisito Funcional** | RF-08 (Tempo de disponibilidade dos vídeos) |
| **Importância** | Alta |

* **Resumo:** Verificar se a rotina automática do sistema (cronjob) identifica e remove vídeos com mais de 7 dias de criação.
* **Pré-condições:** Registro de replay cadastrado no banco de dados com `criado_em = now() - 8 days` (criado há mais de 168h).

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Executar a rotina/script de limpeza e expiração de vídeos no container. | O script é executado com sucesso sem erros. |
| **2** | Consultar o status do vídeo na tabela `replay` no banco de dados. | O registro do vídeo foi atualizado para o status `excluido` ou removido. |
| **3** | Verificar o diretório de armazenamento (storage/volume) no servidor. | O arquivo `.mp4` correspondente foi removido fisicamente do disco. |
| **4** | Tentar buscar o vídeo na interface/API do sistema. | O vídeo não é mais exibido nos resultados de busca do usuário. |

#### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 08/11/26 | **Aprovado** | - | Não é um cronjob, mas sim um comportamento do banco. |

---

### CT-RN-002 — Validação da Janela de 30 Segundos e Buffer Circular (RN-02)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-RN-002 |
| **Suíte de Teste** | ST-RN-02: Captura e Buffer de Vídeo |
| **Autor** | Rick |
| **Regra Coberta** | RN-02 (Buffer circular de 30 segundos) |
| **Requisito Funcional** | RF-05 (Acionamento e gravação de vídeo), RF-09 |
| **Importância** | Alta |

* **Resumo:** Validar se o acionamento do replay gera um arquivo de vídeo contendo exatamente os 30 segundos anteriores da transmissão.
* **Pré-condições:** Câmera da quadra conectada e transmitindo em tempo real com buffer circular ativo.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acionar o botão de gravação/corte de replay na quadra. | O sistema envia a requisição de corte para o serviço de captura. |
| **2** | Aguardar o processamento e salvamento do clipe gerado. | O arquivo MP4 é gerado e disponibilizado para visualização. |
| **3** | Verificar as propriedades do arquivo de vídeo gerado (duração). | A duração total do vídeo é de exatamente 30 segundos. |
| **4** | Verificar os metadados gravados na tabela `replay`. | O clipe contém timestamp, quadra, cidade e identificador da câmera. |

#### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Bloqueado** | - | Pendente de instalação física |

---

### CT-RN-003 — Validação do Bloqueio por Múltiplas Tentativas Incorretas (RN-03)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-RN-003 |
| **Suíte de Teste** | ST-RN-03: Segurança e Controle de Acesso |
| **Autor** | Rick |
| **Regra Coberta** | RN-03 (Bloqueio após 5 tentativas incorretas) |
| **Requisito Funcional** | RF-02 (Autenticação e Login), RNF-04 |
| **Importância** | Alta |

* **Resumo:** Verificar se o sistema bloqueia o acesso da conta/IP temporariamente após 5 tentativas consecutivas de login com senha incorreta.
* **Pré-condições:** Usuário cadastrado no sistema com e-mail conhecido e conta ativa.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Tentar realizar login informando senha incorreta por 4 vezes seguidas. | O sistema recusa o acesso informando credenciais inválidas. |
| **2** | Tentar realizar o login pela 5ª vez consecutiva com a senha incorreta. | O sistema bloqueia a conta e exibe a mensagem de bloqueio por segurança. |
| **3** | Tentar realizar login imediatamente com a senha CORRETA antes do tempo limite (15 min). | O acesso continua bloqueado, impedindo a autenticação. |
| **4** | Aguardar o tempo estipulado de desbloqueio e realizar o login com a senha correta. | O acesso é liberado com sucesso. |

#### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 08/11/2026 | Aprovado | - | Bloqueando devidamente após sucessivas tentativas incorretas. |

---

### CT-RN-004 — Validação da Restrição de Exclusão Manual por Perfil (RN-04)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-RN-004 |
| **Suíte de Teste** | ST-RN-04: Permissões e Perfil de Acesso |
| **Autor** | Rick |
| **Regra Coberta** | RN-04 (Restrição de exclusão manual por perfil) |
| **Requisito Funcional** | RF-10 (Exclusão manual de vídeos pelo cliente) |
| **Importância** | Média |

* **Resumo:** Verificar se apenas perfis autorizados (Cliente proprietário da quadra e Administrador) conseguem excluir manualmente um replay.
* **Pré-condições:** Replay cadastrado. Contas de teste com perfil Atleta (`USR`), Cliente (`CLI`) e Administrador (`ADM`).

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Logar como Atleta (`USR`) e tentar acionar a rota de exclusão manual de um replay. | A requisição é negada com erro de permissão (`HTTP 403 Forbidden`). |
| **2** | Logar como Cliente (`CLI`) proprietário de OUTRA quadra e tentar excluir o replay. | A requisição é negada por falta de privilégios sobre a quadra. |
| **3** | Logar como Cliente (`CLI`) proprietário da quadra onde o replay foi gravado e solicitar a exclusão. | A exclusão é autorizada e processada com sucesso. |
| **4** | Logar como Administrador (`ADM`) e solicitar a exclusão de qualquer replay. | A exclusão é realizada e registrada no log de auditoria. |

#### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Bloqueado** | - | Problema no acesso a contas de gestor e admin. |

---

### CT-RN-005 — Validação da Exibição de Patrocinadores Ativados (RN-05)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-RN-005 |
| **Suíte de Teste** | ST-RN-05: Marca d'Água e Patrocinadores |
| **Autor** | Rick |
| **Regra Coberta** | RN-05 (Exibição obrigatória de patrocinadores) |
| **Requisito Funcional** | RF-07 (Gestão de patrocinadores) |
| **Importância** | Média |

* **Resumo:** Validar se os replays gerados para uma quadra exibem corretamente a marca d'água do patrocinador ativo vinculado à quadra.
* **Pré-condições:** Patrocinador cadastrado com logo (.png) e vinculado à Quadra 1 via tabela `quadra_patrocinador`.

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Gerar um novo clipe de replay na Quadra 1. | O vídeo é processado e disponibilizado para reprodução. |
| **2** | Abrir o player de vídeo na interface do usuário. | A logo do patrocinador é exibida como marca d'água sobreposta no vídeo. |
| **3** | Verificar os metadados do vídeo retornado pela API. | A resposta JSON inclui o ID e os dados do patrocinador ativo associado. |

#### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| :--- | :---: | :---: | :---: | :--- |
| Rick | 17/10/2026 | **Bloqueado** | - | Pendente de implementação |

---

### CT-RN-006 — Validação do Logout Automático por Inatividade de Sessão (RN-06)
| Campo | Detalhes |
| ------ | ------ |
| **Identificador** | CT-RN-006 |
| **Suíte de Teste** | ST-RN-06: Duração e Expiração de Sessão |
| **Autor** | Rick |
| **Regra Coberta** | RN-06 (Logout automático por inatividade de 30 minutos) |
| **Requisito Funcional** | RF-02 (Login de usuário) |
| **Importância** | Alta |

*   **Resumo:** Verificar se a sessão do usuário é encerrada automaticamente após decorridos 30 minutos (1800 segundos) sem atividade, exigindo nova autenticação para acessar rotas protegidas.
*   **Pré-condições:** Usuário cadastrado e autenticado com sessão válida ativa no sistema.

###### Passos de Execução
| Passo | Ação | Resultado Esperado |
| ------ | ------ | ------ |
| **1** | Realizar login no sistema com credenciais válidas e capturar a resposta de autenticação. | Sessão criada com sucesso; cabeçalho de expiração do cookie/token define TTL de 1800 segundos (30 min). |
| **2** | Executar operações normais na API/painel antes de 30 minutos (ex: listar replays). | A requisição é aceita (HTTP 200) e a contagem de expiração da sessão é reiniciada. |
| **3** | Deixar a sessão inativa por tempo superior a 30 minutos (ou enviar token com timestamp expirado). | O token de sessão torna-se inválido no servidor. |
| **4** | Tentar acessar qualquer rota protegida (ex: `/api/me` ou `/api/replays`). | O sistema rejeita a chamada com HTTP 401 Unauthorized e redireciona o usuário para a tela de login. |

###### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| ------ | ------ | ------ | ------ | ------ |
| Rick | 08/11/2026 | **Aprovado** | - | Validade máxima de 1800s e rejeição de token expirado com 401 confirmadas. |

---

### CT-RN-007 — Validação da Validade e Limite de Tentativas do Código de Recuperação (RN-07)
| Campo | Detalhes |
| ------ | ------ |
| **Identificador** | CT-RN-007 |
| **Suíte de Teste** | ST-RN-07: Recuperação de Senha e Tokens |
| **Autor** | Rick |
| **Regra Coberta** | RN-07 (Código válido por 10 min, uso único, máx 3 tentativas e 3 reenvios/h) |
| **Requisito Funcional** | RF-11 (Solicitação de recuperação de senha) |
| **Importância** | Média |

*   **Resumo:** Garantir que o código/token de recuperação de senha expire após 10 minutos, seja invalidado após o primeiro uso e respeite o limite de 3 tentativas/reenvios por hora.
*   **Pré-condições:** Conta de usuário ativa com e-mail cadastrado no sistema.

###### Passos de Execução
| Passo | Ação | Resultado Esperado |
| ------ | ------ | ------ |
| **1** | Solicitar redefinição de senha na rota `POST /api/auth/forgot-password` informando e-mail cadastrado. | O sistema gera código de recuperação com validade de 10 minutos e retorna mensagem genérica (sem vazar se o e-mail existe). |
| **2** | Tentar validar o código após transcorridos mais de 10 minutos desde o envio. | O sistema rejeita o código com status HTTP 400 ou 401 e exibe a mensagem "Código expirado". |
| **3** | Solicitar novo código, submeter com dados válidos e concluir a troca da senha. | Senha redefinida com sucesso (HTTP 200). |
| **4** | Tentar submeter imediatamente uma nova redefinição utilizando o mesmo código já consumido. | O sistema rejeita a operação, comprovando que o código é de uso estritamente único. |
| **5** | Tentar solicitar mais de 3 códigos de recuperação dentro de uma janela de 60 minutos. | O sistema bloqueia novas emissões por excesso de tentativas (HTTP 429 Too Many Requests). |

###### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| ------ | ------ | ------ | ------ | ------ |
| Rick | 08/11/2026 | **Aprovado** | - | Expiração de 10 min, uso único e rate limit de reenvios operacionais. |

---

### CT-RN-008 — Restrição de Download Exclusivo para Usuários Autenticados e Prevenção de Concorrência (RN-08)
| Campo | Detalhes |
| ------ | ------ |
| **Identificador** | CT-RN-008 |
| **Suíte de Teste** | ST-RN-08: Acesso e Download de Replays |
| **Autor** | Rick |
| **Regra Coberta** | RN-08 (Download apenas por usuários logados e intervalo de 30s entre acionamentos) |
| **Requisito Funcional** | RF-06 (Baixar vídeos), RF-05 (Gravar vídeo) |
| **Importância** | Alta |

*   **Resumo:** Verificar se usuários anônimos são impedidos de baixar vídeos e validar a trava de 30 segundos entre cliques consecutivos na quadra para prevenir replays sobrepostos.
*   **Pré-condições:** Vídeo de replay disponível no storage; botão de gravação da quadra conectado à API.

###### Passos de Execução
| Passo | Ação | Resultado Esperado |
| ------ | ------ | ------ |
| **1** | Tentar efetuar requisição de download direto em `GET /api/replays/{id}/download` sem cookies ou token de autenticação. | A requisição é imediatamente barrada com HTTP 401 Unauthorized. |
| **2** | Autenticar-se com perfil de Atleta cadastrado e solicitar o download do mesmo replay. | A requisição é autorizada com HTTP 200 OK, disponibilizando o arquivo .mp4 para download. |
| **3** | Na quadra, acionar o botão de gravação para salvar os últimos 30 segundos de um lance. | A solicitação é aceita e o clipe é gerado com sucesso. |
| **4** | Acionar o botão novamente em intervalo inferior a 30 segundos (ex: 5 segundos após o primeiro clique). | O sistema identifica acionamento concorrente dentro da janela de buffer e ignora/rejeita o disparo para evitar mídias duplicadas. |

###### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| ------ | ------ | ------ | ------ | ------ |
| Rick | 08/11/2026 | **Aprovado** | - | Proteção de download anônimo com 401 e trava de concorrência validadas. |

--------------------------------------------------------------------------------

### CT-RN-009 — Validação de Unicidade de E-mail e Telefone por Conta (RN-09)
| Campo | Detalhes |
| ------ | ------ |
| **Identificador** | CT-RN-009 |
| **Suíte de Teste** | ST-RN-09: Integridade Cadastral e Unicidade |
| **Autor** | Rick |
| **Regra Coberta** | RN-09 (E-mail e telefone vinculados a uma única conta) |
| **Requisito Funcional** | RF-01 (Cadastro de usuário) |
| **Importância** | Alta |

*   **Resumo:** Garantir que o sistema impeça o cadastro de mais de um usuário utilizando o mesmo endereço de e-mail ou o mesmo número de telefone celular.
*   **Pré-condições:** Usuário pré-existente cadastrado no banco com e-mail `atleta.teste@example.com` e telefone `(88) 99888-7766`.

###### Passos de Execução
| Passo | Ação | Resultado Esperado |
| ------ | ------ | ------ |
| **1** | Acessar o formulário de cadastro de usuário (`POST /api/auth/register` ou `/sign-up/email`). | Formulário acessível. |
| **2** | Submeter cadastro informando o e-mail já existente `atleta.teste@example.com`, mas com telefone inédito. | O cadastro é rejeitado com HTTP 409 Conflict (ou 400 Bad Request) informando que o e-mail já está associado a uma conta. |
| **3** | Submeter cadastro informando e-mail inédito, porém com o telefone já cadastrado `(88) 99888-7766`. | O cadastro é rejeitado com mensagem indicando que o telefone já está vinculado a outra conta. |
| **4** | Submeter cadastro fornecendo e-mail inédito e telefone inédito simultaneamente com senha válida. | O sistema efetua o cadastro com sucesso, retornando HTTP 201 Created. |

###### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| ------ | ------ | ------ | ------ | ------ |
| Rick | 08/11/2026 | **Aprovado** | - | Rejeição por duplicidade de chave primária/índice único no banco comprovada. |

--------------------------------------------------------------------------------

### CT-RN-010 — Validação de Complexidade e Não Reutilização de Senha (RN-10)
| Campo | Detalhes |
| ------ | ------ |
| **Identificador** | CT-RN-010 |
| **Suíte de Teste** | ST-RN-10: Complexidade e Políticas de Senha |
| **Autor** | Rick |
| **Regra Coberta** | RN-10 (Nova senha diferente da anterior e critérios mínimos de complexidade) |
| **Requisito Funcional** | RF-01 (Cadastro de usuário), RF-11 (Recuperação de senha) |
| **Importância** | Média |

*   **Resumo:** Validar as exigências de senha forte (mínimo de 8 caracteres, maiúscula, minúscula, número e caractere especial) e a proibição de redefinição de senha com valor idêntico ao atual.
*   **Pré-condições:** Usuário ativo cadastrado no sistema com a senha conhecida `SenhaAntiga@123`.

###### Passos de Execução
| Passo | Ação | Resultado Esperado |
| ------ | ------ | ------ |
| **1** | Tentar cadastrar usuário ou redefinir senha informando senha com menos de 8 caracteres (ex: `Abc@1`). | O sistema recusa com HTTP 400 Bad Request indicando quantidade mínima de caracteres insuficiente. |
| **2** | Tentar cadastrar informando senha sem caractere especial ou sem número (ex: `Senhasemnumero`). | O sistema recusa apontando a ausência dos critérios obrigatórios de segurança. |
| **3** | No fluxo de redefinição de senha (`/auth/reset-password`), informar no campo nova senha exatamente a mesma senha anterior `SenhaAntiga@123`. | O sistema bloqueia a alteração com HTTP 400 Bad Request, informando que a nova senha deve ser diferente da anterior. |
| **4** | Informar nos campos nova senha e confirmação de senha valores divergentes entre si. | O sistema acusa erro indicando que as senhas informadas não coincidem. |
| **5** | Informar senha forte válida e diferente da anterior (ex: `NovaSenhaForte#2026`). | O sistema aceita a nova senha, criptografa o hash e atualiza o cadastro com sucesso (HTTP 200 OK). |

###### Registro de Execução
| Testador | Data | Status | Defeito (Issue) | Observações |
| ------ | ------ | ------ | ------ | ------ |
| Rick | 08/11/2026 | **Aprovado** | - | Validador de complexidade por regex e verificação de histórico de senha ativos. |


## 5. Legendas e Regras de Qualidade

### Status da Execução
* **Aprovado:** Todos os passos foram executados exatamente conforme o resultado esperado.
* **Reprovado:** Qualquer passo divergiu do resultado esperado (exige abertura imediata de Issue de defeito no GitHub).
* **Bloqueado:** O teste não pôde ser executado devido à indisponibilidade do ambiente Docker ou dependência de caso reprovado.
* **Não executado:** Caso planejado, aguardando execução na sprint.
