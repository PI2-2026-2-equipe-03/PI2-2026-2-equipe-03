1. **Requisitos Funcionais**

**RF-01: Cadastro de usuário**

**Descrição:** O sistema deve permitir que novos usuários realizem seu cadastro para acessar as funcionalidades relacionadas aos replays disponíveis na plataforma.

**Atores:** Usuário

**Objetivos:** 

- Permitir a criação de uma conta de usuário;  
- Identificar os usuários que utilizam o sistema;  
- Associar os replays aos respectivos usuários.


**Fluxo Principal:** 

1. O usuário acessa a opção de cadastro;  
2. O sistema apresenta o formulário de cadastro;  
3. Usuário informa os dados;  
4. O sistema realiza o cadastro;  
5. O sistema informa que o cadastro foi realizado com sucesso.  
   

**Fluxo alternativo:** 

- Caso o usuário não preencha um espaço obrigatório, o sistema deve informar ao usuário.  
- Caso o email já esteja cadastrado, o sistema deve informar que já existe uma conta associada.  
- 

**Prioridade:** Essencial

**Versão Gherkin:**  
	Cenário: Cadastro com dados válidos   
Dado que estou na tela de cadastro de usuários  
Quando preencho nome completo, telefone e e-mail válidos  
E digito uma senha  
E clico em "Salvar"   
Então o cliente é cadastrado  
E vejo a mensagem "Conta cadastrada com sucesso"

Cenário: Cadastro com CPF já existente  
Dado que existe um cliente com o   
CPF "123.456.789-09"   
Quando tento cadastrar outro cliente com o mesmo  
CPF Então o cadastro não é realizado   
E vejo a mensagem "CPF já cadastrado" 

**RF-02: Login de usuário**

**Descrição:**O sistema deve permitir que usuários cadastrados realizem login para acessar as funcionalidades disponíveis para sua conta, incluindo a visualização dos replays.

**Atores:** Usuário  
   
**Fluxo principal:** 

1. O usuário acessa a tela de login;  
2. O sistema solicita email e senha;  
3. Usuário informa os dados;  
4. O sistema verifica os dados;  
5. O sistema autentica o usuário;  
6. O sistema direciona o usuário para a área principal.

**Fluxos alternativos:** 

1. Caso os dados inseridos pelo o usuário esteja incorretas, o sistema informa que o email ou senha são inválidos;  
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

**RF-03:** Métricas para o administrador

**Descrição:**   
Informações relevantes para o administrador, auxiliando na tomada de decisão estratégica e acompanhamento do uso do sistema

**Ator:** Administrador

**Fluxo Principal:**

1. Administrador acessa a aplicação  
2. Faz login no sistema  
3. Acessa a tela inicial (dashboard) com as métricas

**Fluxo Alternativo:**

1. Ausência de dados

**Prioridade:** Importante

**Versão Gherkin:**  
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

**RF-04:** Métricas para o cliente

**Descrição:**   
Informações relevantes para o cliente, auxiliando na tomada de decisão estratégica e acompanhamento do uso do sistema

**Ator:** Cliente

**Fluxo Principal:**

1. Cliente acessa a aplicação  
2. Faz login no sistema  
3. Acessa a tela inicial (dashboard) com as métricas

**Fluxo Alternativo:**

1. Ausência de dados

**Prioridade:** Importante

**Versão Gherkin:**  
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
    	E vejo a mensagem "E-mail ou senha inválidos  
E não tenho acesso ao dashboard

**RF-05:** Gravar Vídeo

**Descrição:**   
O cliente aperta um botão na qual a câmera da quadra armazena os últimos 30 segundos gravados

**Ator:** Usuário

**Fluxo Principal:**  
1\. Cliente aperta o botão   
2\. Os últimos 30 segundos gravados são armazenados no banco de dados

**Prioridade:** Essencial

**Versão Gherkin:**  
	Cenário: câmera em condições de perfeito estado  
	Dado que sou um cliente  
Quando estou na arena  
E aperto e seguro o botão por 2 segundos  
Então é armazenado os últimos 30 segundos gravados da câmera

Cenário: câmera com defeito  
Dado que sou um cliente  
Quando estou na arena  
E aperto e seguro o botão por 2 segundos  
Então nenhum vídeo é armazenado 

Cenário: cliente não segura o botão por tempo suficiente  
	Dado que sou um cliente  
Quando estou na arena  
E aperto o botão e solto em seguida  
Então nenhum vídeo é armazenado

**RF-06**: Baixar vídeo

**Descrição:**   
O usuário acessa um site onde ele consegue visualizar e baixar o vídeo escolhido

**Ator:** Usuário

**Fluxo Principal:**

1. Usuário entra na tela de Login  
2. Acessa a sua conta  
3. Procura a cidade na tela principal  
4. Escolhe a quadra  
5. Busca o horário  
6. Busca o video, visualiza ou faz o download do mesmo

**Fluxo Alternativo:**

1. Horários sem nenhuma gravação  
2. Quadras indisponíveis  
3. Cidade não cadastrada

**Prioridade:** Essencial

**Versão Gherkin:**  
Cenário: cliente com cadastro acessa o site, visualiza e baixa o vídeo escolhido  
	Dado que sou um cliente que já está logado em sua conta  
	Quando acesso a cidade, arena, horário e vídeo escolhido  
	E clico em “Baixar”  
	Então é feito o download no meus dispositivo

Cenário: cidade não cadastrada  
	Dado que sou um cliente que já está logado em sua conta  
	Quando digito a cidade desejada  
	Então aparece “cidade não encontrada”

Cenário: arena não cadastrada  
	Dado que sou um cliente que já está logado em sua conta  
	Quando acesso a cidade  
	E digito a arena desejada  
	Então  aparece “arena não encontrada”

Cenário: horário sem vídeos  
	Dado que sou um cliente que já está logado em sua conta  
	Quando acesso a cidade, arena, horário escolhido  
	Então aparece “Horário sem vídeos gravados”

**RF-07**: Cadastrar patrocinadores

**Descrição:**   
O cliente da aplicação cadastra os patrocinadores da(s) sua(s) quadra(s) em específico

**Ator:** Cliente

**Fluxo Principal:**

1. Cliente entra na tela de Login  
2. Acessa a sua conta  
3. Cadastra os patrocinadores (nome, foto, duração, valor)  
4. Escolhe a(s) sua(s) quadra(s)  
5. Adiciona o(s) patrocinador(es)

**Fluxo Alternativo:**

1. Patrocinador já existe  
2. Total de patrocinadores já preenchido

**Prioridade:** Importante

**Versão Gherkin:**  
	Cenário: Vinculação de patrocinador à quadra  
 Dado que o Cliente está no painel de gestão de patrocinadores  
 Quando cadastrar o patrocinador "Empresa X" enviando a imagem da logo   
 e  vinculando à "Quadra 1"  
 Então o sistema deve salvar o vínculo e aplicar a marca d'água nos  
 novos  replays gerados para a Quadra 1 (RN-05).

**RF-08:** Tempo de disponibilidade dos vídeos

**Descrição:** após 7 dias os vídeos armazenados serão excluídos automaticamente

**Ator:** Sistema

**Prioridade:** Importante

**Versão Gherkin:**  
	Cenário: Quadra com vídeos relacionados  
	Dado um vídeo com tempo gravado a mais de 7 dias  
Quando a rotina automática de limpeza (cronjob) for executada	  
Então o sistema deve deletar o arquivo do storage e marcar o registro como expirado (RN-01)  
  	E o vídeo não deve mais aparecer nas buscas dos usuários.

**RF-09:** Associar informações ao replay 

**Descrição:** O sistema deve associar cada replay gerado as informações da quadra, data e horário em que a solicitação foi realizada

**Atores:** Sistema

**Objetivos:** 

1. Identificar a quadra relacionada ao replay;  
2. Registrar a data em que o replay foi gerado;  
3. Registrar o horário da geração do replay;  
4. Facilitar a identificação e consulta dos videos.

**Fluxo principal:**

1. O sistema gera o replay após o acionamento do botão;  
2. O sistema identifica a quadra relacionada a solicitação  
3. O sistema registra a data em que o replay foi gerado;   
4. O sistema registra o horário em que o replay foi gerado. 

**Fluxos alternativos:** 

1. Caso ocorra um erro ao armazenar as informações, o sistema informa a falha e mantém o replay pendente para uma nova tentativa. 

**Prioridade:** Essencial

**Versão Gherkin:**  
	Cenário: Associação automática de metadados durante a gravação  
Dado que o replay foi acionado na "Quadra 2" da cidade "Crateús"  
às   "19:30:00"  
Quando o sistema processar o vídeo  
  	Então deve gravar no banco os metadados {cidade: "Crateús",  
quadra: "Quadra 2", data\_hora: "2026-09-24 19:30:00", patrocinador id: 5}. 

**RF-09:** Exclusão de vídeos

**Descrição:** O cliente, se desejar excluir um certo vídeo a hora que quiser, assim ele poderá, ao invés de ter que esperar a exclusão automaticamente

**Ator:** Cliente

**Fluxo principal:**

1. O cliente com sua conta de administrador loga em sua conta  
2. Busca a arena desejada  
3. seleciona o horário do vídeo  
4. Encontra o vídeo   
5. exclui o video manualmente

**Prioridade:** Desejável

**Versão Gherkin:**  
	Cenário: Exclusão manual autorizada pelo proprietário da quadra  
 	Dado que o Cliente proprietário da quadra está logado  
Quando solicitar a exclusão manual do vídeo ID \#1045 informando o  motivo "Solicitação do usuário"  
  	Então o sistema deve remover o vídeo imediatamente (RN-04)  
  	E registrar um log de auditoria da ação.

