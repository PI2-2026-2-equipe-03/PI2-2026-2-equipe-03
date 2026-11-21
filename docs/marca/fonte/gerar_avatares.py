from caminhos import *  # noqa
"""Avatares de usuário: a "galera da quadra".

O banco não guarda foto de perfil, então cada usuário recebe um destes personagens, escolhido de forma
determinística (ver front-kit/src/components/avatar-usuario.tsx). Cada um é um objeto do universo do
repeteco (vôlei, praia, gravação, replay) com o mesmo rosto do Teco: olho branco com pupila e brilho,
sorriso de traço redondo e bochecha coral. Assim a turma parece da mesma família sem ser o Teco repetido.

Regras de desenho (para ficarem legíveis a 32 px, o tamanho do header):
- canvas 256, recorte circular; o personagem ocupa ~70% do círculo e pode ser cortado embaixo (busto);
- contorno único em INK, 6 px (vira ~0,75 px a 32 px); detalhes internos 3-4 px;
- fundo de uma cor por avatar + uma textura em baixa opacidade que conta onde ele vive (quadra, areia, raios...);
- nenhuma peça encosta na borda do círculo, exceto o que sai por baixo (poste, corpo).
"""
import os, math, json, brand as B
from teco import INK

OUT = MARCA + '/avatares'
os.makedirs(OUT + '/svg', exist_ok=True)
W = 6          # contorno
C = 128        # centro
CORAL = '#F28C6B'; VERMELHO = '#F2545B'; CEU = '#7FC8F8'; VERDE = '#2BB673'; AREIA = '#F6DB8B'; AZUL_MEDIO = '#3D6FD8'
CREME = '#FFF6DF'; LARANJA = '#FF9F43'


# ---------------- rosto (mesma linguagem do Teco, em escala 256) ----------------
def olho(x, y, s=1.0, look=(0, 0)):
    lx, ly = look
    return (f'<ellipse cx="{x}" cy="{y}" rx="{10*s:.1f}" ry="{12.5*s:.1f}" fill="#fff" stroke="{INK}" stroke-width="{3.6*s:.1f}"/>'
            f'<circle cx="{x+lx*s:.1f}" cy="{y+2*s+ly*s:.1f}" r="{5.6*s:.1f}" fill="{INK}"/>'
            f'<circle cx="{x+lx*s-1.8*s:.1f}" cy="{y-0.6*s+ly*s:.1f}" r="{2*s:.1f}" fill="#fff"/>')


def olho_feliz(x, y, w=10, sw=5):
    return f'<path d="M{x-w},{y+3} Q{x},{y-10} {x+w},{y+3}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>'


def sorriso(cx, cy, w=14, sw=5):
    return f'<path d="M{cx-w},{cy} Q{cx},{cy+w*0.85} {cx+w},{cy}" fill="none" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>'


def boca_aberta(cx, cy, w=14):
    return (f'<path d="M{cx-w},{cy} Q{cx},{cy+w*1.5} {cx+w},{cy} Z" fill="{INK}" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'
            f'<path d="M{cx-w*0.48:.1f},{cy+w*0.62:.1f} Q{cx},{cy+w*0.38:.1f} {cx+w*0.48:.1f},{cy+w*0.62:.1f} Q{cx},{cy+w*0.86:.1f} {cx-w*0.48:.1f},{cy+w*0.62:.1f}Z" fill="#F2705B"/>')


def bochecha(x, y, s=1.0):
    return f'<ellipse cx="{x}" cy="{y}" rx="{8.5*s:.1f}" ry="{4.8*s:.1f}" fill="{CORAL}" opacity=".5"/>'


def sobrancelha(x0, y0, x1, y1, sw=4.5):
    return f'<path d="M{x0},{y0} L{x1},{y1}" stroke="{INK}" stroke-width="{sw}" stroke-linecap="round"/>'


def rosto(xe, ye, gap, ym, s=1.0, boca='sorriso', bw=12, look=(0, 0), bochechas=True):
    g = olho(xe - gap, ye, s, look) + olho(xe + gap, ye, s, look)
    if bochechas:
        g += bochecha(xe - gap - 6 * s, ye + 19 * s, s) + bochecha(xe + gap + 6 * s, ye + 19 * s, s)
    g += boca_aberta(xe, ym, bw) if boca == 'aberta' else sorriso(xe, ym, bw)
    return g


def contorno(d, fill, sw=W, extra=''):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{extra}/>'


def brilho(x, y, rx, ry, rot=-35, op=.7):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" transform="rotate({rot} {x} {y})" fill="#fff" opacity="{op}"/>'


def faisca(x, y, s=1.0, c='#fff', op=1.0):
    return (f'<path transform="translate({x},{y}) scale({s})" d="M0,-10 C1.4,-2 2,-1.4 10,0 C2,1.4 1.4,2 0,10 C-1.4,2 -2,1.4 -10,0 C-2,-1.4 -1.4,-2 0,-10Z" '
            f'fill="{c}" opacity="{op}"/>')


# ---------------- fundos ----------------
def fundo(cor, textura, tinta='#fff', op=.16):
    g = f'<circle cx="{C}" cy="{C}" r="128" fill="{cor}"/>'
    t = ''
    if textura == 'quadra':   # linhas de quadra em perspectiva (o chão onde a câmera grava)
        t = (f'<path d="M-10,196 L266,196 M40,256 L84,150 M216,256 L172,150 M84,150 H172 M18,232 H238" fill="none" stroke="{tinta}" stroke-width="5" opacity="{op}"/>')
    elif textura == 'raios':
        for i in range(12):
            a0 = math.radians(i * 30 - 6); a1 = math.radians(i * 30 + 6)
            t += f'<path d="M{C},{C} L{C+200*math.cos(a0):.1f},{C+200*math.sin(a0):.1f} L{C+200*math.cos(a1):.1f},{C+200*math.sin(a1):.1f}Z" fill="{tinta}" opacity="{op}"/>'
    elif textura == 'pontos':
        for yy in range(12, 256, 28):
            for xx in range(12 + (14 if (yy // 28) % 2 else 0), 256, 28):
                t += f'<circle cx="{xx}" cy="{yy}" r="3.4" fill="{tinta}" opacity="{op}"/>'
    elif textura == 'rede':   # malha da rede, em diagonal
        # um path só, e só linhas que cruzam o canvas (linha inteira fora do quadro derruba o resvg)
        d = ''.join(f'M{k},0 L{k+256},256 M{k+256},0 L{k},256 ' for k in range(-242, 256, 22))
        t += f'<path d="{d.strip()}" fill="none" stroke="{tinta}" stroke-width="2.4" opacity="{op}"/>'
    elif textura == 'estrelas':
        for x, y, s in ((40, 70, .9), (212, 58, 1.1), (226, 150, .7), (30, 160, .6), (66, 222, .8), (196, 218, .6), (120, 30, .6)):
            t += faisca(x, y, s, tinta, op * 3.5)
    elif textura == 'confete':
        cores = [B.YEL, '#fff', CORAL, CEU]
        for i, (x, y, r) in enumerate(((36, 80, 20), (220, 70, -30), (46, 170, 40), (214, 168, 12), (90, 34, -10), (168, 30, 50), (24, 120, 70), (234, 112, -60))):
            t += f'<rect x="{x-5}" y="{y-2.5}" width="10" height="5" rx="1.5" transform="rotate({r} {x} {y})" fill="{cores[i % 4]}" opacity=".9"/>'
    elif textura == 'areia':  # céu + faixa de areia embaixo
        t = B.P(B.wave_path(256, 256, 214, 6, 0.2, 0.7), B.YEL) + B.P(B.wave_path(256, 256, 234, 4, 0.6, 1.4), B.YEL_DK)
    elif textura == 'mar':
        t = (f'<path d="{B.wave_path(256, 256, 208, 6, 0.3, 0.9)}" fill="{CEU}"/>'
             f'<path d="{B.wave_path(256, 256, 226, 5, 0.7, 1.6)}" fill="#5BB0EC"/>')
    elif textura == 'listras':  # cortina de cinema
        for x in range(-4, 260, 26):
            t += f'<rect x="{x}" y="0" width="12" height="256" fill="{tinta}" opacity="{op}"/>'
    return g + t


# ---------------- personagens ----------------
def bola_saque():
    """Bola de vôlei tricolor (azul, amarelo, branco) com faixa na testa: o saque."""
    cx, cy, r = 128, 140, 84
    clip = '<clipPath id="bs"><circle cx="128" cy="140" r="84"/></clipPath>'
    # gomos curvos nas laterais, como numa bola de vôlei tricolor: azul à esquerda, amarelo embaixo à direita;
    # o rosto fica no gomo branco do meio
    faixas = [('M70,40 C88,100 78,170 30,232', B.BLUE), ('M262,146 C204,146 176,186 170,262', B.YEL)]
    g = clip + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/><g clip-path="url(#bs)">'
    for d, cor in faixas:   # faixa com borda: traço INK largo por baixo, cor por cima
        g += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="40" stroke-linecap="round"/><path d="{d}" fill="none" stroke="{cor}" stroke-width="32" stroke-linecap="round"/>'
    g += f'<path d="M44,176 a84,84 0 0 0 160,22 a90,90 0 0 1 -160,-22Z" fill="{INK}" opacity=".10"/>'
    # faixa (headband) coral acompanhando a curva da bola
    g += f'<path d="M36,106 Q128,70 220,106" fill="none" stroke="{INK}" stroke-width="28"/><path d="M36,106 Q128,70 220,106" fill="none" stroke="{VERMELHO}" stroke-width="21"/>'
    g += f'<path d="M42,102 Q128,68 214,102" fill="none" stroke="#fff" stroke-width="3" stroke-dasharray="1 9" stroke-linecap="round" opacity=".9"/>'
    g += '</g>'
    # pontas da faixa saindo atrás da cabeça, à direita
    g += contorno('M206,96 C222,86 236,88 242,80 C242,94 232,104 214,108Z', VERMELHO, 5)
    g += contorno('M210,104 C228,104 238,112 246,108 C240,122 226,124 212,116Z', VERMELHO, 5)
    g += brilho(150, 74, 12, 5, -10, .6)
    g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="{W}"/>'
    g += sobrancelha(98, 126, 114, 131) + sobrancelha(158, 126, 142, 131)
    g += rosto(128, 150, 20, 178, 1.0, 'sorriso', 14)
    return g


def sol():
    """Sol de praia de óculos escuros: o vôlei de areia."""
    g = ''
    for i in range(12):
        a = math.radians(i * 30 + 15); a0 = a - 0.16; a1 = a + 0.16
        p = lambda ang, rr: f'{128+rr*math.cos(ang):.1f},{118+rr*math.sin(ang):.1f}'
        g += contorno(f'M{p(a0, 60)} L{p(a, 102 if i % 2 else 92)} L{p(a1, 60)}Z', B.YEL, 5)
    g += f'<circle cx="128" cy="118" r="66" fill="{B.YEL}" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<path d="M86,150 a66,66 0 0 0 100,6 a70,70 0 0 1 -100,-6Z" fill="{B.YEL_DK}" opacity=".55"/>'
    g += brilho(92, 82, 12, 6)
    # óculos
    lente = lambda x: contorno(f'M{x-22},100 H{x+22} V110 C{x+22},128 {x+10},132 {x},132 C{x-10},132 {x-22},128 {x-22},110Z', INK, 5)
    g += lente(102) + lente(154)
    g += f'<path d="M124,104 Q128,98 132,104" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
    g += f'<path d="M80,102 L64,96 M176,102 L192,96" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'
    g += f'<path d="M88,108 l10,-6 M140,108 l10,-6" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".85"/>'
    g += bochecha(84, 140) + bochecha(172, 140)
    g += boca_aberta(128, 144, 20)
    return g


def rec():
    """Câmera da quadra: a lente é um olho só, com a luz REC acesa."""
    g = f'<rect x="116" y="186" width="24" height="90" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{W}"/>'
    g += contorno('M150,70 H190 V58 a6,6 0 0 0 -6,-6 H156 a6,6 0 0 0 -6,6Z', B.BLUE_DK, 5)
    g += f'<rect x="46" y="68" width="164" height="122" rx="26" fill="{B.BLUE}" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<path d="M52,160 C80,176 170,180 204,160 V164 a26,26 0 0 1 -26,24 H78 a26,26 0 0 1 -26,-24Z" fill="{B.BLUE_DK}" opacity=".6"/>'
    g += f'<path d="M60,90 C64,80 72,76 82,76" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" opacity=".5"/>'
    # lente / olho
    g += f'<circle cx="128" cy="124" r="44" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<circle cx="128" cy="124" r="33" fill="{B.YEL}" stroke="{INK}" stroke-width="4"/>'
    g += f'<circle cx="130" cy="127" r="21" fill="{INK}"/>'
    g += f'<circle cx="122" cy="118" r="7" fill="#fff"/><circle cx="138" cy="134" r="3" fill="#fff" opacity=".8"/>'
    g += f'<path d="M98,98 Q128,82 158,98" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round" opacity="0"/>'
    # REC
    g += f'<circle cx="68" cy="88" r="8" fill="{VERMELHO}" stroke="{INK}" stroke-width="3.5"/>'
    g += f'<circle cx="68" cy="88" r="13" fill="none" stroke="{VERMELHO}" stroke-width="2.5" opacity=".55"/>'
    g += sorriso(128, 176, 11, 4.5)
    g += bochecha(74, 168) + bochecha(182, 168)
    return g


def botao():
    """O botão da quadra, feliz da vida por ter sido apertado."""
    g = f'<rect x="116" y="206" width="24" height="70" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{W}"/>'
    # raios de clique
    for d in ('M64,66 l-16,-16', 'M128,50 v-22', 'M192,66 l16,-16'):
        g += f'<path d="{d}" stroke="{INK}" stroke-width="13" stroke-linecap="round"/><path d="{d}" stroke="{B.YEL}" stroke-width="7" stroke-linecap="round"/>'
    g += f'<rect x="52" y="108" width="152" height="106" rx="30" fill="#fff" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<path d="M58,184 C90,200 166,202 198,184 V186 a28,28 0 0 1 -28,26 H86 a28,28 0 0 1 -28,-26Z" fill="{B.LILAC}" opacity=".8"/>'
    # cúpula amarela (cilindro baixo + topo)
    g += contorno('M76,96 V110 A52,17 0 0 0 180,110 V96', B.YEL_DK, 5)
    g += f'<ellipse cx="128" cy="96" rx="52" ry="17" fill="{B.YEL}" stroke="{INK}" stroke-width="5"/>'
    g += brilho(106, 92, 13, 4.5, -8, .8)
    g += olho_feliz(104, 150, 11, 5.5) + olho_feliz(152, 150, 11, 5.5)
    g += bochecha(86, 168) + bochecha(170, 168)
    g += boca_aberta(128, 170, 16)
    return g


def apito():
    """Apito do juiz, bochechas cheias de ar."""
    g = contorno('M70,170 C40,200 44,250 70,280', 'none', 9) + f'<path d="M70,170 C40,200 44,250 70,280" fill="none" stroke="{CORAL}" stroke-width="4" stroke-linecap="round"/>'
    g = (f'<path d="M66,168 C34,196 40,250 64,282" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
         f'<path d="M66,168 C34,196 40,250 64,282" fill="none" stroke="{B.YEL}" stroke-width="5" stroke-linecap="round"/>')
    g += f'<circle cx="68" cy="164" r="9" fill="none" stroke="{INK}" stroke-width="5"/>'
    corpo = 'M108,90 H200 a10,10 0 0 1 10,10 V128 a10,10 0 0 1 -10,10 H161.5 A56,56 0 1 1 108,90 Z'
    g += contorno(corpo, '#fff')
    g += f'<path d="M66,186 A56,56 0 0 0 158,186 A60,60 0 0 1 66,186Z" fill="{B.LILAC}"/>'
    g += f'<path d="{corpo}" fill="none" stroke="{INK}" stroke-width="{W}" stroke-linejoin="round"/>'
    g += f'<rect x="150" y="100" width="22" height="9" rx="4.5" fill="{INK}"/>'   # fenda
    g += brilho(80, 120, 10, 5)
    for d in ('M158,80 l-6,-20', 'M176,78 l6,-22', 'M194,84 l16,-16'):
        g += f'<path d="{d}" stroke="{B.YEL}" stroke-width="7" stroke-linecap="round"/>'
    g += olho(92, 140, .95, (2, 0)) + olho(128, 140, .95, (2, 0))
    g += sobrancelha(82, 118, 100, 124) + sobrancelha(138, 118, 120, 124)
    g += f'<ellipse cx="110" cy="174" rx="7" ry="8" fill="{INK}"/>'
    g += f'<circle cx="78" cy="166" r="10" fill="{CORAL}" opacity=".55"/><circle cx="142" cy="166" r="10" fill="{CORAL}" opacity=".55"/>'
    return g


def claquete():
    """Claquete de cinema: o replay entrando em cena."""
    g = f'<rect x="50" y="104" width="156" height="114" rx="14" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{W}"/>'
    # barra fixa
    def listrada(x, y, w, h, rot=0, oid='l'):
        cid = f'cl{oid}'
        s = f'<g transform="rotate({rot} {x} {y+h})"><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5"/></clipPath>'
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#fff"/><g clip-path="url(#{cid})">'
        for k in range(-1, 9):
            xx = x + k * 24
            s += f'<path d="M{xx},{y+h} L{xx+12},{y} H{xx+24} L{xx+12},{y+h}Z" fill="{B.BLUE}"/>'
        s += f'</g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="none" stroke="{INK}" stroke-width="5"/></g>'
        return s
    g += listrada(50, 86, 156, 22, 0, 'a')
    g += listrada(50, 62, 156, 22, -16, 'b')
    g += f'<circle cx="58" cy="105" r="5" fill="{B.YEL}" stroke="{INK}" stroke-width="3"/>'
    # campos da claquete
    g += f'<path d="M64,196 H112 M128,196 H192" stroke="#fff" stroke-width="3" opacity=".35" stroke-linecap="round"/>'
    g += olho(102, 146, 1.3) + olho(154, 146, 1.3)
    g += bochecha(80, 174, 1.1) + bochecha(176, 174, 1.1)
    g += boca_aberta(128, 172, 16)
    return g


def ampulheta():
    """Ampulheta dos 30 segundos de cada replay."""
    g = ''
    vidro = 'M88,70 C88,112 120,118 120,132 C120,146 88,152 88,194 H168 C168,152 136,146 136,132 C136,118 168,112 168,70 Z'
    g += f'<path d="M78,70 V194 M178,70 V194" stroke="{INK}" stroke-width="13" stroke-linecap="round"/><path d="M78,70 V194 M178,70 V194" stroke="{B.BLUE_DK}" stroke-width="6" stroke-linecap="round"/>'
    g += f'<clipPath id="amp"><path d="{vidro}"/></clipPath><path d="{vidro}" fill="#fff" opacity=".92"/>'
    g += '<g clip-path="url(#amp)">'
    g += f'<path d="M80,112 C100,118 112,120 128,122 C144,120 156,118 176,112 V140 H80Z" fill="{B.YEL}"/>'   # areia de cima
    g += f'<path d="M127,128 V176" stroke="{B.YEL}" stroke-width="3.5"/>'
    g += f'<path d="M80,194 V178 C100,166 116,156 128,154 C140,156 156,166 176,178 V194Z" fill="{B.YEL}"/>'
    g += f'<path d="M80,194 V186 C100,178 156,178 176,186 V194Z" fill="{B.YEL_DK}"/>'
    g += '</g>'
    g += f'<path d="{vidro}" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    g += f'<path d="M98,78 C98,94 104,102 110,106" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".9"/>'
    g += f'<rect x="64" y="52" width="128" height="20" rx="8" fill="{B.BLUE}" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<rect x="64" y="192" width="128" height="20" rx="8" fill="{B.BLUE}" stroke="{INK}" stroke-width="{W}"/>'
    g += olho(114, 90, .82, (0, 1)) + olho(142, 90, .82, (0, 1))
    g += sorriso(128, 104, 7, 4)
    d30 = B.text('30s', 15, 0, 0, align='center')[0]
    g += f'<path transform="translate(128,207)" d="{d30}" fill="#fff"/>'
    return g


def taca():
    """Taça de campeão."""
    g = ''
    for side in (-1, 1):
        d = f'M{128+side*48},80 C{128+side*86},78 {128+side*84},128 {128+side*40},134'
        g += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="18" stroke-linecap="round"/><path d="{d}" fill="none" stroke="{B.YEL}" stroke-width="8" stroke-linecap="round"/>'
    g += contorno('M116,158 H140 L144,184 H112Z', B.YEL_DK, 5)
    g += contorno('M84,186 H172 a6,6 0 0 1 6,6 V214 H78 V192 a6,6 0 0 1 6,-6Z', B.BLUE)
    g += f'<rect x="104" y="194" width="48" height="10" rx="3" fill="{B.YEL}" stroke="{INK}" stroke-width="3"/>'
    copo = 'M70,62 H186 V92 C186,138 160,162 128,162 C96,162 70,138 70,92 Z'
    g += contorno(copo, B.YEL)
    g += f'<clipPath id="tc"><path d="{copo}"/></clipPath><path clip-path="url(#tc)" d="M150,60 C162,110 156,146 120,166 H200 V60Z" fill="{B.YEL_DK}" opacity=".7"/>'
    g += f'<path d="{copo}" fill="none" stroke="{INK}" stroke-width="{W}" stroke-linejoin="round"/>'
    g += f'<path d="M84,74 V100 C84,112 88,122 94,130" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".75"/>'
    g += f'<path d="M66,62 H190" stroke="{INK}" stroke-width="{W}" stroke-linecap="round"/>'
    g += rosto(128, 100, 22, 124, 1.0, 'aberta', 15)
    g += faisca(210, 60, 1.3, '#fff') + faisca(48, 150, .9, B.YEL)
    return g


def tenis():
    """Tênis de quadra, pronto pra pular."""
    g = '<g transform="rotate(-10 128 150)">'
    g += f'<path d="M30,196 l-14,6 M34,176 l-18,-2 M40,158 l-14,-8" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".8"/>'
    caba = 'M46,180 C44,142 52,104 70,92 C80,86 96,88 104,96 C118,112 132,124 156,130 C190,138 214,148 216,178 Z'
    g += contorno(caba, B.BLUE)
    g += f'<clipPath id="tn"><path d="{caba}"/></clipPath><g clip-path="url(#tn)">'
    g += f'<path d="M192,134 C204,140 214,148 222,160 V184 H186 C196,170 198,150 192,134Z" fill="{B.YEL}"/>'      # biqueira
    g += f'<path d="M40,120 C56,124 64,150 60,184 H30Z" fill="{B.YEL}"/>'                # calcanhar
    g += f'<path d="M40,170 H220 V184 H40Z" fill="{B.BLUE_DK}" opacity=".5"/>'
    g += '</g>'
    g += f'<path d="{caba}" fill="none" stroke="{INK}" stroke-width="{W}" stroke-linejoin="round"/>'
    g += f'<path d="M66,92 C74,82 92,82 100,92" fill="none" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>'  # boca do tênis
    for i, (x, y) in enumerate(((104, 104), (116, 114), (128, 122))):
        g += f'<path d="M{x-8},{y+8} L{x+8},{y-6}" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    g += contorno('M38,178 H218 a8,8 0 0 1 8,8 V194 a10,10 0 0 1 -10,10 H44 a10,10 0 0 1 -10,-10 V184 a6,6 0 0 1 4,-6Z', '#fff')
    g += f'<path d="M48,192 H214" stroke="{B.LILAC}" stroke-width="4" stroke-linecap="round"/>'
    g += olho(146, 152, .9, (2, 0)) + olho(172, 155, .9, (2, 0))
    g += sorriso(162, 170, 7, 4)
    g += '</g>'
    return g


def coco():
    """Coco verde de canudinho: o intervalo na praia."""
    g = ''
    g += f'<path d="M150,84 L178,30" stroke="{INK}" stroke-width="13" stroke-linecap="round"/>'
    g += f'<path d="M150,84 L178,30" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
    g += f'<path d="M150,84 L178,30" stroke="{CORAL}" stroke-width="7" stroke-dasharray="6 7"/>'
    # guarda-sol de palito
    g += f'<path d="M96,94 L82,42" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>'
    g += contorno('M52,54 C60,30 98,22 114,42 C104,40 98,44 94,50 C88,44 78,44 72,52 C66,48 58,50 52,54Z', B.YEL, 4.5)
    g += f'<path d="M83,33 C80,42 76,48 72,52 M83,33 C88,40 92,46 94,50" fill="none" stroke="{INK}" stroke-width="3"/>'
    g += f'<circle cx="128" cy="150" r="76" fill="{VERDE}" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<clipPath id="co"><circle cx="128" cy="150" r="76"/></clipPath>'
    g += f'<path clip-path="url(#co)" d="M52,150 a76,76 0 0 0 152,0 a80,80 0 0 1 -6,30 a76,76 0 0 1 -146,-30Z M60,180 C90,226 170,226 200,174 V240 H56Z" fill="#1E8F57" opacity=".75"/>'
    g += f'<circle cx="128" cy="150" r="76" fill="none" stroke="{INK}" stroke-width="{W}"/>'
    g += f'<ellipse cx="128" cy="90" rx="40" ry="13" fill="{CREME}" stroke="{INK}" stroke-width="5"/>'
    g += f'<ellipse cx="128" cy="91" rx="24" ry="6" fill="#E9F3D0"/>'
    g += brilho(86, 128, 11, 6)
    g += rosto(128, 152, 22, 178, 1.0, 'sorriso', 14)
    return g


def placar():
    """Placar da quadra marcando o ponto."""
    g = f'<path d="M84,190 V276 M172,190 V276" stroke="{INK}" stroke-width="16" stroke-linecap="round"/><path d="M84,190 V276 M172,190 V276" stroke="{B.BLUE_DK}" stroke-width="8"/>'
    g += f'<rect x="40" y="58" width="176" height="138" rx="24" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="{W}"/>'
    for x in (58, 140):
        g += f'<rect x="{x}" y="74" width="58" height="50" rx="10" fill="{INK}"/>'
    for txt, x in (('21', 87), ('19', 169)):
        d = B.text(txt, 40, 0, 0, align='center')[0]
        g += f'<path transform="translate({x},114)" d="{d}" fill="{B.YEL}"/>'
    g += f'<circle cx="128" cy="90" r="4" fill="{B.YEL}"/><circle cx="128" cy="106" r="4" fill="{B.YEL}"/>'
    g += olho(106, 150, .95) + olho(150, 150, .95)
    g += bochecha(84, 170) + bochecha(172, 170)
    g += sorriso(128, 170, 12, 4.5)
    g += f'<path d="M50,64 C54,62 62,62 70,62" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity=".4"/>'
    return g


def pipoca():
    """Balde de pipoca para assistir o replay."""
    g = ''
    balde = 'M64,112 H192 L178,232 H78 Z'
    milho = [(78, 104, 18), (102, 88, 21), (130, 80, 22), (158, 88, 21), (182, 104, 18), (90, 70, 15), (144, 60, 16), (118, 58, 14), (170, 72, 13)]
    for x, y, r in milho:
        g += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CREME}" stroke="{INK}" stroke-width="5"/>'
    for x, y, r in milho:
        g += f'<circle cx="{x}" cy="{y}" r="{r-2.5}" fill="{CREME}"/>'
    for x, y in ((96, 82), (150, 66), (170, 98), (122, 70)):
        g += f'<circle cx="{x}" cy="{y}" r="4.5" fill="{B.YEL}" opacity=".9"/>'
    g += f'<clipPath id="pp"><path d="{balde}"/></clipPath><path d="{balde}" fill="#fff"/><g clip-path="url(#pp)">'
    for x in (52, 82, 166, 196):
        g += f'<path d="M{x},100 L{x+6},240 H{x+20} L{x+14},100Z" fill="{VERMELHO}"/>'
    g += f'<path d="M64,206 H192 V240 H64Z" fill="{INK}" opacity=".08"/>'
    g += '</g>'
    g += f'<path d="{balde}" fill="none" stroke="{INK}" stroke-width="{W}" stroke-linejoin="round"/>'
    g += f'<rect x="56" y="104" width="144" height="16" rx="6" fill="#fff" stroke="{INK}" stroke-width="5"/>'
    g += olho(108, 152, .95, (0, -2)) + olho(148, 152, .95, (0, -2))
    g += bochecha(96, 176, .8) + bochecha(160, 176, .8)
    g += boca_aberta(128, 178, 11)
    # pipoca voando
    g += f'<circle cx="214" cy="56" r="11" fill="{CREME}" stroke="{INK}" stroke-width="4"/><circle cx="44" cy="62" r="8" fill="{CREME}" stroke="{INK}" stroke-width="4"/>'
    return g


# nome do arquivo: (nome exibido, descrição, fundo, textura, desenho)
AVATARES = {
    'saque':     ('Saque', 'bola de vôlei tricolor com faixa na testa', LARANJA, 'quadra', bola_saque),
    'sol':       ('Sol', 'sol de praia de óculos escuros', CEU, 'areia', sol),
    'rec':       ('Rec', 'câmera da quadra gravando', B.YEL, 'raios', rec),
    'botao':     ('Botão', 'o botão da quadra, recém-apertado', B.ICE, 'pontos', botao),
    'apito':     ('Apito', 'apito do juiz, de bochecha cheia', CORAL, 'raios', apito),
    'claquete':  ('Claquete', 'claquete do replay entrando em cena', B.LILAC, 'pontos', claquete),
    'ampulheta': ('Ampulheta', 'os 30 segundos de cada replay', B.BLUE_DK, 'estrelas', ampulheta),
    'taca':      ('Taça', 'taça de campeão', B.BLUE, 'confete', taca),
    'tenis':     ('Tênis', 'tênis de quadra pronto pra pular', VERDE, 'quadra', tenis),
    'coco':      ('Coco', 'coco verde no intervalo da praia', AREIA, 'mar', coco),
    'placar':    ('Placar', 'placar marcando o ponto', AZUL_MEDIO, 'rede', placar),
    'pipoca':    ('Pipoca', 'pipoca para assistir o replay', VERMELHO, 'listras', pipoca),
}
TINTA = {'botao': B.BLUE, 'claquete': B.BLUE, 'coco': '#fff', 'rec': '#fff'}
OPAC = {'botao': .14, 'claquete': .22, 'rec': .28, 'sol': .2}


def avatar(nome):
    _, _, cor, textura, fn = AVATARES[nome]
    corpo = fundo(cor, textura, TINTA.get(nome, '#fff'), OPAC.get(nome, .14)) + fn()
    # ids únicos por avatar (vários podem aparecer na mesma página inline)
    corpo = corpo.replace('id="', f'id="{nome}-').replace('url(#', f'url(#{nome}-')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" width="256" height="256"><title>{AVATARES[nome][0]}</title>'
            f'<clipPath id="{nome}-av"><circle cx="128" cy="128" r="128"/></clipPath><g clip-path="url(#{nome}-av)">{corpo}</g></svg>\n')


for k in AVATARES:
    open(f'{OUT}/svg/{k}.svg', 'w').write(avatar(k))

# prévia: grade 4x3 com nome e as 3 variações de papel
cols, cel = 4, 300
linhas = math.ceil(len(AVATARES) / cols)
pw, ph = cols * cel + 80, linhas * (cel + 40) + 200
prev = f'<rect width="{pw}" height="{ph}" fill="{B.ICE}"/>'
prev += B.P(B.text('a galera da quadra', 56, 40, 96, track=-0.02)[0], B.BLUE_DEEP)
prev += B.P(B.text('avatares de usuário · um por pessoa, sorteado pelo id', 26, 40, 140, w='md')[0], B.BLUE)
for i, k in enumerate(AVATARES):
    x = 40 + (i % cols) * cel + 30; y = 190 + (i // cols) * (cel + 40)
    svg = avatar(k).split('>', 1)[1].rsplit('</svg>', 1)[0]
    prev += f'<g transform="translate({x},{y}) scale({220/256})">{svg}</g>'
    prev += B.P(B.text(AVATARES[k][0], 30, x + 110, y + 262, align='center')[0], B.BLUE_DEEP)
open(f'{OUT}/avatares-preview.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {pw} {ph}" width="{pw}" height="{ph}">{prev}</svg>\n')
open(f'{OUT}/indice.json', 'w').write(json.dumps({k: {'nome': v[0], 'descricao': v[1], 'fundo': v[2]} for k, v in AVATARES.items()}, ensure_ascii=False, indent=2))
print(len(AVATARES), 'avatares')
