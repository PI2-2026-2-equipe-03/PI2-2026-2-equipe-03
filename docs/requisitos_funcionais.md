# Requisitos Funcionais em Gherkin

## Funcionalidade: Cadastro de usuário
*O sistema deve permitir que novos usuários realizem seu cadastro.*

```gherkin
Cenário: Cadastro com dados válidos
  Dado que estou na tela de cadastro de usuários
  Quando preencho nome completo, telefone e e-mail válidos
  E digito uma senha
  E clico em "Salvar"
  Então o cliente é cadastrado
  E vejo a mensagem "Conta cadastrada com sucesso"

Cenário: Cadastro com CPF já existente
  Dado que existe um cliente com o CPF "123.456.789-09"
  Quando tento cadastrar outro cliente com o mesmo CPF
  Então o cadastro não é realizado
  E vejo a mensagem "CPF já cadastrado"
```

---

## Funcionalidade: Login de usuário
*O sistema deve permitir que usuários cadastrados realizem login.*

```gherkin
Cenário: Login com credenciais válidas
  Dado que sou um usuário cadastrado com o e-mail "bruninhoGameplay@empresa.com"
  E estou na tela de login
  Quando informo o e-mail "bruninhoGameplay@empresa.com" e a senha correta
  E clico em "Entrar"
  Então sou redirecionado para a página inicial

Cenário: Login com senha incorreta
  Dado que sou um usuário cadastrado com o e-mail "bruninhoGameplay@empresa.com"
  E estou na tela de login
  Quando informo o e-mail "bruninhoGameplay@empresa.com" e uma senha incorreta
  E clico em "Entrar"
  Então permaneço na tela de login
  E vejo a mensagem "E-mail ou senha inválidos"
```

---

## Funcionalidade: Métricas para o administrador
*Como administrador quero visualizar métricas no dashboard para acompanhar o uso do sistema e apoiar decisões estratégicas.*

```gherkin
Cenário: Visualizar métricas no dashboard após o login
  Dado que existem dados de uso registrados no sistema
  Quando faço login com credenciais válidas
  Então sou direcionado para a tela inicial (dashboard)
  E vejo as métricas de uso do sistema

Cenário: Dashboard sem dados disponíveis
  Dado que não existem dados de uso registrados no sistema
  Quando faço login com credenciais válidas
  Então sou direcionado para a tela inicial (dashboard)
  E vejo a mensagem "Ainda não há dados para exibir"
  E não vejo métricas com valores zerados ou inconsistentes

Cenário: Login com credenciais inválidas
  Quando faço login com uma senha incorreta
  Então permaneço na tela de login
  E vejo a mensagem "E-mail ou senha inválidos"
  E não tenho acesso ao dashboard
```

---

## Funcionalidade: Métricas para o cliente
*Como cliente quero visualizar métricas no dashboard para acompanhar meu uso do sistema e apoiar minhas decisões.*

```gherkin
Cenário: Visualizar métricas no dashboard após o login
  Dado que existem dados de uso registrados para o meu perfil
  Quando faço login com credenciais válidas
  Então sou direcionado para a tela inicial (dashboard)
  E vejo as métricas de uso do meu perfil

Cenário: Dashboard sem dados disponíveis
  Dado que não existem dados de uso registrados para o meu perfil
  Quando faço login com credenciais válidas
  Então sou direcionado para a tela inicial (dashboard)
  E vejo a mensagem "Ainda não há dados para exibir"
  E não vejo métricas com valores zerados ou inconsistentes

Cenário: Login com credenciais inválidas
  Quando faço login com uma senha incorreta
  Então permaneço na tela de login
  E vejo a mensagem "E-mail ou senha inválidos"
  E não tenho acesso ao dashboard
```

---

## Funcionalidade: Gravar Vídeo
*Como cliente, em quadra, aperto o botão ligado à câmera onde são guardados os últimos 30 segundos de gravação.*

```gherkin
Cenário: Câmera em condições de perfeito estado
  Dado que sou um cliente
  Quando estou na arena
  E aperto e seguro o botão por 2 segundos
  Então são armazenados os últimos 30 segundos gravados da câmera

Cenário: Câmera com defeito
  Dado que sou um cliente
  Quando estou na arena
  E aperto e seguro o botão por 2 segundos
  Então nenhum vídeo é armazenado

Cenário: Cliente não segura o botão por tempo suficiente
  Dado que sou um cliente
  Quando estou na arena
  E aperto o botão e solto em seguida
  Então nenhum vídeo é armazenado
```

---

## Funcionalidade: Baixar vídeo
*O usuário acessa o site onde ele consegue visualizar e baixar o vídeo escolhido.*

```gherkin
Cenário: Cliente com cadastro acessa o site, visualiza e baixa o vídeo escolhido
  Dado que sou um cliente que já está logado em sua conta
  Quando acesso a cidade, arena, horário e vídeo escolhido
  E clico em "Baixar"
  Então é feito o download no meu dispositivo

Cenário: Cidade não cadastrada
  Dado que sou um cliente que já está logado em sua conta
  Quando digito a cidade desejada
  Então aparece "cidade não encontrada"

Cenário: Arena não cadastrada
  Dado que sou um cliente que já está logado em sua conta
  Quando acesso a cidade
  E digito a arena desejada
  Então aparece "arena não encontrada"

Cenário: Horário sem vídeos
  Dado que sou um cliente que já está logado em sua conta
  Quando acesso a cidade, arena e horário escolhido
  Então aparece "Horário sem vídeos gravados"
```

---

## Funcionalidade: Cadastrar patrocinadores
*O cliente da aplicação cadastra os patrocinadores da(s) sua(s) quadra(s) em específico.*

```gherkin
Cenário: Vinculação de patrocinador à quadra
  Dado que o Cliente está no painel de gestão de patrocinadores
  Quando cadastrar o patrocinador "Empresa X" enviando a imagem da logo e vinculando à "Quadra 1"
  Então o sistema deve salvar o vínculo e aplicar a marca d'água nos novos replays gerados para a Quadra 1 (RN-05).
```

---

## Funcionalidade: Tempo de disponibilidade dos vídeos
*Após 7 dias os vídeos armazenados serão excluídos automaticamente.*

```gherkin
Cenário: Quadra com vídeos relacionados
  Dado um vídeo com tempo gravado a mais de 7 dias
  Quando a rotina automática de limpeza (cronjob) for executada
  Então o sistema deve deletar o arquivo do storage e marcar o registro como expirado (RN-01)
  E o vídeo não deve mais aparecer nas buscas dos usuários.
```

---

## Funcionalidade: Associar informações ao replay
*O sistema associa cada replay gerado às informações da quadra, data e horário em que a solicitação foi realizada.*

```gherkin
Cenário: Associação automática de metadados durante a gravação
  Dado que o replay foi acionado na "Quadra 2" da cidade "Crateús" às "19:30:00"
  Quando o sistema processar o vídeo
  Então deve gravar no banco os metadados {cidade: "Crateús", quadra: "Quadra 2", data_hora: "2026-09-24 19:30:00", patrocinador_id: 5}.
```

---

## Funcionalidade: Exclusão de vídeos
*O cliente, se desejar, pode excluir um certo vídeo a hora que quiser.*

```gherkin
Cenário: Exclusão manual autorizada pelo proprietário da quadra
  Dado que o Cliente proprietário da quadra está logado
  Quando solicitar a exclusão manual do vídeo ID #1045 informando o motivo "Solicitação do usuário"
  Então o sistema deve remover o vídeo imediatamente (RN-04)
  E registrar um log de auditoria da ação.
```
