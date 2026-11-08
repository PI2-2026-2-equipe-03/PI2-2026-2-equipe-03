### **Requisitos Funcionais (RF) x Requisitos Não Funcionais (RNF)**

Esta matriz relaciona as funcionalidades do sistema com as restrições e qualidades técnicas exigidas.

| Código (RF) | Nome do Requisito Funcional | Requisitos Não Funcionais Associados (RNF) | Justificativa da Relação |
| :---- | :---- | :---- | :---- |
| **RF-01** | Cadastro de usuário | RNF-01, RNF-02, RNF-05 | Interface em tela requer adaptação de tema, responsividade e facilidade de uso para novos cadastros. |
| **RF-02** | Login de usuário | RNF-01, RNF-02, RNF-04, RNF-05 | Tela de interação humana, submetida à regra de segurança de bloqueio por falhas sucessivas e limite de simultaneidade. |
| **RF-03** | Métricas para o administrador | RNF-01, RNF-02, RNF-03 | O dashboard de métricas deve carregar e responder em menos de 2 segundos, além de ser responsivo. |
| **RF-04** | Métricas para o cliente | RNF-01, RNF-02, RNF-03 | Semelhante ao RF-03, exige renderização ágil na interface e uso nos diferentes temas e dispositivos. |
| **RF-05** | Gravar Vídeo | RNF-03 | A captura de vídeo e seu armazenamento devem ocorrer sem degradação de tempo. |
| **RF-06** | Baixar vídeo | RNF-01, RNF-02, RNF-03 | O download do vídeo deve ser concluído em menos de 10 segundos, e a tela de busca exige responsividade. |
| **RF-07** | Cadastrar patrocinadores | RNF-01, RNF-02, RNF-05 | Formulário de gestão que requer interface clara, adaptação a dispositivos e usabilidade intuitiva. |
| **RF-08** | Tempo de disponibilidade dos vídeos | RNF-03 | A rotina de exclusão impacta as métricas de armazenamento e desempenho geral do sistema. |
| **RF-09** | Associar informações ao replay | RNF-03 | O processamento e associação de metadados ao vídeo devem atender ao requisito de respostas rápidas no back-end. |
| **RF-10** | Exclusão de vídeos | RNF-01, RNF-02 | Acesso administrativo manual via tela, necessitando suportar temas e resoluções variadas. |
| **RF-11** | Solicitação de recuperação de senha | RNF-01, RNF-02, RNF-04, RNF-05 | Envolve segurança na emissão e validação de tokens, além de interface amigável para o usuário final. |
| **RF-12** | Solicitação de cadastro como gestor | RNF-01, RNF-02, RNF-05 | Formulários de entrada que precisam ser acessíveis, responsivos e seguir a identidade visual. |

### 

### **Regras de Negócio (RN) x Requisitos Funcionais (RF)**

Esta matriz rastreia como as restrições lógicas e diretrizes de negócio impactam diretamente o comportamento das funcionalidades descritas.

| Código (RN) | Regra de Negócio | Requisitos Funcionais Impactados (RF) |
| :---- | :---- | :---- |
| **RN-01** | Retenção e Exclusão Automática de Mídia (7 dias) | **RF-08** (Tempo de disponibilidade dos vídeos) |
| **RN-02** | Janela Fixa e Buffer do Replay (30 segundos) | **RF-05** (Gravar Vídeo) |
| **RN-03** | Bloqueio Temporário por Tentativas de Acesso (5 falhas/15 min) | **RF-02** (Login de usuário) |
| **RN-04** | Permissão de Exclusão Manual de Vídeos | **RF-10** (Exclusão de vídeos) |
| **RN-05** | Vinculação Obrigatória de Patrocinador em Replays | **RF-07** (Cadastrar patrocinadores), **RF-09** (Associar informações ao replay) |

**Requisitos Funcionais x Rotas de Usuário**

| Rotas | Requisitos F | Regras de Negócio |
| :---- | :---- | :---- |
| tela-de-login/ Tela de Cadastro/ | RF-01 e RF-02 | RN-09 e RN-10 |
| tela-de-login/ inicio/ Selecionar Cidade / Selecionar Arena/ Selecionar Quadra/ Selecionar data e Hora/ Selecionar vídeo | RF-06 | RN-08 |
| tela-de-login/recuperar-senha \-\> email ou sms \-\> tela-de-login | RF-11 | RN-07, RN-09 e RN-10 |
| tela-de-login/ inicio/ Torne-se um de Gestor de Quadra/ Solicitar cadastro/ Tela de Cadastro | RF-12 | RN-09 e RN-10 |
| Login/ Inicio/ gestão de quadra/ painel administrativo | RF-03 e RF-04 |  |
| Login/ Inicio/ gestão de quadra/ painel administrativo/excluir quadra | RF-10 | RN-04 |
| Login/ Inicio/ gestão de quadra/ Cadastrar Patrocinador | RF-07 | RN-05 |
| Login/ Inicio/ gestão de quadra/ Cadastrar Camera | RF-15 |  |
| Login/ Inicio/ gestão de quadra/ Cadastrar Quadra | RF-14 |  |
| Login/ inicio/ validar gestores | RF-13 |  |

