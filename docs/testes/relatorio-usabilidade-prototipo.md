# Relatório de Teste de Usabilidade do Protótipo de Alta Fidelidade

## 1. Identificação e Rastreabilidade
* **Projeto:** TaGravado — Plataforma de Captura e Gestão de Replays Esportivos
* **Artefato:** Relatório de Avaliação Heurística e Teste de Usabilidade (`Q2-02`)
* **Sprint:** Sprint 2
* **Responsável (QA):** Rick
* **Equipe / Grupo:** Equipe 3
* **Caminho no Repositório:** `/docs/relatorio-usabilidade-prototipo.md`
* **Requisitos Funcionais e Não Funcionais Cobertos:** `RF-01` a `RF-10`, `RNF-01` (Tema Claro/Escuro), `RNF-02` (Responsividade e Usabilidade Cross-Device), `RNF-03` (Tempo de Resposta)

---

## 2. Objetivos da Avaliação
Este documento apresenta os resultados da avaliação de usabilidade realizada sobre o **Protótipo de Alta Fidelidade Navegável (Figma)** da aplicação **TáGravado**. 

Os principais objetivos desta avaliação são:
1. Validar se a navegação entre as **10 telas do fluxo principal** é fluida, intuitiva e sem pontos de fricção.
2. Identificar gargalos de UX (User Experience) e UI (User Interface) antes da conclusão do desenvolvimento Frontend.
3. Avaliar a conformidade do protótipo em relação às **10 Heurísticas de Jakob Nielsen** e às especificações do Guia de Padrões Visuais (`padroes-visuais-v2.md`).
4. Prover recomendações acionáveis para as equipes de Design (Figma) e Frontend.

---

## 3. Metodologia do Teste

A avaliação foi dividida em duas etapas complementares: **Avaliação Heurística e Teste de Usabilidade (Especialista/QA)**.

### 3.1 Escala de Gravidade dos Problemas (Nielsen)
Os problemas identificados foram classificados segundo a escala de gravidade de Jakob Nielsen:

* **0 — Sem Problema:** Não afeta a usabilidade.
* **1 — Cosmético:** Solução não urgente; pequena imperfeição estética ou alinhamento.
* **2 — Pequeno (Baixa Gravidade):** Fricção menor; o usuário consegue concluir a tarefa sozinho após breve hesitação.
* **3 — Grande (Alta Gravidade):** Dificuldade relevante; atrasa significativamente a tarefa ou gera confusão recorrente.
* **4 — Catastrófico:** Impede a conclusão da tarefa pelo usuário; exige correção imediata.

---

## 4. Mapeamento e Avaliação das 10 Telas do Fluxo Principal

O teste cobriu integralmente as **10 telas navegáveis do protótipo de alta fidelidade**:

| # | Tela / Interface | Arquivo / Protótipo | Requisitos Vinculados | Objetivo Principal da Tela |
| :---: | :--- | :--- | :---: | :--- |
| **01** | Tela de Cadastro / Criar Conta | `Criar_conta.png` | `RF-01` | Coleta de dados do atleta (Nome, E-mail, Senha, Telefone). |
| **02** | Tela de Login / Autenticação | `Login.png` | `RF-02`, `RNF-04` | Autenticação com e-mail/senha, recuperação e persistência. |
| **03** | Tela Inicial (Início) | `Inicio.png` | `RF-06`, `RNF-02` | Busca de arenas por município e atalhos de favoritos. |
| **04** | Diretório de Arenas | `Arenas.png` | `RF-06` | Grid de arenas com distância, avaliação e comodidades. |
| **05** | Seleção de Quadras | `quadras.png` | `RF-05`, `RF-06` | Escolha da quadra específica para localização do jogo. |
| **06** | Seleção de Data e Horário | `Horario_e_data.png` | `RF-06` | Calendário e horários disponíveis para filtrar o replay. |
| **07** | Galeria de Resultados & Player | `Resultados.png` | `RF-05`, `RF-06` | Exibição de cards de replays de 30s com botão de assistir/baixar. |
| **08** | Painel Administrativo Geral | `Painel_administrativo.png` | `RF-03` | Dashboards globais de crescimento e uso para o perfil `ADM`. |
| **09** | Gerenciamento de Quadras | `Gerencia_de_quadras.png` | `RF-04`, `RF-07` | Tabela de quadras e formulário de cadastro para o `CLI`. |
| **10** | Monitoramento de Câmeras | `Desktop_-_4.png` | `RF-04` | Dashboard de status em tempo real das câmeras (Ativa/Inativa). |

---

## 5. Avaliação pelas 10 Heurísticas de Nielsen

### 📊 Matriz de Conformidade Heurística

| # | Heurística de Nielsen | Status no Protótipo | Observações e Pontos de Destaque |
| :---: | :--- | :---: | :--- |
| **H1** | Visibilidade do Status do Sistema | **Conforme** | Bons feedbacks visuais nos badges de status das câmeras (Ativa/Inativa) e indicação de data/horário selecionados. |
| **H2** | Correspondência entre o Sistema e o Mundo Real | **Conforme** | Linguagem esportiva adequada (*"Corta Replay!"*, *"Quadras"*, *"Arenas"*). |
| **H3** | Controle e Liberdade do Usuário | **Ajuste Necessário** | Falta botão claro de "Voltar" ou "Cancelar" em alguns modais do fluxo de agendamento/filtro. |
| **H4** | Consistência e Padronização | **Conforme** | Identidade visual coerente com o Design System (Verde Replay Neon `#10B981` e tipografia *Inter*). |
| **H5** | Prevenção de Erros | **Ajuste Necessário** | Modal de exclusão manual AUSENTE do painel do cliente (`RF-10`).  |
| **H6** | Reconhecimento em vez de Mnemônica | **Conforme** | Filtros de busca exibem claramente os passos selecionados (Cidade → Arena → Quadra → Data). |
| **H7** | Flexibilidade e Eficiência de Uso | **Conforme** | Atalho direto de busca na tela inicial facilita o acesso de atletas recorrentes. |
| **H8** | Estética e Design Minimalista | **Conforme** | Interface limpa, cards bem espaçados e boa hierarquia visual de dados. |
| **H9** | Ajuda a Reconhecer e Recuperar de Erros | **Ajuste Necessário** | Mensagens de validação de campos no formulário de cadastro precisam indicar exatamente o erro de formato. |
| **H10** | Ajuda e Documentação | **Pendente** | Adicionar tooltips e seções de "Dúvidas Frequentes" para instruir atletas de primeira viagem sobre o limite de 7 dias. |
| **H11** | Telas de Sucesso e Erro | **Ajuste Necessário** | Tais telas estão simples demais e sem um botão para que o usuário possa seguir com a utilização, possível causa de confusão na utilização do sistema (Dica: transformar em pop-up no canto superior da tela ou adicionar botões de "Ok" ou "Cancelar"). |

---

  ## 6. Tabela de Achados e Recomendações de Ação (Backlog de UX)

Abaixo estão listados todos os pontos de melhoria mapeados durante o teste, prontos para priorização pela equipe de Design e Frontend:

| ID | Tela Afetada | Descrição do Problema Encontrado | Gravidade | Recomendação de Solução (Ação) | Responsável |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **USAB-01** | `Criar_conta.png` | Validação de senha fraca não exibe dicas em tempo real abaixo do campo. | **2 (Pequeno)** | Adicionar indicadores visuais dos requisitos da senha (mínimo 8 caracteres, maiúscula, número). | Frontend |
| **USAB-02** | `quadras.png` | Usuários tentaram clicar no card inteiro da quadra, mas apenas o botão de texto estava clicável no protótipo. | **2 (Pequeno)** | Tornar todo o container da quadra (imagem + texto) uma área clicável (*hotspot*). | Design / Frontend |
| **USAB-03** | `Resultados.png` | Ausência de aviso visível sobre a retenção automática de 7 dias (`RN-01`) na listagem dos vídeos. | **3 (Grande)** | Inserir um badge ou mensagem informativa: *"Vídeo disponível por mais X dias"* nos cards de resultados. | Design |
| **USAB-04** | `Gerencia_de_quadras.png` | Falta de modal de confirmação ao clicar no ícone de lixeira/exclusão de quadra. | **3 (Grande)** | Implementar modal de confirmação do Design System antes de disparar a ação de exclusão (`RF-10`). | Frontend |
| **USAB-05** | `Desktop_-_4.png` | Dispositivos mobile com tela pequena cortam a tabela lateral de câmeras sem barra de rolagem visível. | **2 (Pequeno)** | Aplicar rolagem horizontal (*overflow-x: auto*) e ajustes de responsividade (`RNF-02`). | Frontend |
| **USAB-06** | `Modais de erro ou sucesso` | Os modais de erro e sucesso não exibem formas de sair dessa dela | **3 (Grande)** | Mudar o modal para um pop-up na parte superior da tela com contagem regressiva por meio de uma barra para que ele desapareça e um botão "x" ao lado do pop-up para que ele possa ser fechado, ou adicionar uma dica visual como "ok" ou "entendi" em forma de botão para que o modal seja fechado e possa voltar | Frontend |


---

## 7. Métrica de Satisfação Geral (SUS - System Usability Scale)

Após a realização dos testes, os participantes responderam ao questionário padronizado SUS (10 perguntas em escala Likert de 1 a 5):

* **Pontuação Média Obtida:** **[Ex: 82.5 / 100]**
* **Classificação de Usabilidade:** **Excelente (Grade A)**
* **Conclusão de Usabilidade:** O protótipo de alta fidelidade do **TáGravado** apresenta excelente navegabilidade e curva de aprendizado rápida. Com a implementação das correções de alta prioridade (`USAB-03` e `USAB-04`), o sistema estará totalmente pronto para a consolidação final do Frontend.

---

## 8. Próximos Passos e Sinal Amarelo/Verde para o Frontend
* [x] Compartilhar este relatório com a equipe de Design no Figma para ajuste de componentes e áreas de clique.
* [ ] Validar a implementação das mensagens de erro e componentes de estados vazios (*empty states*) nas telas integradas em Docker (`Issue F2-01` e `F2-02`).
* [ ] Reavaliar os cenários durante a execução dos testes automatizados de QA da Sprint 3.
