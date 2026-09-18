import math, os, shutil
from PIL import Image, ImageDraw, ImageFont

S = 2                      # supersample scale for sharpness
W, H = 740*S, 500*S

# ---------- palette ----------
BG=(13,17,23); GRID=(22,26,32); PANL=(29,21,26); PANR=(14,30,28)
BRDL=(81,32,37); BRDR=(19,71,44); DIVID=(34,38,44)
ARRL=(220,38,38); ARRR=(22,163,74); LOOP=(234,88,12); RETARR=(217,119,6)
NFL,NBL=(26,15,15),(239,68,68); NFR,NBR=(10,26,16),(34,197,94)
NFS,NBS=(15,39,24),(74,222,128); NFW,NBW=(18,32,13),(134,239,172)
NFD,NBD=(26,24,0),(245,158,11); NFA,NBA=(28,21,0),(217,119,6)
TXT=(226,232,240); DIM=(71,85,105); DOTL=(249,115,22); DOTR=(6,182,212)
HDRL=(252,165,165); HDRR=(134,239,172)

F="C:/Windows/Fonts/"
def font(names,size):
    for n in names:
        p=F+n
        if os.path.exists(p): return ImageFont.truetype(p,size)
    return ImageFont.load_default()
f_node=font(["segoeui.ttf"],11*S)
f_nodeb=font(["seguisb.ttf","segoeuib.ttf"],11*S)
f_hdr=font(["seguibl.ttf","segoeuib.ttf"],11*S)
f_lbl=font(["segoeui.ttf"],9*S)
f_stat=font(["seguisb.ttf","segoeuib.ttf"],11*S)

LX,RX=185*S,555*S
NW,NH=148*S,36*S

def N(x,y,lbl,t,s=False): return dict(x=x*S,y=y*S,lbl=lbl,t=t,s=s)
Ln={'p':N(185,62,'Prompt','oval'),'g':N(185,138,'grep / glob repo','rect'),
    'o':N(185,210,'Open candidate file','rect'),'d':N(185,292,'Right place?','diam'),
    'e':N(185,396,'Finally edit','rect',True)}
Rn={'p':N(555,55,'Prompt','oval'),'i':N(555,138,'wiki-index resolver','rect'),
    'w':N(555,225,'page-wiki.md','rect'),'e':N(555,325,'Edit right files','rect',True),
    'u':N(555,420,'Update wiki + re-anchor hash','rect')}

def rot(px,py,a): return (px*math.cos(a)-py*math.sin(a), px*math.sin(a)+py*math.cos(a))
def arrowhead(d,x,y,ang,color):
    pts=[(0,0),(-8*S,-4*S),(-8*S,4*S)]
    d.polygon([(x+rot(px,py,ang)[0],y+rot(px,py,ang)[1]) for px,py in pts],fill=color)
def arrow(d,x1,y1,x2,y2,color):
    d.line([(x1,y1),(x2,y2)],fill=color,width=2*S)
    arrowhead(d,x2,y2,math.atan2(y2-y1,x2-x1),color)
def dashed_poly(d,pts,color):
    for i in range(len(pts)-1):
        (x1,y1),(x2,y2)=pts[i],pts[i+1]
        seg=math.hypot(x2-x1,y2-y1)
        if seg==0: continue
        ux,uy=(x2-x1)/seg,(y2-y1)/seg
        t=0
        while t<seg:
            a,b=t,min(t+6*S,seg)
            d.line([(x1+ux*a,y1+uy*a),(x1+ux*b,y1+uy*b)],fill=color,width=2*S); t+=11*S
def tc(d,x,y,lbl,fnt,fill):
    w=d.textlength(lbl,font=fnt); d.text((x-w/2,y-7*S),lbl,font=fnt,fill=fill)
def node_text(d,n,fill):
    x,y,lbl=n['x'],n['y'],n['lbl']
    if len(lbl)>17:
        wd=lbl.split(' '); m=(len(wd)+1)//2
        tc(d,x,y-6*S,' '.join(wd[:m]),f_node,fill); tc(d,x,y+7*S,' '.join(wd[m:]),f_node,fill)
    else:
        tc(d,x,y,lbl,f_nodeb if fill==(255,255,255) else f_node,fill)
def draw_node(d,n,lit=False,fill=None,border=None):
    x,y,t,s=n['x'],n['y'],n['t'],n['s']; isL=x<370*S
    nf=fill or (NFS if s else (NFL if isL else NFR)); nb=border or (NBS if s else (NBL if isL else NBR))
    if t=='diam': nf,nb=NFD,NBD
    w=3*S if lit else 1*S
    if t=='oval': d.ellipse([x-NW/2,y-NH/2,x+NW/2,y+NH/2],fill=nf,outline=nb,width=w)
    elif t=='diam':
        d.polygon([(x,y-27*S),(x+70*S,y),(x,y+27*S),(x-70*S,y)],fill=nf,outline=nb)
        d.line([(x,y-27*S),(x+70*S,y),(x,y+27*S),(x-70*S,y),(x,y-27*S)],fill=nb,width=w)
    else: d.rounded_rectangle([x-NW/2,y-NH/2,x+NW/2,y+NH/2],radius=7*S,fill=nf,outline=nb,width=w)
    node_text(d,n,(255,255,255) if lit else TXT)

def build_base():
    base=Image.new("RGBA",(W,H),BG+(255,)); d=ImageDraw.Draw(base)
    for x in range(0,W,28*S): d.line([(x,0),(x,H)],fill=GRID,width=1*S)
    for y in range(0,H,28*S): d.line([(0,y),(W,y)],fill=GRID,width=1*S)
    d.rounded_rectangle([8*S,32*S,364*S,H-8*S],radius=12*S,fill=PANL,outline=BRDL,width=1*S)
    d.rounded_rectangle([376*S,32*S,732*S,H-8*S],radius=12*S,fill=PANR,outline=BRDR,width=1*S)
    dashed_poly(d,[(368*S,38*S),(368*S,H-15*S)],DIVID)
    tc(d,LX,20*S,"WITHOUT WIKI",f_hdr,HDRL); tc(d,RX,20*S,"WITH WIKI",f_hdr,HDRR)
    arrow(d,LX,Ln['p']['y']+NH/2,LX,Ln['g']['y']-NH/2,ARRL)
    arrow(d,LX,Ln['g']['y']+NH/2,LX,Ln['o']['y']-NH/2,ARRL)
    arrow(d,LX,Ln['o']['y']+NH/2,LX,Ln['d']['y']-27*S,ARRL)
    arrow(d,LX,Ln['d']['y']+27*S,LX,Ln['e']['y']-NH/2,ARRL)
    d.text((LX+6*S,(Ln['d']['y']+27*S+Ln['e']['y']-NH/2)/2-6*S),"yes",font=f_lbl,fill=DIM)
    lp=[(LX-70*S,Ln['d']['y']),(LX-94*S,Ln['d']['y']),(LX-94*S,Ln['g']['y']),(LX-NW/2,Ln['g']['y'])]
    dashed_poly(d,lp,LOOP); arrowhead(d,LX-NW/2,Ln['g']['y'],0,LOOP)
    d.text((LX-150*S,(Ln['d']['y']+Ln['g']['y'])/2-6*S),"no / not sure",font=f_lbl,fill=DIM)
    arrow(d,RX,Rn['p']['y']+NH/2,RX,Rn['i']['y']-NH/2,ARRR)
    arrow(d,RX,Rn['i']['y']+NH/2,RX,Rn['w']['y']-NH/2,ARRR)
    arrow(d,RX,Rn['w']['y']+NH/2,RX,Rn['e']['y']-NH/2,ARRR)
    arrow(d,RX,Rn['e']['y']+NH/2,RX,Rn['u']['y']-NH/2,ARRR)
    ex,ey=RX+NW/2,Rn['e']['y']; uy=Rn['u']['y']; bx=ex+30*S
    dashed_poly(d,[(ex,ey),(bx,ey),(bx,uy),(ex,uy)],RETARR); arrowhead(d,ex,uy,math.pi,RETARR)
    return base
BASE=build_base()

def mkpath(wps):
    segs,tot=[],0.0
    for i in range(len(wps)-1):
        dx,dy=wps[i+1][0]-wps[i][0],wps[i+1][1]-wps[i][1]; ln=math.hypot(dx,dy)
        segs.append((wps[i],wps[i+1],ln,tot)); tot+=ln
    return segs,tot
def pos_at(path,t):
    segs,tot=path; d=max(0,min(1,t))*tot
    for a,b,ln,cum in segs:
        if d<=cum+ln:
            u=(d-cum)/ln if ln>0 else 0
            return (a[0]+(b[0]-a[0])*u,a[1]+(b[1]-a[1])*u)
    return segs[-1][1]
Lwp=[(LX,Ln['p']['y']),(LX,Ln['g']['y']),(LX,Ln['o']['y']),(LX,Ln['d']['y']-27*S),
    (LX-70*S,Ln['d']['y']),(LX-94*S,Ln['d']['y']),(LX-94*S,Ln['g']['y']),(LX-NW/2,Ln['g']['y']),
    (LX,Ln['g']['y']),(LX,Ln['o']['y']),(LX,Ln['d']['y']-27*S),
    (LX-70*S,Ln['d']['y']),(LX-94*S,Ln['d']['y']),(LX-94*S,Ln['g']['y']),(LX-NW/2,Ln['g']['y']),
    (LX,Ln['g']['y']),(LX,Ln['o']['y']),(LX,Ln['d']['y']-27*S),
    (LX,Ln['d']['y']+27*S),(LX,Ln['e']['y'])]
Rwp=[(RX,Rn['p']['y']),(RX,Rn['i']['y']),(RX,Rn['w']['y']),(RX,Rn['e']['y']),(RX,Rn['u']['y'])]
Rwp2=[(RX,Rn['u']['y']),(RX+NW/2,Rn['u']['y']),(RX+NW/2+30*S,Rn['u']['y']),
    (RX+NW/2+30*S,Rn['w']['y']),(RX+NW/2,Rn['w']['y']),(RX,Rn['w']['y'])]
Lpath,Rpath,Rpath2=mkpath(Lwp),mkpath(Rwp),mkpath(Rwp2)
def ease(t): return 2*t*t if t<.5 else -1+(4-2*t)*t

L_DUR,PAUSE=5200,1400; R_DOWN,R_RETURN=2200,800; R_TOTAL=R_DOWN+R_RETURN
CYCLE=L_DUR+PAUSE; FPS=25; DT=1000//FPS; NFRAMES=CYCLE//DT; TM=14

def add_trail(ov,trail,color):
    d=ImageDraw.Draw(ov,"RGBA"); n=len(trail)
    for i,(x,y) in enumerate(trail):
        a=int((i/n)*0.45*255); r=(1.5+(i/n)*3.5)*S
        d.ellipse([x-r,y-r,x+r,y+r],fill=color+(a,))
def add_glow(ov,x,y,color):
    d=ImageDraw.Draw(ov,"RGBA")
    for i in range(10,0,-1):
        r=18*S*i/10; a=int(55*(1-i/10)); d.ellipse([x-r,y-r,x+r,y+r],fill=color+(a,))
def dotcore(d,x,y,color):
    d.ellipse([x-5*S,y-5*S,x+5*S,y+5*S],fill=color); d.ellipse([x-2*S,y-2*S,x+2*S,y+2*S],fill=(255,255,255))

FD="D:/Github/arungudelli/export/frames"
if os.path.isdir(FD): shutil.rmtree(FD)
os.makedirs(FD)

Ltr,Rtr=[],[]
for k in range(NFRAMES):
    ph=k*DT
    lDone=ph>=L_DUR
    rPhase=2 if ph>=R_TOTAL else (1 if ph>=R_DOWN else 0)
    lpos=rpos=None
    if not lDone:
        lpos=pos_at(Lpath,ease(min(ph/L_DUR,1))); Ltr.append(lpos); Ltr[:]=Ltr[-TM:]
    else: Ltr.clear()
    if rPhase==0:
        rpos=pos_at(Rpath,ease(min(ph/R_DOWN,1))); Rtr.append(rpos); Rtr[:]=Rtr[-TM:]
    elif rPhase==1:
        rpos=pos_at(Rpath2,ease(min((ph-R_DOWN)/R_RETURN,1))); Rtr.append(rpos); Rtr[:]=Rtr[-TM:]
    else: Rtr.clear()

    frame=BASE.copy()
    tl=Image.new("RGBA",(W,H),(0,0,0,0))
    if Ltr: add_trail(tl,Ltr,DOTL)
    if Rtr: add_trail(tl,Rtr,DOTR)
    frame=Image.alpha_composite(frame,tl)
    d=ImageDraw.Draw(frame,"RGBA")
    for n in Ln.values(): draw_node(d,n,lit=(lDone and n['s']))
    for key,n in Rn.items():
        if key=='e': draw_node(d,n,lit=(rPhase>=1))
        elif key=='u': draw_node(d,n,lit=(rPhase>=1),fill=NFW,border=NBW)
        elif key=='w':
            if rPhase==2: draw_node(d,n,lit=True,fill=(15,32,16),border=NBS)
            elif rPhase==1: draw_node(d,n,lit=True,fill=NFA,border=NBA)
            else: draw_node(d,n)
        else: draw_node(d,n)
    if rPhase==2: tc(d,RX,Rn['w']['y']+NH/2+11*S,"# hash updated",f_lbl,NBS)
    gl=Image.new("RGBA",(W,H),(0,0,0,0))
    if lpos: add_glow(gl,lpos[0],lpos[1],DOTL)
    if rpos: add_glow(gl,rpos[0],rpos[1],DOTR)
    frame=Image.alpha_composite(frame,gl)
    d=ImageDraw.Draw(frame,"RGBA")
    if lpos: dotcore(d,lpos[0],lpos[1],DOTL)
    if rpos: dotcore(d,rpos[0],rpos[1],DOTR)
    if not lDone:
        loop=min(3,int(ph/(L_DUR/3))+1); tc(d,LX,H-20*S,f"Loop {loop} of 3",f_stat,(251,146,60))
    else: tc(d,LX,H-20*S,"Done",f_stat,HDRL)
    if rPhase==2: tc(d,RX,H-20*S,"Wiki re-anchored",f_stat,HDRR)
    elif rPhase==1: tc(d,RX,H-20*S,"Re-anchoring hash...",f_stat,(251,191,36))
    else: tc(d,RX,H-20*S,"Reading wiki -> editing...",f_stat,(6,182,212))

    frame.convert("RGB").save(f"{FD}/f_{k:04d}.png")

print("frames:",NFRAMES,"size:",W,"x",H,"fps:",FPS)
