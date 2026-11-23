"""Mãos (luvas) do Teco desenhadas como silhuetas únicas e suaves.

Referência de estilo: luvas de desenho animado clássico (rubber hose / mascote de bola):
- três dedos + polegar ("four-fingered hand"), dedos gordinhos, curtos, com ponta redonda;
- palma "fofa", maior que um dedo e meio de altura; os dedos têm ~1/3 da largura da palma;
- uma única linha de contorno por peça, com a mesma espessura do contorno do corpo;
- vincos internos finos e afinando para dentro, nunca linhas cruzando o contorno;
- volume com uma sombra lateral (luz vindo do alto à esquerda, igual ao corpo).

Cada peça é a união de formas simples (círculos, cápsulas afinadas, retângulos arredondados),
arredondada nas junções (fechamento morfológico) e exportada como um único <path>.
Assim o contorno é contínuo, sem emendas nem serrilhado onde os dedos encostam na palma.

Unidades: Teco de raio 100. Desenho base = mão que fica à DIREITA de quem olha (mão esquerda do Teco),
com o polegar para dentro (lado esquerdo do desenho). A outra mão é o espelho.
"""
from shapely.geometry import Point, Polygon, LineString, box
from shapely.ops import unary_union
from shapely import affinity
import brand as B

INK = B.BLUE_DEEP
W_CONTORNO = 4.6   # contorno do corpo é 7 em r=100; a luva (escala ~1.25) fica um pouco mais fina, como acessório
W_VINCO = 2.2
SOMBRA = '#D5DEF0'
Q = 24  # segmentos por quarto de círculo
ESCALA = 1.12  # luvas um pouco maiores que o desenho-base: mais expressivas (referência: luvas de cartum)


def circ(x, y, r):
    return Point(x, y).buffer(r, quad_segs=Q)


def dedo(x0, y0, x1, y1, r0, r1=None):
    """Cápsula afinada: base (x0,y0) raio r0, ponta (x1,y1) raio r1."""
    r1 = r0 * 0.92 if r1 is None else r1
    return unary_union([circ(x0, y0, r0), circ(x1, y1, r1)]).convex_hull


def bloco(x0, y0, x1, y1, r):
    return box(x0 + r, y0 + r, x1 - r, y1 - r).buffer(r, quad_segs=Q)


def trapezio(cx, y0, y1, w_top, w_bot, r):
    p = Polygon([(cx - w_top / 2 + r, y0 + r), (cx + w_top / 2 - r, y0 + r), (cx + w_bot / 2 - r, y1 - r), (cx - w_bot / 2 + r, y1 - r)])
    return p.buffer(r, quad_segs=Q)


def liso(g, r=1.6):
    """Arredonda os cantos côncavos (onde dedo encontra palma)."""
    return g.buffer(r, quad_segs=Q).buffer(-r, quad_segs=Q)


def _d(g):
    g = g.simplify(0.04)
    polys = getattr(g, 'geoms', [g])
    out = []
    for p in polys:
        for ring in [p.exterior, *p.interiors]:
            pts = list(ring.coords)[:-1]
            out.append('M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in pts) + 'Z')
    return ''.join(out)


def _sombra(sil, dx, dy):
    return sil.difference(affinity.translate(sil, dx, dy))


def peca(sil, cor='#fff', vincos=(), sombra=True, espelho=False):
    """Uma camada da luva: preenchimento, sombra interna, vincos e contorno, nessa ordem."""
    g = f'<path d="{_d(sil)}" fill="{cor}"/>'
    if sombra:
        # luz do alto à esquerda (como no corpo). No espelho a geometria já vem invertida, então a sombra continua à direita.
        sh = _sombra(sil, -3.2, -3.6).intersection(sil)
        if not sh.is_empty:
            g += f'<path d="{_d(sh)}" fill="{SOMBRA if cor == "#fff" else B.BLUE_DK}"/>'
    for v in vincos:
        (x0, y0), (x1, y1) = v[0], v[1]
        w0 = v[2] if len(v) > 2 else W_VINCO
        if espelho:
            x0, x1 = -x0, -x1
        t = dedo(x0, y0, x1, y1, w0 / 2, 0.45).intersection(sil.buffer(-0.2))
        if not t.is_empty:
            g += f'<path d="{_d(t)}" fill="{INK}"/>'
    g += f'<path d="{_d(sil)}" fill="none" stroke="{INK}" stroke-width="{W_CONTORNO}" stroke-linejoin="round"/>'
    return g


def punho_azul(cx=1, y=12, w=24, h=9):
    """Barra do punho: um rolinho azul por cima do pulso da luva, um pouco mais largo embaixo."""
    return trapezio(cx, y, y + h, w, w + 2.5, 4.6)


# ---------------- poses ----------------
# Cada pose: lista de camadas (de trás para a frente): (geometria, vincos, cor)
# vincos: ((x0,y0) no contorno, (x1,y1) ponta interna que afina, largura opcional)

def _aberta():
    palma = trapezio(1, -10, 16, 30, 25, 10)
    dedos = [dedo(-8, -6, -11, -20.5, 5.8, 5.5), dedo(2.4, -7, 2.9, -24, 5.9, 5.6), dedo(12.4, -5, 15.4, -18.5, 5.6, 5.3)]
    polegar = dedo(-8, 7, -19.5, -2, 6.0, 5.6)
    sil = liso(unary_union([palma, *dedos, polegar]), 1.0)
    vincos = [((-3.9, -14), (-3.1, -7.5)), ((7.9, -13), (7.4, -7))]
    palma_v = [((-1, 9), (7, 8), 1.6)]  # linha da palma, curtinha
    return [(sil, vincos + palma_v, '#fff')]


def _punho():
    corpo = bloco(-15, -10, 16, 15, 10)
    juntas = [circ(-8.6, -10.5, 5.8), circ(1, -11.8, 6.0), circ(10.4, -10.5, 5.7)]
    sil = liso(unary_union([corpo, *juntas]), 1.0)
    vincos = [((-3.8, -15.5), (-4, -5)), ((5.8, -15.5), (5.8, -5))]
    pol = liso(dedo(-14.5, 5.5, -4, 1.5, 5.8, 5.4))   # polegar dobrado por cima dos dedos, lado de dentro
    return [(sil, vincos, '#fff'), (pol, [], '#fff')]


def _aponta():
    corpo = bloco(-15, -8, 16, 15, 10)
    indicador = dedo(-8.2, -4, -8.8, -27, 5.8, 5.4)
    juntas = [circ(2, -8.8, 5.8), circ(11, -7.4, 5.5)]
    sil = liso(unary_union([corpo, indicador, *juntas]), 1.0)
    vincos = [((-2.4, -12.5), (-2.8, -3.5)), ((6.6, -12.5), (6.5, -3.5))]
    pol = liso(dedo(-14.5, 6, -3.5, 2.5, 5.8, 5.4))
    return [(sil, vincos, '#fff'), (pol, [], '#fff')]


def _joinha():
    # 👍 de frente: os dedos dobrados aparecem como rolinhos empilhados (pontas para dentro),
    # o dorso da mão fica atrás, e o polegar curto, grosso e inclinado sobe de cima dos rolinhos, com unha.
    dorso = bloco(-6, -6, 16, 18, 9)
    polegar = dedo(1.5, -4, 5.5, -20, 7.2, 6.6)
    sil = liso(unary_union([dorso, polegar]), 2.2)
    rolos = [dedo(-17, -1.5, 8, -1.5, 5.4, 5.4), dedo(-18, 8, 8, 8, 5.3, 5.3), dedo(-16.5, 17, 8, 17, 4.9, 4.9)]
    frente = unary_union(rolos)
    vincos = [((-24, 3.3), (2, 3.3)), ((-24, 12.6), (2, 12.6))]
    unha = [((2.5, -17.5), (9, -16.6), 1.6)]
    return [(sil, unha, '#fff'), (frente, vincos, '#fff')]


POSES = {'aberta': _aberta, 'punho': _punho, 'aponta': _aponta, 'joinha': _joinha}
CUFF = {'aberta': (1.5, 12.5, 25), 'punho': (1, 12, 27), 'aponta': (1, 12, 27), 'joinha': (5, 19, 22)}


def desenhar(pose, espelho=False):
    camadas = POSES[pose]()
    cx, cy, cw = CUFF[pose]
    cuff = punho_azul(cx, cy, cw)
    out = ''
    # punho azul por cima do pulso, como o elástico de uma luva
    todas = camadas + [(cuff, [], B.BLUE)]
    for sil, vincos, cor in todas:
        sil = affinity.scale(sil, -ESCALA if espelho else ESCALA, ESCALA, origin=(0, 0))
        vincos = [tuple((x * ESCALA, y * ESCALA) for x, y in v[:2]) + tuple(v[2:]) for v in vincos]
        out += peca(sil, cor, vincos, espelho=espelho)
    return out


MAO = {p: desenhar(p) for p in POSES}
MAO_ESP = {p: desenhar(p, True) for p in POSES}


def borda_figurinha(pose, espelho=False, folga=4.0, cor='#fff'):
    """Silhueta da luva inteira alargada: a borda branca de adesivo, para usar atrás da mão nas figurinhas."""
    camadas = POSES[pose]()
    cx, cy, cw = CUFF[pose]
    todas = unary_union([sil for sil, _, _ in camadas] + [punho_azul(cx, cy, cw)])
    todas = affinity.scale(todas, -ESCALA if espelho else ESCALA, ESCALA, origin=(0, 0))
    return f'<path d="{_d(todas.buffer(folga + W_CONTORNO / 2, quad_segs=Q))}" fill="{cor}"/>'
