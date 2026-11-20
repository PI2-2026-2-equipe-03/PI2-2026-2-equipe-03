from caminhos import *  # noqa
import glob, json, os, subprocess
from PIL import Image
M=MARCA+''; S=TMP
jobs=[]
for f in glob.glob(M+'/logo/svg/*.svg'):
    n=os.path.basename(f)[:-4]
    for w in ((512,1024) if 'simbolo' in n else (800,2400)): jobs.append([f,f'{M}/logo/png/{n}-{w}.png',w,None])
for f in glob.glob(M+'/social/*.svg'): jobs.append([f,f[:-4]+'.png',None,None])
jobs.append([M+'/social/slogan.svg',M+'/social/og-image-1200x630.png',1200,None])
for f in glob.glob(M+'/icones/app/*.svg'): jobs.append([f,f[:-4]+'.png',512,None])
jobs.append([M+'/icones/icones-preview.svg',M+'/icones/icones-preview.png',2400,None])
for f in glob.glob(M+'/emojis/svg/*.svg'):
    n=os.path.basename(f)[:-4]; jobs.append([f,f'{M}/emojis/png-512/{n}.png',512,None]); jobs.append([f,f'{M}/emojis/png-128/{n}.png',128,None])
for f in glob.glob(M+'/ilustracoes/svg/*.svg'):
    n=os.path.basename(f)[:-4]; jobs.append([f,f'{M}/ilustracoes/png/{n}.png',960,None])
for f in glob.glob(M+'/ilustracoes/capas/*.svg'): jobs.append([f,f[:-4]+'.png',1280 if 'capa-' in f else 512,None])
jobs.append([M+'/ilustracoes/ilustracoes-preview.svg',M+'/ilustracoes/ilustracoes-preview.png',2000,None])
for pat,w in [('/teco/cenas/*.svg',1080),('/teco/ficha/*.svg',2400),('/social/carrossel-como-funciona/*.svg',1080),('/social/stories/*.svg',1080),('/social/frases/*.svg',1080)]:
    for f in glob.glob(M+pat): jobs.append([f,f[:-4]+'.png',w,None])
fv=M+'/favicon'
for w in (16,32,48,64): jobs.append([fv+'/favicon.svg',f'{S}/fav{w}.png',w,None])
jobs+=[[fv+'/favicon.svg',fv+'/icon-192.png',192,None],[fv+'/favicon.svg',fv+'/icon-512.png',512,None],[fv+'/_apple.svg',fv+'/apple-touch-icon.png',180,None],[fv+'/_maskable.svg',fv+'/icon-maskable-512.png',512,None]]
json.dump(jobs,open(S+'/alljobs.json','w')); subprocess.run(['node',os.path.join(HERE,'batch.js'),S+'/alljobs.json'],check=True)
ims=[Image.open(f'{S}/fav{w}.png') for w in (16,32,48,64)]
ims[-1].save(fv+'/favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64)],append_images=ims[:-1])
for x in ('_apple.svg','_maskable.svg'): os.remove(fv+'/'+x)
open(fv+'/site.webmanifest','w').write(json.dumps({"name":"repeteco","short_name":"repeteco","description":"Esse lance merece repeteco.","theme_color":"#103A9E","background_color":"#103A9E","display":"standalone",
 "icons":[{"src":"/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/icon-512.png","sizes":"512x512","type":"image/png"},{"src":"/icon-maskable-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},indent=2,ensure_ascii=False))
print(len(jobs),'pngs')
