from caminhos import *  # noqa
"""Ilustrações de estado do app (vazio, erro, vídeo indisponível, alertas...) e capas de fallback.

Cada cena fica num "palco" redondo azul com areia, então funciona no tema claro e no escuro sem
variação. O Teco faz o papel principal. As animações são CSS dentro do próprio SVG (funcionam em
<img>) e param com prefers-reduced-motion. Grade: viewBox 480x360, palco centrado em (240,190), raio 140.
"""
import os, math, brand as B
from teco import ball, eye, closed_eye, blush, word, sparkle, heart, rede_lateral, INK

OUT = MARCA + '/ilustracoes'
os.makedirs(OUT + '/svg', exist_ok=True)
CX, CY, RS = 240, 190, 140
W, H = 480, 360
RED = '#F2545B'; GREEN = '#2BB673'; ORANGE = '#FF8A2B'; GRAY = '#9AA7C2'

CSS = ('<style>'
       '.flutua{animation:flutua 3.2s ease-in-out infinite}'
       '@keyframes flutua{0%,100%{transform:translateY(0)}50%{transform:translateY(-7px)}}'
       '.brilha{animation:brilha 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}'
       '.brilha.b2{animation-delay:-.8s}.brilha.b3{animation-delay:-1.6s}'
       '@keyframes brilha{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.35;transform:scale(.6)}}'
       '.balanca{animation:balanca 2.6s ease-in-out infinite;transform-box:fill-box;transform-origin:50% 0}'
       '@keyframes balanca{0%,100%{transform:rotate(-7deg)}50%{transform:rotate(7deg)}}'
       '.acena{animation:acena 2.2s ease-in-out infinite;transform-box:fill-box;transform-origin:50% 100%}'
       '@keyframes acena{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(6deg)}}'
       '.luz{animation:luz 1.2s steps(2,jump-none) infinite}'
       '@keyframes luz{0%{opacity:1}100%{opacity:.15}}'
       '.sobe{animation:sobe 3s ease-in infinite;transform-box:fill-box;transform-origin:center}'
       '.sobe.s2{animation-delay:-1s}.sobe.s3{animation-delay:-2s}'
       '@keyframes sobe{0%{opacity:0;transform:translate(0,10px) scale(.7)}30%{opacity:1}100%{opacity:0;transform:translate(10px,-26px) scale(1.1)}}'
       '.voa{animation:voa 3s ease-in-out infinite}'
       '@keyframes voa{0%,100%{transform:translate(0,0)}50%{transform:translate(6px,-8px)}}'
       '.tremor{animation:tremor 1.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}'
       '@keyframes tremor{0%,70%,100%{transform:rotate(0)}75%{transform:rotate(-4deg)}85%{transform:rotate(4deg)}95%{transform:rotate(-2deg)}}'
       '.gira{animation:gira 6s linear infinite;transform-box:fill-box;transform-origin:center}'
       '@keyframes gira{to{transform:rotate(360deg)}}'
       '@media (prefers-reduced-motion:reduce){*{animation:none!important}}'
       '</style>')


def doc(nome, titulo, corpo, w=W, h=H):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img">'
            f'<title>{titulo}</title>{CSS}{corpo}</svg>\n')


# ---------------- palco ----------------
def palco(ceu=B.BLUE, areia=True, extra=''):
    g = f'<clipPath id="palco"><circle cx="{CX}" cy="{CY}" r="{RS}"/></clipPath>'
    g += f'<circle cx="{CX}" cy="{CY}" r="{RS}" fill="{ceu}"/>'
    g += f'<g clip-path="url(#palco)">{extra}'
    if areia:
        g += B.P(B.wave_path(W, H, 262, 10, 0.12, 0.4), B.YEL) + B.P(B.wave_path(W, H, 284, 7, 0.55, 1.3, (1.4, 0.8, 2.1)), B.YEL_DK)
    return g + '</g>'


def no_palco(svg):
    """Coisas que ficam dentro do círculo (cortadas pela borda)."""
    return f'<g clip-path="url(#palco)">{svg}</g>'


# ---------------- Teco com expressões (coordenadas do emoji: centro 256,272, raio 168) ----------------
def _brows(kind):
    if kind == 'tristes':
        return (f'<path d="M176,206 L226,196" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
                f'<path d="M286,196 L336,206" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>')
    if kind == 'bravas':
        return (f'<path d="M178,204 L228,218" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>'
                f'<path d="M284,218 L334,204" stroke="{INK}" stroke-width="12" stroke-linecap="round"/>')
    return ''


def _mouth(kind):
    if kind == 'sorriso':
        return f'<path d="M216,318 Q256,354 296,318" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
    if kind == 'aberta':
        return (f'<path d="M210,312 Q256,384 302,312 Z" fill="{INK}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
                f'<path d="M232,342 Q256,332 280,342 Q256,356 232,342Z" fill="#F2705B"/>')
    if kind == 'triste':
        return f'<path d="M222,344 Q256,316 290,344" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
    if kind == 'onda':
        return f'<path d="M212,338 q14,-14 28,0 t28,0 t28,0" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>'
    if kind == 'o':
        return f'<ellipse cx="256" cy="338" rx="20" ry="25" fill="{INK}"/>'
    if kind == 'reta':
        return f'<path d="M232,334 H284" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
    if kind == 'mini':
        return f'<ellipse cx="256" cy="334" rx="12" ry="9" fill="{INK}"/>'
    if kind == 'meia':
        return f'<path d="M238,330 Q262,346 286,326" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
    return ''


def _spiral(x, y):
    return (f'<path d="M{x},{y} m-4,0 a4,4 0 1 1 8,0 a10,10 0 1 1 -18,0 a16,16 0 1 1 30,0 a22,22 0 1 1 -42,0" '
            f'fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>')


def _x_eye(x, y):
    return f'<path d="M{x-18},{y-18} L{x+18},{y+18} M{x+18},{y-18} L{x-18},{y+18}" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'


ROSTOS = {
    'feliz': lambda: eye(206, 250) + eye(306, 250) + blush(170, 312) + blush(342, 312) + _mouth('sorriso'),
    'olha-dir': lambda: eye(206, 250, 1, (8, -2)) + eye(306, 250, 1, (8, -2)) + blush(170, 312) + blush(342, 312) + _mouth('sorriso'),
    'olha-esq': lambda: eye(206, 250, 1, (-8, -2)) + eye(306, 250, 1, (-8, -2)) + blush(170, 312) + blush(342, 312) + _mouth('sorriso'),
    'olha-cima': lambda: eye(206, 250, 1, (4, -10)) + eye(306, 250, 1, (4, -10)) + _mouth('mini'),
    'pensativo': lambda: eye(206, 250, 1, (8, -9)) + eye(306, 250, 1, (8, -9)) + _mouth('meia'),
    'triste': lambda: _brows('tristes') + eye(206, 252, 1, (0, 7)) + eye(306, 252, 1, (0, 7)) + _mouth('triste')
              + f'<path d="M170,280 q-14,22 0,32 q14,-10 0,-32z" fill="#7FC8F8" stroke="{INK}" stroke-width="5"/>',
    'preocupado': lambda: _brows('tristes') + eye(206, 252, 0.95, (0, -4)) + eye(306, 252, 0.95, (0, -4)) + _mouth('onda'),
    'surpreso': lambda: eye(204, 246, 1.25, (0, -4)) + eye(308, 246, 1.25, (0, -4)) + _mouth('o'),
    'dormindo': lambda: closed_eye(206, 262, False) + closed_eye(306, 262, False) + blush(170, 312) + blush(342, 312) + _mouth('mini'),
    'tonto': lambda: _spiral(206, 252) + _spiral(306, 252) + _mouth('onda'),
    'ko': lambda: _x_eye(206, 252) + _x_eye(306, 252) + _mouth('onda'),
    'piscando': lambda: eye(206, 250, 1, (4, -2)) + closed_eye(306, 254) + blush(170, 312) + blush(342, 312) + _mouth('sorriso'),
    'serio': lambda: _brows('bravas') + eye(206, 254, 0.95) + eye(306, 254, 0.95),
    'risada': lambda: closed_eye(206, 250) + closed_eye(306, 250) + _mouth('aberta'),
    'craque': lambda: (f'<path d="M150,228 H362 L352,262 Q340,292 300,290 Q270,288 262,256 H250 Q242,288 212,290 Q172,292 160,262Z" '
                       f'fill="{INK}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
                       f'<path d="M188,246 l26,-10 M286,246 l26,-10" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
                       f'<path d="M216,336 Q262,358 304,322" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'),
    'focado': lambda: _brows('bravas') + eye(206, 254, 0.95, (6, 2)) + eye(306, 254, 0.95, (6, 2)) + _mouth('meia'),
}


def teco(cx, cy, r, rosto='feliz', rot=0, anim='flutua', extra=''):
    """Teco em (cx,cy) com raio r. `extra` é desenhado por cima no mesmo sistema do emoji (chapéu, apito...)."""
    k = r / 168
    g = (f'<g transform="translate({cx},{cy}) rotate({rot}) scale({k:.4f}) translate(-256,-272)">'
         + ball(borda=False) + ROSTOS[rosto]() + extra + '</g>')
    return f'<g class="{anim}">{g}</g>' if anim else g


def sombra(cx, y, rx):
    return f'<ellipse cx="{cx}" cy="{y}" rx="{rx}" ry="{rx*0.16:.1f}" fill="{INK}" opacity=".18"/>'


# ---------------- pecinhas ----------------
SW = 4
# Regra de composição: tudo fica DENTRO do palco. Só "figurinhas" com borda branca (?, 404, selo, cartão,
# o tile do "e") podem passar da borda, de propósito. Enfeites soltos (estrelas, confete, risquinhos)
# são puxados para dentro automaticamente, para não virar traço perdido fora do círculo.
MARGEM = 18


def dentro(x, y, m=MARGEM):
    dx, dy = x - CX, y - CY
    d = math.hypot(dx, dy); lim = RS - m
    if d <= lim:
        return x, y
    return CX + dx * lim / d, CY + dy * lim / d


def estrela(x, y, s=1, c=B.YEL, cls='brilha'):
    x, y = dentro(x, y, 18 * s)
    return f'<g class="{cls}">{sparkle(x, y, s * 0.42, c).replace("stroke-width=\"5\"", "stroke-width=\"6\"")}</g>'


def confete(x, y, rot, c, w=10, h=5):
    x, y = dentro(x, y, 10)
    return f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="1.5" fill="{c}" transform="rotate({rot} {x} {y})"/>'


def linhas_mov(x, y, n=3, dx=-26, gap=11, cor='#fff'):
    return ''.join(f'<path d="M{x},{y+i*gap} h{dx + (i % 2) * 8}" stroke="{cor}" stroke-width="5" stroke-linecap="round"/>' for i in range(n))


def interrog(x, y, s=60, rot=10, fill=B.YEL):
    return word('?', s, x, y, fill=fill, rot=rot)


def poste_botao(x, y_base, top):
    """O botão físico da quadra num poste (igual ao do motion)."""
    g = f'<rect x="{x-7}" y="{top+40}" width="14" height="{y_base-top-40}" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{SW}"/>'
    g += f'<rect x="{x-44}" y="{top}" width="88" height="62" rx="16" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
    g += (f'<path d="M{x-28},{top+24} v9 a28,10 0 0 0 56,0 v-9" fill="{B.YEL_DK}" stroke="{INK}" stroke-width="{SW}"/>'
          f'<ellipse cx="{x}" cy="{top+24}" rx="28" ry="10" fill="{B.YEL}" stroke="{INK}" stroke-width="{SW}"/>')
    return g


def tela_video(x, y, w, h, conteudo='', moldura='#fff'):
    """Player: moldura arredondada, tela azul-noite e barra de progresso."""
    g = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{moldura}" stroke="{INK}" stroke-width="{SW}"/>'
    g += f'<rect x="{x+10}" y="{y+10}" width="{w-20}" height="{h-38}" rx="9" fill="{B.BLUE_DEEP}"/>'
    g += f'<path d="M{x+18},{y+h-15} H{x+w-18}" stroke="{B.LILAC}" stroke-width="5" stroke-linecap="round"/>'
    return g + conteudo


def ampulheta(cx, cy, h, areia_baixo=1.0, cls=''):
    """Ampulheta de areia: a areia toda embaixo = tempo esgotado."""
    w = h * 0.62; hh = h / 2; t = cy - hh; b = cy + hh
    vidro = (f'M{cx-w/2+8},{t+12} C{cx-w/2+8},{cy-18} {cx-8},{cy-10} {cx-6},{cy} C{cx-8},{cy+10} {cx-w/2+8},{cy+18} {cx-w/2+8},{b-12} '
             f'H{cx+w/2-8} C{cx+w/2-8},{cy+18} {cx+8},{cy+10} {cx+6},{cy} C{cx+8},{cy-10} {cx+w/2-8},{cy-18} {cx+w/2-8},{t+12}Z')
    g = f'<g class="{cls}">' if cls else '<g>'
    g += f'<clipPath id="vidro{cx}{cy}"><path d="{vidro}"/></clipPath><path d="{vidro}" fill="#fff" opacity=".22"/>'
    pile = b - 12 - (hh - 20) * 0.75 * areia_baixo
    g += (f'<g clip-path="url(#vidro{cx}{cy})"><path d="M{cx-w/2},{b} V{pile+22} Q{cx},{pile-14} {cx+w/2},{pile+22} V{b}Z" fill="{B.YEL}"/>'
          f'<path d="M{cx-w/2},{b} V{pile+40} Q{cx},{pile+16} {cx+w/2},{pile+40} V{b}Z" fill="{B.YEL_DK}"/></g>')
    g += f'<path d="{vidro}" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
    g += (f'<rect x="{cx-w/2-6}" y="{t}" width="{w+12}" height="14" rx="6" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{SW}"/>'
          f'<rect x="{cx-w/2-6}" y="{b-14}" width="{w+12}" height="14" rx="6" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{SW}"/>')
    return g + '</g>'


def envelope(cx, cy, w, rot=0):
    h = w * 0.66; x = cx - w / 2; y = cy - h / 2
    return (f'<g transform="rotate({rot} {cx} {cy})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
            f'<path d="M{x+4},{y+6} L{cx},{cy+8} L{x+w-4},{y+6}" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<path d="M{x+6},{y+h-6} L{cx-14},{cy+2} M{x+w-6},{y+h-6} L{cx+14},{cy+2}" stroke="{B.LILAC}" stroke-width="3" stroke-linecap="round"/></g>')


def selo_check(cx, cy, r, cor=GREEN):
    pts = []
    for i in range(28):
        a = math.radians(i * 360 / 28); rr = r if i % 2 == 0 else r * 0.84
        pts.append(f'{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}')
    p = ' '.join(pts)
    return (f'<polygon points="{p}" fill="#fff" stroke="#fff" stroke-width="10" stroke-linejoin="round"/>'
            f'<polygon points="{p}" fill="{cor}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<path d="M{cx-r*0.42},{cy+r*0.02} L{cx-r*0.1},{cy+r*0.32} L{cx+r*0.45},{cy-r*0.3}" fill="none" stroke="#fff" stroke-width="{r*0.2:.1f}" stroke-linecap="round" stroke-linejoin="round"/>')


def pino(cx, tipo_y, h, fill=B.YEL, dentro=''):
    """Pino de mapa com a ponta em (cx, tipo_y)."""
    r = h * 0.38; cy = tipo_y - h + r
    d = f'M{cx},{tipo_y} C{cx-r*0.5},{cy+r*1.2} {cx-r},{cy+r*0.6} {cx-r},{cy} A{r},{r} 0 1 1 {cx+r},{cy} C{cx+r},{cy+r*0.6} {cx+r*0.5},{cy+r*1.2} {cx},{tipo_y}Z'
    return (f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.52:.1f}" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>' + dentro.format(x=cx, y=cy, r=r))


def camera(x, y, s=1.0, luz=GRAY):
    """Câmera de quadra (olhando para a esquerda) presa num suporte; (x,y) é o ponto do suporte."""
    g = f'<g transform="translate({x},{y}) scale({s})">'
    g += f'<rect x="-92" y="-30" width="96" height="56" rx="14" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
    g += f'<path d="M-92,-20 h-16 a6,6 0 0 0 -6,6 v24 a6,6 0 0 0 6,6 h16" fill="{B.LILAC}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
    g += f'<circle cx="-62" cy="-2" r="15" fill="{B.BLUE_DEEP}" stroke="{INK}" stroke-width="{SW}"/><circle cx="-66" cy="-7" r="4" fill="#fff" opacity=".8"/>'
    g += f'<circle cx="-18" cy="-14" r="6" fill="{luz}" stroke="{INK}" stroke-width="3"/>'
    g += f'<path d="M-2,-24 h22 v22" fill="none" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
    return g + '</g>'


def placa(x, y, w, h):
    g = ''.join(f'<rect x="{px-6}" y="{y+h-6}" width="12" height="{276-(y+h)+30}" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{SW}"/>' for px in (x + w * 0.22, x + w * 0.78))
    g += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
    g += f'<rect x="{x+14}" y="{y+14}" width="{w-28}" height="{h-28}" rx="8" fill="none" stroke="{B.LILAC}" stroke-width="4" stroke-dasharray="10 9"/>'
    g += f'<path d="M{x+w/2},{y+h/2-16} v32 M{x+w/2-16},{y+h/2} h32" stroke="{B.BLUE}" stroke-width="7" stroke-linecap="round"/>'
    return g


# ---------------- as cenas ----------------
IL = {}


def cena(nome, titulo, uso, corpo):
    IL[nome] = (titulo, uso, corpo)


cena('boas-vindas', 'Boas-vindas', 'primeiro acesso, home sem histórico, fim do cadastro',
     palco() + sombra(CX, 272, 46)
     + teco(CX, 212, 58, 'feliz', anim='acena')
     + ''.join(confete(x, y, r, c) for x, y, r, c in [(130, 92, 20, B.YEL), (170, 62, -30, '#fff'), (318, 70, 40, B.LILAC), (352, 120, -10, B.YEL),
                                                      (112, 150, 60, B.LILAC), (378, 176, 25, '#fff'), (150, 118, 10, '#fff'), (300, 104, -50, B.YEL)])
     + f'<g transform="rotate(12 362 74)">{B.tile(326, 38, 72, B.BLUE, B.YEL)}<rect x="326" y="38" width="72" height="72" rx="19.7" fill="none" stroke="#fff" stroke-width="5"/></g>'
     + estrela(106, 92, 1) + estrela(392, 240, 0.8, '#fff', 'brilha b2'))

cena('sem-replays', 'Nenhum replay ainda', 'galeria de replays vazia (convida a apertar o botão na quadra)',
     palco(extra=poste_botao(184, 320, 122)) + sombra(310, 272, 40)
     + ''.join(f'<path d="M{170+dx},{100+dy} l{ex},{ey}" stroke="{B.YEL}" stroke-width="7" stroke-linecap="round" class="brilha {c}"/>'
               for dx, dy, ex, ey, c in [(-32, 12, -8, -10, ''), (14, 8, 0, -14, 'b2'), (60, 12, 8, -10, 'b3')])
     + teco(312, 228, 46, 'olha-esq')
     + f'<g class="voa"><rect x="256" y="100" width="78" height="50" rx="11" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="8 7"/>'
       f'<path d="M288,114 v22 l18,-11z" fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round"/></g>')

lupa_x, lupa_y = 230 + (306 - 256) * 56 / 168, 214 + (250 - 272) * 56 / 168
cena('busca-vazia', 'Busca sem resultado', 'busca e filtros que não encontraram nada',
     palco() + sombra(230, 274, 46)
     + '<g class="flutua">' + teco(230, 214, 56, 'pensativo', anim='')
     + f'<path d="M{lupa_x+22},{lupa_y+22} L{lupa_x+70},{lupa_y+74}" stroke="{INK}" stroke-width="18" stroke-linecap="round"/>'
       f'<path d="M{lupa_x+22},{lupa_y+22} L{lupa_x+70},{lupa_y+74}" stroke="{B.BLUE}" stroke-width="10" stroke-linecap="round"/>'
       f'<circle cx="{lupa_x}" cy="{lupa_y}" r="30" fill="#fff" stroke="{INK}" stroke-width="5"/>'
       f'<g transform="translate({lupa_x},{lupa_y}) scale(.62) translate(-306,-250)">{eye(306, 250, 1.35, (8, -9))}</g>'
       f'<circle cx="{lupa_x}" cy="{lupa_y}" r="30" fill="none" stroke="{B.LILAC}" stroke-width="3" opacity=".6"/></g>'
     + f'<g class="balanca">{interrog(340, 128, 66, 12)}</g>' + estrela(140, 110, 0.8, '#fff'))

cena('sem-quadras', 'Nenhuma quadra', 'listagem de quadras vazia ou filtro sem quadras',
     palco(extra=rede_lateral(182, 300, 240, 274, 148, 98, sw=0.9))
     + no_palco(f'<path d="M110,306 Q240,286 380,300" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="10 10" opacity=".7"/>')
     + sombra(330, 276, 38) + teco(330, 236, 40, 'pensativo')
     + f'<g class="balanca">{interrog(330, 160, 52, 10)}</g>')

cena('sem-arenas', 'Nenhuma arena', 'listagem de arenas vazia ou cidade sem arenas',
     palco() + f'<ellipse cx="270" cy="284" rx="34" ry="7" fill="{INK}" opacity=".2"/>'
     + '<g class="flutua">' + pino(270, 250, 150, dentro=f'<path d="M{{x}},{{y}}" />') + word('?', 46, 270, 172, fill=B.BLUE, stroke=INK) + '</g>'
     + sombra(168, 278, 36) + teco(168, 244, 36, 'olha-cima', anim='')
     + estrela(352, 110, 0.9) + estrela(120, 140, 0.7, '#fff', 'brilha b3'))

cabo = lambda d: f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="12" stroke-linecap="round"/><path d="{d}" fill="none" stroke="{B.LILAC}" stroke-width="6" stroke-linecap="round"/>'
cena('sem-conexao', 'Sem conexão', 'falha de rede ou API fora do ar (QueryErrorState)',
     palco(extra=cabo('M60,250 C120,250 140,160 190,150') + cabo('M420,250 C360,250 340,160 296,150'))
     + f'<g class="tremor"><rect x="186" y="132" width="34" height="36" rx="8" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
       f'<path d="M220,141 h16 M220,159 h16" stroke="{INK}" stroke-width="6" stroke-linecap="round"/></g>'
     + f'<rect x="262" y="130" width="38" height="40" rx="9" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
       f'<circle cx="276" cy="143" r="3.5" fill="{INK}"/><circle cx="276" cy="157" r="3.5" fill="{INK}"/>'
     + ''.join(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{B.YEL}" stroke-width="5" stroke-linecap="round" class="brilha {c}"/>'
               for x1, y1, x2, y2, c in [(246, 126, 252, 112, ''), (248, 150, 258, 150, 'b2'), (246, 174, 252, 188, 'b3')])
     + sombra(CX, 278, 40) + teco(CX, 240, 42, 'preocupado'))

# bola na rede: rede vista de frente em close (aqui não há trajetória, então a vista frontal faz sentido)
malha = ''.join(f'<path d="M{x},96 V214" stroke="#fff" stroke-width="2.5" opacity=".75"/>' for x in range(96, 400, 22))
malha += ''.join(f'<path d="M90,{y} H390" stroke="#fff" stroke-width="2.5" opacity=".75"/>' for y in range(118, 214, 22))
bojo = ''.join(f'<path d="M{CX-70},{y} Q{CX},{y+28} {CX+70},{y}" fill="none" stroke="#fff" stroke-width="3"/>' for y in (150, 178, 206))
bojo += ''.join(f'<path d="M{x},{120} Q{x+(x-CX)*0.25},{170} {x},{226}" fill="none" stroke="#fff" stroke-width="3"/>' for x in (CX - 40, CX - 14, CX + 14, CX + 40))
cena('bola-na-rede', 'Algo deu errado', 'erro genérico (exceção inesperada, ação que falhou)',
     palco(extra=malha + f'<path d="M80,96 H400" stroke="#fff" stroke-width="10"/><path d="M80,214 H400" stroke="#fff" stroke-width="5"/>')
     + '<g class="tremor">' + teco(CX, 176, 50, 'tonto', anim='')
     + f'<g clip-path="url(#bojoclip)">{bojo}</g><clipPath id="bojoclip"><circle cx="{CX}" cy="176" r="50"/></clipPath></g>'
     + estrela(170, 122, 0.8, '#fff') + estrela(316, 116, 0.9, B.YEL, 'brilha b2') + estrela(300, 236, 0.6, '#fff', 'brilha b3'))

def rack(x, y, w, h):
    g = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
    for i, cor in enumerate((GREEN, GREEN, RED)):
        yy = y + 16 + i * (h - 24) / 3
        g += f'<rect x="{x+12}" y="{yy}" width="{w-24}" height="{(h-24)/3-10}" rx="7" fill="{B.ICE}" stroke="{INK}" stroke-width="3"/>'
        g += f'<path d="M{x+24},{yy+(h-24)/6-5} h{w*0.38}" stroke="{B.LILAC}" stroke-width="5" stroke-linecap="round"/>'
        g += f'<circle cx="{x+w-30}" cy="{yy+(h-24)/6-5}" r="6" fill="{cor}" stroke="{INK}" stroke-width="2.5" class="{"luz" if cor == RED else ""}"/>'
    return g
fumaca = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity=".85" class="sobe {c}"/>' for x, y, r, c in [(198, 102, 11, ''), (212, 90, 8, 's2'), (186, 86, 7, 's3')])
cena('erro-servidor', 'Servidor fora do ar', 'erro 5xx, serviço indisponível',
     palco() + rack(146, 114, 108, 158) + fumaca + sombra(318, 276, 40) + teco(318, 238, 42, 'preocupado'))

cena('nao-encontrado', 'Página não encontrada', 'rota inexistente (404) e replay/arena/quadra que não existe mais',
     palco() + sombra(CX, 272, 44)
     + word('4', 150, 128, 252, fill=B.YEL, rot=-8) + word('4', 150, 352, 252, fill=B.YEL, rot=8)
     + teco(CX, 200, 56, 'surpreso')
     + f'<g transform="translate({CX},300) scale(.16)">{B.e_mark("#fff")}</g>'
     + estrela(110, 96, 0.9, '#fff') + estrela(372, 90, 0.8, B.YEL, 'brilha b2'))

play_cortado = (f'<path d="M226,104 v40 l34,-20z" fill="#fff" opacity=".9"/>'
                f'<path d="M206,150 L282,98" stroke="{B.BLUE_DEEP}" stroke-width="12" stroke-linecap="round"/><path d="M206,150 L282,98" stroke="{RED}" stroke-width="6" stroke-linecap="round"/>')
cena('video-indisponivel', 'Vídeo indisponível', 'player sem arquivo, vídeo que falhou ao carregar',
     palco() + '<g class="flutua"><g transform="translate(240,142) scale(.74) translate(-240,-132)">' + tela_video(140, 64, 200, 136, play_cortado) + '</g></g>'
     + sombra(CX, 280, 40) + teco(CX, 244, 40, 'triste', anim=''))

cena('replay-expirado', 'Replay expirado', 'replay cujo prazo acabou (ReplayExpiry = expirado)',
     palco() + sombra(196, 278, 46) + ampulheta(198, 196, 156, 1.0, 'tremor')
     + sombra(320, 278, 36) + teco(320, 242, 38, 'dormindo', rot=-8, anim='')
     + ''.join(f'<g class="sobe {c}">{word("z", s, x, y, rot=-12)}</g>' for x, y, s, c in [(352, 182, 28, ''), (368, 156, 36, 's2'), (346, 130, 24, 's3')]))

apito = (f'<g transform="translate(256,330) rotate(-12)"><rect x="-6" y="-26" width="70" height="44" rx="20" fill="#fff" stroke="{INK}" stroke-width="10"/>'
         f'<rect x="-50" y="-26" width="64" height="26" rx="10" fill="#fff" stroke="{INK}" stroke-width="10"/><circle cx="34" cy="-4" r="9" fill="{INK}"/></g>')
cena('acesso-negado', 'Acesso não permitido', 'rota/ação sem permissão (RequireRole, ForbiddenDialog)',
     palco() + sombra(214, 276, 46) + teco(214, 222, 52, 'serio', extra=apito)
     + ''.join(f'<path d="M{x1},{y1} l{dx},{dy}" stroke="#fff" stroke-width="5" stroke-linecap="round" class="brilha {c}"/>'
               for x1, y1, dx, dy, c in [(170, 270, -16, 10, ''), (164, 252, -20, 0, 'b2')])
     + f'<g class="balanca"><g transform="rotate(14 336 130)"><rect x="306" y="84" width="60" height="86" rx="9" fill="#fff" stroke="#fff" stroke-width="10"/>'
       f'<rect x="306" y="84" width="60" height="86" rx="9" fill="{RED}" stroke="{INK}" stroke-width="{SW}"/>'
       f'<path d="M318,96 h20" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".7"/></g></g>')

cena('sem-patrocinadores', 'Nenhum patrocinador', 'lista de patrocinadores vazia (espaço disponível)',
     palco(extra=placa(170, 100, 152, 100)) + sombra(146, 278, 34) + teco(146, 246, 34, 'olha-dir', anim='flutua')
     + estrela(368, 96, 0.9) + estrela(120, 120, 0.6, '#fff', 'brilha b2'))

cena('email-enviado', 'E-mail enviado', 'recuperação de senha enviada, confirmação de cadastro',
     palco() + sombra(196, 276, 46) + teco(196, 232, 48, 'piscando')
     + f'<g class="voa">{linhas_mov(254, 128, 3, -28, 12)}{envelope(300, 138, 78, -12)}'
       f'<g transform="rotate(-12 300 138)">{selo_check(330, 120, 15)}</g></g>'
     + estrela(392, 196, 0.7, '#fff', 'brilha b2'))

def elo(cx, cy, rot, cor='#fff'):
    return (f'<g transform="rotate({rot} {cx} {cy})"><rect x="{cx-38}" y="{cy-20}" width="76" height="40" rx="20" fill="none" stroke="{INK}" stroke-width="18"/>'
            f'<rect x="{cx-38}" y="{cy-20}" width="76" height="40" rx="20" fill="none" stroke="{cor}" stroke-width="10"/></g>')
cena('link-expirado', 'Link expirado', 'link de redefinição de senha expirado ou inválido',
     palco() + elo(172, 146, -24, B.LILAC) + elo(306, 134, 18)
     + ''.join(f'<path d="M{x1},{y1} l{dx},{dy}" stroke="{B.YEL}" stroke-width="6" stroke-linecap="round" class="brilha {c}"/>'
               for x1, y1, dx, dy, c in [(232, 120, 6, -12, ''), (238, 140, 12, 0, 'b2'), (232, 160, 6, 12, 'b3')])
     + sombra(CX, 278, 42) + teco(CX, 238, 44, 'preocupado'))

cena('sucesso', 'Tudo certo', 'ação concluída: solicitação enviada, senha alterada, dados salvos',
     palco() + sombra(226, 274, 48) + teco(226, 220, 56, 'craque')
     + f'<g class="acena">{selo_check(338, 104, 36)}</g>'
     + ''.join(confete(x, y, r, c) for x, y, r, c in [(126, 100, 20, B.YEL), (160, 70, -30, '#fff'), (390, 170, 40, B.LILAC), (110, 170, 60, '#fff'), (286, 70, -20, B.YEL)])
     + estrela(380, 220, 0.7, '#fff', 'brilha b2'))

lua = f'<path d="M160,74 a34,34 0 1 0 34,46 a28,28 0 1 1 -34,-46z" fill="{B.ICE}" stroke="{INK}" stroke-width="{SW}"/>'
cena('sessao-expirada', 'Sessão expirada', 'sessão que expirou, pedido para entrar de novo',
     palco(ceu=B.BLUE_DK) + lua
     + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" class="brilha {c}"/>' for x, y, r, c in [(250, 78, 3, ''), (300, 104, 2.5, 'b2'), (340, 72, 3, 'b3'), (216, 120, 2, 'b2'), (360, 140, 2, '')])
     + sombra(CX, 276, 48) + teco(CX, 230, 52, 'dormindo', rot=-6)
     + ''.join(f'<g class="sobe {c}">{word("z", s, x, y, rot=-12)}</g>' for x, y, s, c in [(298, 176, 28, ''), (318, 148, 38, 's2'), (294, 120, 24, 's3')]))

capacete = (f'<path d="M120,186 Q118,70 256,64 Q394,70 392,186 Z" fill="#fff" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            f'<path d="M256,64 V186" stroke="{B.LILAC}" stroke-width="22"/><path d="M96,190 H416" stroke="{INK}" stroke-width="26" stroke-linecap="round"/>'
            f'<path d="M96,190 H416" stroke="#fff" stroke-width="12" stroke-linecap="round"/>')
cone = (f'<path d="M140,282 L160,190 h20 L200,282Z" fill="{ORANGE}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
        f'<path d="M151,236 h38 l3,16 h-44z M157,208 h26 l2,10 h-30z" fill="#fff"/>'
        f'<rect x="126" y="278" width="88" height="12" rx="5" fill="{ORANGE}" stroke="{INK}" stroke-width="{SW}"/>')
chave = (f'<g transform="translate(8,40) scale(.82) rotate(-38 340 150)" class="balanca"><rect x="333" y="120" width="14" height="74" rx="6" fill="{GRAY}" stroke="{INK}" stroke-width="{SW}"/>'
         f'<path d="M340,92 a22,22 0 1 0 0.1,0 M330,92 v26 h20 v-26" fill="{GRAY}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/></g>')
cena('manutencao', 'Em manutenção', 'sistema em manutenção ou recurso temporariamente desligado',
     palco() + sombra(256, 276, 46) + cone + teco(262, 226, 50, 'focado', extra=capacete) + chave)

cena('camera-offline', 'Câmera offline', 'câmera da quadra sem sinal (painel do gestor/admin)',
     palco(extra=f'<rect x="300" y="130" width="14" height="190" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{SW}"/>')
     + f'<g class="tremor">{camera(310, 128, 1.1)}</g>'
     + f'<path d="M262,148 C268,176 240,186 252,214" fill="none" stroke="{INK}" stroke-width="9" stroke-linecap="round"/>'
       f'<path d="M262,148 C268,176 240,186 252,214" fill="none" stroke="{B.LILAC}" stroke-width="4" stroke-linecap="round"/>'
     + ''.join(f'<path d="M{x1},{y1} l{dx},{dy}" stroke="{B.YEL}" stroke-width="5" stroke-linecap="round" class="brilha {c}"/>'
               for x1, y1, dx, dy, c in [(258, 222, 12, 6, ''), (250, 226, 0, 13, 'b2'), (244, 220, -11, 6, 'b3')])
     + f'<g transform="translate(140,146)"><circle r="20" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
       f'<path d="M-9,-2 a13,13 0 0 1 18,0 M-4,4 a6,6 0 0 1 8,0" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linecap="round"/>'
       f'<path d="M-12,12 L12,-12" stroke="{RED}" stroke-width="4" stroke-linecap="round"/></g>'
     + sombra(176, 278, 38) + teco(176, 242, 40, 'olha-cima', anim='flutua'))

sino = (f'<g class="balanca"><path d="M240,62 v12" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
        f'<path d="M196,170 C200,150 202,128 206,112 C212,88 226,76 240,76 C254,76 268,88 274,112 C278,128 280,150 284,170 Z" fill="#fff" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round"/>'
        f'<rect x="188" y="166" width="104" height="16" rx="8" fill="{B.LILAC}" stroke="{INK}" stroke-width="{SW}"/>'
        f'<circle cx="240" cy="190" r="10" fill="{B.YEL}" stroke="{INK}" stroke-width="{SW}"/></g>')
cena('notificacao', 'Notificação', 'central de avisos, alerta importante, novidade',
     palco() + sino
     + f'<path d="M176,110 q-14,22 0,44 M160,100 q-20,32 0,64" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" class="brilha"/>'
     + f'<path d="M304,110 q14,22 0,44 M320,100 q20,32 0,64" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" class="brilha b2"/>'
     + f'<circle cx="282" cy="94" r="18" fill="{RED}" stroke="#fff" stroke-width="5"/>' + B.P(B.text('!', 26, 282, 103, align='center')[0], '#fff')
     + sombra(CX, 280, 36) + teco(CX, 248, 36, 'surpreso', anim=''))

# ---------------- capas de fallback (mídia sem imagem) ----------------
def capa(nome, glifo):
    w, h = 640, 360
    body = f'<rect width="{w}" height="{h}" fill="{B.BLUE}"/>'
    body += f'<g transform="translate(520,96) scale(.9)" opacity=".18">{B.e_mark(B.LILAC)}</g>'
    body += B.P(B.wave_path(w, h, 292, 12, 0.12, 0.4), B.YEL) + B.P(B.wave_path(w, h, 318, 8, 0.55, 1.3, (1.4, 0.8, 2.1)), B.YEL_DK)
    body += glifo
    open(f'{OUT}/capas/{nome}.svg', 'w').write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" width="{w}" height="{h}"><title>{nome}</title>{body}</svg>\n')


os.makedirs(OUT + '/capas', exist_ok=True)
capa('capa-replay', f'<circle cx="320" cy="168" r="58" fill="#fff" opacity=".95"/><path d="M304,138 v60 l50,-30z" fill="{B.BLUE}" stroke="{B.BLUE}" stroke-width="8" stroke-linejoin="round"/>')
capa('capa-quadra', rede_lateral(286, 316, 352, 290, 210, 140, sw=1.1))
capa('capa-arena', f'<ellipse cx="320" cy="300" rx="34" ry="7" fill="{INK}" opacity=".25"/>' + pino(320, 292, 170, fill=B.YEL))

# avatar padrão (perfil sem foto)
av = (f'<clipPath id="av"><circle cx="128" cy="128" r="128"/></clipPath><circle cx="128" cy="128" r="128" fill="{B.BLUE}"/>'
      f'<g clip-path="url(#av)">{B.P(B.wave_path(256, 256, 206, 8, 0.12, 0.4), B.YEL)}'
      f'<g transform="translate(128,150) scale(.5) translate(-256,-272)">{ball(borda=False)}{ROSTOS["feliz"]()}</g></g>')
open(f'{OUT}/capas/avatar-teco.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256"><title>avatar</title>{av}</svg>\n')

for k, (titulo, uso, corpo) in IL.items():
    open(f'{OUT}/svg/{k}.svg', 'w').write(doc(k, titulo, corpo))

# índice para o README e para o componente
open(f'{OUT}/indice.tsv', 'w').write(''.join(f'{k}\t{t}\t{u}\n' for k, (t, u, _) in IL.items()))
print(len(IL), 'ilustrações + 3 capas + avatar')

# folha de visualização (ids prefixados para não colidirem entre as cenas)
import re
cols, cw, chh = 4, 500, 420
nomes = list(IL)
rows = (len(nomes) + cols - 1) // cols
folha = ''
for i, k in enumerate(nomes):
    corpo = IL[k][2]
    corpo = re.sub(r'id="([^"]+)"', lambda m: f'id="{k}-{m.group(1)}"', corpo)
    corpo = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#{k}-{m.group(1)})', corpo)
    x, y = (i % cols) * cw, (i // cols) * chh
    folha += f'<g transform="translate({x+10},{y+4})">{corpo}</g>'
    folha += B.P(B.text(k, 20, x + cw / 2, y + chh - 22, w='md', track=0, align='center')[0], '#55627f')
open(f'{OUT}/ilustracoes-preview.svg', 'w').write(B.svg(cols * cw, rows * chh, folha, bg=B.ICE, title='ilustrações repeteco'))
