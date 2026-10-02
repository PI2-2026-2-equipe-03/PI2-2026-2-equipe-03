# Guia de Padrões Visuais e Design System — Plataforma "Tá Gravado"

## 1. Identificação e Rastreabilidade
* **Projeto:** Plataforma de Captura e Gestão de Replays Esportivos "Tá Gravado"
* **Documento:** Guia de Padrões Visuais (Design System & UI Components - Versão 2)
* **Responsável:** Integrante 3 — Frontend / UI & Design System
* **Caminho no Repositório:** `/docs/padroes-visuais.md`
* **Requisitos Associados:** `RNF-01` (Tema Claro e Escuro), `RNF-02` (Responsividade Cross-Device), `RNF-03` (Tempo de Resposta), `RF-01` a `RF-10`

---

## 2. Identidade Visual e Paleta de Cores (RNF-01)

A paleta de cores do **"Tá Gravado"** reflete a energia das quadras esportivas com alto contraste para visibilidade sob luz solar (em smartphones na quadra) e conforto visual no modo noturno.

### 2.1 Cores da Marca e Ação (Brand & Sport Colors)
| Função | Nome da Cor | Hex (Light) | Hex (Dark) | Uso Principal no "Tá Gravado" |
| :--- | :--- | :---: | :---: | :--- |
| **Primária / Ação** | Verde Replay / Neon | `#10B981` | `#059669` | Botão principal "Corta Replay!", destaques de jogada e status ativo. |
| **Primária Hover** | Verde Gramado Escuro | `#059669` | `#047857` | Estado hover/pressed de ações primárias. |
| **Secundária** | Azul Arena Esportiva | `#2563EB` | `#3B82F6` | Seleção de cidades, filtro de quadras e botões de navegação. |
| **Destaque / Badge** | Amarelo Troféu | `#F59E0B` | `#D97706` | Badges de tempo (30s), área de patrocinadores e marcador "Novo". |

### 2.2 Cores Neutras e de Superfície
| Função | Nome da Cor | Hex (Light) | Hex (Dark) | Uso Principal |
| :--- | :--- | :---: | :---: | :--- |
| **Fundo Principal** | Background | `#F8FAFC` | `#0F172A` | Tela de fundo do app e galeria de vídeos. |
| **Superfície / Card** | Surface | `#FFFFFF` | `#1E293B` | Cards de replays, modais, formulários de login e navbar. |
| **Bordas / Divisores** | Border | `#E2E8F0` | `#334155` | Linhas de separação e contornos dos cards de vídeo. |
| **Texto Principal** | Text Primary | `#0F172A` | `#F8FAFC` | Títulos das quadras, horários e nomes dos atletas. |
| **Texto Secundário** | Text Secondary | `#64748B` | `#94A3B8` | Subtítulos, localização (Cidade/Quadra) e metadados. |

### 2.3 Cores de Feedback e Estado
| Estado | Hex (Light) | Hex (Dark) | Aplicação no Sistema |
| :--- | :---: | :---: | :--- |
| **Sucesso (Success)** | `#16A34A` | `#22C55E` | Confirmação de gravação do lance, download concluído (`RF-06`). |
| **Erro (Danger)** | `#DC2626` | `#EF4444` | Falha de autenticação (`RF-02`), erro de câmera ou exclusão manual (`RF-10`). |
| **Aviso (Warning)** | `#D97706` | `#F59E0B` | Alertas de expiração automática em 7 dias (`RN-01` / `RF-08`). |
| **Informação (Info)** | `#0284C7` | `#38BDF8` | Status de processamento do buffer de vídeo de 30s. |

---

## 3. Tipografia e Escala Visual

A tipografia oficial do **"Tá Gravado"** é a **Inter** (com fallback `system-ui, -apple-system, sans-serif`), garantindo leitura rápida em dispositivos móveis (`RNF-02`).

### 3.1 Escala Tipográfica
| Nível | Tamanho (px / rem) | Peso | Espaçamento (Line-Height) | Uso no "Tá Gravado" |
| :--- | :---: | :---: | :---: | :--- |
| **Heading 1 (H1)** | 32px / 2.0rem | Bold (700) | 1.2 (38.4px) | Títulos das páginas principais ("Galeria de Replays", "Dashboard Arena"). |
| **Heading 2 (H2)** | 24px / 1.5rem | SemiBold (600) | 1.3 (31.2px) | Nomes das Quadras/Arenas e Títulos de Modais. |
| **Heading 3 (H3)** | 18px / 1.125rem | SemiBold (600) | 1.4 (25.2px) | Títulos de Cards de Vídeo e Seções de Filtro. |
| **Body (Padrão)** | 16px / 1.0rem | Regular (400) | 1.5 (24px) | Textos de instrução, formulários de cadastro e login. |
| **Body Small** | 14px / 0.875rem | Regular (400) | 1.4 (19.6px) | Horário da jogada, cidade, nome do atleta e mensagens de alerta. |
| **Caption / Tag** | 12px / 0.75rem | Medium (500) | 1.3 (15.6px) | Badges "30s", marca d'água de patrocinador e contador de dias restantes. |

---

## 4. Componentes de Botões e Interação

Todos os botões possuem altura mínima de **44px** e área de toque expandida, conforme exigências de acessibilidade em telas touch (`RNF-02`).

### 4.1 Variantes de Botão
1. **Botão "Corta Replay!" (Botão de Ação Principal / Action Hero):**
   * **Uso:** Acionamento imediato da gravação do lance dos últimos 30 segundos (`RF-05`).
   * **Estilo:** Fundo Verde Neon `#10B981`, Texto Branco `#FFFFFF` em caixa alta, Ícone de Câmera/Raios, Border-Radius `12px`, Efeito Pulse sutil.
2. **Botão Primário (Primary Button):**
   * **Uso:** Formulários de Login, Cadastro e Download de Vídeo MP4 (`RF-01`, `RF-02`, `RF-06`).
   * **Estilo:** Fundo Verde `#10B981`, Texto Branco `#FFFFFF`, Border-Radius `8px`, Font-Weight `600`.
3. **Botão Secundário (Secondary Button):**
   * **Uso:** Filtros por Cidade, Quadra e Horário (`RF-06`).
   * **Estilo:** Fundo Transparente com Borda `#2563EB`, Texto Azul `#2563EB`, Border-Radius `8px`.
4. **Botão Destrutivo (Danger Button):**
   * **Uso:** Exclusão manual de vídeos pelo proprietário da quadra (`RF-10`).
   * **Estilo:** Fundo Vermelho `#DC2626`, Texto Branco `#FFFFFF`, Border-Radius `8px`.

### 4.2 Estados Interativos
* **Default:** Apresentação padrão do componente.
* **Hover / Touch:** Redução de 10% no brilho do fundo e cursor `pointer`.
* **Focus:** Contorno (outline) de `2px` na cor secundária com offset de `2px`.
* **Active / Press:** Escala reduzida (`transform: scale(0.97)`) simulando o clique do botão físico da quadra.
* **Disabled:** Fundo `#E2E8F0` / `#334155`, texto `#94A3B8`, cursor `not-allowed`.
* **Loading:** Exibição de spinner circular central com desativação de cliques duplos.

---

## 5. Anatomia do Card de Replay e Player de Vídeo

### 5.1 Card de Vídeo (Galeria de Replays)
Cada card na galeria representa um vídeo gravado e contém:
* **Thumbnail (Miniatura):** Frame inicial do vídeo de 30 segundos.
* **Badge Superior Esquerdo:** Duração fixa `"00:30"` em fundo escuro semi-transparente.
* **Badge Superior Direito:** Tag de patrocinador ativo vinculada à quadra (`RN-05` / `RF-07`).
* **Corpo do Card:**
  * **Título/Horário:** Ex: `"Lance das 19:30 - Quadra 1"`.
  * **Metadados:** Ícone de localização + `"Crateús • Arena Central"`.
  * **Indicador de Expiração:** Ex: `"Expira em 5 dias"` (`RN-01` / `RF-08`).
* **Ações:** Botão "Assistir" e Botão "Baixar MP4" (`RF-06`).

---

## 6. Mensagens de Feedback, Alertas e Modais

### 6.1 Notificações Toast / Banners
* **Sucesso:** `"Replay de 30s capturado com sucesso! Disponível na galeria."` (`RF-05`).
* **Erro de Login:** `"E-mail ou senha incorretos. Tentativa 3 de 5."` (`RN-03`).
* **Alerta de Expiração:** `"Atenção: Este vídeo será excluído automaticamente amanhã."` (`RN-01`).

### 6.2 Modais de Confirmação
* **Modal de Exclusão de Vídeo (`RF-10`):**
  * **Título:** "Excluir Replay Definitivamente?"
  * **Mensagem:** "Tem certeza que deseja remover o vídeo gravado em 24/09 às 19:30 na Quadra 1?"
  * **Ações:** Botão Destrutivo ("Excluir Vídeo") + Botão Secundário ("Cancelar").

---

## 7. Indicadores de Carregamento e Desempenho (RNF-03)

### 7.1 Skeleton Screens (Carregamento de Galeria)
* Blocos retangulares com iluminação pulsante (`#E2E8F0` Light / `#334155` Dark) simulando a grade de cards de vídeo enquanto as requisições da API retornam dados em menos de 2 segundos (`RNF-03`).

### 7.2 Barra de Progresso de Download MP4
* Exibida durante o download de vídeos, garantindo acompanhamento do progresso de 0% a 100% com indicador numérico.

---

## 8. Grade Layout e Responsividade (RNF-02)

* **Mobile (Smartphones < 640px):** Layout de 1 coluna, botões de ação com 100% de largura, navegação simplificada.
* **Tablet (640px a 1024px):** Grade de 2 colunas para os cards de vídeo.
* **Desktop (> 1024px):** Grade de 3 a 4 colunas para galeria, barra lateral de filtros e dashboards de métricas.

---

## 9. Arquitetura de Estilos no Docker (CSS / Tailwind)

Para alinhamento com a infraestrutura em contêineres Docker (Frontend 1 e 2):
* As variáveis do Design System ficam concentradas no arquivo `src/styles/theme.css` ou no `tailwind.config.js`.
* O modo de tema é alternado dinamicamente através do atributo `<html data-theme="dark">`.
