

**Matriz de Backlog de continuidade**

| ID | Título | Categoria  | Prioridade |
| :---- | :---- | :---- | :---- |
| BC-01 | Módulo de Agendamento de Quadras | Escopo Adiado | Must |
| BC-02 | Autenticação em dois fatores (2FA) via e-mail para administradores  | Melhoria Evolutiva | Should |
| BC-03 | Falta de padronização backend  | Débitos técnicos | Should |
| BC-04 | Exportação de relatórios gerenciais em formato XLSX  | Melhoria Evolutiva | Could |

**Detalhamento Técnico**

#### **BC-01** \- Módulo de Agendamento de Quadras

O cliente necessita de um módulo inteiro no sistema para gerenciar agendamentos de quadras em sua arena pelos usuários. Devido ao curto prazo e a complexidade do desenvolvimento não foi conseguido implementá-ló

#### **BC-02** \- Autenticação em dois fatores (2FA) via e-mail para administradores

Para melhor segurança do sistema, deverá ser implementado uma medida de verificação de dois fatores (e-mail e telefone) para a solicitação de gestor de quadra

**BC-03** \- Falta de padronização backend 

O sistema deverá ser refatorar cada rota para com todas terem o mesmo padrão para melhor manutenção e leitura de novos desenvolvedores no sistema

#### **BC-04** \- Exportação de relatórios gerenciais em formato XLSX

O cliente que desejar poderá exportar planilhas de suas métrica para fins de relatório e documentação

**Critérios de Classificação  e Escala de Prioridade (MoSCoW):**

1. **Classificação:** 

**Funcionalidades adiadas (Escopo remanescente):** Requisitos que faziam parte da visão do produto, mas foram cortados ou postergados para garantir o cumprimento do prazo ou orçamento da versão atual.  
**Melhorias evolutivas:** Novas necessidades ou otimizações de usabilidade sugeridas pelos usuários e *stakeholders* durante as fases de validação e homologação.  
**Débitos técnicos:** Refatorações de código, melhorias de arquitetura, atualização de dependências ou ajustes de performance que a equipe decidiu adiar conscientemente para priorizar entregas de negócio.  
**Defeitos conhecidos de baixa severidade:** Falhas cosméticas ou *bugs* menores que não impedem o uso do sistema nem violam regras de negócio críticas, mas que precisam ser corrigidos futuramente.  
**Demandas de infraestrutura e segurança:** Ajustes de escalabilidade, automação de *deploy* (CI/CD), monitoramento ou conformidade regulatória previstos para o médio prazo.

2. **MoSCow**

 **Must** \- Obrigatório no próximo ciclo  
 **Should** \- Importante, mas não urgente  
 **Could** \- Desejável se houver capacidade 