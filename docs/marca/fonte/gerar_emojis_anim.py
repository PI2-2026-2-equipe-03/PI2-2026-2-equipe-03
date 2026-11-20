from caminhos import *  # noqa
import math, anim as A, brand as B
from gerar_emojis import E, ball, eye, blush, mouth_smile, INK
OUT=MARCA+'/emojis/animados'
def wrap(body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">{body}</svg>'
def tf(body,tx=0,ty=0,rot=0,sx=1,sy=1,ox=256,oy=256,base=0.86):
    return f'<g transform="translate(256 256) scale({base}) translate(-256 -256) translate({tx:.2f} {ty:.2f}) translate({ox} {oy}) rotate({rot:.2f}) scale({sx:.3f} {sy:.3f}) translate({-ox} {-oy})">{body}</g>'
face=''.join([eye(206,250),eye(306,250),blush(170,312),blush(342,312),mouth_smile(256,318,40)])
def quicando(t):
    p=abs(math.sin(math.pi*t)); h=-150*p**0.9
    sq=max(0,1-p/0.18)  # amassa perto do chão
    sy=1-0.16*sq; sx=1+0.14*sq
    sh=0.45+0.55*(1-p)
    shadow=f'<ellipse cx="256" cy="470" rx="{120*sh:.1f}" ry="{18*sh:.1f}" fill="{B.BLUE_DEEP}" opacity="{0.25*sh+0.05:.2f}"/>'
    return wrap(tf(shadow)+tf(E['teco-oi'],0,h+40,rot=20*math.sin(2*math.pi*t),sx=sx,sy=sy,oy=440))
def risada(t): return wrap(tf(E['teco-risada'],0,-10*abs(math.sin(4*math.pi*t)),rot=7*math.sin(4*math.pi*t),oy=420))
def girando(t):
    r=-360*A.seg(t,0.15,0.55,A.ease_io); s=1+0.08*math.sin(math.pi*A.seg(t,0.15,0.55,lambda p:p))
    return wrap(tf(E['replay-ja'],rot=r,sx=s,sy=s))
def pulso(t):
    p=A.seg(t%0.5,0,0.18,lambda q:A.back_out(q,2.2)) if (t%0.5)<0.18 else 1-0.1*A.seg(t%0.5,0.18,0.32,A.ease_io)
    s=0.9+0.12*p; return wrap(tf(E['balao-repeteco'],rot=4*math.sin(2*math.pi*t),sx=s,sy=s))
def carimbo(t):
    p=A.seg(t,0,0.18,lambda q:q); s=1.8-0.8*A.ease_out(p) if t<0.18 else 1+0.06*math.exp(-12*(t-0.18))*math.sin(40*(t-0.18))
    op=min(1,t/0.08)
    return wrap(f'<g opacity="{op:.2f}">'+tf(E['selo-salvo'],rot=-6+6*A.seg(t,0,0.18),sx=s,sy=s)+'</g>')
def clique(t):
    press=math.exp(-((t-0.25)/0.06)**2)
    rays=A.seg(t,0.27,0.08)*(1-A.seg(t,0.5,0.2))
    body=E['botao-clique']
    return wrap(tf(body,sx=1+0.05*press,sy=1-0.09*press,oy=490)+f'<g opacity="{rays:.2f}">'+tf(f'<circle cx="256" cy="250" r="{150+90*A.seg(t,0.27,0.35)}" fill="none" stroke="{B.YEL}" stroke-width="10"/>')+'</g>')
def respirando(t):
    s=1+0.04*math.sin(2*math.pi*t); return wrap(tf(E['teco-zzz'],0,6*math.sin(2*math.pi*t),sx=s,sy=s,oy=440))
def fogo(t):
    return wrap(tf(E['teco-fogo'],2*math.sin(18*math.pi*t),0,rot=1.5*math.sin(10*math.pi*t),sx=1+0.03*math.sin(6*math.pi*t),sy=1-0.03*math.sin(6*math.pi*t),oy=440))
for name,fn,n in [('teco-quicando',quicando,30),('teco-risada',risada,30),('replay-girando',girando,36),('repeteco-pulsando',pulso,30),
                  ('salvo-carimbo',carimbo,40),('botao-clique',clique,36),('teco-dormindo',respirando,40),('teco-fogo',fogo,30)]:
    A.render(name,fn,n,24,OUT,256)
print('anim ok')
