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
| Rick | 17/10/26 | **Reprovado** | Issue #21 | Script não implementado |

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
| Rick | 17/10/2026 | **Reprovado** | Issue #7 | Ao realizar sucessivas tentativas de login, o usuário não é bloqueado |

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
| Rick | 17/10/2026 | **Bloqueado** | - | Pendente de implementação |

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

## 5. Legendas e Regras de Qualidade

### Status da Execução
* **Aprovado:** Todos os passos foram executados exatamente conforme o resultado esperado.
* **Reprovado:** Qualquer passo divergiu do resultado esperado (exige abertura imediata de Issue de defeito no GitHub).
* **Bloqueado:** O teste não pôde ser executado devido à indisponibilidade do ambiente Docker ou dependência de caso reprovado.
* **Não executado:** Caso planejado, aguardando execução na sprint.
