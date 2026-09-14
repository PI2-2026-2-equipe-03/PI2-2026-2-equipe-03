# Plano de Projeto - **TaGravado**

## 1. Introdução e Contexto do Cliente
1.1 **Cliente/Parceiro na Comunidade:** Rennan - Arena Dunnas Beach

1.2 **Problema Identificado:** Nas quadras de esportes de areia, algo muito requisitado é a presença de sistemas de replays nas câmeras de segurança, para que os jogadores possam resgatar os _highlights_ de suas partidas.

1.3 **Solução Proposta:** 
  * Na primeira parte do projeto: Será desenvolvido um software em formato Web que destaque esses momentos mais interessantes das partidas e tal momento ficará disponível para que as pessoas baixem no site. De forma intuitiva e de fácil acesso. Faremos ainda a instalação da botoeira, fiação e microcontroladores necessários.
  * Na segunda parte do projeto: Adicionaremos o módulo de **Reserva de Horários**, onde os clientes da arena poderão acessar quais os horários estão disponíveis no momento e a partir dessa mesma tela, reservar o seu horário desejado.

## 2. Objetivos
* **Objetivo Geral:** Desenvolver uma aplicação conteinerizada que solucione o problema de falta de um sistema de replays e de reserva de horários, aplicando os conhecimentos integrados do curso.
* **Objetivos Específicos:**
  * Realizar o levantamento completo de requisitos funcionais e não funcionais na Sprint 1.
  * Modelar e implementar o banco de dados relacional que apoie as operações do cliente.
  * Projetar uma interface intuitiva e prototipada de alta fidelidade no Figma.
  * Garantir o deploy simplificado da aplicação via ambiente Docker.

## 3. Divisão de Papéis (Equipe)
* **Analistas de Requisitos e Design:**
  * Kauan
  * Laryssa
* **Desenvolvedores Backend e Infraestrutura:**
  * Pedro
  * Lucas
  * Pablo
* **Desenvolvedores Frontend:**
  * Alan
  * Kaik
* **QA / Testes:**
  * Rick

## 4. Extensão e Impacto Social
1. **Beneficiários Diretos:** Quadras de esportes de areia e os seus clientes serão os beneficiários diretos
2. **Impacto na Prática:** Atualmente eles tem que abrir os arquivos da camera, procurar a hora em que o clipe foi feito e após isso mandar para o cliente. Após isso, com o toque de um botão todo esse fluxo será feito de maneira automática e disponibilizado no site.
3. **Desafios de Implantação:** Instalação dos microcontroladores e botões, possível fluxo não intuitivo para os usuarios.
4. **Continuidade:** Será estudada como o projeto será mantido após o término do semestre.

## 5. Acordo de Trabalho da Equipe (Governança Git)
* Nenhuma alteração será enviada diretamente para as branches principais (`main`/`master`) sem um Pull Request (PR).
* Todo PR aberto exige a revisão de pelo menos um colega da equipe antes de ser integrado.
* Toda tarefa realizada deve nascer como uma Issue antes do início do trabalho, possuir um único responsável, estar vinculada à milestone da Sprint vigente e conter a label correspondente de rastreabilidade (ex: `EC-04` ou `RF-01`).
* Tarefas que não estiverem em conformidade com as regras do manual de rastreabilidade do professor Bruno Riccelli serão canceladas ou reestruturadas para garantir a pontuação quinzenal de todos.
