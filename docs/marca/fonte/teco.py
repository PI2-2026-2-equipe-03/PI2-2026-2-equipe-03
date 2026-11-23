from caminhos import *  # noqa
"""Teco, o mascote (bola de vôlei amarela), e peças de desenho compartilhadas por emojis e ilustrações."""
import math, brand as B
INK=B.BLUE_DEEP
def ball(cx=256,cy=272,r=168,rot=0,squash=1.0,shade=True,borda=True):
    """Teco: bola de vôlei amarela com costuras azuis."""
    sx=1/squash**0.5; sy=squash
    # costuras começam e terminam FORA da bola (cortadas pelo clip), entrando quase perpendiculares à borda:
    # assim nenhuma ponta fica rente ao contorno parecendo um traço escapando do personagem.
    seams=[f'M{-r*1.08:.0f},{-r*0.4:.0f} C{-r*0.35:.0f},{-r*0.3:.0f} {r*0.05:.0f},{r*0.15:.0f} {-r*0.12:.0f},{r*1.1:.0f}',
           f'M{-r*0.52:.0f},{-r*1.02:.0f} C{r*0.1:.0f},{-r*0.55:.0f} {r*0.55:.0f},{-r*0.35:.0f} {r*1.1:.0f},{-r*0.1:.0f}',
           f'M{r*1.0:.0f},{r*0.56:.0f} C{r*0.4:.0f},{r*0.32:.0f} {-r*0.1:.0f},{r*0.45:.0f} {-r*0.88:.0f},{r*0.8:.0f}']
    g=f'<g transform="translate({cx},{cy}) scale({sx:.3f},{sy:.3f})">'
    if borda: g+=f'<circle r="{r+18}" fill="#fff"/>'  # borda de figurinha
    g+=f'<clipPath id="bc{cx}{cy}{r}"><circle r="{r}"/></clipPath><circle r="{r}" fill="{B.YEL}"/>'
    g+=f'<g clip-path="url(#bc{cx}{cy}{r})" transform="rotate({rot})">'
    if shade:  # meia-lua de sombra embaixo à direita (sem anel: a borda interna dele virava um traço solto)
        g+=(f'<path d="M{-r},0 a{r},{r} 0 1,0 {2*r},0 a{r},{r} 0 1,0 {-2*r},0Z M{-r*1.07:.1f},{-r*0.12:.1f} a{r*0.95:.1f},{r*0.95:.1f} 0 1,1 {r*1.9:.1f},0 a{r*0.95:.1f},{r*0.95:.1f} 0 1,1 {-r*1.9:.1f},0Z" '
            f'fill="{B.YEL_DK}" fill-rule="evenodd" opacity=".55"/>')
    g+=''.join(f'<path d="{d}" fill="none" stroke="#B98600" stroke-width="{r*0.055:.1f}" stroke-linecap="round" opacity=".8"/>' for d in seams)
    g+='</g>'
    g+=f'<ellipse cx="{-r*0.42}" cy="{-r*0.5}" rx="{r*0.2}" ry="{r*0.11}" transform="rotate(-35 {-r*0.42} {-r*0.5})" fill="#fff" opacity=".75"/>'
    g+=f'<circle r="{r}" fill="none" stroke="{INK}" stroke-width="{r*0.075:.1f}"/></g>'
    return g
def eye(x,y,s=1.0,look=(0,0)):
    return (f'<ellipse cx="{x}" cy="{y}" rx="{24*s}" ry="{30*s}" fill="#fff" stroke="{INK}" stroke-width="7"/>'
            f'<circle cx="{x+look[0]*s}" cy="{y+4*s+look[1]*s}" r="{13*s}" fill="{INK}"/><circle cx="{x+look[0]*s-4*s}" cy="{y-2*s+look[1]*s}" r="{4.5*s}" fill="#fff"/>')
def closed_eye(x,y,up=True,w=26):
    d=f'M{x-w},{y+8} Q{x},{y-22} {x+w},{y+8}' if up else f'M{x-w},{y-6} Q{x},{y+20} {x+w},{y-6}'
    return f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
def blush(x,y): return f'<ellipse cx="{x}" cy="{y}" rx="22" ry="12" fill="#F28C6B" opacity=".45"/>'
def mouth_smile(cx,cy,w=46,open_=False):
    if open_:
        return (f'<path d="M{cx-w},{cy} Q{cx},{cy+w*1.5} {cx+w},{cy} Z" fill="{INK}" stroke="{INK}" stroke-width="8" stroke-linejoin="round"/>'
                f'<path d="M{cx-w*0.5},{cy+w*0.62} Q{cx},{cy+w*0.4} {cx+w*0.5},{cy+w*0.62} Q{cx},{cy+w*0.85} {cx-w*0.5},{cy+w*0.62}Z" fill="#F2705B"/>')
    return f'<path d="M{cx-w},{cy} Q{cx},{cy+w*0.9} {cx+w},{cy}" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>'
def word(s,size,x,y,fill=B.YEL,stroke=B.BLUE_DEEP,rot=0,align='center'):
    d=B.text(s,size,0,0,track=-0.02,align=align)[0]
    return (f'<g transform="translate({x},{y}) rotate({rot})"><path d="{d}" fill="#fff" stroke="#fff" stroke-width="{size*0.32:.0f}" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="{stroke}" stroke="{stroke}" stroke-width="{size*0.16:.0f}" stroke-linejoin="round" transform="translate(0,{size*0.05:.0f})"/>'
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{size*0.1:.0f}" stroke-linejoin="round" paint-order="stroke"/></g>')
def sparkle(x,y,s=1,c=B.YEL):
    return f'<path transform="translate({x},{y}) scale({s})" d="M0,-30 C4,-6 6,-4 30,0 C6,4 4,6 0,30 C-4,6 -6,4 -30,0 C-6,-4 -4,-6 0,-30Z" fill="{c}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
def heart(x,y,s=1):
    return f'<path transform="translate({x},{y}) scale({s})" d="M0,12 C-30,-8 -26,-34 -12,-34 C-4,-34 0,-26 0,-22 C0,-26 4,-34 12,-34 C26,-34 30,-8 0,12Z" fill="#F2545B" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
def burst(cx,cy,r1,r2,n,fill,rot=0):
    pts=[]
    for i in range(n*2):
        a=math.radians(rot+i*180/n); r=r1 if i%2==0 else r2
        pts.append(f'{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}')
    p=' '.join(pts)
    return f'<polygon points="{p}" fill="#fff" stroke="#fff" stroke-width="30" stroke-linejoin="round"/><polygon points="{p}" fill="{fill}" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>'
def bubble(txt,size,fill,tfill,tstroke,rot=-4):
    d=f'M90,110 Q90,70 130,70 H382 Q422,70 422,110 V300 Q422,340 382,340 H230 L150,430 L170,340 H130 Q90,340 90,300Z'
    return (f'<g transform="rotate({rot} 256 256)"><path d="{d}" fill="#fff" stroke="#fff" stroke-width="30" stroke-linejoin="round"/><path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="10" stroke-linejoin="round"/>'
            +B.P(B.text(txt,size,256,205+size*0.35,track=-0.02,align='center')[0],tfill)+'</g>')

def rede_lateral(nx,ny,fx,fy,nh,fh,band=0.36,sw=1.0,cor='#fff',fundo=None):
    """Rede de vôlei vista da lateral da quadra, em leve perspectiva: poste da frente (nx,ny = pé) maior,
    poste do fundo (fx,fy) menor e mais alto. A malha ocupa o terço de cima."""
    fundo=fundo or B.LILAC
    t0=(nx,ny-nh+4*sw); t1=(fx,fy-fh+3*sw); b0=(nx,ny-nh+band*nh); b1=(fx,fy-fh+band*fh)
    L=lambda p,q,u:(p[0]+(q[0]-p[0])*u,p[1]+(q[1]-p[1])*u)
    g=f'<rect x="{fx-3*sw:.1f}" y="{fy-fh:.1f}" width="{6*sw:.1f}" height="{fh:.1f}" rx="{2*sw:.1f}" fill="{fundo}"/>'
    g+=f'<polygon points="{t0[0]:.1f},{t0[1]:.1f} {t1[0]:.1f},{t1[1]:.1f} {b1[0]:.1f},{b1[1]:.1f} {b0[0]:.1f},{b0[1]:.1f}" fill="{cor}" opacity=".12"/>'
    for i in range(1,8):
        p=L(t0,t1,i/8); q=L(b0,b1,i/8); g+=f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{cor}" stroke-width="{1.2*sw:.1f}" opacity=".7"/>'
    for j in range(1,4):
        p=L(t0,b0,j/4); q=L(t1,b1,j/4); g+=f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{q[0]:.1f}" y2="{q[1]:.1f}" stroke="{cor}" stroke-width="{1.2*sw:.1f}" opacity=".7"/>'
    g+=f'<line x1="{b0[0]:.1f}" y1="{b0[1]:.1f}" x2="{b1[0]:.1f}" y2="{b1[1]:.1f}" stroke="{cor}" stroke-width="{2.4*sw:.1f}" stroke-linecap="round"/>'
    g+=f'<line x1="{t0[0]:.1f}" y1="{t0[1]:.1f}" x2="{t1[0]:.1f}" y2="{t1[1]:.1f}" stroke="{cor}" stroke-width="{5*sw:.1f}" stroke-linecap="round"/>'
    for u,hh in ((0.08,0.2*nh),(0.92,0.18*fh)):
        p=L(t0,t1,u); q=L(b0,b1,u)
        g+=f'<line x1="{p[0]:.1f}" y1="{q[1]:.1f}" x2="{p[0]:.1f}" y2="{p[1]-hh:.1f}" stroke="#fff" stroke-width="{3.4*sw:.1f}" stroke-linecap="round"/>'
        g+=f'<line x1="{p[0]:.1f}" y1="{p[1]:.1f}" x2="{p[0]:.1f}" y2="{p[1]-hh:.1f}" stroke="{B.YEL}" stroke-width="{3.4*sw:.1f}" stroke-dasharray="{6*sw:.1f} {6*sw:.1f}"/>'
    g+=f'<rect x="{nx-4*sw:.1f}" y="{ny-nh:.1f}" width="{8*sw:.1f}" height="{nh:.1f}" rx="{3*sw:.1f}" fill="#fff"/>'
    return g
