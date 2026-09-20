# Requisitos Não Funcionais

## RNF-01 - Tema escuro e tema claro

O sistema deve permitir que usuários e administradores alternem entre os temas claro e escuro da interface.

**Métrica:** o usuário ou administrador deve conseguir alternar entre os dois temas, e a alteração deve ser aplicada a todas as telas disponíveis do sistema.

---

## RNF-02 - Responsividade

O sistema deve adaptar sua interface aos diferentes dispositivos utilizados para acesso, incluindo dispositivos móveis, tablets e desktops.

**Métrica:** as telas do sistema devem se adaptar corretamente às resoluções de mobile, tablet e desktop, sem perda das funcionalidades principais.

---

## RNF-03 - Tempo de resposta

O sistema deve apresentar respostas rápidas durante a utilização de suas funcionalidades e durante o download dos vídeos.

**Métrica:** as telas devem apresentar resposta em menos de **2 segundos** e o download dos vídeos deve ser concluído em menos de **10 segundos**, considerando condições normais de funcionamento.

---

## RNF-04 - Segurança de acesso

O sistema deve controlar as tentativas de acesso dos usuários e garantir o funcionamento adequado para acessos simultâneos.

**Métrica:** o usuário terá no máximo **5 tentativas de login** antes de ser bloqueado temporariamente. O sistema deve suportar até **20 usuários simultâneos** sem degradação perceptível de desempenho.

---

## RNF-05 - Usabilidade

O sistema deve possuir uma interface intuitiva, permitindo que novos usuários utilizem suas principais funcionalidades sem treinamento prévio.

**Métrica:** pelo menos **80% dos usuários participantes de um teste de usabilidade** devem conseguir realizar as principais tarefas sem auxílio. As mensagens de erro devem ser claras e orientar o usuário sobre como corrigir o problema.