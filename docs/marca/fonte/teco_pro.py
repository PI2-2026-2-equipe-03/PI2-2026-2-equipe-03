from caminhos import *  # noqa
"""Teco detalhado: a versão "de cena" do mascote, para pôsteres, posts e motion.

As figurinhas (teco.py) continuam como estão. Aqui o Teco ganha:
- mãos flutuantes (luvinhas brancas com punho azul): ele não tem braços, então a silhueta redonda não muda;
- faixa azul na testa com o "e" amarelo da marca;
- costuras com pesponto, luz e sombra, brilho de bola nova.
Tudo é desenhado num Teco de raio 100 centrado em (0,0) e depois escalado.
"""
import math
import brand as B

INK = B.BLUE_DEEP
SEAM = '#B98600'
LIGHT = '#FFD94A'
BLUSH = '#F28C6B'
_n = [0]


def _uid(p):
    _n[0] += 1
    return f'{p}{_n[0]}'


# ---------------- corpo ----------------
SEAMS = ['M-108,-40 C-35,-30 5,15 -12,110',   # pontas fora do círculo (o clip corta), entrando firmes na borda
         'M-52,-102 C10,-55 55,-35 110,-10',
         'M100,56 C40,32 -10,45 -88,80']


def corpo(faixa=True, giro=0):
    """Bola em r=100. `giro` gira só as costuras (a bola rolando sem o rosto girar)."""
    c = _uid('tc')
    g = f'<clipPath id="{c}"><circle r="100"/></clipPath><circle r="100" fill="{B.YEL}"/>'
    g += f'<g clip-path="url(#{c})">'
    # volume: meia-lua de sombra embaixo à direita (círculo menos círculo deslocado) e luz em cima à esquerda.
    # Nada de anel com traço: a borda interna do anel aparecia como uma linha solta no meio da bola.
    g += f'<path d="M-100,0 a100,100 0 1,0 200,0 a100,100 0 1,0 -200,0Z M-109,-14 a95,95 0 1,1 190,0 a95,95 0 1,1 -190,0Z" fill="{B.YEL_DK}" fill-rule="evenodd" opacity=".6"/>'
    g += f'<circle cx="-24" cy="-28" r="72" fill="{LIGHT}" opacity=".45"/>'
    g += f'<g transform="rotate({giro})">'
    for d in SEAMS:
        g += f'<path d="{d}" fill="none" stroke="{SEAM}" stroke-width="5" stroke-linecap="round" opacity=".85"/>'
        g += f'<path d="{d}" fill="none" stroke="{SEAM}" stroke-width="11" stroke-dasharray="1.6 8" opacity=".45"/>'
    g += '</g>'
    if faixa:
        g += (f'<path d="M-104,-46 Q0,-86 104,-46 L104,-20 Q0,-60 -104,-20Z" fill="{B.BLUE}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
              f'<path d="M-104,-41 Q0,-80 104,-41" fill="none" stroke="#fff" stroke-width="3" opacity=".35"/>')
        g += f'<g transform="translate(0,-50) scale(.115)">{B.e_mark(B.YEL)}</g>'
    g += '</g>'
    if faixa:  # pontas do nó saindo pela direita
        g += (f'<path d="M96,-38 C118,-50 130,-44 138,-58 C134,-34 120,-30 100,-28Z" fill="{B.BLUE}" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>'
              f'<path d="M98,-30 C120,-30 128,-18 142,-24 C132,-6 116,-12 99,-21Z" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="4.5" stroke-linejoin="round"/>')
    g += f'<ellipse cx="-46" cy="-58" rx="17" ry="9" transform="rotate(-35 -46 -58)" fill="#fff" opacity=".85"/><circle cx="-64" cy="-36" r="4" fill="#fff" opacity=".7"/>'
    g += f'<circle r="100" fill="none" stroke="{INK}" stroke-width="7"/>'
    return g


# ---------------- rosto ----------------
def olho(x, y, s=1.0, look=(0, 0)):
    lx, ly = look
    return (f'<ellipse cx="{x}" cy="{y}" rx="{15*s}" ry="{19*s}" fill="#fff" stroke="{INK}" stroke-width="4.5"/>'
            f'<circle cx="{x+lx*s}" cy="{y+3*s+ly*s}" r="{9*s}" fill="{INK}"/>'
            f'<circle cx="{x+lx*s-3*s}" cy="{y-1*s+ly*s}" r="{3.4*s}" fill="#fff"/><circle cx="{x+lx*s+3*s}" cy="{y+6*s+ly*s}" r="{1.6*s}" fill="#fff"/>')


def olho_feliz(x, y):
    return f'<path d="M{x-14},{y+5} Q{x},{y-14} {x+14},{y+5}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'


def olho_fechado(x, y):
    return f'<path d="M{x-14},{y-2} Q{x},{y+12} {x+14},{y-2}" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'


def sobrancelha(x, y, ang):
    a = math.radians(ang)
    return f'<path d="M{x-12*math.cos(a):.1f},{y-12*math.sin(a):.1f} L{x+12*math.cos(a):.1f},{y+12*math.sin(a):.1f}" stroke="{INK}" stroke-width="6.5" stroke-linecap="round"/>'


def bochechas():
    return f'<ellipse cx="-50" cy="24" rx="13" ry="7" fill="{BLUSH}" opacity=".5"/><ellipse cx="50" cy="24" rx="13" ry="7" fill="{BLUSH}" opacity=".5"/>'


def coracao(x, y, s=1):
    return f'<path transform="translate({x},{y}) scale({s})" d="M0,8 C-18,-4 -16,-20 -7,-20 C-3,-20 0,-16 0,-13 C0,-16 3,-20 7,-20 C16,-20 18,-4 0,8Z" fill="#F2545B" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'


BOCA = {
    'sorriso': f'<path d="M-22,22 Q0,44 22,22" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
    'aberta': (f'<path d="M-26,18 Q0,62 26,18 Z" fill="{INK}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
               f'<path d="M-13,36 Q0,30 13,36 Q0,46 -13,36Z" fill="#F2705B"/><path d="M-20,20 H20 L18,25 H-18Z" fill="#fff"/>'),
    'o': f'<ellipse cx="0" cy="30" rx="11" ry="14" fill="{INK}"/><ellipse cx="0" cy="35" rx="6" ry="5" fill="#F2705B"/>',
    'canto': f'<path d="M-14,30 Q8,40 24,20" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
    'triste': f'<path d="M-18,36 Q0,20 18,36" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
    'reta': f'<path d="M-14,30 H14" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>',
}

ROSTO = {
    'feliz': lambda: olho(-32, -4) + olho(32, -4) + bochechas() + BOCA['sorriso'],
    'empolgado': lambda: olho(-32, -6, 1.12, (0, -2)) + olho(32, -6, 1.12, (0, -2)) + bochechas() + BOCA['aberta'],
    'piscando': lambda: olho(-32, -4, 1, (2, 0)) + olho_feliz(32, -2) + bochechas() + BOCA['canto'],
    'focado': lambda: sobrancelha(-32, -28, 14) + sobrancelha(32, -28, -14) + olho(-32, -4, 0.95, (5, 1)) + olho(32, -4, 0.95, (5, 1)) + BOCA['canto'],
    'surpreso': lambda: sobrancelha(-32, -32, -10) + sobrancelha(32, -32, 10) + olho(-32, -4, 1.18, (0, -3)) + olho(32, -4, 1.18, (0, -3)) + BOCA['o'],
    'triste': lambda: sobrancelha(-32, -28, -16) + sobrancelha(32, -28, 16) + olho(-32, -2, 1, (0, 5)) + olho(32, -2, 1, (0, 5)) + BOCA['triste']
              + f'<path d="M-50,12 q-9,14 0,21 q9,-7 0,-21z" fill="#7FC8F8" stroke="{INK}" stroke-width="3"/>',
    'orgulhoso': lambda: olho_feliz(-32, -2) + olho_feliz(32, -2) + bochechas() + BOCA['aberta'],
    'apaixonado': lambda: coracao(-32, 0, 1.25) + coracao(32, 0, 1.25) + bochechas() + BOCA['aberta'],
    'olha-dir': lambda: olho(-32, -4, 1, (6, -1)) + olho(32, -4, 1, (6, -1)) + bochechas() + BOCA['sorriso'],
    'olha-esq': lambda: olho(-32, -4, 1, (-6, -1)) + olho(32, -4, 1, (-6, -1)) + bochechas() + BOCA['sorriso'],
    'olha-cima': lambda: olho(-32, -4, 1, (2, -7)) + olho(32, -4, 1, (2, -7)) + bochechas() + BOCA['o'],
    'dormindo': lambda: olho_fechado(-32, -2) + olho_fechado(32, -2) + bochechas() + f'<ellipse cx="0" cy="30" rx="7" ry="5" fill="{INK}"/>',
}


# ---------------- mãos flutuantes ----------------
# Desenhadas em maos.py como silhuetas únicas (contorno contínuo, vincos internos, sombra de volume).
# Desenho base = mão à DIREITA de quem olha (mão esquerda do Teco); MAO_ESP é a outra, já espelhada
# e com a sombra do lado certo (luz sempre do alto à esquerda).
from maos import MAO, MAO_ESP  # noqa: E402


def mao(pose, x, y, rot=0, s=1.0, espelho=False):
    d = (MAO_ESP if espelho else MAO)[pose]
    return f'<g transform="translate({x},{y}) rotate({rot}) scale({s})">{d}</g>'


# ---------------- Teco completo ----------------
def teco(cx, cy, r, rosto='feliz', rot=0, maos=(), faixa=True, giro=0, squash=1.0, sombra=None, cls=''):
    """maos: lista de (pose, x, y, rot, escala, espelho) em unidades do Teco (raio 100).
    sombra: y da sombra no chão (em px da peça) ou None."""
    k = r / 100
    sx, sy = 1 / squash ** 0.5, squash
    g = ''
    if sombra is not None:
        g += f'<ellipse cx="{cx}" cy="{sombra}" rx="{r*0.9:.1f}" ry="{r*0.16:.1f}" fill="{INK}" opacity=".22"/>'
    body = f'<g transform="scale({sx:.3f},{sy:.3f})">{corpo(faixa, giro)}<g>{ROSTO[rosto]()}</g></g>'
    hands = ''.join(mao(p, x, y, a, s, e) for p, x, y, a, s, e in maos)
    g += f'<g class="{cls}" transform="translate({cx},{cy}) rotate({rot}) scale({k:.4f})">{body}{hands}</g>'
    return g


# ---------------- efeitos ----------------
def rebobina(cx, cy, r, ang0=-30, arco=300, cor=B.YEL, w=None):
    """Arco de replay em volta de algo (sentido anti-horário), com a ponta de seta da marca."""
    w = w or r * 0.16
    a0 = math.radians(ang0); a1 = math.radians(ang0 - arco)
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    large = 1 if arco > 180 else 0
    d = f'M{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 0 {x1:.1f},{y1:.1f}'
    tx, ty = math.sin(a1), -math.cos(a1)  # tangente no sentido anti-horário
    nx, ny = math.cos(a1), math.sin(a1)
    hw, L = w * 1.35, w * 1.7
    tri = [(x1 + nx * hw, y1 + ny * hw), (x1 + tx * L, y1 + ty * L), (x1 - nx * hw, y1 - ny * hw)]
    pts = ' '.join(f'{px:.1f},{py:.1f}' for px, py in tri)
    return (f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{w+8:.1f}" stroke-linecap="round"/>'
            f'<polygon points="{pts}" fill="{INK}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{cor}" stroke-width="{w:.1f}" stroke-linecap="round"/>'
            f'<polygon points="{pts}" fill="{cor}" stroke="{cor}" stroke-width="2" stroke-linejoin="round"/>')


def raios(cx, cy, n=18, r=2200, c1=B.BLUE, c2='#1646B4', rot=0):
    g = f'<rect x="-5000" y="-5000" width="10000" height="10000" fill="{c1}"/>'
    for i in range(n):
        a0 = math.radians(rot + i * 360 / n); a1 = math.radians(rot + (i + 0.5) * 360 / n)
        g += f'<path d="M{cx},{cy} L{cx+r*math.cos(a0):.0f},{cy+r*math.sin(a0):.0f} L{cx+r*math.cos(a1):.0f},{cy+r*math.sin(a1):.0f}Z" fill="{c2}"/>'
    return g


def brilho(x, y, s=1, c=B.YEL):
    return (f'<path transform="translate({x},{y}) scale({s})" d="M0,-30 C4,-6 6,-4 30,0 C6,4 4,6 0,30 C-4,6 -6,4 -30,0 C-6,-4 -4,-6 0,-30Z" '
            f'fill="{c}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>')


def confete(x, y, rot, c, w=22, h=10):
    return f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="3" fill="{c}" transform="rotate({rot} {x} {y})"/>'


def linhas_vel(x, y, n=3, comp=90, gap=26, ang=0, cor='#fff', w=10):
    g = f'<g transform="rotate({ang} {x} {y})">'
    for i in range(n):
        L = comp * (1 - 0.22 * (i % 2))
        g += f'<path d="M{x},{y+i*gap} h{-L:.0f}" stroke="{cor}" stroke-width="{w}" stroke-linecap="round"/>'
    return g + '</g>'
