from caminhos import *  # noqa
import os, brand as B
OUT=MARCA+'/social'; os.makedirs(OUT,exist_ok=True)
def save(n,s): open(f'{OUT}/{n}.svg','w').write(s)
def header(x,y,size,ecol=B.YEL,wcol=B.YEL):
    """logo sem tile, com x = borda esquerda do e, y = baseline."""
    s=size/350*1.25; cx=x+104*s; cy=y-92*size/350
    wm,bb=B.wordmark(cx+104*s+95*size/350-12.6*size/350,y,size,wcol)
    return B.e_mark(ecol,cx,cy,s)+wm
def T(s,size,x,y,col,w='xb',track=-0.025,align='left'): return B.P(B.text(s,size,x,y,w=w,track=track,align=align)[0],col)
# 1) slogan 2400x1260 (recriação fiel) == og-image 1200x630 em 2x
def slogan(W=2400,H=1260):
    b=header(175,192,89)
    b+=T('Esse lance merece',223,160,522,B.WHITE)
    b+=T('repeteco.',223,158,742,B.YEL)
    b+=T('Apertou o botão na quadra, o replay é seu.',68,168,920,B.LILAC,w='rg',track=-0.005)
    b+=B.sand(W,H,1140,38)
    return B.svg(W,H,b,bg=B.BLUE)
save('slogan',slogan())
# 2) github social preview 1280x640
W1=B.text('Esse lance merece',100,0,0,track=-0.025)[1]
b=header(96,140,60)+T('Esse lance merece',100,90,330,B.WHITE)+T('repeteco.',100,88,440,B.YEL)
b+=T('Replays de 30 s direto da quadra pro seu celular.',34,94,525,B.LILAC,w='rg',track=0)
b+=B.sand(1280,640,585,18)
b+=f'<g transform="translate(1100,175) rotate(-8)">'+B.tile(-95,-95,190,B.YEL,B.BLUE)+'</g>'
assert 90+W1<1000, W1
save('github-social-preview',B.svg(1280,640,b,bg=B.BLUE))
# 3) banner do README 1600x500
w1=B.text('Esse lance merece ',64,0,0,track=-0.025)[1]
b=header(110,215,120)
b+=T('Esse lance merece',64,116,330,B.WHITE)+T('repeteco.',64,116+w1,330,B.YEL)
b+=T('Aperte o botão na quadra · receba o clipe · reviva o lance',34,118,400,B.LILAC,w='rg',track=0)
b+=B.sand(1600,500,440,14)
b+=f'<g transform="translate(1390,215) rotate(-8)">'+B.tile(-120,-120,240,B.YEL,B.BLUE)+'</g>'
save('readme-banner',B.svg(1600,500,b,bg=B.BLUE))
# 4) post quadrado 1080x1080
b=header(90,150,64)
b+=T('Esse lance',150,80,520,B.WHITE)+T('merece',150,80,680,B.WHITE)+T('repeteco.',150,78,840,B.YEL)
b+=B.sand(1080,1080,960,22)
save('post-1080',B.svg(1080,1080,b,bg=B.BLUE))
# 5) story 1080x1920
b=header(90,210,72)
b+=f'<g transform="translate(800,560) rotate(-10)">'+B.tile(-170,-170,340,B.YEL,B.BLUE)+'</g>'
b+=T('Aquele lance',150,80,1000,B.WHITE)+T('absurdo',150,80,1160,B.YEL)+T('na areia?',150,80,1320,B.WHITE)
b+=T('Aperta o botão.',66,86,1490,B.LILAC,w='md',track=0)+T('O replay é seu.',66,86,1575,B.LILAC,w='md',track=0)
b+=B.sand(1080,1920,1720,40)
save('story-1080x1920',B.svg(1080,1920,b,bg=B.BLUE))
# 6) avatar (org GitHub / redes) 1000x1000
save('avatar',B.svg(1000,1000,f'<rect width="1000" height="1000" fill="{B.BLUE}"/>'+B.e_mark(B.YEL,505,500,2.55)))
# 7) capa/cover larga 3000x1000 (LinkedIn/Notion/YouTube)
b=header(300,500,240)+B.sand(3000,1000,820,30)
w1=B.text('Esse lance merece ',88,0,0,track=-0.02)[1]
b+=T('Esse lance merece',88,312,660,B.WHITE,track=-0.02)+T('repeteco.',88,312+w1,660,B.YEL,track=-0.02)
save('capa-3000x1000',B.svg(3000,1000,b,bg=B.BLUE))
print('social ok')
