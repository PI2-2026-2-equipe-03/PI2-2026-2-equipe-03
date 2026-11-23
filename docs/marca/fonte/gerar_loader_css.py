from caminhos import *  # noqa
import math, brand as B
M=MARCA+''
L=B.e_len(); a=math.radians(B.END); ex,ey=B.R*math.cos(a),B.R*math.sin(a)
tri=' '.join(f'{x:.2f},{y:.2f}' for x,y in B.e_arrow())
CSS=f'''.rp-g{{transform-box:view-box;transform-origin:190px 190px;animation:rp-rew 1.8s infinite}}
.rp-d{{stroke-dasharray:{L:.1f} {L+10:.1f};animation:rp-draw 1.8s infinite}}
.rp-a{{transform-box:view-box;transform-origin:{190+ex:.1f}px {190+ey:.1f}px;animation:rp-pop 1.8s infinite}}
@keyframes rp-draw{{0%{{stroke-dashoffset:{L:.1f};animation-timing-function:cubic-bezier(.65,0,.35,1)}}40%,86%{{stroke-dashoffset:0;animation-timing-function:cubic-bezier(.65,0,.35,1)}}100%{{stroke-dashoffset:{-L:.1f}}}}}
@keyframes rp-pop{{0%,36%{{transform:scale(0);animation-timing-function:cubic-bezier(.34,1.8,.64,1)}}48%,86%{{transform:scale(1);animation-timing-function:cubic-bezier(.65,0,.35,1)}}100%{{transform:scale(0)}}}}
@keyframes rp-rew{{0%,48%{{transform:rotate(0);animation-timing-function:cubic-bezier(.65,0,.35,1)}}86%,100%{{transform:rotate(-360deg)}}}}
@media (prefers-reduced-motion:reduce){{.rp-g,.rp-d,.rp-a{{animation:none}}.rp-d{{stroke-dashoffset:0}}.rp-g{{animation:rp-pulse 1.6s ease-in-out infinite}}}}
@keyframes rp-pulse{{50%{{opacity:.45}}}}'''
def svg(color,tile=False):
    t=f'<rect width="380" height="380" rx="104" fill="{B.BLUE}"/>' if tile else ''
    s=1.0 if tile else 0.8
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 380" width="96" height="96" role="img" aria-label="Carregando">'
            f'<style>{CSS}</style>{t}<g class="rp-g"><g transform="translate(192 190) scale({s})">'
            f'<path class="rp-d" d="{B.e_path()}" fill="none" stroke="{color}" stroke-width="{B.SW}" stroke-linejoin="miter"/>'
            f'</g></g></svg>\n')
# a seta precisa de origem própria; montamos com o grupo rotacionado contendo seta posicionada
def svg2(color,tile=False):
    t=f'<rect width="380" height="380" rx="104" fill="{B.BLUE}"/>' if tile else ''
    s=1.0 if tile else 0.8
    ax,ay=192+ex*s,190+ey*s
    css=CSS.replace(f'transform-origin:{190+ex:.1f}px {190+ey:.1f}px',f'transform-origin:{ax:.1f}px {ay:.1f}px')
    pts=' '.join(f'{192+x*s:.2f},{190+y*s:.2f}' for x,y in B.e_arrow())
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 380" width="96" height="96" role="img" aria-label="Carregando">'
            f'<style>{css}</style>{t}<g class="rp-g">'
            f'<path class="rp-d" transform="translate(192 190) scale({s})" d="{B.e_path()}" fill="none" stroke="{color}" stroke-width="{B.SW}" stroke-linejoin="miter"/>'
            f'<polygon class="rp-a" points="{pts}" fill="{color}" stroke="{color}" stroke-width="{7*s:.1f}" stroke-linejoin="round"/>'
            f'</g></svg>\n')
for n,c,tl in [('amarelo',B.YEL,False),('azul',B.BLUE,False),('branco',B.WHITE,False),('tile',B.YEL,True),('cor-atual','currentColor',False)]:
    open(f'{M}/loading/loader-{n}.svg','w').write(svg2(c,tl))
# componente React (usa currentColor; troque a cor via className)
s=0.8; pts=' '.join(f'{192+x*s:.2f},{190+y*s:.2f}' for x,y in B.e_arrow()); ax,ay=192+ex*s,190+ey*s
css=CSS.replace(f'transform-origin:{190+ex:.1f}px {190+ey:.1f}px',f'transform-origin:{ax:.1f}px {ay:.1f}px')
tsx=f'''import {{ cn }} from '@/lib/utils'

// loader da marca repeteco: o "e" se desenha, a seta estala e ele rebobina (gira -360°).
// usa currentColor -> controle a cor com text-* (ex.: text-tg-brand-yellow).
// respeita prefers-reduced-motion (vira um pulso suave).
const CSS = `{css}`

type RepetecoLoaderProps = {{
  className?: string
  /** texto lido por leitores de tela; vazio quando o contexto já anuncia (ex.: dentro de um toast) */
  label?: string
}}

export function RepetecoLoader({{ className, label = 'Carregando' }}: RepetecoLoaderProps) {{
  return (
    <span
      role={{label ? 'status' : undefined}}
      aria-live={{label ? 'polite' : undefined}}
      aria-hidden={{label ? undefined : true}}
      className={{cn('inline-flex', className)}}
    >
      <svg viewBox="0 0 380 380" className="size-full" aria-hidden="true">
        <style>{{CSS}}</style>
        <g className="rp-g">
          <path
            className="rp-d"
            transform="translate(192 190) scale({s})"
            d="{B.e_path()}"
            fill="none"
            stroke="currentColor"
            strokeWidth={{{B.SW}}}
            strokeLinejoin="miter"
          />
          <polygon
            className="rp-a"
            points="{pts}"
            fill="currentColor"
            stroke="currentColor"
            strokeWidth={{{7*s:.1f}}}
            strokeLinejoin="round"
          />
        </g>
      </svg>
      {{label ? <span className="sr-only">{{label}}</span> : null}}
    </span>
  )
}}
'''
open(f'{M}/loading/RepetecoLoader.tsx','w').write(tsx)
print('css ok')
