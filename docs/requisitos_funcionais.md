# Requisitos Funcionais

---

## RF-01: Cadastro de usuário

* **Descrição:** O sistema deve permitir que novos usuários realizem seu cadastro para acessar as funcionalidades relacionadas aos replays disponíveis na plataforma. Dados como nome completo, email e telefone e criação de uma senha serão necessários nessa etapa.
* **Atores:** Usuário
* **Objetivos:**
  * Permitir a criação de uma conta de usuário;
  * Identificar os usuários que utilizam o sistema;
  * Associar os replays aos respectivos usuários.
* **Fluxo Principal:**
  1. O usuário acessa a opção de cadastro;
  2. O sistema apresenta o formulário de cadastro;
  3. Usuário informa os dados;
  4. O sistema realiza o cadastro;
  5. O sistema informa que o cadastro foi realizado com sucesso.
* **Fluxo Alternativo:**
  * Caso o usuário não preencha um espaço obrigatório, o sistema deve informar ao usuário.
  * Caso o email já esteja cadastrado, o sistema deve informar que já existe uma conta associada.
* **Prioridade:** Essencial

---

## RF-02: Login de usuário

* **Descrição:** O sistema deve permitir que usuários cadastrados realizem login para acessar as funcionalidades disponíveis para sua conta, incluindo a visualização dos replays. O sistema também terá um tempo máximo de 30 minutos de conta logada, após esse tempo será feito o logout automaticamente.
* **Atores:** Usuário
* **Fluxo Principal:**
  1. O usuário acessa a tela de login;
  2. O sistema solicita email e senha;
  3. Usuário informa os dados;
  4. O sistema verifica os dados;
  5. O sistema autentica o usuário;
  6. O sistema direciona o usuário para a área principal.
* **Fluxos Alternativos:**
  1. Caso os dados inseridos pelo usuário estejam incorretos, o sistema informa que o email ou senha são inválidos;
  2. Caso os campos obrigatórios não sejam preenchidos, o sistema solicita o preenchimento.
* **Prioridade:** Essencial

---

## RF-03: Métricas para o administrador

* **Descrição:** Dashboard de dados e estatísticas, quadras mais acessadas, quantidade de clientes ativos e etc. Tela com informações que auxiliam na tomada de decisão estratégica e acompanhamento do uso do sistema.
* **Ator:** Administrador
* **Fluxo Principal:**
  1. Administrador acessa a aplicação;
  2. Faz login no sistema;
  3. Acessa a tela inicial (dashboard) com as métricas.
* **Fluxo Alternativo:**
  1. Ausência de dados.
* **Prioridade:** Importante

---

## RF-04: Métricas para o cliente

* **Descrição:** Dashboard de dados e estatísticas, edição de patrocinadores cadastrados, visualização de horários de pico e etc. Tela com informações que auxiliam na tomada de decisão estratégica e acompanhamento do uso do sistema.
* **Ator:** Cliente
* **Fluxo Principal:**
  1. Cliente acessa a aplicação;
  2. Faz login no sistema;
  3. Acessa a tela inicial (dashboard) com as métricas.
* **Fluxo Alternativo:**
  1. Ausência de dados.
* **Prioridade:** Importante

---

## RF-05: Gravar Vídeo

* **Descrição:** O cliente aperta o botão da quadra e a câmera armazenará os últimos 30 segundos gravados.
* **Ator:** Usuário
* **Fluxo Principal:**
  1. Cliente aperta o botão;
  2. Os últimos 30 segundos gravados são armazenados no banco de dados.
* **Prioridade:** Essencial

---

## RF-06: Baixar vídeo

* **Descrição:** O usuário acessa um site onde ele consegue visualizar e baixar o vídeo escolhido em MP4.
* **Ator:** Usuário
* **Fluxo Principal:**
  1. Usuário entra na tela de Login;
  2. Acessa a sua conta;
  3. Procura a cidade na tela principal;
  4. Escolhe a quadra;
  5. Busca o horário;
  6. Busca o vídeo, visualiza ou faz o download do mesmo.
* **Fluxo Alternativo:**
  1. Horários sem nenhuma gravação;
  2. Quadras indisponíveis;
  3. Cidade não cadastrada.
* **Prioridade:** Essencial

---

## RF-07: Cadastrar patrocinadores

* **Descrição:** O cliente da aplicação cadastra os patrocinadores da(s) sua(s) quadra(s) em específico.
* **Ator:** Cliente
* **Fluxo Principal:**
  1. Cliente entra na tela de Login;
  2. Acessa a sua conta;
  3. Cadastra os patrocinadores (nome, foto, duração, valor);
  4. Escolhe a(s) sua(s) quadra(s);
  5. Adiciona o(s) patrocinador(es).
* **Fluxo Alternativo:**
  1. Patrocinador já existe;
  2. Total de patrocinadores já preenchido.
* **Prioridade:** Importante

---

## RF-08: Tempo de disponibilidade dos vídeos

* **Descrição:** Após 7 dias os vídeos armazenados serão excluídos automaticamente.
* **Ator:** Sistema
* **Prioridade:** Importante

---

## RF-09: Associar informações ao replay

* **Descrição:** O sistema deve associar cada replay gerado às informações da quadra, data e horário em que a solicitação foi realizada.
* **Atores:** Sistema
* **Objetivos:**
  1. Identificar a quadra relacionada ao replay;
  2. Registrar a data em que o replay foi gerado;
  3. Registrar o horário da geração do replay;
  4. Facilitar a identificação e consulta dos vídeos.
* **Fluxo Principal:**
  1. O sistema gera o replay após o acionamento do botão;
  2. O sistema identifica a quadra relacionada à solicitação;
  3. O sistema registra a data em que o replay foi gerado;
  4. O sistema registra o horário em que o replay foi gerado.
* **Fluxos Alternativos:**
  1. Caso ocorra um erro ao armazenar as informações, o sistema informa a falha e mantém o replay pendente para uma nova tentativa.
* **Prioridade:** Essencial

---

## RF-10: Exclusão de vídeos

* **Descrição:** O cliente (dono da quadra) e/ou Administrador, se desejar excluir um certo vídeo a hora que quiser, assim ele poderá, ao invés de ter que esperar a exclusão automaticamente.
* **Ator:** Cliente e Administrador
* **Fluxo Principal:**
  1. O cliente ou Administrador loga em sua conta;
  2. Busca a arena desejada;
  3. Seleciona o horário do vídeo;
  4. Encontra o vídeo;
  5. Exclui o vídeo manualmente.
* **Prioridade:** Desejável

---

## RF-11: Recuperar senha

* **Descrição:** O sistema deve permitir que um usuário cadastrado redefina a senha da conta a partir do link "Esqueci minha senha" na tela de login. O usuário informa o e-mail; caso ele exista, o sistema envia uma mensagem com o botão "Redefinir senha". Ao clicar, o usuário informa a nova senha e a confirmação, e é redirecionado à tela de login.
* **Atores:** Usuário
* **Objetivos:**
  * Permitir a recuperação de acesso quando a senha for esquecida;
  * Atualizar a senha da conta sem exigir sessão autenticada.
* **Fluxo Principal:**
  1. O usuário clica em "Esqueci minha senha" na tela de login;
  2. O sistema redireciona para a página de recuperação;
  3. O usuário informa o e-mail;
  4. Caso o e-mail exista, o sistema envia um e-mail com o botão "Redefinir senha";
  5. O usuário clica no botão, informa a nova senha e a confirmação, e clica em "Redefinir";
  6. O sistema atualiza a senha e redireciona o usuário para a tela de login.
* **Fluxo Alternativo:**
  * Caso o e-mail não esteja cadastrado, o sistema não envia o e-mail de redefinição.
  * Caso os campos de senha estejam em branco ou não coincidam, o sistema solicita a correção.
* **Prioridade:** Essencial