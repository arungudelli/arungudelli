import math, os
from PIL import Image, ImageDraw, ImageFont

S = 2  # supersample for sharpness
BG   = (13, 17, 23)
GRID = (22, 26, 32)
TXT  = (226, 232, 240)
DIM  = (110, 118, 129)
# node palettes
NEU_F, NEU_B = (22, 27, 34), (72, 84, 100)      # neutral
GRN_F, GRN_B = (10, 26, 16), (34, 197, 94)      # green (reuse / good)
AMB_F, AMB_B = (26, 24, 0), (245, 158, 11)      # amber (decision / stale)
TEAL_F, TEAL_B = (8, 26, 30), (6, 182, 212)     # teal (start / io)
WIKI_F, WIKI_B = (18, 32, 13), (134, 239, 172)  # wiki
ARR = (100, 116, 139)
GRNARR = (34, 197, 94)

F = "C:/Windows/Fonts/"
def font(names, size):
    for n in names:
        p = F + n
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def grid(d, W, H):
    for x in range(0, W, 28*S): d.line([(x,0),(x,H)], fill=GRID, width=1)
    for y in range(0, H, 28*S): d.line([(0,y),(W,y)], fill=GRID, width=1)

def rot(px, py, a): return (px*math.cos(a)-py*math.sin(a), px*math.sin(a)+py*math.cos(a))
def ahead(d, x, y, ang, color, sz=9):
    pts=[(0,0),(-sz*S,-4*S),(-sz*S,4*S)]
    d.polygon([(x+rot(px,py,ang)[0], y+rot(px,py,ang)[1]) for px,py in pts], fill=color)
def arrow(d, x1,y1,x2,y2, color, dashed=False, w=2):
    if dashed:
        seg=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/seg,(y2-y1)/seg; t=0
        while t<seg:
            a,b=t,min(t+6*S,seg); d.line([(x1+ux*a,y1+uy*a),(x1+ux*b,y1+uy*b)],fill=color,width=w*S); t+=11*S
    else:
        d.line([(x1,y1),(x2,y2)], fill=color, width=w*S)
    ahead(d, x2,y2, math.atan2(y2-y1,x2-x1), color)

def wrap(d, text, fnt, maxw):
    words=text.split(' '); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if d.textlength(t, font=fnt) <= maxw: cur=t
        else:
            if cur: lines.append(cur)
            cur=w
    if cur: lines.append(cur)
    return lines

def center_lines(d, cx, cy, lines, fnt, fill, lh=None):
    if lh is None: lh = fnt.size + 4*S
    total=len(lines)*lh
    y=cy-total/2+lh/2
    for ln in lines:
        w=d.textlength(ln, font=fnt); d.text((cx-w/2, y-fnt.size/2), ln, font=fnt, fill=fill); y+=lh

def rrect(d, cx, cy, w, h, r, fill, border, bw=2):
    d.rounded_rectangle([cx-w/2, cy-h/2, cx+w/2, cy+h/2], radius=r, fill=fill, outline=border, width=bw*S)

def stadium(d, cx, cy, w, h, fill, border, bw=2):
    d.rounded_rectangle([cx-w/2, cy-h/2, cx+w/2, cy+h/2], radius=h/2, fill=fill, outline=border, width=bw*S)

def diamond(d, cx, cy, w, h, fill, border, bw=2):
    pts=[(cx,cy-h/2),(cx+w/2,cy),(cx,cy+h/2),(cx-w/2,cy)]
    d.polygon(pts, fill=fill); d.line(pts+[pts[0]], fill=border, width=bw*S)

def subroutine(d, cx, cy, w, h, r, fill, border, bw=2):
    rrect(d, cx, cy, w, h, r, fill, border, bw)
    d.line([(cx-w/2+7*S, cy-h/2),(cx-w/2+7*S, cy+h/2)], fill=border, width=bw*S)
    d.line([(cx+w/2-7*S, cy-h/2),(cx+w/2-7*S, cy+h/2)], fill=border, width=bw*S)

# ============================================================
# DIAGRAM 2 — flowchart: produce-or-reuse team pipeline
# ============================================================
def flowchart():
    W, H = 1120*S, 1000*S
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    grid(d, W, H)
    f_title = font(["seguisb.ttf","segoeuib.ttf"], 22*S)
    f_node  = font(["segoeui.ttf"], 19*S)
    f_lbl   = font(["seguisb.ttf","segoeuib.ttf"], 16*S)

    d.text((40*S, 30*S), "Produce-or-reuse: one page, shared across the team", font=f_title, fill=TXT)

    CX = W//2
    NW, NH = 470*S, 78*S
    # y positions
    yP, yR, yQ, yGEN, yRE, yW, yN = 150*S, 270*S, 400*S, 560*S, 690*S, 810*S, 920*S
    xGEN = CX + 250*S   # generate node offset to the right

    # nodes
    stadium(d, CX, yP, 360*S, 66*S, TEAL_F, TEAL_B)
    center_lines(d, CX, yP, ["Prompt (any session, any user)"], f_node, TXT)

    rrect(d, CX, yR, NW, NH, 12*S, NEU_F, NEU_B)
    center_lines(d, CX, yR, ["Resolve the page via wiki-index"], f_node, TXT)

    diamond(d, CX, yQ, 420*S, 150*S, AMB_F, AMB_B)
    center_lines(d, CX, yQ, wrap(d, "Fresh page-wiki.md exists?", f_node, 300*S), f_node, TXT)

    rrect(d, xGEN, yGEN, 430*S, NH, 12*S, AMB_F, AMB_B)
    center_lines(d, xGEN, yGEN, wrap(d, "LLM produces or refreshes page-wiki.md and anchors it", f_node, 400*S), f_node, TXT)

    rrect(d, CX, yRE, 430*S, NH, 12*S, GRN_F, GRN_B)
    center_lines(d, CX, yRE, ["Reuse the page — source NOT re-read"], f_node, (220,252,231))

    rrect(d, CX, yW, 300*S, NH, 12*S, NEU_F, NEU_B)
    center_lines(d, CX, yW, ["Do the work"], f_node, TXT)

    subroutine(d, CX, yN, 520*S, NH, 12*S, WIKI_F, WIKI_B)
    center_lines(d, CX, yN, ["Next session or teammate reuses it"], f_node, (220,252,231))

    # edges
    arrow(d, CX, yP+33*S, CX, yR-NH/2, ARR)
    arrow(d, CX, yR+NH/2, CX, yQ-75*S, ARR)
    # yes -> RE (straight down through left of diamond)
    arrow(d, CX, yQ+75*S, CX, yRE-NH/2, GRNARR)
    d.text((CX+12*S, (yQ+75*S+yRE-NH/2)//2 - 10*S), "yes", font=f_lbl, fill=GRNARR)
    # no/stale -> GEN (diamond right to gen)
    arrow(d, CX+210*S, yQ, xGEN, yGEN-NH/2, AMB_B)
    d.text((CX+230*S, yQ-40*S), "no / stale", font=f_lbl, fill=AMB_B)
    # GEN -> RE (down-left back to reuse)
    arrow(d, xGEN, yGEN+NH/2, CX+215*S, yRE, AMB_B)
    # RE -> W
    arrow(d, CX, yRE+NH/2, CX, yW-NH/2, GRNARR)
    # W -> N
    arrow(d, CX, yW+NH/2, CX, yN-NH/2, ARR)

    out="D:/Github/arungudelli/static/images/page-wiki-team-pipeline.png"
    img.save(out); print("saved", out, img.size)

# ============================================================
# DIAGRAM 1 — sequence: resolve, check freshness, reuse-or-refresh
# ============================================================
def sequence():
    W, H = 1300*S, 940*S
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    grid(d, W, H)
    f_title = font(["seguisb.ttf","segoeuib.ttf"], 22*S)
    f_head  = font(["seguisb.ttf","segoeuib.ttf"], 17*S)
    f_msg   = font(["segoeui.ttf"], 15*S)
    f_lbl   = font(["seguibl.ttf","segoeuib.ttf"], 14*S)

    d.text((40*S, 26*S), "One request: resolve, check freshness, reuse or refresh", font=f_title, fill=TXT)

    actors=[("You","You",150*S,TEAL_B,TEAL_F),("LLM","LLM / Agent",420*S,NEU_B,NEU_F),
            ("wiki-index","wiki-index",680*S,NEU_B,NEU_F),("page-wiki.md","page-wiki.md",930*S,WIKI_B,WIKI_F),
            ("Source code","Source code",1180*S,NEU_B,NEU_F)]
    top=90*S; bot=880*S
    xs={}
    for key,name,x,bd,fl in actors:
        xs[key]=x
        rrect(d, x, top, 200*S, 52*S, 10*S, fl, bd)
        w=d.textlength(name, font=f_head); d.text((x-w/2, top-f_head.size/2), name, font=f_head, fill=TXT)
        # lifeline
        seg=top+30*S
        while seg<bot:
            d.line([(x,seg),(x,min(seg+8*S,bot))], fill=(50,58,68), width=1*S); seg+=14*S

    def msg(y, a, b, text, dashed=False, color=ARR):
        x1,x2=xs[a],xs[b]
        arrow(d, x1 + (10*S if x2>x1 else -10*S), y, x2 + (-10*S if x2>x1 else 10*S), y, color, dashed=dashed)
        t=text; cx=(x1+x2)/2; w=d.textlength(t, font=f_msg)
        d.text((cx-w/2, y-f_msg.size-6*S), t, font=f_msg, fill=TXT)

    y=170*S
    msg(y, "You","LLM","Add a search box to the book list page"); y+=64*S
    msg(y, "LLM","wiki-index","Which page maps to this prompt?"); y+=64*S
    msg(y, "wiki-index","LLM","book-list + its source file list", dashed=True); y+=64*S
    msg(y, "LLM","page-wiki.md","Read one distilled page"); y+=64*S
    msg(y, "LLM","Source code","Re-hash files, compare to stored hashes"); y+=40*S

    # alt frame
    fx1, fx2 = xs["LLM"]-150*S, xs["Source code"]+120*S
    fy1 = y
    fy2 = y + 330*S
    d.rounded_rectangle([fx1,fy1,fx2,fy2], radius=8*S, outline=(70,80,92), width=2*S)
    # alt tab
    d.rectangle([fx1, fy1, fx1+70*S, fy1+30*S], fill=(70,80,92))
    d.text((fx1+12*S, fy1+6*S), "alt", font=f_lbl, fill=(13,17,23))
    d.text((fx1+84*S, fy1+6*S), "All hashes match  →  FRESH", font=f_lbl, fill=GRNARR)

    yy=fy1+70*S
    msg(yy, "Source code","LLM","Unchanged", dashed=True, color=GRNARR); yy+=46*S
    # note box
    nx1,nx2=xs["LLM"]-120*S, xs["Source code"]+90*S
    d.rounded_rectangle([nx1,yy-4*S,nx2,yy+40*S], radius=6*S, fill=(10,26,16), outline=GRN_B, width=1*S)
    nt="Reuse the page — source is NOT re-read"; w=d.textlength(nt,font=f_msg)
    d.text(((nx1+nx2)/2-w/2, yy+8*S), nt, font=f_msg, fill=(220,252,231)); yy+=70*S

    # else divider
    d.line([(fx1,yy),(fx2,yy)], fill=(70,80,92), width=1*S)
    d.text((fx1+12*S, yy+6*S), "else  a file drifted  →  STALE", font=f_lbl, fill=AMB_B); yy+=44*S
    msg(yy, "Source code","LLM","Return only the changed files", dashed=True, color=AMB_B); yy+=52*S
    msg(yy, "LLM","page-wiki.md","Update the summary + re-anchor", color=AMB_B)

    y=fy2+56*S
    msg(y, "LLM","You","Edit the right files, gotchas already known", dashed=True, color=GRNARR)

    out="D:/Github/arungudelli/static/images/page-wiki-query-flow.png"
    img.save(out); print("saved", out, img.size)

flowchart()
sequence()
