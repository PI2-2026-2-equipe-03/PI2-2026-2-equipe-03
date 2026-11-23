"""Gera os HTMLs de cada formato a partir do _modelo.html."""
import os
H = os.path.dirname(os.path.abspath(__file__))
m = open(os.path.join(H, '_modelo.html')).read()
for nome, w, h, modo, d in [('index', 1080, 1920, 'apresenta', 15), ('apresenta-quadrado', 1080, 1080, 'apresenta', 15),
                            ('apresenta-16x9', 1920, 1080, 'apresenta', 15), ('loop', 1080, 1080, 'loop', 4)]:
    open(os.path.join(H, nome + '.html'), 'w').write(m.replace('__W__', str(w)).replace('__H__', str(h)).replace('__MODE__', modo).replace('__D__', str(d)))
print('htmls ok')
