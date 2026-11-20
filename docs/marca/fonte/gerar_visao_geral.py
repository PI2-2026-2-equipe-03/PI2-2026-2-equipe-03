from caminhos import *  # noqa
"""Monta marca/visao-geral.png: logo, peças sociais, figurinhas, ilustrações e ícones numa folha só."""
import glob
from PIL import Image
M = MARCA
W = 2400
canvas = Image.new('RGB', (W, 4000), (234, 241, 251)); y = 60
def paste(path, x, y, w=None, h=None, box=None):
    im = Image.open(path).convert('RGBA')
    if w: im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    if h: im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    if box:
        b = Image.new('RGBA', (im.width + 80, im.height + 80), box); b.alpha_composite(im, (40, 40)); im = b
    canvas.paste(im, (x, y), im); return im.size
paste(M + '/logo/png/logo-horizontal-800.png', 80, y + 20, w=820)
paste(M + '/logo/png/logo-horizontal-branco-amarelo-800.png', 1000, y, w=820, box=(16, 58, 158, 255))
paste(M + '/logo/png/simbolo-512.png', 2040, y, h=250)
y += 340
w, h = paste(M + '/social/slogan.png', 80, y, w=1150); x = 1270
w2, _ = paste(M + '/social/story-1080x1920.png', x, y, h=h); x += w2 + 40
paste(M + '/social/post-1080.png', x, y, h=h)
y += h + 60; x = 80
for f in sorted(glob.glob(M + '/emojis/png-512/*.png')): paste(f, x, y, w=140); x += 150
y += 200
for i, n in enumerate(['sem-replays', 'busca-vazia', 'sem-conexao', 'video-indisponivel', 'replay-expirado', 'nao-encontrado']):
    _, ih = paste(f'{M}/ilustracoes/png/{n}.png', 80 + i * 378, y, w=360)
y += ih + 40
_, ih = paste(M + '/icones/icones-preview.png', 80, y, w=2240); y += ih + 60
canvas.crop((0, 0, W, y)).save(M + '/visao-geral.png', optimize=True)
print('visão geral ok')
