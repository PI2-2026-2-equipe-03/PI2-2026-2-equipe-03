from caminhos import *  # noqa
"""Artes do Teco detalhado: ficha do personagem, cenas (pôsteres 4:5), carrossel "como funciona",
stories e posts de frase. Saída em marca/teco/ e marca/social/."""
import os, math, json
import brand as B
import teco_pro as T
from teco import rede_lateral

INK = B.BLUE_DEEP
TECO = MARCA + '/teco'
SOC = MARCA + '/social'
for d in (TECO + '/cenas', TECO + '/ficha', SOC + '/carrossel-como-funciona', SOC + '/stories', SOC + '/frases'):
    os.makedirs(d, exist_ok=True)


def Tx(s, size, x, y, col, w='xb', track=-0.025, align='left'):
    return B.P(B.text(s, size, x, y, w=w, track=track, align=align)[0], col)


def largura(s, size, w='xb', track=-0.025):
    return B.text(s, size, 0, 0, w=w, track=track)[1]


def linha(partes, size, x, y, align='left'):
    """partes: [(texto, cor), ...] numa linha só (uma palavra em amarelo por frase)."""
    esp = largura('a a', size) - largura('aa', size)
    total = sum(largura(t, size) for t, _ in partes) + esp * (len(partes) - 1)
    cx = x - total / 2 if align == 'center' else x
    g = ''
    for t, c in partes:
        g += Tx(t, size, cx, y, c); cx += largura(t, size) + esp
    return g


def logo(x, y, size, ecol=B.YEL, wcol='#fff'):
    """logo sem caixa; x = borda esquerda do e, y = linha de base."""
    s = size / 350 * 1.25; cx = x + 104 * s; cy = y - 92 * size / 350
    wm, _ = B.wordmark(cx + 104 * s + 95 * size / 350 - 12.6 * size / 350, y, size, wcol)
    return B.e_mark(ecol, cx, cy, s) + wm


def areia(W, H, top, amp=26):
    return B.sand(W, H, top, amp)


def save(path, w, h, body, titulo):
    open(path, 'w').write(B.svg(w, h, body, title=titulo))


# ---------------- peças de cenário ----------------
def botao_quadra(cx, top, chao, s=1.0):
    """Botão físico da quadra num poste, visto de lado: caixa branca com o botão amarelo em cima."""
    bw, bh = 200 * s, 120 * s
    x, y = cx - bw / 2, top
    g = f'<rect x="{cx-16*s}" y="{y+bh-10}" width="{32*s}" height="{chao-(y+bh)+40}" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="7"/>'
    g += f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="{30*s}" fill="#fff" stroke="{INK}" stroke-width="7"/>'
    g += f'<rect x="{x+22*s}" y="{y+bh*0.55}" width="{bw-44*s}" height="{14*s}" rx="{7*s}" fill="{B.LILAC}"/>'
    g += Tx('repeteco', 22 * s, cx, y + bh * 0.4, B.BLUE, align='center')
    rx, ry, hh = 64 * s, 18 * s, 26 * s
    g += (f'<path d="M{cx-rx},{y} v{-hh} a{rx},{ry} 0 0 0 {2*rx},0 v{hh} a{rx},{ry} 0 0 1 {-2*rx},0Z" fill="{B.YEL_DK}" stroke="{INK}" stroke-width="7" stroke-linejoin="round"/>'
          f'<ellipse cx="{cx}" cy="{y-hh}" rx="{rx}" ry="{ry}" fill="{B.YEL}" stroke="{INK}" stroke-width="7"/>'
          f'<ellipse cx="{cx-20*s}" cy="{y-hh-5*s}" rx="{18*s}" ry="{5*s}" fill="#fff" opacity=".6"/>')
    return g


def ondas_clique(cx, cy, s=1.0):
    g = ''
    for i, r in enumerate((95, 140)):
        g += f'<ellipse cx="{cx}" cy="{cy}" rx="{r*s}" ry="{r*0.32*s}" fill="none" stroke="{B.YEL}" stroke-width="{9-i*3}" opacity="{0.9-i*0.35}"/>'
    for a in (-150, -120, -60, -30):
        ar = math.radians(a)
        g += f'<path d="M{cx+math.cos(ar)*120*s:.0f},{cy+math.sin(ar)*90*s:.0f} l{math.cos(ar)*44*s:.0f},{math.sin(ar)*44*s:.0f}" stroke="{B.YEL}" stroke-width="12" stroke-linecap="round"/>'
    return g


def celular(cx, cy, w, h, rot=0, conteudo=True):
    x, y = cx - w / 2, cy - h / 2
    g = f'<g transform="rotate({rot} {cx} {cy})">'
    g += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w*0.15}" fill="{INK}"/>'
    p = w * 0.055
    g += f'<rect x="{x+p}" y="{y+p}" width="{w-2*p}" height="{h-2*p}" rx="{w*0.11}" fill="{B.ICE}"/>'
    g += f'<rect x="{cx-w*0.14}" y="{y+p+10}" width="{w*0.28}" height="{w*0.06}" rx="{w*0.03}" fill="{INK}"/>'
    if conteudo:
        vx, vy, vw, vh = x + p + 22, y + p + 70, w - 2 * p - 44, (w - 2 * p - 44) * 0.62
        cid = f'tela{int(cx)}{int(cy)}'
        g += f'<clipPath id="{cid}"><rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" rx="22"/></clipPath>'
        g += f'<g clip-path="url(#{cid})"><rect x="{vx}" y="{vy}" width="{vw}" height="{vh}" fill="{B.BLUE}"/>'
        g += B.P(B.wave_path(vw, vh, vh * 0.72, vh * 0.05, 0.2, 0.7), B.YEL).replace('d="M', f'transform="translate({vx},{vy})" d="M')
        g += rede_lateral(vx + vw * 0.42, vy + vh * 0.86, vx + vw * 0.5, vy + vh * 0.78, vh * 0.6, vh * 0.44, sw=0.9)
        g += f'<path d="M{vx+vw*0.12},{vy+vh*0.6} Q{vx+vw*0.45},{vy+vh*0.02} {vx+vw*0.74},{vy+vh*0.3}" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="3 12" stroke-linecap="round"/>'
        g += T.teco(vx + vw * 0.78, vy + vh * 0.32, vh * 0.15, 'empolgado', faixa=True)
        g += '</g>'
        g += f'<circle cx="{vx+vw/2}" cy="{vy+vh/2}" r="{vh*0.17}" fill="#fff" opacity=".9"/><path d="M{vx+vw/2-vh*0.05},{vy+vh/2-vh*0.08} v{vh*0.16} l{vh*0.13},{-vh*0.08}z" fill="{B.BLUE}"/>'
        by = vy + vh + 26
        g += f'<rect x="{vx}" y="{by}" width="{vw}" height="10" rx="5" fill="{B.LILAC}"/><rect x="{vx}" y="{by}" width="{vw*0.62}" height="10" rx="5" fill="{B.YEL}"/>'
        g += Tx('Meu replay', w * 0.085, vx, by + 74, B.BLUE)
        g += Tx('Quadra 2 · 30 s', w * 0.055, vx, by + 118, '#6B7A9C', w='md', track=0)
        cy2 = by + 190
        g += f'<rect x="{vx}" y="{cy2}" width="{vw}" height="{w*0.17}" rx="{w*0.085}" fill="{B.YEL}"/>'
        g += f'<circle cx="{vx+w*0.085}" cy="{cy2+w*0.085}" r="{w*0.055}" fill="{INK}"/>'
        g += f'<path d="M{vx+w*0.06},{cy2+w*0.087} l{w*0.02},{w*0.022} l{w*0.035},{-w*0.04}" fill="none" stroke="{B.YEL}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        g += Tx('clipe salvo', w * 0.07, vx + w * 0.17, cy2 + w * 0.11, INK)
    return g + '</g>'


def tira_de_frames(x, y, n, fw, fh, acesos):
    g = ''
    for i in range(n):
        fx = x + i * (fw + 16)
        on = i >= n - acesos
        g += f'<rect x="{fx}" y="{y}" width="{fw}" height="{fh}" rx="16" fill="{B.YEL if on else "#fff"}" stroke="{INK}" stroke-width="6"/>'
        g += f'<rect x="{fx+12}" y="{y+12}" width="{fw-24}" height="{fh-24}" rx="9" fill="{B.BLUE if on else B.LILAC}"/>'
        g += f'<rect x="{fx+12}" y="{y+fh*0.62}" width="{fw-24}" height="{fh*0.38-12}" rx="0" fill="{B.YEL_DK if on else "#fff"}" opacity="{1 if on else .55}"/>'
    return g


def sol(cx, cy, r):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*1.35}" fill="{B.YEL}" opacity=".12"/><circle cx="{cx}" cy="{cy}" r="{r*1.15}" fill="{B.YEL}" opacity=".18"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{B.YEL}"/>')


# ---------------- composições reaproveitadas ----------------
def comp_botao(ox=0, oy=0, s=1.0):
    g = f'<g transform="translate({ox},{oy}) scale({s})">'
    g += botao_quadra(800, 830, 1190, 1.25) + ondas_clique(800, 788, 1.15)
    g += T.teco(480, 960, 180, 'focado', sombra=1140,
                maos=[('aponta', 136, -142, 142, 1.3, False), ('punho', -128, 30, -10, 1.2, True)])
    g += f'<g transform="rotate(-10 880 610)">' + Tx('clique!', 86, 880, 610, B.YEL, align='center') + '</g>'
    return g + '</g>'


def comp_lance(ox=0, oy=0, s=1.0):
    g = f'<g transform="translate({ox},{oy}) scale({s})">'
    g += rede_lateral(470, 1196, 610, 1150, 440, 300, sw=2.6)
    g += f'<path d="M150,1120 Q300,520 560,620" fill="none" stroke="#fff" stroke-width="9" stroke-dasharray="4 26" stroke-linecap="round" opacity=".85"/>'
    for i, (gx, gy, a) in enumerate([(250, 850, .16), (330, 710, .26), (430, 640, .38)]):
        g += f'<circle cx="{gx}" cy="{gy}" r="{70+i*14}" fill="#fff" opacity="{a}"/>'
    g += T.linhas_vel(500, 580, 3, 120, 34, -20)
    g += T.teco(650, 610, 135, 'empolgado', rot=18,
                maos=[('aberta', -112, -78, -35, 1.2, True), ('aberta', 112, -84, 35, 1.2, False)])
    for x, y, r in [(170, 1140, 20), (130, 1120, 14), (210, 1128, 12)]:
        g += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{B.YEL}" stroke="{INK}" stroke-width="4"/>'
    return g + '</g>'


def comp_celular(ox=0, oy=0, s=1.0):
    g = f'<g transform="translate({ox},{oy}) scale({s})">'
    g += celular(700, 820, 360, 700, rot=8)
    g += T.teco(330, 990, 170, 'apaixonado', sombra=1150,
                maos=[('punho', 122, -150, 98, 1.25, False), ('punho', 126, -50, 92, 1.25, False)])
    g += T.brilho(930, 420, 1.3) + T.brilho(240, 700, 0.9, '#fff')
    return g + '</g>'


def comp_rebobina(cx=540, cy=800, s=1.0):
    g = f'<g transform="translate({cx},{cy}) scale({s})">'
    # rastro: linhas de velocidade acompanhando o giro (para trás)
    for i, r in enumerate((250, 340)):
        a0, a1 = math.radians(150 - i * 10), math.radians(215 - i * 10)
        g += f'<path d="M{r*math.cos(a0):.0f},{r*math.sin(a0):.0f} A{r},{r} 0 0 1 {r*math.cos(a1):.0f},{r*math.sin(a1):.0f}" fill="none" stroke="#fff" stroke-width="10" stroke-linecap="round" opacity=".55"/>'
    g += T.rebobina(0, 0, 300, ang0=-20, arco=290, w=46)
    g += T.teco(0, 0, 210, 'orgulhoso', rot=-35,
                maos=[('aberta', -118, -70, -40, 1.25, True), ('aberta', 118, -70, 40, 1.25, False)])
    return g + '</g>'


# ---------------- pôsteres 4:5 ----------------
W, H = 1080, 1350


def poster(nome, linhas, sub, cena, fundo=None, sand=1170):
    b = fundo if fundo is not None else T.raios(540, 860, 20)
    b += areia(W, H, sand, 26)
    b += cena
    b += logo(80, 120, 50)
    y = 270
    for ln in linhas:
        b += linha(ln, 92, 80, y); y += 96
    if sub:
        for s in sub:
            b += Tx(s, 38, 82, y + 10, B.LILAC, w='md', track=-0.005); y += 48
    save(f'{TECO}/cenas/{nome}.svg', W, H, b, nome)


FUNDO_SOL = (T.raios(540, 860, 20) + sol(880, 330, 90))

poster('conheca-o-teco', [[('Conheça o', '#fff')], [('Teco.', B.YEL)]],
       ['A bola mais empolgada da areia.', 'Não deixa nenhum lance passar.'],
       ''.join(T.confete(x, y, r, c) for x, y, r, c in [(150, 640, 20, B.YEL), (930, 620, -30, '#fff'), (880, 760, 40, B.LILAC), (180, 820, -10, '#fff'), (960, 900, 25, B.YEL)])
       + T.brilho(170, 560, 1.3) + T.brilho(930, 520, 0.9, '#fff')
       + T.teco(540, 880, 240, 'empolgado', sombra=1135,
                maos=[('aberta', -132, 4, -22, 1.25, True), ('joinha', 130, 30, 10, 1.25, False)]))

poster('teco-aperta-o-botao', [[('Fez o ponto?', '#fff')], [('Aperta o', '#fff'), ('botão.', B.YEL)]], None, comp_botao(0, 40))

poster('teco-replay-no-celular', [[('O lance chega', '#fff')], [('no seu', '#fff'), ('celular.', B.YEL)]], None, comp_celular(0, 40))

poster('teco-rebobina', [[('Rebobina que', '#fff')], [('esse foi', '#fff'), ('lindo.', B.YEL)]], None, comp_rebobina(540, 830),
       fundo=T.raios(540, 830, 24, rot=4))

poster('teco-lance-absurdo', [[('Lance absurdo?', '#fff')], [('Tem', '#fff'), ('repeteco.', B.YEL)]], None, comp_lance(0, 60),
       fundo=FUNDO_SOL)

# ---------------- carrossel "como funciona" (6 slides 4:5) ----------------
def slide(i, linhas, cena, sub=None):
    b = f'<rect width="{W}" height="{H}" fill="{B.BLUE}"/>'
    b += f'<circle cx="540" cy="880" r="430" fill="#1646B4"/>'
    b += areia(W, H, 1180, 24) + cena
    b += logo(80, 118, 46)
    b += Tx(f'{i}/6', 34, 1000, 112, B.LILAC, w='md', track=0, align='right')
    y = 270
    if 1 < i < 6:
        b += f'<circle cx="122" cy="{y-32}" r="42" fill="{B.YEL}"/>' + Tx(str(i - 1), 56, 122, y - 12, INK, align='center')
        x0 = 186
    else:
        x0 = 80
    for ln in linhas:
        b += linha(ln, 84, x0, y); y += 90
    for s in (sub or []):
        b += Tx(s, 38, x0 + 2, y + 6, B.LILAC, w='md', track=-0.005); y += 48
    # bolinhas de progresso
    for k in range(6):
        b += f'<circle cx="{540-75+k*30}" cy="1300" r="{9 if k == i-1 else 6}" fill="{INK if k == i-1 else B.BLUE_DK}" opacity="{1 if k == i-1 else .45}"/>'
    save(f'{SOC}/carrossel-como-funciona/{i:02d}.svg', W, H, b, f'como funciona {i}')


slide(1, [[('Como funciona', '#fff')], [('o', '#fff'), ('repeteco', B.YEL)]],
      T.teco(520, 890, 230, 'piscando', sombra=1140, maos=[('aponta', 140, -10, 90, 1.3, False), ('punho', -128, 50, 0, 1.2, True)])
      + T.linhas_vel(1010, 860, 3, 80, 30, 180, B.YEL, 12) + T.brilho(200, 560, 1.1),
      ['Arrasta pro lado →'])
slide(2, [[('Rolou aquele', '#fff')], [('lance', '#fff'), ('absurdo.', B.YEL)]], comp_lance(60, 120, 0.9))
slide(3, [[('Aperta o', '#fff'), ('botão', B.YEL)], [('da quadra.', '#fff')]], comp_botao(30, 110, 0.94))
strip = (tira_de_frames(70, 640, 8, 106, 150, 4)
         + f'<path d="M548,610 v-30 h462 v30" fill="none" stroke="{B.YEL}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
         + Tx('30 s', 64, 779, 560, B.YEL, align='center')
         + f'<path d="M1006,600 V820" stroke="#fff" stroke-width="8" stroke-linecap="round"/><circle cx="1006" cy="598" r="14" fill="#fff"/>'
         + Tx('agora', 32, 1006, 870, '#fff', w='bd', track=0, align='center')
         + T.teco(380, 1010, 150, 'olha-dir', sombra=1150, maos=[('aponta', 130, -60, 50, 1.2, False), ('punho', -120, 30, 0, 1.15, True)]))
slide(4, [[('Os 30 segundos', '#fff')], [('anteriores viram', '#fff')], [('clipe.', B.YEL)]], strip)
slide(5, [[('Baixa no', '#fff'), ('celular', B.YEL)], [('e compartilha.', '#fff')]], comp_celular(40, 110, 0.92))
fim = (f'<g transform="translate(540,800) rotate(-6)">{B.tile(-150,-150,300,B.YEL,B.BLUE)}<rect x="-150" y="-150" width="300" height="300" rx="82" fill="none" stroke="{INK}" stroke-width="8"/></g>'
       + T.teco(800, 1010, 140, 'orgulhoso', sombra=1150, maos=[('joinha', -120, 20, -10, 1.2, True), ('aberta', 118, -40, 30, 1.15, False)])
       + T.brilho(300, 620, 1.2) + T.brilho(860, 600, 0.8, '#fff'))
slide(6, [[('Esse lance merece', '#fff')], [('repeteco.', B.YEL)]], fim, ['Procure o botão na sua arena.'])

# ---------------- stories 9:16 ----------------
SW_, SH_ = 1080, 1920


def story(nome, linhas, sub, cena, fundo):
    b = fundo + areia(SW_, SH_, 1700, 34) + cena + logo(80, 170, 56)
    y = 400
    for ln in linhas:
        b += linha(ln, 112, 80, y); y += 116
    for s in sub:
        b += Tx(s, 44, 84, y + 14, B.LILAC, w='md', track=-0.005); y += 56
    save(f'{SOC}/stories/{nome}.svg', SW_, SH_, b, nome)


story('story-conheca-o-teco', [[('Esse é o', '#fff')], [('Teco.', B.YEL)]], ['Ele não perde um lance.', 'E agora você também não.'],
      T.teco(540, 1260, 300, 'empolgado', sombra=1600, maos=[('aberta', -132, 0, -22, 1.25, True), ('joinha', 130, 30, 10, 1.25, False)])
      + T.brilho(170, 860, 1.4) + T.brilho(930, 900, 1.0, '#fff')
      + ''.join(T.confete(x, y, r, c) for x, y, r, c in [(160, 1050, 20, B.YEL), (950, 1080, -30, '#fff'), (900, 1400, 40, B.LILAC), (150, 1420, -10, '#fff')]),
      T.raios(540, 1260, 22))
story('story-aperta-o-botao', [[('Fez o ponto?', '#fff')], [('Aperta o', '#fff')], [('botão.', B.YEL)]], ['O replay é seu.'],
      comp_botao(0, 520), T.raios(540, 1300, 22) + sol(880, 820, 80))

# ---------------- posts de frase 1:1 ----------------
def frase(nome, linhas, cena):
    b = f'<rect width="1080" height="1080" fill="{B.BLUE}"/>' + cena + logo(80, 1030, 44, B.BLUE, INK)
    y = 250
    for ln in linhas:
        b += linha(ln, 130, 80, y); y += 134
    save(f'{SOC}/frases/{nome}.svg', 1080, 1080, b, nome)


espia = (T.teco(780, 862, 250, 'piscando', rot=-8) + areia(1080, 1080, 900, 22)
         + T.mao('aberta', 520, 880, -20, 2.3, True) + T.mao('punho', 1030, 890, 10, 2.3, False)
         + T.brilho(480, 700, 0.9) + T.brilho(1000, 560, 0.7, '#fff'))
frase('ninguem-viu-o-teco-viu', [[('Ninguém viu?', '#fff')], [('O Teco', B.YEL)], [('viu.', B.YEL)]], espia)
prova = (areia(1080, 1080, 930, 20) + T.teco(800, 760, 190, 'orgulhoso', sombra=905, maos=[('joinha', -132, 10, -10, 1.3, True), ('punho', 128, 40, 0, 1.2, False)])
         + T.brilho(560, 600, 1.0) + T.brilho(990, 520, 0.8, '#fff'))
frase('foi-ponto-tem-prova', [[('Foi ponto.', '#fff')], [('E tem', '#fff')], [('prova.', B.YEL)]], prova)

# ---------------- ficha do personagem ----------------
FW, FH = 2400, 1500
b = f'<rect width="{FW}" height="{FH}" fill="{B.ICE}"/>'
b += f'<rect x="0" y="0" width="900" height="{FH}" fill="{B.BLUE}"/>'
b += f'<clipPath id="lado"><rect width="900" height="{FH}"/></clipPath><g clip-path="url(#lado)">{T.raios(450, 760, 20)}{areia(900, FH, 1290, 26)}</g>'
b += T.teco(450, 860, 270, 'empolgado', sombra=1160, maos=[('aberta', -132, 4, -22, 1.25, True), ('joinha', 130, 30, 10, 1.25, False)])
b += logo(70, 120, 48)
b += Tx('Teco', 150, 70, 330, B.YEL) + Tx('o mascote do repeteco', 42, 74, 400, '#fff', w='md', track=0)
b += Tx('Uma bola de vôlei de praia que vive', 34, 74, 1380, INK, w='md', track=0)
b += Tx('fazendo lance absurdo e odeia quando', 34, 74, 1424, INK, w='md', track=0)
b += Tx('ninguém vê. Por isso ele aperta o botão.', 34, 74, 1468, INK, w='md', track=0)
X = 980


def titulo(s, y): return Tx(s, 44, X, y, B.BLUE)
def nota(s, x, y, size=26, col='#55627f', align='center'): return Tx(s, size, x, y, col, w='md', track=0, align=align)


b += titulo('Expressões', 110)
for i, f in enumerate(['feliz', 'empolgado', 'piscando', 'focado', 'surpreso', 'triste', 'orgulhoso', 'apaixonado']):
    x = X + 75 + i * 172
    b += T.teco(x, 210, 66, f) + nota(f, x, 320)
b += titulo('Mãos flutuantes', 420)
b += nota('Luvas de cartum: três dedos gordinhos e polegar, contorno único. Esquerda e direita espelhadas.', X, 465, 28, align='left')
for i, p in enumerate(['aberta', 'punho', 'aponta', 'joinha']):
    x = X + 92 + i * 200
    b += f'<rect x="{x-88}" y="510" width="176" height="160" rx="40" fill="#fff"/>' + T.mao(p, x - 42, 600, 0, 1.3, True) + T.mao(p, x + 42, 600, 0, 1.3) + nota(p, x, 715)
b += f'<g transform="translate({X+930},585)">{T.teco(0,0,95,"focado",maos=[("aponta",125,-40,40,1.2,False)])}</g>' + nota('mão + corpo', X + 950, 715)
b += titulo('Detalhes da marca', 800)
det = [('faixa azul com o "e"', 'a assinatura vai na testa'), ('costuras com pesponto', 'bola de vôlei de verdade'), ('punho azul nas luvas', 'mesmo azul do app')]
for i, (a, c) in enumerate(det):
    y = 860 + i * 92
    b += f'<circle cx="{X+22}" cy="{y+16}" r="14" fill="{B.YEL}" stroke="{INK}" stroke-width="4"/>'
    b += Tx(a, 34, X + 52, y + 28, INK, w='bd', track=0) + nota(c, X + 52, y + 66, 26, align='left')
for i, (c, n) in enumerate([(B.YEL, '#F2C111'), (B.YEL_DK, '#E0AD00'), (B.BLUE, '#103A9E'), (INK, '#081F57'), ('#fff', '#FFFFFF')]):
    x = X + 30 + i * 112
    b += f'<circle cx="{x+30}" cy="1180" r="38" fill="{c}" stroke="{INK}" stroke-width="3"/>' + nota(n, x + 30, 1250, 22)
GX = X + 740
b += Tx('Gesto de assinatura', 44, GX, 800, B.BLUE) + nota('Lance bom? Ele gira para trás, como o "e" do logo.', GX, 845, 26, align='left')
for i, a in enumerate((0, -120, -240)):
    x = GX + 100 + i * 205
    if i:
        b += T.rebobina(x, 1010, 98, ang0=a + 40, arco=110 + i * 50, w=15)
    b += T.teco(x, 1010, 70, 'orgulhoso' if i == 2 else 'focado', rot=a)
b += nota('1. prepara', GX + 100, 1150) + nota('2. gira', GX + 305, 1150) + nota('3. repeteco!', GX + 510, 1150)
b += titulo('Regras', 1330)
regras = ['Sempre amarelo, sempre com a faixa.', 'Sem braços e sem pernas: só as luvas.', 'Uma expressão por vez, bem clara.', 'Nunca triste no fim: o lance sempre volta.']
for i, r in enumerate(regras):
    b += Tx('•  ' + r, 28, X + (i % 2) * 700, 1385 + (i // 2) * 44, '#33415f', w='md', track=0)
save(f'{TECO}/ficha/ficha-do-teco.svg', FW, FH, b, 'ficha do Teco')

# ---------------- geometria para o motion ----------------
_motion = {
    'corpo': T.corpo(True), 'corpoSemFaixa': T.corpo(False),
    'rostos': {k: f() for k, f in T.ROSTO.items()},
    'maos': T.MAO, 'maosEsp': T.MAO_ESP,
    # cenário em coordenadas do palco do motion (1080x1080, chão em y=900)
    'rede': rede_lateral(500, 906, 640, 884, 470, 330, sw=2.6)
            + f'<ellipse cx="500" cy="906" rx="44" ry="11" fill="{B.YEL_DK}"/><ellipse cx="640" cy="884" rx="30" ry="8" fill="{B.YEL_DK}"/>',
    'botao': botao_quadra(850, 750, 880, 1.1) + f'<ellipse cx="850" cy="906" rx="46" ry="11" fill="{B.YEL_DK}"/>',
    'celular': celular(0, 0, 300, 580),
    'rebobina': T.rebobina(0, 0, 210, ang0=-20, arco=300, w=34),
}
os.makedirs(MARCA + '/motion/teco', exist_ok=True)
open(MARCA + '/motion/teco/teco.js', 'w').write('// gerado por fonte/gerar_teco.py: o Teco detalhado (raio 100, centro 0,0)\nwindow.TECO=' + json.dumps(_motion, ensure_ascii=False) + ';\n')
print('teco ok')
