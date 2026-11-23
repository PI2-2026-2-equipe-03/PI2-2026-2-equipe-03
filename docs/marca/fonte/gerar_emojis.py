from caminhos import *  # noqa
import os, math, brand as B
OUT=MARCA+'/emojis'; os.makedirs(OUT+'/svg',exist_ok=True)
from teco import *  # noqa: F401,F403  (ball, eye, word, burst, bubble...)
E={}
F=lambda *p:''.join(p)
import maos as _M
_aceno=f'<g transform="translate(420,156) rotate(20) scale(2.35)">{_M.borda_figurinha("aberta")}{_M.MAO["aberta"]}</g>'
E['teco-oi']=F(ball(),eye(206,250),eye(306,250),blush(170,312),blush(342,312),mouth_smile(256,318,40),_aceno)  # acenando com a luva do Teco
E['teco-uau']=F(ball(),eye(204,246,1.25,(0,-4)),eye(308,246,1.25,(0,-4)),f'<ellipse cx="256" cy="345" rx="26" ry="32" fill="{INK}"/>',word('!',130,430,170,rot=12),word('!',90,92,170,rot=-14))
E['teco-risada']=F(ball(rot=12),closed_eye(206,250),closed_eye(306,250),mouth_smile(256,300,62,True),
    f'<path d="M168,262 q-22,26 -6,46 q18,-8 6,-46z" fill="#7FC8F8" stroke="{INK}" stroke-width="5"/><path d="M344,262 q22,26 6,46 q-18,-8 -6,-46z" fill="#7FC8F8" stroke="{INK}" stroke-width="5"/>')
E['teco-craque']=F(ball(rot=-8),
    f'<path d="M150,228 H362 L352,262 Q340,292 300,290 Q270,288 262,256 H250 Q242,288 212,290 Q172,292 160,262Z" fill="{INK}" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>',
    f'<path d="M188,246 l26,-10" stroke="#fff" stroke-width="7" stroke-linecap="round"/><path d="M286,246 l26,-10" stroke="#fff" stroke-width="7" stroke-linecap="round"/>',
    f'<path d="M216,340 Q262,362 304,326" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>',sparkle(420,120,1.2,'#fff'))
FL='M256,40 C300,100 360,90 350,170 C390,140 400,110 392,80 C450,140 470,260 410,330 L102,330 C40,260 62,140 120,80 C112,110 122,140 162,170 C152,90 212,100 256,40Z'
E['teco-fogo']=F(f'<path d="{FL}" fill="#FF8A2B" stroke="#fff" stroke-width="30" stroke-linejoin="round"/><path d="{FL}" fill="#FF8A2B" stroke="{INK}" stroke-width="9" stroke-linejoin="round"/>',
    f'<path d="M256,110 C286,150 320,150 316,200 C340,180 346,160 342,140 C380,190 380,260 350,300 L162,300 C132,260 132,190 170,140 C166,160 172,180 196,200 C192,150 226,150 256,110Z" fill="{B.YEL}"/>',
    ball(256,300,150),f'<path d="M180,262 l46,16" stroke="{INK}" stroke-width="11" stroke-linecap="round"/><path d="M332,262 l-46,16" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>',
    eye(208,300,0.9,(3,0)),eye(304,300,0.9,(-3,0)),f'<path d="M222,370 Q256,352 290,370" fill="none" stroke="{INK}" stroke-width="11" stroke-linecap="round"/>')
E['teco-zzz']=F(ball(rot=20),closed_eye(206,262,False),closed_eye(306,262,False),blush(170,312),blush(342,312),
    f'<ellipse cx="256" cy="336" rx="14" ry="10" fill="{INK}"/>',word('z',70,380,150,rot=-10),word('z',96,436,86,rot=-14))
E['teco-apaixonado']=F(ball(rot=-15),heart(206,262,1.5),heart(306,262,1.5),mouth_smile(256,318,40),heart(420,110,1.1),heart(96,150,0.8))
spiral=lambda x,y:f'<path d="M{x},{y} m-4,0 a4,4 0 1 1 8,0 a10,10 0 1 1 -18,0 a16,16 0 1 1 30,0 a22,22 0 1 1 -42,0" fill="none" stroke="{INK}" stroke-width="7" stroke-linecap="round"/>'
E['teco-tonto']=F(ball(rot=35),spiral(206,252),spiral(306,252),f'<path d="M212,340 q14,-14 28,0 t28,0 t28,0" fill="none" stroke="{INK}" stroke-width="10" stroke-linecap="round"/>',sparkle(110,120,0.8),sparkle(410,110,1.0),sparkle(440,210,0.6))
E['botao-clique']=F(f'<rect x="96" y="150" width="320" height="230" rx="60" fill="#fff" stroke="#fff" stroke-width="30"/>',
    f'<rect x="96" y="150" width="320" height="230" rx="60" fill="#fff" stroke="{INK}" stroke-width="10"/>',
    f'<path d="M150,250 v40 a106,38 0 0 0 212,0 v-40" fill="{B.YEL_DK}" stroke="{INK}" stroke-width="9"/><ellipse cx="256" cy="250" rx="106" ry="38" fill="{B.YEL}" stroke="{INK}" stroke-width="9"/>',
    f'<rect x="232" y="380" width="48" height="110" fill="{B.BLUE_DK}" stroke="{INK}" stroke-width="9"/>',
    f'<path d="M110,120 l-36,-36 M256,96 v-52 M402,120 l36,-36" stroke="{B.YEL}" stroke-width="22" stroke-linecap="round"/><path d="M110,120 l-36,-36 M256,96 v-52 M402,120 l36,-36" stroke="{INK}" stroke-width="7" stroke-linecap="round" opacity=".0"/>',
    word('clique!',88,256,470,fill='#fff',stroke=B.BLUE,rot=-6))
check='M150,262 L224,334 L366,186'
E['selo-salvo']=F(burst(256,236,190,160,14,'#2BB673',8),f'<path d="{check}" fill="none" stroke="#fff" stroke-width="40" stroke-linecap="round" stroke-linejoin="round"/>',word('salvo!',100,256,470,rot=-4))
E['selo-30s']=F(f'<circle cx="256" cy="266" r="180" fill="#fff" stroke="#fff" stroke-width="30"/><circle cx="256" cy="266" r="180" fill="{B.BLUE}" stroke="{INK}" stroke-width="10"/>',
    f'<rect x="222" y="40" width="68" height="44" rx="12" fill="{B.YEL}" stroke="{INK}" stroke-width="9"/>',
    f'<path d="M256,266 L256,120 A146,146 0 0 1 382,193 Z" fill="{B.YEL}" opacity=".95"/>',
    f'<circle cx="256" cy="266" r="146" fill="none" stroke="#fff" stroke-width="8" stroke-dasharray="4 34.2" stroke-linecap="round"/>',
    word('30s',124,256,316,fill='#fff',stroke=INK))
E['balao-de-novo']=bubble('de novo!',74,B.YEL,INK,None)
E['balao-repeteco']=F(burst(256,256,236,180,16,B.YEL,5),word('REPETECO!',74,256,284,fill='#fff',stroke=B.BLUE,rot=-8))
E['replay-ja']=F(f'<g transform="rotate(-10 256 256)">'+'<rect x="86" y="86" width="340" height="340" rx="96" fill="#fff" stroke="#fff" stroke-width="30"/>'+B.tile(86,86,340,B.BLUE,B.YEL,rx=96)+f'<rect x="86" y="86" width="340" height="340" rx="96" fill="none" stroke="{INK}" stroke-width="9"/></g>',
    f'<path d="M40,190 h44 M28,250 h56 M40,310 h44" stroke="{B.YEL}" stroke-width="18" stroke-linecap="round"/>',sparkle(440,90,1.1))
E['quadra-areia']=F(f'<circle cx="256" cy="256" r="200" fill="#fff" stroke="#fff" stroke-width="30"/><clipPath id="qa"><circle cx="256" cy="256" r="200"/></clipPath><circle cx="256" cy="256" r="200" fill="{B.BLUE}"/>',
    f'<g clip-path="url(#qa)">'+rede_lateral(222,352,290,318,232,160,sw=1.6)+B.P(B.wave_path(512,512,320,22,0.1,0.4),B.YEL)+B.P(B.wave_path(512,512,370,14,0.5,1.2),B.YEL_DK)
    +f'<g transform="translate(372,150) rotate(20)">'+ball(0,0,30,borda=False)+'</g>'
    +f'<path d="M140,200 q60,-130 210,-60" fill="none" stroke="#fff" stroke-width="5" stroke-dasharray="2 14" stroke-linecap="round" opacity=".8"/></g>',
    f'<circle cx="256" cy="256" r="200" fill="none" stroke="{INK}" stroke-width="10"/>')
for k,v in E.items(): open(f'{OUT}/svg/{k}.svg','w').write(B.svg(512,512,v,title=k))
print(len(E),'emojis')
