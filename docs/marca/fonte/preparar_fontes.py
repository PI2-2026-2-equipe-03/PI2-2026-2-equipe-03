"""Baixa a Bricolage Grotesque (OFL, Google Fonts) e cria as instâncias usadas pelos geradores."""
import os, urllib.request
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from caminhos import TMP
d=os.path.join(TMP,'fonts'); os.makedirs(d,exist_ok=True)
vf=os.path.join(d,'BricolageVF.ttf')
if not os.path.exists(vf):
    urllib.request.urlretrieve('https://github.com/google/fonts/raw/main/ofl/bricolagegrotesque/BricolageGrotesque%5Bopsz,wdth,wght%5D.ttf',vf)
for name,loc in {'xb':{'opsz':96,'wght':800,'wdth':100},'bd':{'opsz':48,'wght':700,'wdth':100},'md':{'opsz':24,'wght':500,'wdth':100},'rg':{'opsz':24,'wght':400,'wdth':100}}.items():
    f=TTFont(vf); instancer.instantiateVariableFont(f,loc,inplace=True); f.save(os.path.join(d,name+'.ttf'))
print('fontes prontas em',d)
