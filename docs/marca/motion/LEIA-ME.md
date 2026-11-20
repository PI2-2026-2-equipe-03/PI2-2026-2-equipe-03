# Motion graphics do repeteco

Feitos em HTML + GSAP e renderizados com [HyperFrames](https://hyperframes.heygen.com) (o mesmo motor da skill `claude-video`). Um relógio só move tudo (`studio.js`), então o mesmo instante sempre gera a mesma imagem.

## Arquivos do projeto (`projeto/`)

| Arquivo | O que é |
|---|---|
| `cena.js` | as 6 cenas, com os tempos e o layout de cada formato (16:9, 9:16, 1:1) |
| `marca.js` | geometria exata do símbolo e da palavra (gerada por `../fonte/brand.py`) |
| `studio.js` | relógio único (da skill claude-video, MIT) |
| `index.html` | manifesto 16:9 · `vertical.html` 9:16 · `quadrado.html` 1:1 |
| `vinheta.html` / `vinheta-quadrada.html` | só a assinatura do logo |
| `_modelo.html` | molde dos HTMLs acima (estilos e fontes) |

## Linha do tempo do manifesto (27 s)

| Tempo | Cena |
|---|---|
| 0,0 – 4,6 s | "Aquele lance **absurdo** na areia…" (quadra vista da lateral: a rede atravessa a quadra para dentro da tela, com o poste da frente maior e o do fundo menor. A bola vem da esquerda, passa por cima da fita e cai na areia do outro lado. Depois o lance esmaece) |
| 4,6 – 9,0 s | "…que ninguém conseguiu **rever?**" (abrir as câmeras, achar o horário, mandar pro cliente, riscados) |
| 9,0 – 13,4 s | "Aperta o **botão.**" (o botão sobe da areia, clique em 10,85 s, selo "lance salvo") |
| 13,4 – 17,4 s | "Os 30 segundos anteriores viram **clipe.**" (a gravação para e os 30 s acendem) |
| 17,4 – 21,6 s | "Direto no seu **celular.**" (o download completa e aparece "clipe salvo no celular") |
| 21,6 – 27,0 s | o "e" se desenha e rebobina, a palavra entra, "Esse lance merece **repeteco.**", e o "e" rebobina de novo |

## Renderizar

Precisa de Node 22+, ffmpeg e internet (GSAP e Google Fonts vêm de CDN).

```bash
cd marca/motion/projeto
npx hyperframes@0.8.181 render . -o ../repeteco-manifesto-16x9.mp4 -q high -c index.html
npx hyperframes@0.8.181 render . -o ../repeteco-manifesto-9x16.mp4 -q high -c vertical.html
npx hyperframes@0.8.181 render . -o ../repeteco-vinheta-16x9.mp4 -q high -c vinheta.html
```

Para conferir quadros antes de renderizar: `npx hyperframes@0.8.181 snapshot . --at 2,7.6,11.2,15.9,20.4,25.5 --no-end -o quadros/`.
Para pré-visualizar no navegador: `npx hyperframes@0.8.181 preview .`.

Os vídeos não têm áudio, para cada um colocar a trilha que preferir. Os pontos fortes para sincronizar com a música: clique do botão (10,85 s), captura dos 30 s (14,75 s), download completo (20,1 s) e entrada da palavra (23,35 s).

## Checagens feitas

Rodadas com os scripts da skill `claude-video`:

- `ritmo.py`: nada parado por mais de 1 s e nada na tela por menos de 0,3 s.
- `pericia-movimento.py --contra` o motion original recuperado: amplitude, tempo em quase-parada e número de picos dentro das metas tiradas do original.

Os "socos" (um clarão suave de 0,6 s) ficam no clique do botão (10,85 s), na captura dos 30 s (14,75 s) e na seta do logo (22,5 s).

## Motions do Teco (`teco/`)

Mesmo motor e mesmo relógio único. O desenho do Teco vem de `../fonte/gerar_teco.py` (arquivo `teco/teco.js`), então ele é idêntico ao das artes estáticas.

| Arquivo | Formato | O que é |
|---|---|---|
| `teco-apresenta-9x16.mp4` | 1080×1920 | "Esse é o Teco", 15 s, para Reels/Stories |
| `teco-apresenta-1x1.mp4` | 1080×1080 | o mesmo para o feed |
| `teco-apresenta-16x9.mp4` | 1920×1080 | o mesmo para YouTube, slides e apresentação |
| `teco-loop-1x1.mp4` / `teco-loop.gif` | 1080 / 540 | 4 s em loop perfeito: o Teco quica, gira para trás e pisca |

Linha do tempo do "Teco apresenta":

| Tempo | Cena |
|---|---|
| 0,0 – 2,6 s | "Esse é o **Teco.**" (cai na areia, amassa, acena e faz joinha) |
| 2,6 – 5,6 s | "Ele vive fazendo lance **absurdo.**" (a rede sobe da areia e ele salta por cima dando cambalhota) |
| 5,6 – 8,0 s | "E odeia quando **ninguém** vê." (olha para os lados e fica triste) |
| 8,0 – 10,6 s | "Então ele aperta o **botão.**" (o botão sobe da areia, clique em 9,42 s) |
| 10,6 – 11,8 s | "**Repeteco!**" (gira para trás dentro do arco de replay, com linhas de fita rebobinando) |
| 11,8 – 13,2 s | "O lance volta pra **você.**" (abraça o celular com o clipe salvo) |
| 13,2 – 15,0 s | logo + "Esse lance merece **repeteco.**" (ele gira para trás de novo e pisca) |

```bash
cd marca/motion/teco
python3 montar.py   # gera index.html (9:16), apresenta-quadrado.html, apresenta-16x9.html e loop.html
npx hyperframes@0.8.181 render . -o ../teco-apresenta-9x16.mp4 -q high -c index.html
npx hyperframes@0.8.181 render . -o ../teco-apresenta-1x1.mp4 -q high -c apresenta-quadrado.html
npx hyperframes@0.8.181 render . -o ../teco-apresenta-16x9.mp4 -q high -c apresenta-16x9.html
npx hyperframes@0.8.181 render . -o ../teco-loop-1x1.mp4 -q high -c loop.html
```
