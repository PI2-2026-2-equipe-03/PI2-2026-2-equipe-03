# Requisitos Funcionais em Gherkin

---

### Funcionalidade: Cadastro de usuário
O sistema deve permitir que novos usuários realizem seu cadastro.

* **Cenário: Cadastro com dados válidos**
  * **Dado** que estou na tela de cadastro de usuários
  * **Quando** preencho nome completo, telefone e e-mail válidos
  * **E** digito uma senha
  * **E** clico em "Salvar"
  * **Então** o cliente é cadastrado
  * **E** vejo a mensagem "Conta cadastrada com sucesso"

* **Cenário: Cadastro com CPF já existente**
  * **Dado** que existe um cliente com o CPF "123.456.789-09"
  * **Quando** tento cadastrar outro cliente com o mesmo CPF
  * **Então** o cadastro não é realizado
  * **E** vejo a mensagem "CPF já cadastrado"

* **Atores:** Usuário
* **Prioridade:** Essencial

---

### Funcionalidade: Login de usuário
O sistema deve permitir que usuários cadastrados realizem login.

* **Cenário: Login com credenciais válidas**
  * **Dado** que sou um usuário cadastrado com o e-mail "bruninhoGameplay@empresa.com"
  * **E** estou na tela de login
  * **Quando** informo o e-mail "bruninhoGameplay@empresa.com" e a senha correta
  * **E** clico em "Entrar"
  * **Então** sou redirecionado para a página inicial

* **Cenário: Login com senha incorreta**
  * **Dado** que sou um usuário cadastrado com o e-mail "bruninhoGameplay@empresa.com"
  * **E** estou na tela de login
  * **Quando** informo o e-mail "bruninhoGameplay@empresa.com" e uma senha incorreta
  * **E** clico em "Entrar"
  * **Então** permaneço na tela de login
  * **E** vejo a mensagem "E-mail ou senha inválidos"

* **Atores:** Usuário
* **Prioridade:** Essencial

---

### Funcionalidade: Métricas para o administrador
Como administrador quero visualizar métricas no dashboard para acompanhar o uso do sistema e apoiar decisões estratégicas.

* **Cenário: Visualizar métricas no dashboard após o login**
  * **Dado** que existem dados de uso registrados no sistema
  * **Quando** faço login com credenciais válidas
  * **Então** sou direcionado para a tela inicial (dashboard)
  * **E** vejo as métricas de uso do sistema

* **Cenário: Dashboard sem dados disponíveis**
  * **Dado** que não existem dados de uso registrados no sistema
  * **Quando** faço login com credenciais válidas
  * **Então** sou direcionado para a tela inicial (dashboard)
  * **E** vejo a mensagem "Ainda não há dados para exibir"
  * **E** não vejo métricas com valores zerados ou inconsistentes

* **Cenário: Login com credenciais inválidas**
  * **Quando** faço login com uma senha incorreta
  * **Então** permaneço na tela de login
  * **E** vejo a mensagem "E-mail ou senha inválidos"
  * **E** não tenho acesso ao dashboard

* **Ator:** Administrador
* **Prioridade:** Importante

---

### Funcionalidade: Métricas para o cliente
Como cliente quero visualizar métricas no dashboard para acompanhar meu uso do sistema e apoiar minhas decisões.

* **Cenário: Visualizar métricas no dashboard após o login**
  * **Dado** que existem dados de uso registrados para o meu perfil
  * **Quando** faço login com credenciais válidas
  * **Então** sou direcionado para a tela inicial (dashboard)
  * **E** vejo as métricas de uso do meu perfil

* **Cenário: Dashboard sem dados disponíveis**
  * **Dado** que não existem dados de uso registrados para o meu perfil
  * **Quando** faço login com credenciais válidas
  * **Então** sou direcionado para a tela inicial (dashboard)
  * **E** vejo a mensagem "Ainda não há dados para exibir"
  * **E** não vejo métricas com valores zerados ou inconsistentes

* **Cenário: Login com credenciais inválidas**
  * **Quando** faço login com uma senha incorreta
  * **Então** permaneço na tela de login
  * **E** vejo a mensagem "E-mail ou senha inválidos"
  * **E** não tenho acesso ao dashboard

* **Ator:** Cliente
* **Prioridade:** Importante

---

### Funcionalidade: Gravar Video
Como cliente, em quadra, aperto o botão ligado à câmera onde é guardado os últimos 30 segundos de gravação.

* **Cenário: Câmera em condições de perfeito estado**
  * **Dado** que sou um cliente
  * **Quando** estou na arena
  * **E** aperto e seguro o botão por 2 segundos
  * **Então** é armazenado os últimos 30 segundos gravados da câmera

* **Cenário: Câmera com defeito**
  * **Dado** que sou um cliente
  * **Quando** estou na arena
  * **E** aperto e seguro o botão por 2 segundos
  * **Então** nenhum vídeo é armazenado

* **Cenário: Cliente não segura o botão por tempo suficiente**
  * **Dado** que sou um cliente
  * **Quando** estou na arena
  * **E** aperto o botão e solto em seguida
  * **Então** nenhum vídeo é armazenado

* **Autor:** Sistema
* **Prioridade:** Essencial

---

### Funcionalidade: Baixar vídeo
O usuário acessa o site onde ele consegue visualizar e baixar o vídeo escolhido.

* **Cenário: Cliente com cadastro acessa o site, visualiza e baixa o vídeo escolhido**
  * **Dado** que sou um cliente que já está logado em sua conta
  * **Quando** acesso a cidade, arena, horário e vídeo escolhido
  * **E** clico em "Baixar"
  * **Então** é feito o download no meu dispositivo

* **Cenário: Cidade não cadastrada**
  * **Dado** que sou um cliente que já está logado em sua conta
  * **Quando** digito a cidade desejada
  * **Então** aparece "cidade não encontrada"

* **Cenário: Arena não cadastrada**
  * **Dado** que sou um cliente que já está logado em sua conta
  * **Quando** acesso a cidade
  * **E** digito a arena desejada
  * **Então** aparece "arena não encontrada"

* **Cenário: Horário sem vídeos**
  * **Dado** que sou um cliente que já está logado em sua conta
  * **Quando** acesso a cidade, arena, horário escolhido
  * **Então** aparece "Horário sem vídeos gravados"

* **Autor:** Sistema
* **Prioridade:** Essencial

---

### Funcionalidade: Cadastrar patrocinadores
O cliente da aplicação cadastra os patrocinadores da(s) sua(s) quadra(s) em específico.

* **Cenário: Vinculação de patrocinador à quadra**
  * **Dado** que o Cliente está no painel de gestão de patrocinadores
  * **Quando** cadastrar o patrocinador "Empresa X" enviando a imagem da logo e vinculando à "Quadra 1"
  * **Então** o sistema deve salvar o vínculo e aplicar a marca d'água nos novos replays gerados para a Quadra 1 (RN-05).

* **Autor:** Cliente
* **Prioridade:** Importante

---

### Funcionalidade: Tempo de disponibilidade dos vídeos
Após 7 dias os vídeos armazenados serão excluídos automaticamente.

* **Cenário: Quadra com vídeos relacionados**
  * **Ator:** Sistema
  * **Dado** um vídeo com tempo gravado a mais de 7 dias
  * **Quando** a rotina automática de limpeza (cronjob) for executada
  * **Então** o sistema deve deletar o arquivo do storage e marcar o registro como expirado (RN-01)
  * **E** o vídeo não deve mais aparecer nas buscas dos usuários.

* **Prioridade:** Importante

---

### Funcionalidade: Associar informações ao replay
O sistema associa cada replay gerado às informações da quadra, data e horário em que a solicitação foi realizada.

* **Cenário: Associação automática de metadados durante a gravação**
  * **Dado** que o replay foi acionado na "Quadra 2" da cidade "Crateús" às "19:30:00"
  * **Quando** o sistema processar o vídeo
  * **Então** deve gravar no banco os metadados `{cidade: "Crateús", quadra: "Quadra 2", data_hora: "2026-09-24 19:30:00", patrocinador_id: 5}`.

* **Atores:** Sistema
* **Prioridade:** Essencial

---

### Funcionalidade: Exclusão de vídeos
O cliente, se desejar, pode excluir um certo vídeo a hora que quiser.

* **Cenário: Exclusão manual autorizada pelo proprietário da quadra**
  * **Dado** que o Cliente proprietário da quadra está logado
  * **Quando** solicitar a exclusão manual do vídeo ID #1045 informando o motivo "Solicitação do usuário"
  * **Então** o sistema deve remover o vídeo imediatamente (RN-04)
  * **E** registrar um log de auditoria da ação.

* **Autor:** Cliente e Administrador
* **Prioridade:** Importante

---

### Funcionalidade: Recuperação de senha como usuário
Cliente poderá recuperar a senha caso tenha esquecido ou modificá-la se desejar.

* **Cenário: Recuperação de senha via e-mail com sucesso**
  * **Quando** solicito a mudança de senha
  * **E** escolho receber o código de verificação por e-mail
  * **Então** recebo um código de verificação no e-mail cadastrado
  * **Quando** digito o código correto
  * **Então** o sistema solicita que eu digite a nova senha duas vezes
  * **Quando** informo a mesma nova senha nos dois campos
  * **Então** minha senha é alterada
  * **E** sou redirecionado para a tela de login

* **Cenário: Recuperação de senha via telefone com sucesso**
  * **Quando** solicito a mudança de senha
  * **E** escolho receber o código de verificação por telefone
  * **Então** recebo um código de verificação por SMS no telefone cadastrado
  * **Quando** digito o código correto
  * **Então** o sistema solicita que eu digite a nova senha duas vezes
  * **Quando** informo a mesma nova senha nos dois campos
  * **Então** minha senha é alterada
  * **E** sou redirecionado para a tela de login

* **Cenário: Código de verificação incorreto**
  * **Quando** solicito a mudança de senha
  * **E** escolho receber o código de verificação por e-mail
  * **E** digito um código incorreto
  * **Então** o sistema aponta "Código inválido"
  * **E** retorno para a etapa de escolha do meio de recebimento do código

* **Cenário: Nova senha e confirmação não coincidem**
  * **Dado** que digitei o código de verificação corretamente
  * **Quando** informo a nova senha e uma confirmação diferente dela
  * **Então** o sistema informa "As senhas não coincidem"
  * **E** permaneço na tela de redefinição de senha

* **Cenário: Nova senha não atende aos critérios mínimos**
  * **Dado** que digitei o código de verificação corretamente
  * **Quando** informo uma nova senha que não atende aos critérios mínimos de segurança
  * **Então** o sistema informa os requisitos não atendidos
  * **E** a senha não é alterada

* **Cenário: E-mail ou telefone não cadastrado**
  * **Quando** solicito a mudança de senha
  * **E** informo um e-mail ou telefone não cadastrado no sistema
  * **Então** o sistema informa "Não encontramos uma conta com esses dados"
  * **E** nenhum código é enviado

---

### Funcionalidade: Solicitação de cadastro como gestor de quadra
Como cliente quero solicitar o cadastro como gestor de quadra para obter permissões de administrador de quadra após aprovação.

* **Cenário: Solicitação de cadastro com dados válidos**
  * **Quando** insiro dados válidos e envio a solicitação de cadastro
  * **Então** a solicitação fica pendente de aprovação
  * **E** um administrador é notificado da nova solicitação

* **Cenário: Aprovação da solicitação pelo administrador**
  * **Dado** que existe uma solicitação de cadastro pendente com dados válidos
  * **Quando** um administrador verifica e confirma o cadastro
  * **Então** o cliente passa a ter o perfil de administrador de quadra
  * **E** o cliente é notificado da aprovação

* **Cenário: Reprovação por solicitante não ser dono de quadra**
  * **Dado** que existe uma solicitação de cadastro de um usuário que não é dono de uma quadra
  * **Quando** um administrador avalia a solicitação
  * **Então** a solicitação é reprovada
  * **E** o cliente não recebe o perfil de administrador de quadra
  * **E** o cliente é notificado da reprovação

* **Cenário: Tentativa de cadastro com e-mail já existente**
  * **Dado** que já existe uma conta cadastrada com o e-mail "cliente@email.com"
  * **Quando** tento enviar uma solicitação de cadastro com o e-mail "cliente@email.com"
  * **Então** o sistema informa "Já existe uma conta associada a este e-mail"
  * **E** a solicitação não é criada

* **Cenário: Solicitação com dados incorretos é indeferida**
  * **Dado** que existe uma solicitação de cadastro com dados incorretos ou incompletos
  * **Quando** um administrador avalia a solicitação
  * **Então** a solicitação é indeferida
  * **E** o sistema indica quais dados precisam ser corrigidos
  * **E** o cliente pode reenviar a solicitação com os dados corrigidos

* **Cenário: Reenvio da solicitação após correção dos dados**
  * **Dado** que recebi um indeferimento solicitando correção de dados
  * **Quando** corrijo os dados e reenvio a solicitação
  * **Então** a solicitação volta a ficar pendente de aprovação
