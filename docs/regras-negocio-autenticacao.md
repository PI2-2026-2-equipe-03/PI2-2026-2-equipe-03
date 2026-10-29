## **Regras de Negócio \- Autenticação**

### **Introdução**

Para garantir a integridade e a disponibilidade do projeto, o sistema **Repeteco** adota uma política de proteção à autenticação de usuários. O objetivo é evitar que um volume massivo de requisições sobrecarregue o servidor e o deixe fora do ar.

### **Desenvolvimento**

Como medida de prevenção contra ataques DDoS (*Distributed Denial of Service*, ou ataque de negação de serviço distribuído), SYN Flood e HTTP Flood, o sistema **Repeteco** mantém um contador das tentativas de requisição por e-mail ou endereço IP. Ao atingir 5 tentativas, o sistema passa para o estado de bloqueado. Por meio da API Better Auth, o bloqueio dura 30 minutos e, depois desse período, o estado normal é restabelecido. Qualquer tentativa feita durante o bloqueio retorna o erro HTTP 429 (*Too Many Requests*). Além disso, após 30 minutos de inatividade, o sistema executa o logout automático.

### **Requisitos Vinculados**

RF-02, RNF-04 e RN-06.

