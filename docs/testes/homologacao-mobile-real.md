# Relatório de homologação da aplicação em dispositivos mobile

* **Issue:** [F5-05 — Homologação e Verificação do Sistema em Aparelho Celular Real do Cliente](https://github.com/PI2-2026-2-equipe-03/pi2-frontend/issues/35) (`pi2-frontend#35`)
* **Rastreabilidade (labels da issue):** `RF-01`, `RF-02`, `RF-06`, `RNF-03`
* **Requisitos verificados de forma complementar:** `RNF-01` (tema claro e escuro), `RNF-02` (responsividade), `RF-03`, `RF-04`, `RF-07`, `RF-11`, `RF-12`

> **Observação sobre a quantidade de dispositivos**: a issue pede testes em pelo menos 2 modelos de smartphones físicos, incluindo Android e iOS. Esse critério não pôde ser atendido. A equipe só tinha um aparelho disponível e não possui nenhum dispositivo iOS. Por isso, os testes foram feitos em um único aparelho, um Samsung Galaxy S24 (modelo SM-S921B/DS, Android). A aplicação foi acessada pela rede local, a partir do servidor de origem.

## 1. Objetivo

Verificar se a aplicação TaGravado funciona corretamente no cenário em que o **cliente (usuário final) usa o sistema em um celular**. Foram avaliados:

- **Funcionalidades:** execução das telas e fluxos do usuário, do gestor e do administrador;
- **Desempenho e fluidez** (`RNF-03`): tempo de resposta das ações e fluidez da interface;
- **Responsividade** (`RNF-02`): adaptação do layout à tela do aparelho;
- **Temas claro e escuro** (`RNF-01`): alternância e legibilidade nos dois temas.

## 2. Ambiente de teste

| Item | Descrição |
| :--- | :--- |
| Dispositivo | Samsung Galaxy S24 (SM-S921B/DS), Android |
| Acesso | Navegador do dispositivo, via rede local, conectado ao servidor de origem |
| Perfis utilizados | Usuário, gestor (cliente) e administrador |

## 3. Checklist de verificação

Legenda: `[x]` tarefa executada; `[ ]` tarefa não executada ou executada só em parte. A explicação aparece entre parênteses.

- [x] **Login** (`RF-02`)
- [x] **Criação de conta** (`RF-01`)
- [ ] **Recuperação de senha** (`RF-11`) (parcial: a tela e a solicitação funcionam, mas o e-mail de recuperação não é enviado porque o serviço de e-mail ainda não foi implementado)
- [x] **Tela inicial** (`RF-06`)
- [x] **Tela de arenas** (`RF-06`) (funciona, com ressalva no menu de seleção; ver P-01)
- [x] **Tela de quadras** (`RF-06`) (funciona, com ressalva no menu de seleção; ver P-01)
- [x] **Tela de replays** (`RF-06`) (funciona, com ressalva no menu de seleção; ver P-01)
- [x] **Tela de perfil**
- [x] **Tela de solicitar gestão** (`RF-12`)
- [x] **Dashboard do cliente** (`RF-04`)
- [x] **Dashboard do administrador** (`RF-03`)
- [ ] **Listagem de quadras** (parcial: a listagem funciona, mas a exclusão de quadra falha; ver P-02)
- [x] **Listagem de patrocinadores** (`RF-07`)

## 4. Resultados

### 4.1 Funcionalidades

As telas e fluxos da checklist funcionaram normalmente. As exceções são a recuperação de senha, que depende do serviço de e-mail ainda não implementado, e os pontos descritos na seção 5.

**Resultado:** ⚠️ Aprovado com ressalvas

### 4.2 Desempenho e fluidez (`RNF-03`)

A interface ficou fluida durante todo o teste, sem travamentos ou atrasos perceptíveis nas transições entre telas. No pior caso observado, as ações levaram cerca de **800 ms** para responder, abaixo do limite de 2 segundos definido no `RNF-03`.

Não foi possível testar o tempo de download de vídeo, porque ainda não há arquivo de replay real disponível para download.

**Resultado:** ⚠️ Aprovado com ressalvas (tempo de resposta das telas atendido; download não testado)

### 4.3 Responsividade (`RNF-02`)

O layout se adaptou bem à tela do dispositivo em todas as telas avaliadas. Não houve rolagem horizontal indevida, sobreposição de elementos nem conteúdo cortado. Botões, campos e cards ficaram legíveis e fáceis de tocar.

**Resultado:** ✅ Aprovado

## 5. Problemas identificados

| ID | Tela / Funcionalidade | Descrição | Impacto |
| :---: | :--- | :--- | :--- |
| P-01 | Componente reutilizável de menu de seleção (telas de arenas, quadras e replays) | No mobile, o "modal" que o menu de seleção abre não se comporta como esperado, o que prejudica a escolha da opção. O problema foi observado nos campos de cidade e de horário. | Usabilidade |
| P-02 | Listagem de quadras — exclusão | Ao clicar no botão de excluir, o frontend envia ao backend a requisição de exclusão da quadra. O backend responde que a rota de exclusão não existe, e a quadra não é excluída. | Funcional |

> P-01 está em um único componente reutilizável, e não em cada campo separadamente. O erro fica no "modal" que o menu de seleção abre no mobile. Como o mesmo componente é usado nas telas de arenas, quadras e replays, uma única correção nele resolve o problema em todas essas telas. P-02 indica que a rota de exclusão de quadra não está disponível no backend.

## 6. Evidências

- [Vídeo de validação e homologação](https://drive.google.com/file/d/1lM_3uxDxvyfHYoQjXKS7U6lNkO1OfMWh/view?usp=sharing) (Google Drive, cerca de 15 minutos): mostra o sistema em uso no dispositivo descrito na seção 2.

## 7. Conclusão

A aplicação foi **homologada com ressalvas** para uso em dispositivo mobile. A responsividade e os temas claro e escuro funcionaram sem problemas. O tempo de resposta ficou dentro do limite do `RNF-03` e as funcionalidades funcionaram normalmente. As pendências são:

- o "modal" do componente reutilizável de menu de seleção no mobile, usado nas telas de arenas, quadras e replays (P-01);
- a rota de exclusão de quadra, que não existe no backend (P-02);
- o envio do e-mail de recuperação de senha, que depende de um serviço ainda não implementado;
- o teste do tempo de download de vídeo, que depende de haver um replay real disponível.

Recomenda-se corrigir esses pontos e repetir o teste deles no mesmo dispositivo. O critério de 2 modelos de smartphone (Android e iOS) continua não atendido, pelos motivos explicados na observação do início deste documento.
