from caminhos import *  # noqa
"""Gerador de marca repeteco: helpers de texto->path e do símbolo."""
import math, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
FD=os.path.join(TMP,'fonts')+'/'
BLUE='#103A9E'; BLUE_DK='#0B2A75'; BLUE_DEEP='#081F57'; YEL='#F2C111'; YEL_DK='#E0AD00'; WHITE='#FFFFFF'; ICE='#EAF1FB'; LILAC='#C9D6F5'
_cache={}
def _font(w):
    if w not in _cache:
        p=FD+w+'.ttf'; blob=hb.Blob.from_file_path(p); face=hb.Face(blob); f=hb.Font(face)
        _cache[w]=(f,TTFont(p))
    return _cache[w]
def text(s,size,x=0,y=0,w='xb',track=0.0,align='left'):
    """Retorna (d, largura, (xmin,ymin,xmax,ymax)) com baseline em y."""
    f,tt=_font(w); upm=tt['head'].unitsPerEm; sc=size/upm
    buf=hb.Buffer(); buf.add_str(s); buf.guess_segment_properties(); hb.shape(f,buf,{'kern':True,'liga':True})
    gs=tt.getGlyphSet(); order=tt.getGlyphOrder()
    pen=SVGPathPen(gs); bp=BoundsPen(gs)
    cx=0; glyphs=[]
    for info,pos in zip(buf.glyph_infos,buf.glyph_positions):
        glyphs.append((order[info.codepoint],cx+pos.x_offset,pos.y_offset)); cx+=pos.x_advance+track*upm
    width=(cx-track*upm)*sc
    if align=='center': x-=width/2
    elif align=='right': x-=width
    for g,gx,gy in glyphs:
        t=(sc,0,0,-sc,x+gx*sc,y-gy*sc)
        gs[g].draw(TransformPen(pen,t)); gs[g].draw(TransformPen(bp,t))
    return pen.getCommands(), width, bp.bounds
def P(d,fill): return f'<path d="{d}" fill="{fill}"/>'

# ---- símbolo: "e" que vira seta de replay. Grade: centro (0,0), raio do traço 87.5, espessura 33 (unidades do tile 380)
R=87.5; SW=33; END=62  # ângulo (graus, sentido da tela) onde o arco de baixo termina
def e_path(end=END):
    a=math.radians(end); ex,ey=R*math.cos(a),R*math.sin(a)
    return f"M{-R:.2f},0 L{R:.2f},0 A{R},{R} 0 1 0 {ex:.2f},{ey:.2f}"
def e_len(end=END):
    return 2*R+math.radians(360-end)*R
def e_arrow(end=END):
    a=math.radians(end); ex,ey=R*math.cos(a),R*math.sin(a); tx,ty=math.sin(a),-math.cos(a); nx,ny=math.cos(a),math.sin(a)
    hw,L,back=42,52,6; bx,by=ex-tx*back,ey-ty*back
    return [(bx+nx*hw,by+ny*hw),(ex+tx*L,ey+ty*L),(bx-nx*hw,by-ny*hw)]
def e_mark(color, cx=0, cy=0, s=1.0, arrow=True, end=END, sweep=1.0, cls=''):
    """`sweep` 0..1 desenha parcialmente (para animação estática). Retorna <g>."""
    ri,ro=R-SW/2,R+SW/2
    a=math.radians(end)
    ex,ey=R*math.cos(a),R*math.sin(a)
    tx,ty=math.sin(a),-math.cos(a)      # tangente (sentido da seta)
    nx,ny=math.cos(a),math.sin(a)       # normal radial
    hw,L,back=42,52,6
    bx,by=ex-tx*back,ey-ty*back
    tri=[(bx+nx*hw,by+ny*hw),(ex+tx*L,ey+ty*L),(bx-nx*hw,by-ny*hw)]
    parts=[]
    # um traço contínuo: barra da esquerda p/ direita, sobe pelo topo, desce pela esquerda e termina embaixo à direita
    parts.append(f'<path d="{e_path(end)}" fill="none" stroke="{color}" stroke-width="{SW}" stroke-linejoin="miter" stroke-miterlimit="4"/>')
    if arrow:
        pts=' '.join(f'{px:.2f},{py:.2f}' for px,py in tri)
        parts.append(f'<polygon points="{pts}" fill="{color}" stroke="{color}" stroke-width="7" stroke-linejoin="round"/>')
    return f'<g transform="translate({cx},{cy}) scale({s})" {cls}>'+''.join(parts)+'</g>'
def tile(x=0,y=0,size=380,bg=BLUE,fg=YEL,rx=None):
    s=size/380; rx=104*s if rx is None else rx
    return f'<rect x="{x}" y="{y}" width="{size}" height="{size}" rx="{rx:.2f}" fill="{bg}"/>'+e_mark(fg,x+size/2+2*s,y+size/2,s)
def svg(w,h,body,bg=None,title='repeteco'):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}"><title>{title}</title>{b}{body}</svg>\n'

TRACK=-0.032
def wordmark(x,baseline,size,color,track=TRACK):
    d,w,bb=text('repeteco',size,x,baseline,track=track); return P(d,color),bb
def wave_path(W,H,y0,amp,phase=0.0,seed=1.0,k=(1.0,2.3,0.6)):
    """Faixa de areia: borda ondulada em y0 descendo até H."""
    import math
    pts=[]
    N=48
    for i in range(N+1):
        x=W*i/N; u=i/N
        y=y0+amp*(0.55*math.sin(2*math.pi*(k[0]*u+phase))+0.3*math.sin(2*math.pi*(k[1]*u+phase*1.7+seed))+0.15*math.sin(2*math.pi*(k[2]*u+seed*0.3)))
        pts.append((x,y))
    # curva suave (Catmull-Rom -> Bezier)
    d=f'M0,{H} L{pts[0][0]:.1f},{pts[0][1]:.1f} '
    for i in range(len(pts)-1):
        p0=pts[max(i-1,0)];p1=pts[i];p2=pts[i+1];p3=pts[min(i+2,len(pts)-1)]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6); c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        d+=f'C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} '
    return d+f'L{W},{H} Z'
def sand(W,H,top,amp):
    return P(wave_path(W,H,top,amp,0.1,0.4),YEL)+P(wave_path(W,H,top+amp*1.3,amp*0.7,0.55,1.3,(1.4,0.8,2.1)),YEL_DK)
