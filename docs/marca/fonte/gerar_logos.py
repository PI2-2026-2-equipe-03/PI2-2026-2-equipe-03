from caminhos import *  # noqa
import os, brand as B
OUT=MARCA+''
os.makedirs(OUT+'/logo/svg',exist_ok=True); os.makedirs(OUT+'/favicon',exist_ok=True); os.makedirs(OUT+'/social',exist_ok=True)
def save(path,s): open(OUT+'/'+path,'w').write(s)
T=380; GAP=85; WS=350; BL=282
def horizontal(bg_tile,e_col,word_col,with_tile=True):
    if with_tile:
        body=B.tile(0,0,T,bg_tile,e_col)
        wm,bb=B.wordmark(T+GAP-12.6,BL,WS,word_col)
        return body+wm, bb[2]+1
    # sem tile: e maior, alinhado ao meio da altura-x
    s=1.25; cx=104*s+2; cy=BL-B.text('x',WS)[2][3]/2 if False else BL-92
    body=B.e_mark(e_col,cx,cy,s)
    x0=cx+104*s+95
    wm,bb=B.wordmark(x0-12.6,BL,WS,word_col)
    return body+wm, bb[2]+1
variants={
 'logo-horizontal':          ('tile',B.BLUE,B.YEL,B.BLUE,None),
 'logo-horizontal-negativo': ('tile',B.YEL,B.BLUE,B.WHITE,B.BLUE),
 'logo-horizontal-sem-fundo-azul': ('free',None,B.YEL,B.BLUE,None),
 'logo-horizontal-branco-amarelo': ('free',None,B.YEL,B.WHITE,B.BLUE),
 'logo-horizontal-amarelo':  ('free',None,B.YEL,B.YEL,B.BLUE),
 'logo-mono-azul':           ('free',None,B.BLUE,B.BLUE,None),
 'logo-mono-branco':         ('free',None,B.WHITE,B.WHITE,B.BLUE),
 'logo-mono-preto':          ('free',None,'#111111','#111111',None),
}
for name,(kind,tb,ec,wc,preview_bg) in variants.items():
    body,w=horizontal(tb,ec,wc,kind=='tile')
    W=round(w); H=T if kind=='tile' else 380
    y0=0
    save(f'logo/svg/{name}.svg',B.svg(W,H,body,title='repeteco'))
# vertical (tile em cima, palavra embaixo)
for name,tb,ec,wc in [('logo-vertical',B.BLUE,B.YEL,B.BLUE),('logo-vertical-negativo',B.YEL,B.BLUE,B.WHITE)]:
    d,w,bb=B.text('repeteco',260,0,0,track=B.TRACK)
    W=round(bb[2]-bb[0])+2; x=(W-(bb[2]-bb[0]))/2-bb[0]
    tx=(W-T)/2
    body=B.tile(tx,0,T,tb,ec)+B.P(B.text('repeteco',260,x,T+70+260*0.528,track=B.TRACK)[0],wc)
    save(f'logo/svg/{name}.svg',B.svg(W,round(T+70+260*0.528+260*0.27+4),body))
# só a palavra
for name,c in [('wordmark-azul',B.BLUE),('wordmark-branco',B.WHITE),('wordmark-amarelo',B.YEL)]:
    d,w,bb=B.text('repeteco',350,0,0,track=B.TRACK)
    W=bb[2]-bb[0]+2; Hh=bb[3]-bb[1]+2
    save(f'logo/svg/{name}.svg',B.svg(round(W),round(Hh),B.P(B.text('repeteco',350,1-bb[0],1-bb[1],track=B.TRACK)[0],c)))
# símbolos
save('logo/svg/simbolo.svg',B.svg(T,T,B.tile(0,0,T,B.BLUE,B.YEL)))
save('logo/svg/simbolo-amarelo.svg',B.svg(T,T,B.tile(0,0,T,B.YEL,B.BLUE)))
save('logo/svg/simbolo-escuro.svg',B.svg(T,T,B.tile(0,0,T,B.BLUE_DEEP,B.YEL)))
save('logo/svg/simbolo-circulo.svg',B.svg(T,T,f'<circle cx="190" cy="190" r="190" fill="{B.BLUE}"/>'+B.e_mark(B.YEL,192,190,1.02)))
for name,c in [('simbolo-e-amarelo',B.YEL),('simbolo-e-azul',B.BLUE),('simbolo-e-branco',B.WHITE)]:
    save(f'logo/svg/{name}.svg',B.svg(270,270,B.e_mark(c,128,128,1.0)))
# favicons
save('favicon/favicon.svg',B.svg(T,T,B.tile(0,0,T,B.BLUE,B.YEL)))
save('favicon/_apple.svg',B.svg(T,T,f'<rect width="380" height="380" fill="{B.BLUE}"/>'+B.e_mark(B.YEL,194,190,1.12)))
save('favicon/_maskable.svg',B.svg(T,T,f'<rect width="380" height="380" fill="{B.BLUE}"/>'+B.e_mark(B.YEL,193,190,0.92)))
print('logos ok')
