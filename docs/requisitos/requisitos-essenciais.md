# **Repeteco \- Requisitos Essenciais (versão Gherkin)**

---

## **RE-01:** Cadastro de usuário (RF-01)

**Descrição:** O sistema deve permitir que novos usuários realizem seu cadastro para acessar as funcionalidades relacionadas aos replays disponíveis na plataforma.

**Atores:** Usuário

**Objetivos:**

- Permitir a criação de uma conta de usuário;  
- Identificar os usuários que utilizam o sistema;  
- Associar os replays aos respectivos usuários.

**Fluxo Principal:**

1. O usuário acessa a opção de cadastro;  
2. O sistema apresenta o formulário de cadastro;  
3. O usuário informa nome completo, telefone, e-mail e senha;  
4. O sistema valida os dados e realiza o cadastro;  
5. O sistema informa que o cadastro foi realizado com sucesso.

**Fluxos Alternativos:**

- Caso o usuário não preencha um campo obrigatório, o sistema informa qual campo falta;  
- Caso o e-mail já esteja cadastrado, o sistema informa que já existe uma conta associada;  
- Caso a senha não atenda ao padrão de segurança (mínimo de 8 caracteres, com maiúsculas, minúsculas, números e caracteres especiais), o sistema informa os requisitos não atendidos.

**Prioridade:** Essencial

**Versão Gherkin:**

Cenário: Cadastro com dados válidos  
  Dado que estou na tela de cadastro de usuários  
  Quando preencho nome completo, telefone e e-mail válidos  
  E digito uma senha que atende ao padrão de segurança  
  E clico em "Salvar"  
  Então o usuário é cadastrado  
  E vejo a mensagem "Conta cadastrada com sucesso"

Cenário: Cadastro com e-mail já existente  
  Dado que existe uma conta cadastrada com o e-mail "atleta@email.com"  
  Quando tento me cadastrar com o e-mail "atleta@email.com"  
  Então o cadastro não é realizado  
  E vejo a mensagem "Já existe uma conta associada a este e-mail"

Cenário: Cadastro com campo obrigatório vazio  
  Dado que estou na tela de cadastro de usuários  
  Quando deixo o campo e-mail em branco  
  E clico em "Salvar"  
  Então o cadastro não é realizado  
  E vejo a mensagem "Preencha todos os campos obrigatórios"

Cenário: Cadastro com senha fraca  
  Dado que estou na tela de cadastro de usuários  
  Quando preencho os dados corretamente  
  E digito a senha "12345"  
  E clico em "Salvar"  
  Então o cadastro não é realizado  
  E o sistema informa os requisitos de senha não atendidos

---

## **RE-02:** Login de usuário (RF-02)

**Descrição:** O sistema deve permitir que usuários cadastrados realizem login para acessar as funcionalidades disponíveis para sua conta, incluindo a visualização dos replays.

**Atores:** Usuário, Cliente e Administrador

**Fluxo Principal:**

1. O usuário acessa a tela de login;  
2. O sistema solicita e-mail e senha;  
3. O usuário informa os dados;  
4. O sistema verifica os dados;  
5. O sistema autentica o usuário;  
6. O sistema direciona o usuário para a área principal do seu perfil.

**Fluxos Alternativos:**

1. Caso e-mail ou senha estejam incorretos, o sistema informa que são inválidos;  
2. Caso os campos obrigatórios não sejam preenchidos, o sistema solicita o preenchimento.

**Prioridade:** Essencial

**Versão Gherkin:**

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

Cenário: Login com e-mail não cadastrado  
  Dado que estou na tela de login  
  Quando informo um e-mail que não possui cadastro  
  E clico em "Entrar"  
  Então permaneço na tela de login  
  E vejo a mensagem "E-mail ou senha inválidos"

Cenário: Login com campos obrigatórios vazios  
  Dado que estou na tela de login  
  Quando deixo o e-mail ou a senha em branco  
  E clico em "Entrar"  
  Então permaneço na tela de login  
  E vejo a mensagem "Preencha e-mail e senha"

---

## **RE-03:** Gravar vídeo (replay) (RF-05)

**Descrição:** O cliente aperta e segura um botão na arena e a câmera da quadra armazena os últimos 30 segundos gravados.

**Atores:** Usuário/Cliente (quem estiver na arena)

**Fluxo Principal:**

1. A pessoa na arena aperta e segura o botão por 2 segundos;  
2. O sistema identifica a câmera vinculada à quadra;  
3. Os últimos 30 segundos gravados são armazenados.

**Fluxos Alternativos:**

- Câmera com defeito ou offline: nenhum vídeo é armazenado;  
- Botão solto antes de 2 segundos: nenhum vídeo é armazenado;  
- Quadra sem câmera cadastrada: nenhum vídeo é armazenado.

**Prioridade:** Essencial

**Versão Gherkin:**

Cenário: Câmera em perfeito estado  
  Dado que estou na arena  
  E a câmera da quadra está funcionando  
  Quando aperto e seguro o botão por 2 segundos  
  Então são armazenados os últimos 30 segundos gravados pela câmera

Cenário: Câmera com defeito  
  Dado que estou na arena  
  E a câmera da quadra está com defeito ou offline  
  Quando aperto e seguro o botão por 2 segundos  
  Então nenhum vídeo é armazenado

Cenário: Botão não pressionado pelo tempo suficiente  
  Dado que estou na arena  
  Quando aperto o botão e solto em seguida  
  Então nenhum vídeo é armazenado

Cenário: Quadra sem câmera cadastrada  
  Dado que estou em uma quadra sem câmera cadastrada no sistema  
  Quando aperto e seguro o botão por 2 segundos  
  Então nenhum vídeo é armazenado

---

## **RE-04:** Visualizar e baixar vídeo(RF-06)

**Descrição:** O usuário acessa o site, navega por cidade, arena e horário, e visualiza ou baixa o vídeo escolhido.

**Atores:** Usuário

**Fluxo Principal:**

1. O usuário entra na tela de login e acessa a sua conta;  
2. Procura a cidade na tela principal;  
3. Escolhe a arena;  
4. Escolhe o horário;  
5. Seleciona o vídeo e o visualiza ou faz o download.

**Fluxos Alternativos:**

1. Horário sem nenhuma gravação;  
2. Arena indisponível ou não cadastrada;  
3. Cidade não cadastrada;  
4. Usuário não autenticado é direcionado ao login.

**Prioridade:** Essencial

**Versão Gherkin:**

Cenário: Visualizar e baixar o vídeo escolhido  
  Dado que sou um usuário logado em minha conta  
  Quando acesso a cidade, a arena, o horário e o vídeo escolhido  
  E clico em "Baixar"  
  Então o vídeo é baixado no meu dispositivo

Cenário: Visualizar o vídeo sem baixar  
  Dado que sou um usuário logado em minha conta  
  Quando acesso a cidade, a arena, o horário e o vídeo escolhido  
  Então consigo reproduzir o vídeo na tela

Cenário: Cidade não cadastrada  
  Dado que sou um usuário logado em minha conta  
  Quando digito a cidade desejada  
  Então aparece a mensagem "Cidade não encontrada"

Cenário: Arena não cadastrada  
  Dado que sou um usuário logado em minha conta  
  Quando acesso a cidade  
  E digito a arena desejada  
  Então aparece a mensagem "Arena não encontrada"

Cenário: Horário sem vídeos  
  Dado que sou um usuário logado em minha conta  
  Quando acesso a cidade, a arena e o horário escolhido  
  Então aparece a mensagem "Horário sem vídeos gravados"

Cenário: Acesso sem estar logado  
  Dado que não estou logado  
  Quando tento acessar a tela de vídeos  
  Então sou redirecionado para a tela de login

---

## **RE-05:** Associar informações ao replay (RF-09)

**Descrição:** O sistema deve associar a cada replay gerado as informações de cidade, quadra, data e horário em que a solicitação foi realizada.

**Atores:** Sistema

**Objetivos:**

1. Identificar a quadra relacionada ao replay;  
2. Registrar a data em que o replay foi gerado;  
3. Registrar o horário da geração do replay;  
4. Facilitar a identificação e a consulta dos vídeos.

**Fluxo Principal:**

1. O sistema gera o replay após o acionamento do botão;  
2. O sistema identifica a quadra relacionada à solicitação;  
3. O sistema registra a data e o horário em que o replay foi gerado.

**Fluxo Alternativo:**

1. Caso ocorra erro ao armazenar as informações, o sistema informa a falha e mantém o replay pendente para uma nova tentativa.

**Prioridade:** Essencial

**Versão Gherkin:**  
Cenário: Associação automática de metadados durante a gravação  
  Dado que o replay foi acionado na "Quadra 2" da cidade "Crateús"  
  E o acionamento ocorreu às "19:30:00" do dia "2026-09-24"  
  Quando o sistema processar o vídeo  
  Então deve gravar no banco os metadados {cidade: "Crateús", quadra: "Quadra 2", data\_hora: "2026-09-24 19:30:00"}

Cenário: Falha ao gravar os metadados  
  Dado que o replay foi acionado na "Quadra 2"  
  Quando ocorrer um erro ao gravar os metadados no banco  
  Então o sistema registra a falha  
  E mantém o replay como "pendente"  
  E tenta gravar novamente os metadados

Cenário: Replay encontrado pela busca após associação  
  Dado que um replay foi associado à "Quadra 2" às "19:30:00"  
  Quando um usuário busca pela "Quadra 2" no horário "19:30"  
  Então o replay aparece nos resultados  
---

## **RE-06**: Solicitação de cadastro como gestor de quadra (inclui o RF-13)

**Descrição:** O usuário faz uma solicitação para ser gestor de quadra (perfil Cliente). Após a análise de um administrador, a solicitação é aprovada, reprovada ou indeferida para correção.

**Atores:** Usuário e Administrador

**Fluxo Principal:**

1. O usuário acessa a tela de cadastro de gestor de quadra;  
2. Insere dados válidos e envia a solicitação;  
3. Um administrador verifica e aprova a solicitação;  
4. O usuário passa a ter o perfil de Cliente (gestor de quadra) e é notificado.

**Fluxos Alternativos:**

- Solicitante que não é dono de quadra: o administrador reprova e o solicitante é notificado;  
- E-mail já cadastrado como gestor: o sistema informa que já existe uma conta associada;  
- Dados incorretos ou incompletos: o administrador indefere e indica o que corrigir, e o solicitante pode reenviar.

**Prioridade:** Essencial

**Versão Gherkin:**

Cenário: Solicitação de cadastro com dados válidos  
  Dado que sou um usuário logado  
  Quando insiro dados válidos e envio a solicitação de cadastro como gestor de quadra  
  Então a solicitação fica pendente de aprovação  
  E um administrador é notificado da nova solicitação

Cenário: Aprovação da solicitação pelo administrador  
  Dado que existe uma solicitação pendente com dados válidos  
  Quando um administrador verifica e confirma o cadastro  
  Então o usuário passa a ter o perfil de Cliente (gestor de quadra)  
  E o usuário é notificado da aprovação

Cenário: Reprovação por solicitante não ser dono de quadra  
  Dado que existe uma solicitação de um usuário que não é dono de quadra  
  Quando um administrador avalia a solicitação  
  Então a solicitação é reprovada  
  E o usuário não recebe o perfil de Cliente  
  E o usuário recebe a mensagem "Solicitação Reprovada"

Cenário: Tentativa de solicitação com e-mail já existente  
  Dado que já existe uma solicitação ou conta de gestor com o e-mail "cliente@email.com"  
  Quando tento enviar uma solicitação com o e-mail "cliente@email.com"  
  Então o sistema informa "Já existe uma conta associada a este e-mail"  
  E a solicitação não é criada

Cenário: Solicitação com dados incorretos é indeferida  
  Dado que existe uma solicitação com dados incorretos ou incompletos  
  Quando um administrador avalia a solicitação  
  Então a solicitação é indeferida  
  E o sistema indica quais dados precisam ser corrigidos  
  E o usuário pode reenviar a solicitação com os dados corrigidos

Cenário: Reenvio da solicitação após correção dos dados  
  Dado que recebi um indeferimento solicitando correção de dados  
  Quando corrijo os dados e reenvio a solicitação  
  Então a solicitação volta a ficar pendente de aprovação  
---

## **RE-07**: Cadastrar câmeras (RF-14)

**Descrição:** O Cliente cadastra uma câmera e a vincula a uma quadra da sua arena. Sem câmera vinculada, não é possível gerar replays (RF-05).

**Atores:** Cliente

**Fluxo Principal:**

1. O Cliente acessa a tela "Câmeras";  
2. Clica em "Cadastrar câmera";  
3. Informa os dados da câmera e escolhe a quadra;  
4. O sistema salva e confirma o cadastro.

**Fluxo Alternativo:**

1. Dados obrigatórios não informados: a câmera não é cadastrada.

**Prioridade:** Essencial

**Versão Gherkin:**

Cenário: Câmera cadastrada  
  Dado que sou um Cliente logado e possuo a "Quadra 1" cadastrada  
  Quando entro na tela "Câmeras"  
  E clico em "Cadastrar câmera"  
  E informo todas as informações válidas e vinculo à "Quadra 1"  
  Então aparece a mensagem "Câmera cadastrada"  
  E a câmera fica vinculada à "Quadra 1"

Cenário: Câmera não cadastrada por falta de informações  
  Dado que sou um Cliente logado  
  Quando entro na tela "Câmeras"  
  E clico em "Cadastrar câmera"  
  E não informo todas as informações obrigatórias  
  Então aparece a mensagem "Câmera não cadastrada"

Cenário: Cliente sem quadra cadastrada  
  Dado que sou um Cliente logado e não possuo nenhuma quadra cadastrada  
  Quando tento cadastrar uma câmera  
  Então vejo a mensagem "Cadastre uma quadra antes de adicionar câmeras"

---

## **RE-08** Cadastrar quadras (RF-16)

**Descrição:** O Cliente cadastra as quadras da sua arena. As buscas (RF-06) e a associação de metadados (RF-09) dependem desse cadastro.

**Atores:** Cliente

**Fluxo Principal:**

1. O Cliente acessa a tela "Quadras";  
2. Clica em "Cadastrar quadra";  
3. Informa os dados (nome, arena, cidade);  
4. O sistema salva e confirma o cadastro.

**Fluxo Alternativo:**

1. Dados obrigatórios não informados: a quadra não é cadastrada.

**Prioridade:** Essencial

**Versão Gherkin:**  
Cenário: Quadra cadastrada  
  Dado que sou um Cliente logado  
  Quando entro na tela "Quadras"  
  E clico em "Cadastrar quadra"  
  E informo todas as informações válidas  
  Então aparece a mensagem "Quadra cadastrada"  
  E a quadra passa a aparecer na busca por cidade e arena

Cenário: Quadra não cadastrada por falta de informações  
  Dado que sou um Cliente logado  
  Quando entro na tela "Quadras"  
  E clico em "Cadastrar quadra"  
  E não informo todas as informações obrigatórias  
  Então aparece a mensagem "Quadra não cadastrada"

