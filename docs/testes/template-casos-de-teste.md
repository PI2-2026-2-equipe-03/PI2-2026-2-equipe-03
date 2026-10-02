# Especificação e Execução de Testes

## 1. Plano de Teste

| Campo | Informação |
| :--- | :--- |
| **Projeto** | [Nome do Projeto Integrador] |
| **Equipe** | [Nome da Equipe / Número do Grupo] |
| **Responsável (QA)** | [Nome do Integrante Responsável por QA/Testes] |
| **Data** | [DD/MM/AAAA] |

---

## 2. Suítes de Teste

> Agrupe os casos de teste por funcionalidade. Cada suíte reúne casos de um mesmo conjunto de requisitos.

| Código | Suíte | Descrição |
| :---: | :--- | :--- |
| **ST-01** | [Nome da Suíte, ex: Autenticação] | [Descrição breve do conjunto de requisitos e testes] |
| **ST-02** | [Nome da Suíte, ex: Gestão de Replays] | [Descrição breve do conjunto de requisitos e testes] |

---

## 3. Casos de Teste

### CT-001 — [Título Curto do Caso de Teste]

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-001 |
| **Versão** | 1.0 |
| **Suíte de Teste** | ST-01 [Nome da Suíte] |
| **Autor** | [Nome do Autor] |
| **Requisito Coberto** | [RF-XX / RNF-XX] |
| **Importância** | [Alta / Média / Baixa] |

* **Resumo:** [Descreva sucintamente o objetivo da verificação e o comportamento esperado].
* **Pré-condições:** [Descreva o estado prévio necessário do sistema, dados cadastrados ou perfil logado].

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | [Descreva a primeira ação do usuário] | [Resultado esperado na interface/sistema] |
| **2** | [Descreva a segunda ação] | [Resultado esperado] |
| **3** | [Descreva a ação principal/confirmação] | [Resultado esperado final] |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| [Nome] | DD/MM/AAAA | [Aprovado / Reprovado / Bloqueado / Não executado] | [— ou Issue #XX] | [Relato de bugs ou observações gerais] |

---

### CT-002 — [Template em Branco para Novos Casos de Teste]

| Campo | Detalhes |
| :--- | :--- |
| **Identificador** | CT-002 |
| **Versão** | 1.0 |
| **Suíte de Teste** | [Código e Nome da Suíte] |
| **Autor** | [Nome do Autor] |
| **Requisito Coberto** | [RF-XX / RNF-XX] |
| **Importância** | [Alta / Média / Baixa] |

* **Resumo:** [Descrição do teste]
* **Pré-condições:** [Pré-condições para execução]

#### Passos de Execução
| Passo | Ação | Resultado Esperado |
| :---: | :--- | :--- |
| **1** | | |
| **2** | | |
| **3** | | |
| **4** | | |

#### Registro de Execução
| Testador | Data | Status | Defeito | Observações |
| :--- | :---: | :---: | :---: | :--- |
| | | | | |

---

## 4. Evidências de Teste

> Uma evidência por passo reprovado ou bloqueado. Nomeie no padrão **`CT-XXX-En`** e versione o arquivo no repositório no caminho **`docs/testes/evidencias/`**.

### CT-___-E_ — [Código do Teste] — [Passo X: Descrição da falha identificada]
*(Anexar captura de tela, log do container ou payload aqui)*
* **Caminho do Arquivo:** `/docs/testes/evidencias/CT-XXX-E1.png`
* **Descrição:** [Detalhamento do comportamento anômalo ou erro capturado].

---

## 5. Legendas e Regras de Execução

### Status da Execução
* **Aprovado:** Todos os passos foram executados exatamente conforme o resultado esperado.
* **Reprovado:** Qualquer passo divergiu do resultado esperado (obriga o registro do passo que falhou no campo *Observações*).
* **Bloqueado:** Não foi possível executar o teste por indisponibilidade do ambiente ou dependência de um caso anterior reprovado.
* **Não executado:** Caso planejado, mas ainda pendente de teste na sprint.

### Status do Caso de Teste
* **Rascunho** · **Em revisão** · **Final** · **Obsoleto**

> ⚠️ **Regra Obrigatória:** Todo caso marcado como **Reprovado** exige a abertura de uma **Issue de defeito no GitHub Projects**, cujo número da issue deve ser anotado na coluna **Defeito**, e o print/log registrado como evidência na pasta `/docs/testes/evidencias/`.
