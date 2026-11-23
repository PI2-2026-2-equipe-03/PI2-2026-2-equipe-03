# Especificação e Execução de Casos de Teste — Requisitos Importantes

## 1. Plano e Escopo de Testes
* **Projeto:** Plataforma de Captura e Gestão de Replays Esportivos (TáGravado / Repeteco)
* **Escopo:** Especificação exclusiva dos Casos de Teste referentes aos Requisitos Funcionais classificados com prioridade **Importante** (RF-03, RF-04, RF-07, RF-08 e RF-11).
* **Equipe:** Equipe de QA — UFC Campus Crateús (Projeto Integrador II)
* **Responsável (QA):** Rick Farias / Time de Testes
* **Data do Documento:** 23/11/2026 (Sprint 5 — Marco de Validação de Requisitos Importantes)

---

## 2. Suítes de Teste dos Requisitos Importantes

| Código Suíte | Nome da Suíte de Testes | Requisitos Cobertos | Regras de Negócio Vinculadas |
| :--- | :--- | :---: | :--- |
| **ST-IMP-01** | Dashboards e Métricas Analíticas | RF-03, RF-04 | RBAC, Contrato da API |
| **ST-IMP-02** | Gestão de Patrocinadores e Marca d'Água | RF-07 | RN-05 |
| **ST-IMP-03** | Ciclo de Vida e Retenção de Mídias (7 Dias) | RF-08 | RN-01 |
| **ST-IMP-04** | Recuperação de Senha e Políticas de Segurança | RF-11 | RN-07, RN-10 |

---

## 3. Matriz de Rastreabilidade dos Requisitos Importantes

| Requisito Funcional | Descrição do Requisito | Prioridade | Casos de Teste Mapeados |
| :---: | :--- | :---: | :--- |
| **RF-03** | Métricas para o administrador | Importante | CT-IMP-001, CT-IMP-002, CT-IMP-003 |
| **RF-04** | Métricas para o cliente (gestor de quadra) | Importante | CT-IMP-004, CT-IMP-005, CT-IMP-006 |
| **RF-07** | Cadastrar patrocinadores | Importante | CT-IMP-007, CT-IMP-008, CT-IMP-009 |
| **RF-08** | Tempo de disponibilidade dos vídeos (Retenção 7 dias) | Importante | CT-IMP-010, CT-IMP-011, CT-IMP-012 |
| **RF-11** | Solicitação de recuperação de senha | Importante | CT-IMP-013, CT-IMP-014, CT-IMP-015, CT-IMP-016, CT-IMP-017, CT-IMP-018, CT-IMP-019 |

---

## 4. Detalhamento dos Casos de Teste

### Suíte ST-IMP-01 — Dashboards e Métricas Analíticas (RF-03 e RF-04)

#### CT-IMP-001 — Visualização de Métricas Globais pelo Administrador com Dados (RF-03)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-001 |
| **Suíte de Teste** | ST-IMP-01 Dashboards e Métricas Analíticas |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-03 (Métricas para o administrador) |
| **Importância** | Alta |

* **Resumo:** Verificar se o administrador do sistema visualiza as estatísticas globais consolidadas (total de quadras, total de replays, volume de downloads e status de armazenamento) ao acessar a rota administrativa `/admin/metrics`.
* **Pré-condições:** Administrador autenticado no sistema (`admin01@example.com`). Base de dados alimentada com instâncias de replays, quadras e acessos.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a aplicação e realizar login com perfil Administrador. | Login efetuado com sucesso e redirecionamento para o Dashboard Admin. |
| **2** | Navegar até a aba de estatísticas globais. | O sistema dispara uma requisição GET para `/api/admin/metrics` retornando status `200 OK`. |
| **3** | Validar a renderização dos cartões e gráficos analíticos. | Exibição correta do total de quadras ativas, replays gerados no mês e taxa de ocupação de disco. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Sim | Rick | 18/11/2026 | **Aprovado** | - | Métricas consolidadas carregadas corretamente. |

---

#### CT-IMP-002 — Dashboard do Administrador sem Dados Cadastrados (RF-03)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-002 |
| **Suíte de Teste** | ST-IMP-01 Dashboards e Métricas Analíticas |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-03 (Métricas para o administrador) |
| **Importância** | Média |

* **Resumo:** Validar o comportamento do painel administrativo quando o banco de dados não possui registros de uso ou quadras cadastradas.
* **Pré-condições:** Administrador logado no sistema. Banco de dados zerado (sem registros de replays).

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Logar como Administrador e acessar a tela inicial de métricas. | O sistema realiza a consulta e identifica ausência de dados. |
| **2** | Observar o comportamento dos componentes visuais. | Exibição da mensagem "Ainda não há dados para exibir", sem quebras de layout ou erros de `NaN`/`null`. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Sim | Rick | 20/11/2026 | **Aprovado** | - | Estado vazio (Empty State) apresentado com mensagem clara. |

---

#### CT-IMP-003 — Bloqueio de Acesso de Atleta ao Dashboard do Administrador (RF-03 / RBAC)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-003 |
| **Suíte de Teste** | ST-IMP-01 Dashboards e Métricas Analíticas |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-03 (Métricas para o administrador) e RBAC |
| **Importância** | Alta |

* **Resumo:** Garantir que um usuário comum (Atleta/USR) seja impedido de acessar o endpoint de métricas administrativas `/api/admin/metrics`.
* **Pré-condições:** Usuário cadastrado com perfil Atleta (`atleta.teste@example.com`) devidamente autenticado.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Autenticar-se com perfil Atleta (USR). | Token de sessão emitido com perfil Atleta. |
| **2** | Tentar acessar via URL ou requisição direta o endpoint `/api/admin/metrics`. | A API nega a requisição retornando `HTTP 403 Forbidden` ou `401 Unauthorized`. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Sim | Rick | 20/11/2026 | **Aprovado** | — | Controle de permissão RBAC validado nos testes automatizados. |

---

#### CT-IMP-004 — Visualização de Métricas pelo Cliente/Gestor da Quadra (RF-04)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-004 |
| **Suíte de Teste** | ST-IMP-01 Dashboards e Métricas Analíticas |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-04 (Métricas para o cliente) |
| **Importância** | Alta |

* **Resumo:** Verificar se o cliente (dono/gestor da quadra) visualiza exclusivamente as estatísticas relativas às suas próprias arenas e quadras ao acessar `/manager/metrics`.
* **Pré-condições:** Cliente gestor (`carlos.mendes@example.com`) logado no sistema.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Realizar login como Gestor de Quadra (CLI). | Autenticação realizada com perfil Cliente. |
| **2** | Acessar o Dashboard do Gestor. | O sistema faz GET em `/api/manager/metrics` e retorna `200 OK` com o total de replays e acionamentos daquela arena. |
| **3** | Conferir a filtragem das métricas. | Os dados apresentados são restritos às quadras pertencentes ao gestor logado. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Sim | Rick | 20/11/2026 | **Aprovado** | - | Isolamento multitenant verificado com sucesso. |

---

#### CT-IMP-005 — Dashboard do Gestor sem Replays Registrados (RF-04)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-005 |
| **Suíte de Teste** | ST-IMP-01 Dashboards e Métricas Analíticas |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-04 (Métricas para o cliente) |
| **Importância** | Média |

* **Resumo:** Validar a apresentação do painel do gestor para uma quadra recém-cadastrada que ainda não possui vídeos gravados.
* **Pré-condições:** Gestor cadastrado com uma quadra sem registros no histórico de replays.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar o painel do gestor para a quadra nova. | Carregamento da página inicial de métricas. |
| **2** | Verificar os componentes visuais. | Exibição do aviso "Ainda não há dados para exibir", mantendo a estrutura da tela sem erros de código. |

##### Registro de Execução
| Build | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1.0 | Rick | 20/11/2026 | **Bloqueado** | - | Funcionalidade de virar gestor ainda não implementada totalmente. |

---

#### CT-IMP-006 — Bloqueio de Acesso de Atleta às Métricas do Gestor (RF-04 / RBAC)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-006 |
| **Suíte de Teste** | ST-IMP-01 Dashboards e Métricas Analíticas |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-04 (Métricas para o cliente) e RBAC |
| **Importância** | Alta |

* **Resumo:** Garantir que um usuário comum (Atleta/USR) seja impedido de acessar o painel de métricas de gestores (`/api/manager/metrics`).
* **Pré-condições:** Usuário Atleta autenticado na plataforma.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Logar como Atleta (USR). | Sessão iniciada. |
| **2** | Enviar requisição GET para a rota `/api/manager/metrics`. | Requisição recusada com código `HTTP 403 Forbidden`. |

##### Registro de Execução
| Resteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Sim | Rick | 21/11/2026 | **Aprovado** | - | Restrição de perfil validada. |

---

### Suíte ST-IMP-02 — Gestão de Patrocinadores e Marca d'Água (RF-07 e RN-05)

#### CT-IMP-007 — Cadastro de Patrocinador e Vinculação à Quadra (RF-07)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-007 |
| **Suíte de Teste** | ST-IMP-02 Gestão de Patrocinadores e Marca d'Água |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-07 (Cadastrar patrocinadores) |
| **Importância** | Alta |

* **Resumo:** Verificar se o cliente gestor consegue cadastrar um patrocinador com nome, foto da logo, duração e valor, vinculando-o à sua quadra.
* **Pré-condições:** Cliente autenticado com permissão de Gestor de Quadra.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a tela de cadastro de patrocinadores (`POST /api/sponsors`). | Formulário exibido com os campos obrigatórios. |
| **2** | Preencher Nome "Empresa X", carregar a logo (`logo.png`), definir tempo de vinheta e selecionar "Quadra 1". | Upload e preenchimento concluídos sem inconsistências. |
| **3** | Clicar no botão "Salvar Patrocinador". | O sistema armazena o patrocinador no banco, vincula à "Quadra 1" e retorna mensagem "Patrocinador cadastrado com sucesso". |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Não | Rick | 21/11/2026 | **Bloqueado** | - | Pendente de implementação. |

---

#### CT-IMP-008 — Aplicação da Marca d'Água / Vinheta nos Replays da Quadra (RF-07 e RN-05)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-008 |
| **Suíte de Teste** | ST-IMP-02 Gestão de Patrocinadores e Marca d'Água |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-07 (Patrocinadores) e RN-05 (Vinculação obrigatória) |
| **Importância** | Alta |

* **Resumo:** Validar se os replays gerados para uma quadra patrocinada contêm os metadados do patrocinador ativo para exibição no player e vinheta (RN-05).
* **Pré-condições:** Patrocinador ativo cadastrado e vinculado à Quadra 1.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acionar a gravação de um replay na Quadra 1. | Replay de 30s gerado com sucesso. |
| **2** | Consultar os dados do vídeo via API (`GET /api/replays/{id}`). | A resposta traz o objeto `patrocinador` ou `sponsor` contendo a URL da imagem da logo (`imageUrl`). |
| **3** | Abrir o vídeo no player do sistema. | A marca d'água do patrocinador é renderizada sobre o vídeo. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Não | Rick | 21/11/2026 | **Bloqueado** | - | Pedente de implementação. |

---

#### CT-IMP-009 — Bloqueio de Cadastro de Patrocinadores por Usuário Comum (RF-07 / RBAC)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-009 |
| **Suíte de Teste** | ST-IMP-02 Gestão de Patrocinadores e Marca d'Água |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-07 (Cadastrar patrocinadores) e RBAC |
| **Importância** | Média |

* **Resumo:** Garantir que um usuário com perfil Atleta (USR) receba erro de permissão ao tentar cadastrar patrocinadores.
* **Pré-condições:** Usuário Atleta logado na aplicação.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Tentar enviar requisição POST para `/api/sponsors` logado como Atleta. | A requisição é negada com erro `HTTP 403 Forbidden`. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Sim | Rick | 21/11/2026 | **Aprovado** | - | Permissão restrita a gestores e administradores. |

---

### Suíte ST-IMP-03 — Ciclo de Vida e Retenção de Mídias (RF-08 e RN-01)

#### CT-IMP-010 — Exclusão Automática de Vídeos Atingindo 7 Dias / 168h (RF-08 e RN-01)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-010 |
| **Suíte de Teste** | ST-IMP-03 Ciclo de Vida e Retenção de Mídias |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-08 (Tempo de disponibilidade dos vídeos) e RN-01 |
| **Importância** | Alta |

* **Resumo:** Verificar se a rotina automática de limpeza (cronjob) remove arquivos fisicamente do storage e atualiza o banco para status expirado após 7 dias corridos (168h).
* **Pré-condições:** Replay cadastrado no banco com `data_criacao` igual a `now() - 8 dias`.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Disparar a rotina/cronjob diária de expiração de vídeos. | A rotina executa sem erros, identificando registros com mais de 7 dias. |
| **2** | Verificar a presença do arquivo `.mp4` no storage. | O arquivo de vídeo foi removido fisicamente da pasta/bucket. |
| **3** | Consultar a mídia no banco de dados. | Registro atualizado para o status `EXPIRADO` ou removido. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Não | Rick |  |  | - |  |

---

#### CT-IMP-011 — Manutenção de Vídeos Recentes (< 7 Dias) no Sistema (RF-08)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-011 |
| **Suíte de Teste** | ST-IMP-03 Ciclo de Vida e Retenção de Mídias |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-08 (Tempo de disponibilidade dos vídeos) |
| **Importância** | Alta |

* **Resumo:** Garantir que mídias gravadas há menos de 7 dias permaneçam totalmente ativas e disponíveis para consulta e download.
* **Pré-condições:** Replay gravado há 3 dias na base de dados.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Executar a rotina automática de varredura. | A rotina ignora o vídeo por estar dentro do prazo de validade. |
| **2** | Buscar o vídeo via API ou interface (`GET /api/replays/{id}`). | O vídeo é retornado com status `200 OK` e permanece disponível para reprodução. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Não | Rick | 08/11/2026 | **Bloqueado** | - | Ainda não é possivel testar. |

---

#### CT-IMP-012 — Tentativa de Acesso a Vídeo Expirado Retorna Indisponível (RF-08 e RN-01)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-012 |
| **Suíte de Teste** | ST-IMP-03 Ciclo de Vida e Retenção de Mídias |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-08 (Tempo de disponibilidade) e RN-01 |
| **Importância** | Média |

* **Resumo:** Verificar se a busca por um ID de vídeo expirado retorna resposta HTTP informando indisponibilidade do vídeo.
* **Pré-condições:** ID de um replay já expirado e removido pela rotina.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Tentar consultar a URL do replay expirado. | O sistema responde com `HTTP 404 Not Found` ou `410 Gone`. |
| **2** | Tentar realizar o download do arquivo. | O download é impedido e o sistema exibe mensagem "Vídeo expirado ou indisponível". |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
| Não | Rick | 08/11/2026 | **Bloqueado** | - | Ainda não é possível testar. |

---

### Suíte ST-IMP-04 — Recuperação de Senha e Políticas de Segurança (RF-11, RN-07 e RN-10)

#### CT-IMP-013 — Recuperação de Senha por E-mail com Sucesso (RF-11, RN-07 e RN-10)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-013 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 (Recuperação de senha), RN-07 e RN-10 |
| **Importância** | Alta |

* **Resumo:** Validar todo o fluxo de recuperação de senha por e-mail: solicitação, recebimento do código de verificação, inserção de nova senha válida e autenticação com a nova senha.
* **Pré-condições:** Usuário cadastrado com e-mail válido no sistema.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Acessar a opção "Esqueci minha senha" na tela de login. | Formulário de recuperação de senha é exibido. |
| **2** | Digitar o e-mail cadastrado e escolher o envio por e-mail. | O sistema envia um código de verificação de 6 dígitos para o e-mail informado. |
| **3** | Digitar o código de verificação recebido dentro do prazo de 10 minutos (RN-07). | Código validado com sucesso e tela de redefinição de senha liberada. |
| **4** | Digitar a nova senha que atenda aos requisitos mínimos (diferente da anterior, min 8 caracteres, maiúscula, minúscula, número e símbolo) duas vezes. | A senha é alterada no banco com hash seguro e a mensagem "Senha alterada com sucesso" é exibida. |
| **5** | Realizar login utilizando a nova senha. | Login efetuado com sucesso. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

---

#### CT-IMP-014 — Recuperação de Senha via Telefone / SMS com Sucesso (RF-11)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-014 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 (Recuperação de senha por telefone) |
| **Importância** | Média |

* **Resumo:** Verificar a recuperação de senha solicitando o código de verificação via número de telefone/SMS.
* **Pré-condições:** Usuário cadastrado com telefone válido.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Na tela de recuperação, escolher a opção de envio por SMS/Telefone. | O código de verificação é enviado via SMS para o número associado. |
| **2** | Informar o código e cadastrar a nova senha válida. | Alteração efetuada com sucesso e redirecionamento para o login. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

---

#### CT-IMP-015 — Rejeição de Código de Recuperação Expirado (> 10 minutos) (RF-11 e RN-07)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-015 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 (Recuperação de senha) e RN-07 (Validade de 10 min) |
| **Importância** | Alta |

* **Resumo:** Validar se o sistema recusa o código de verificação caso a tentativa de uso ocorra após 10 minutos do envio (RN-07).
* **Pré-condições:** Código de recuperação gerado há mais de 10 minutos em ambiente de testes.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Digitar o código expirado no campo de confirmação. | O sistema recusa o código e exibe a mensagem "Código expirado". |
| **2** | Tentar avançar para a redefinição de senha. | O sistema bloqueia a transição e oferece a opção de reenvio de código. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

---

#### CT-IMP-016 — Bloqueio de Redefinição quando Confirmação de Senha Diverge (RF-11)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-016 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 (Recuperação de senha) |
| **Importância** | Média |

* **Resumo:** Verificar se o sistema impede a alteração de senha quando o campo "Nova Senha" e "Confirmar Nova Senha" contêm valores diferentes.
* **Pré-condições:** Código de verificação validado com sucesso.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Preencher "Nova Senha" com `SenhaNova#123` e "Confirmar Senha" com `OutraSenha#456`. | Os campos aceitam a digitação. |
| **2** | Clicar em "Alterar Senha". | O sistema bloqueia o envio e exibe o alerta "As senhas não coincidem". |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

---

#### CT-IMP-017 — Rejeição de Nova Senha sem Requisitos Mínimos de Segurança (RF-11 e RN-10)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-017 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 e RN-10 (Complexidade de senha) |
| **Importância** | Alta |

* **Resumo:** Validar a recusa de uma nova senha fraca que não possua 8 caracteres, maiúscula, minúscula, número e caractere especial (RN-10).
* **Pré-condições:** Tela de digitação da nova senha ativa.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Informar a nova senha `123456` (sem letras ou caracteres especiais). | O sistema identifica descumprimento da política de segurança. |
| **2** | Clicar em "Salvar Nova Senha". | O sistema recusa a senha e exibe os critérios não atendidos (mínimo 8 caracteres, maiúscula, minúscula, número e símbolo). |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

---

#### CT-IMP-018 — Bloqueio de Redefinição com Senha Idêntica à Anterior (RF-11 e RN-10)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-018 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 e RN-10 (Não repetição da senha anterior) |
| **Importância** | Média |

* **Resumo:** Verificar se o sistema impede o usuário de cadastrar uma nova senha que seja idêntica à senha utilizada anteriormente (RN-10).
* **Pré-condições:** Usuário com senha atual `SenhaAtual#2026` em processo de redefinição.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Informar nos dois campos de nova senha o texto `SenhaAtual#2026`. | O sistema compara a hash da senha digitada com a hash armazenada. |
| **2** | Clicar em "Salvar". | O sistema rejeita com erro `HTTP 400 Bad Request` informando "A nova senha deve ser diferente da anterior". |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

---

#### CT-IMP-019 — Solicitação de Recuperação para E-mail ou Telefone Inexistente (RF-11 e RN-03)

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-IMP-019 |
| **Suíte de Teste** | ST-IMP-04 Recuperação de Senha e Políticas de Segurança |
| **Autor** | Rick Farias |
| **Requisito Coberto** | RF-11 (Recuperação de senha) e Segurança |
| **Importância** | Média |

* **Resumo:** Garantir a proteção contra enumeração de usuários, retornando mensagem neutra ao solicitar recuperação para conta inexistente.
* **Pré-condições:** E-mail `inexistente999@exemplo.com` não presente na base de dados.

##### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | Informar o e-mail `inexistente999@exemplo.com` no campo de recuperação e confirmar. | O sistema processa o pedido sem revelar se o e-mail existe no banco. |
| **2** | Verificar a mensagem exibida na tela. | Apresentação de resposta neutra: "Se este e-mail estiver cadastrado, um código de verificação foi enviado", sem confirmação de inexistência do usuário. |

##### Registro de Execução
| Reteste | Testador | Data | Status | Defeito | Observações |
| :---: | :--- | :---: | :---: | :---: | :--- |
|  | Rick |  |  | - |  |

