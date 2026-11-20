from caminhos import *  # noqa
"""Animações quadro a quadro -> GIF / WebP / MP4 (loading e emojis animados)."""
import os, math, json, subprocess, shutil, brand as B
import gerar_emojis as EM
S=TMP
M=MARCA+''
def ease_out(p): return 1-(1-p)**3
def ease_io(p): return 4*p**3 if p<.5 else 1-(-2*p+2)**3/2
def back_out(p,s=1.6): p-=1; return 1+(s+1)*p**3+s*p**2
def seg(t,a,d,f=ease_out): return f(min(1,max(0,(t-a)/d)))
def e_draw(color,t_draw,arrow_s,rot=0,cx=0,cy=0,s=1.0,width=B.SW):
    L=B.e_len(); off=L*(1-t_draw)
    g=f'<g transform="translate({cx},{cy}) rotate({rot}) scale({s})">'
    if t_draw>0: g+=f'<path d="{B.e_path()}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{L:.1f} {L+10:.1f}" stroke-dashoffset="{off:.2f}" stroke-linejoin="miter"/>'
    if arrow_s>0:
        tri=B.e_arrow(); a=math.radians(B.END); ex,ey=B.R*math.cos(a),B.R*math.sin(a)
        pts=' '.join(f'{px:.2f},{py:.2f}' for px,py in tri)
        g+=f'<g transform="translate({ex:.2f},{ey:.2f}) scale({arrow_s:.3f}) translate({-ex:.2f},{-ey:.2f})"><polygon points="{pts}" fill="{color}" stroke="{color}" stroke-width="7" stroke-linejoin="round"/></g>'
    return g+'</g>'
def loader_frame(t,fg=B.YEL,bg=None,tile=False,W=256):
    """ciclo de 1,8 s: desenha (0-.42), seta estala, rebobina girando -360 (.5-.86), desfaz (.86-1)."""
    draw=seg(t,0.0,0.40,ease_io); arrow=back_out(seg(t,0.36,0.12,lambda p:p)) if t>=0.36 else 0
    rot=-360*seg(t,0.48,0.38,ease_io)
    und=seg(t,0.86,0.14,ease_io)
    d=max(0,draw-und) if und==0 else 1-und
    arrow=arrow*(1-und)
    sc=W/380; body=''
    if tile: body+=f'<rect width="380" height="380" rx="104" fill="{B.BLUE}"/>'
    if bg: body=f'<rect width="380" height="380" fill="{bg}"/>'+body
    # rebobinar: um leve "pulo" de escala no meio do giro
    pump=1+0.06*math.sin(math.pi*seg(t,0.48,0.38,lambda p:p))
    body+=e_draw(fg,d if und==0 else 1,arrow,rot,192,190,(0.78 if not tile else 1.0)*pump)
    if und>0:  # desfaz pelo começo do traço
        L=B.e_len()
        body=body.replace(f'stroke-dashoffset="0.00"',f'stroke-dashoffset="{-L*und:.2f}"')
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 380" width="{W}" height="{W}">{body}</svg>'
def render(name,frame_fn,n,fps,outdir,size,formats=('gif','webp'),alpha=True,mp4=False):
    tmp=f'{S}/frames/{name}'; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
    jobs=[]
    for i in range(n):
        open(f'{tmp}/{i:04d}.svg','w').write(frame_fn(i/n)); jobs.append([f'{tmp}/{i:04d}.svg',f'{tmp}/{i:04d}.png',size,None])
    json.dump(jobs,open(f'{tmp}/jobs.json','w')); subprocess.run(['node',os.path.join(HERE,'batch.js'),f'{tmp}/jobs.json'],check=True)
    os.makedirs(outdir,exist_ok=True); base=f'{outdir}/{name}'
    if 'gif' in formats:
        pal='palettegen=reserve_transparent=1:stats_mode=full' if alpha else 'palettegen=stats_mode=full'
        subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(fps),'-i',f'{tmp}/%04d.png','-filter_complex',
            f'[0:v]split[a][b];[a]{pal}[p];[b][p]paletteuse=dither=none:alpha_threshold=128','-loop','0',base+'.gif'],check=True)
    if 'webp' in formats:
        subprocess.run(['ffmpeg','-v','error','-y','-framerate',str(fps),'-i',f'{tmp}/%04d.png','-c:v','libwebp_anim','-lossless','0','-q:v','90','-loop','0',base+'.webp'],check=True)
    if mp4:
        subprocess.run(['ffmpeg','-v','error','-y','-stream_loop','2','-framerate',str(fps),'-i',f'{tmp}/%04d.png','-vf','format=yuv420p','-c:v','libx264','-crf','18',base+'.mp4'],check=True)
    return base
if __name__=='__main__':
    LD=M+'/loading'
    render('loader-amarelo',lambda t:loader_frame(t,B.YEL),54,30,LD,256)
    render('loader-azul',lambda t:loader_frame(t,B.BLUE),54,30,LD,256)
    render('loader-branco',lambda t:loader_frame(t,B.WHITE),54,30,LD,256)
    render('loader-tile',lambda t:loader_frame(t,B.YEL,tile=True),54,30,LD,256)
    render('loader-tela-azul',lambda t:loader_frame(t,B.YEL,bg=B.BLUE),54,30,LD,512,formats=('gif',),alpha=False,mp4=True)
    print('loaders ok')
