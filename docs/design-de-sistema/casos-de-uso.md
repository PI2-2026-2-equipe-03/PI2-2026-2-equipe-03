# Especificação dos Casos de Uso (UC)

## 1. Identificação do Projeto

- **Projeto:** Tá Gravado
- **Equipe:** Equipe 3
- **Autores (Analistas):** Rick Farias
- **Data da Última Atualização:** 24/09/2026

---

## 2. Sumário dos Casos de Uso

> Rastreabilidade inicial conectando os Casos de Uso aos Requisitos Funcionais (RFs) correspondentes.


| Código    | Nome do Caso de Uso             | Atores Envolvidos | Requisito Associado | Prioridade |
| --------- | ------------------------------- | ----------------- | ------------------- | ---------- |
| **UC-01** | Cadastrar Usuário               | Usuário           | `RF-01`             | Essencial  |
| **UC-02** | Autenticar Usuário no Sistema   | Usuário           | `RF-02`             | Essencial  |
| **UC-03** | Gravar Replay da Quadra         | Usuário, Sistema  | `RF-05`, `RF-09`    | Essencial  |
| **UC-04** | Baixar Replay                   | Usuário           | `RF-06`             | Essencial  |
| **UC-05** | Cadastrar Patrocinador da Arena | Cliente           | `RF-07`             | Importante |
| **UC-06** | Recuperar Senha                 | Usuário           | `RF-11`             | Essencial  |
| **UC-07** | Cadastrar Gestor de Quadra      | Usuário, Administrador | `RF-12`        | Essencial  |


---



## 3. Especificação Detalhada dos Casos de Uso



### UC-01 — Cadastrar Usuário


| Campo                   | Detalhes                                                                                           |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-01                                                                                              |
| **Nome**                | Cadastrar Usuário no Sistema                                                                       |
| **Atores**              | Usuário                                                                                            |
| **Requisito Associado** | `RF-01` (Cadastro de usuário)                                                                      |
| **Prioridade**          | Essencial                                                                                          |
| **Pré-condições**       | O ator possuir conexão à internet e ainda não possuir uma conta cadastrada com o e-mail informado. |
| **Pós-condições**       | Conta de usuário criada; usuário apto a realizar login.                                            |




#### Fluxo Principal (Caminho Feliz)

1. O ator acessa a opção "Criar conta" na tela inicial da aplicação.
2. O sistema exibe o formulário de cadastro solicitando nome completo, e-mail, telefone e senha.
3. O ator preenche todos os campos e confirma o envio.
4. O sistema valida os dados informados e verifica se o e-mail já está em uso.
5. O sistema cria a conta do usuário e a armazena no banco de dados.
6. O sistema exibe a mensagem de sucesso e direciona o ator para a tela de login.



#### Fluxos Alternativos

Não se aplica.



#### Fluxos de Exceção

**3a. Campo obrigatório não preenchido**

3a.1. O ator tenta enviar o formulário com algum campo obrigatório em branco.
3a.2. O sistema bloqueia o envio e destaca o(s) campo(s) pendente(s), solicitando o preenchimento.
3a.3. O caso de uso retorna ao passo 3.

**4a. E-mail já cadastrado**

4a.1. O sistema identifica que o e-mail informado já está associado a uma conta existente.
4a.2. O sistema exibe a mensagem: *"Já existe uma conta associada a este e-mail"* e sugere ao ator recuperar a senha (UC-06) ou realizar login (UC-02).
4a.3. O caso de uso é encerrado.

---



### UC-02 — Autenticar Usuário no Sistema


| Campo                   | Detalhes                                                                                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-02                                                                                                                                                               |
| **Nome**                | Autenticar Usuário no Sistema                                                                                                                                       |
| **Atores**              | Usuário                                                                                                                                                             |
| **Requisito Associado** | `RF-02` (Login de usuário)                                                                                                                                          |
| **Prioridade**          | Essencial                                                                                                                                                           |
| **Pré-condições**       | Usuário previamente cadastrado (UC-01) e com conexão à internet.                                                                                                    |
| **Pós-condições**       | Sessão autenticada criada, com validade de até 30 minutos, e usuário direcionado à área principal correspondente ao seu perfil (Usuário, Cliente ou Administrador). |




#### Fluxo Principal

1. O ator acessa a tela de login da aplicação.
2. O sistema solicita e-mail e senha.
3. O ator informa as credenciais e confirma.
4. O sistema verifica os dados junto à base de usuários.
5. O sistema autentica o ator e inicia uma sessão com tempo máximo de 30 minutos.
6. O sistema direciona o ator para a área principal de acordo com seu perfil.



#### Fluxos Alternativos

**3a. Esqueci minha senha**

3a.1. O ator clica no link "Esqueci minha senha" na tela de login.
3a.2. O sistema inicia o UC-06 (Recuperar Senha).
3a.3. O caso de uso é encerrado.



#### Fluxos de Exceção

**3b. Campos obrigatórios não preenchidos**

3b.1. O ator tenta enviar o formulário sem preencher e-mail e/ou senha.
3b.2. O sistema bloqueia o envio e solicita o preenchimento dos campos.
3b.3. O caso de uso retorna ao passo 3.

**4a. Credenciais inválidas**

4a.1. O sistema identifica que o e-mail ou a senha informados estão incorretos.
4a.2. O sistema exibe a mensagem: *"E-mail e/ou senha inválidos"*.
4a.3. O ator permanece na tela de login para nova tentativa.
4a.4. O caso de uso retorna ao passo 3.

**5a. Expiração da sessão**

5a.1. Decorridos 30 minutos de sessão ativa, o sistema realiza o logout automático do ator.
5a.2. O sistema redireciona o ator para a tela de login, solicitando nova autenticação.
5a.3. O caso de uso é encerrado.

---



### UC-03 — Gravar Replay da Quadra


| Campo                   | Detalhes                                                                                                       |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-03                                                                                                          |
| **Nome**                | Gravar Replay da Quadra                                                                                        |
| **Atores**              | Usuário (aciona a gravação); Sistema (processa e associa os dados)                                             |
| **Requisito Associado** | `RF-05` (Gravar Vídeo) e `RF-09` (Associar informações ao replay)                                              |
| **Prioridade**          | Essencial                                                                                                      |
| **Pré-condições**       | Câmera da quadra ativa e conectada à rede; usuário presente fisicamente na quadra no momento do acionamento.   |
| **Pós-condições**       | Vídeo dos últimos 30 segundos armazenado no banco de dados, associado à quadra, data e horário da solicitação. |



#### Fluxo Principal

1. O usuário aperta o botão de gravação disponível na quadra.
2. O sistema captura o buffer de vídeo correspondente aos últimos 30 segundos.
3. O sistema identifica a quadra relacionada à solicitação.
4. O sistema registra a data e o horário em que o replay foi gerado.
5. O sistema armazena o vídeo e as informações associadas no banco de dados.



#### Fluxos Alternativos

Não se aplica.



#### Fluxos de Exceção

**5a. Falha ao armazenar as informações**

5a.1. O sistema identifica um erro ao persistir o vídeo ou seus metadados (quadra, data, horário).
5a.2. O sistema informa a falha e mantém o replay marcado como pendente para uma nova tentativa automática.
5a.3. O caso de uso é encerrado.

---



### UC-04 — Baixar Replay


| Campo                   | Detalhes                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-04                                                                                                     |
| **Nome**                | Baixar Replay                                                                                             |
| **Atores**              | Usuário Autenticado                                                                                       |
| **Requisito Associado** | `RF-06` (Baixar vídeo)                                                                                    |
| **Prioridade**          | Essencial                                                                                                 |
| **Pré-condições**       | Usuário autenticado (UC-02); vídeo desejado ainda dentro do prazo de disponibilidade de 7 dias (`RF-08`). |
| **Pós-condições**       | Vídeo em formato MP4 visualizado ou baixado com sucesso pelo ator.                                        |




#### Fluxo Principal

1. O ator acessa a tela principal após o login.
2. O ator busca e seleciona a cidade desejada.
3. O ator escolhe a quadra correspondente.
4. O ator busca o horário do vídeo desejado.
5. O sistema exibe o vídeo encontrado para visualização ou download.
6. O ator visualiza o vídeo em tela ou realiza o download em MP4.



#### Fluxos Alternativos

**2a. Cidade não cadastrada**

2a.1. O sistema verifica que não há quadras cadastradas para a cidade informada.
2a.2. O sistema exibe a mensagem: *"Nenhuma cidade encontrada"*.
2a.3. O caso de uso retorna ao passo 2.

**3a. Quadra indisponível**

3a.1. O sistema identifica que a quadra selecionada está temporariamente indisponível.
3a.2. O sistema informa a indisponibilidade e sugere outras quadras da mesma cidade.
3a.3. O caso de uso retorna ao passo 3.

**4a. Horário sem gravação**

4a.1. O sistema verifica que não existe vídeo registrado para o horário buscado.
4a.2. O sistema exibe a mensagem: *"Nenhum replay disponível para este horário"*.
4a.3. O caso de uso retorna ao passo 4.



#### Fluxos de Exceção

Não se aplica.

---



### UC-05 — Cadastrar Patrocinador da Arena


| Campo                   | Detalhes                                                                                           |
| ----------------------- | -------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-05                                                                                              |
| **Nome**                | Cadastrar Patrocinador da Arena                                                                    |
| **Atores**              | Cliente (dono da(s) quadra(s))                                                                     |
| **Requisito Associado** | `RF-07` (Cadastrar patrocinadores)                                                                 |
| **Prioridade**          | Importante                                                                                         |
| **Pré-condições**       | Cliente autenticado (UC-02) com perfil de gestor de arena; possuir ao menos uma quadra cadastrada. |
| **Pós-condições**       | Patrocinador cadastrado e vinculado à(s) quadra(s) selecionada(s).                                 |



#### Fluxo Principal

1. O ator acessa a área de patrocinadores da sua conta.
2. O ator inicia o cadastro de um novo patrocinador, informando nome, foto, duração de exibição e valor.
3. O ator seleciona a(s) quadra(s) às quais o patrocinador será vinculado.
4. O ator confirma o cadastro.
5. O sistema valida os dados e associa o patrocinador à(s) quadra(s) selecionada(s).



#### Fluxos Alternativos

Não se aplica.



#### Fluxos de Exceção

**4a. Patrocinador já existente**

4a.1. O sistema identifica que já existe um patrocinador cadastrado com os mesmos dados (nome) para a(s) quadra(s) selecionada(s).
4a.2. O sistema informa que o patrocinador já existe e cancela o novo cadastro.
4a.3. O caso de uso é encerrado.

**4b. Limite de patrocinadores atingido**

4b.1. O sistema verifica que o total de patrocinadores permitidos para a(s) quadra(s) já está preenchido.
4b.2. O sistema informa que o limite foi atingido e impede o cadastro até que uma vaga seja liberada.
4b.3. O caso de uso é encerrado.

---



### UC-06 — Recuperar Senha


| Campo                   | Detalhes                                                                                          |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-06                                                                                             |
| **Nome**                | Recuperar Senha                                                                                   |
| **Atores**              | Usuário                                                                                           |
| **Requisito Associado** | `RF-11` (Recuperar senha)                                                                         |
| **Prioridade**          | Essencial                                                                                         |
| **Pré-condições**       | Usuário cadastrado (UC-01); acesso à tela de login e ao e-mail associado à conta.                 |
| **Pós-condições**       | Senha da conta atualizada; ator redirecionado à tela de login, ainda sem sessão autenticada.      |



#### Fluxo Principal

1. O ator está na tela de login da aplicação.
2. O ator clica no link "Esqueci minha senha".
3. O sistema redireciona o ator para a página de recuperação de senha.
4. O ator informa o e-mail cadastrado e confirma o envio.
5. O sistema verifica se o e-mail informado existe na base de usuários.
6. O sistema envia ao e-mail informado uma mensagem contendo o botão "Redefinir senha".
7. O ator abre o e-mail e clica no botão "Redefinir senha".
8. O sistema exibe a página de redefinição com os campos "Senha" e "Confirmar senha".
9. O ator preenche os campos e clica em "Redefinir".
10. O sistema persiste a nova senha e redireciona o ator para a tela de login.



#### Fluxos Alternativos

Não se aplica.



#### Fluxos de Exceção

**4a. E-mail vazio ou inválido**

4a.1. O ator tenta enviar o formulário com o campo de e-mail em branco ou em formato inválido.
4a.2. O sistema bloqueia o envio e solicita a correção do e-mail.
4a.3. O caso de uso retorna ao passo 4.

**5a. E-mail não cadastrado**

5a.1. O sistema verifica que o e-mail informado não está associado a nenhuma conta.
5a.2. O sistema não envia o e-mail de redefinição.
5a.3. O caso de uso é encerrado.

**8a. Senhas em branco ou não coincidentes**

8a.1. O ator clica em "Redefinir" com um ou ambos os campos em branco, ou com valores diferentes em "Senha" e "Confirmar senha".
8a.2. O sistema bloqueia a redefinição e solicita o preenchimento correto dos campos.
8a.3. O caso de uso retorna ao passo 9.

---



### UC-07 — Cadastrar Gestor de Quadra


| Campo                   | Detalhes                                                                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Identificador**       | UC-07                                                                                                                                    |
| **Nome**                | Cadastrar Gestor de Quadra                                                                                                               |
| **Atores**              | Usuário (solicita o cadastro); Administrador (analisa e decide)                                                                          |
| **Requisito Associado** | `RF-12` (Cadastro de gestor de quadra)                                                                                                   |
| **Prioridade**          | Essencial                                                                                                                                |
| **Pré-condições**       | Usuário cadastrado (UC-01) e autenticado (UC-02); ainda não possui perfil de gestor de quadra nem solicitação pendente de análise.       |
| **Pós-condições**       | Solicitação registrada com status pendente; após análise, perfil de gestor concedido (aprovação) ou mantido apenas o perfil básico (reprovação). |



#### Fluxo Principal

1. O ator acessa a seção de perfil da sua conta.
2. O ator clica no botão "Cadastrar-se como gestor de quadra".
3. O sistema exibe o formulário solicitando CPF, CNPJ, razão social, quantidade de quadras e endereço (rua, bairro, CEP, cidade e UF).
4. O ator preenche todos os campos e confirma o envio.
5. O sistema valida os dados informados.
6. O sistema registra a solicitação com status pendente de análise.
7. O sistema informa ao ator que deve aguardar a análise dos administradores e o contato posterior.
8. O administrador analisa a solicitação.
9. O administrador aprova o cadastro.
10. O sistema atualiza o perfil do ator para gestor de quadra.



#### Fluxos Alternativos

**9a. Administrador reprova a solicitação**

9a.1. O administrador reprova o cadastro de gestor de quadra.
9a.2. O sistema atualiza o status da solicitação para reprovada.
9a.3. O sistema mantém o ator apenas com o perfil básico de usuário.
9a.4. O caso de uso é encerrado.



#### Fluxos de Exceção

**1a. Usuário não autenticado**

1a.1. O sistema identifica que não há sessão autenticada válida.
1a.2. O sistema redireciona o ator para a tela de login (UC-02).
1a.3. O caso de uso é encerrado.

**2a. Usuário já é gestor de quadra**

2a.1. O sistema identifica que o ator já possui o perfil de gestor de quadra.
2a.2. O sistema informa que o cadastro já foi concluído.
2a.3. O caso de uso é encerrado.

**2b. Solicitação já pendente**

2b.1. O sistema identifica que o ator já possui uma solicitação aguardando análise.
2b.2. O sistema informa que a análise ainda está em andamento.
2b.3. O caso de uso é encerrado.

**4a. Campo obrigatório não preenchido**

4a.1. O ator tenta enviar o formulário com algum campo obrigatório em branco.
4a.2. O sistema bloqueia o envio e solicita o preenchimento do(s) campo(s) pendente(s).
4a.3. O caso de uso retorna ao passo 4.

**5a. CPF ou CNPJ inválido ou já associado**

5a.1. O sistema identifica que o CPF e/ou o CNPJ informados são inválidos ou já estão associados a outro gestor.
5a.2. O sistema informa a inconsistência e solicita a correção dos dados.
5a.3. O caso de uso retorna ao passo 4.

---



## 4. Diretrizes de Associação com o Diagrama UML (R-05)

- Todos os atores citados nesta documentação (`Usuário`, `Cliente`, `Administrador`, `Sistema`) devem possuir a representação gráfica equivalente no **Diagrama de Casos de Uso UML** (`/docs/diagrama-casos-de-uso.png`).
- Os relacionamentos de inclusão (`<<include>>`) e extensão (`<<extend>>`) do diagrama UML devem refletir os fluxos principais e alternativos descritos neste documento — por exemplo, UC-03 (Gravar Replay), UC-04 (Baixar Replay) e UC-07 (Cadastrar Gestor de Quadra) devem incluir (`<<include>>`) o UC-02 (Autenticar Usuário), já que dependem de uma sessão autenticada válida. O UC-06 (Recuperar Senha) estende (`<<extend>>`) o UC-02 a partir do fluxo alternativo 3a ("Esqueci minha senha").
