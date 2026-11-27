#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build A5 reading PDF from approved revision source and archival Canva thumbnails.
This workflow version is reading-quality, NOT the local 44 MB print artwork original.
"""
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageOps
import fitz, json, os, re, hashlib, urllib.request, time

ROOT=Path(__file__).resolve().parents[1]
MD=ROOT/"fuentes/MANUSCRITO_V4_06_1_REV03_CIERRES_APLICADOS.md"
URLS=ROOT/"materiales/canva_rev02_miniaturas_origen_REV03.json"
ASSETS=ROOT/"materiales/miniaturas_canva_REV02"
OUT=ROOT/"ediciones/V4_06_1_REV03"
OUT.mkdir(parents=True,exist_ok=True)
ASSETS.mkdir(parents=True,exist_ok=True)
manifest=json.loads(URLS.read_text("utf-8"))
u={int(k):v for k,v in manifest["images"].items()}
for n,url in u.items():
    path=ASSETS/f"pagina_{n:03}.png"
    if path.exists() and path.stat().st_size>500:continue
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (book archival pipeline)"})
    with urllib.request.urlopen(req,timeout=40) as resp:
        data=resp.read()
    im=Image.open(BytesIO(data)).convert("RGB")
    if min(im.size)<90:raise RuntimeError(f"Unexpected thumbnail: {n} {im.size}")
    im.save(path,optimize=True)
    time.sleep(.10)
assert all((ASSETS/f"pagina_{n:03}.png").exists() for n in u)
text=MD.read_text("utf-8")
parts=re.split(r"(?m)^# (.+)\n",text)
chapters={parts[i]:parts[i+1].strip() for i in range(1,len(parts),2)}
assert len(chapters)==16
P=fitz.open()
W,H=419.528,595.276
regular_path="/usr/share/fonts/truetype/freefont/FreeSerif.ttf"
bold_path="/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf"
if not Path(regular_path).exists():
    regular_path="/usr/share/fonts/opentype/freefont/FreeSerif.otf"
    bold_path="/usr/share/fonts/opentype/freefont/FreeSerifBold.otf"
font=fitz.Font(fontfile=regular_path)
S=10.5;LD=13.7;X0=54.3;X1=W-54.3;WM=X1-X0;BOTTOM=544
def page():
    p=P.new_page(width=W,height=H)
    p.insert_font(fontname="FS",fontfile=regular_path)
    p.insert_font(fontname="FSB",fontfile=bold_path)
    return p
def number(p):
    t=str(len(P));p.insert_text(((W-font.text_length(t,fontsize=10.5))/2,566),t,fontname="FS",fontsize=10.5)
def imagepage(n):
    p=page();p.insert_image(fitz.Rect(0,0,W,H),filename=str(ASSETS/f"pagina_{n:03}.png"));return p
for n in [1,2]:imagepage(n)
index=page()
for n in range(4,15):imagepage(n)
source_open=[15,17,27,33,40,49,57,66,79,85,98,106,117,123,133,138]
start_pages={}
def get_page(first,pageindex=None):
    p=page()
    if first:
        orig=Image.open(ASSETS/f"pagina_{pageindex:03}.png").convert("RGB")
        crop=orig.crop((0,0,orig.width,int(orig.height*0.49)))
        buf=BytesIO();crop.save(buf,format="PNG")
        p.insert_image(fitz.Rect(0,0,W,291),stream=buf.getvalue())
        # Chapter opener starts with dropcap below original banner and illustration.
        return p,326
    return p,61.5
def wrap(txt,indent=0):
    words=txt.split();res=[];line=[]
    for wd in words:
        limit=WM-(indent if not res else 0)
        candidate=" ".join(line+[wd])
        if not line or font.text_length(candidate,fontsize=S)<=limit:line.append(wd)
        else:res.append(" ".join(line));line=[wd]
    if line:res.append(" ".join(line))
    return res
def put(p,t,y,indent=0):
    p.insert_text((X0+indent,y),t,fontname="FS",fontsize=S)
for ci,(name,body) in enumerate(chapters.items()):
    start_pages[name]=len(P)+1
    p,y=get_page(True,source_open[ci])
    first=True
    for para in [x.strip() for x in body.split("\n\n") if x.strip()]:
        if para.startswith("[Lámina interior original:"):
            number(p)
            p=imagepage(81);number(p)
            p,y=get_page(False)
            continue
        if first:
            txt=para[1:];lines=wrap(txt,22)
            p.insert_text((X0,y+2),para[0],fontname="FSB",fontsize=28)
            for li,line in enumerate(lines):
                if y>BOTTOM:number(p);p,y=get_page(False)
                put(p,line,y,22 if li==0 else 0);y+=LD
            y+=6;first=False;continue
        lines=wrap(para)
        if y+(min(2,len(lines))-1)*LD>BOTTOM:number(p);p,y=get_page(False)
        for line in lines:
            if y>BOTTOM:number(p);p,y=get_page(False)
            put(p,line,y);y+=LD
        y+=6
    number(p)
# Index with updated page numbers
index=P[2]  # reload page after page insertions; prior handle is orphaned
index.insert_text((184,83),"Índice",fontname="FSB",fontsize=20)
index.draw_line((58,104),(W-58,104),color=(.4,.4,.4),width=.5)
y=133
index.insert_text((63,y),"Galería de personajes",fontname="FS",fontsize=11)
index.insert_text((W-70,y),"4",fontname="FS",fontsize=11)
y+=25
for name in chapters:
    label=name.replace(" — "," · ")
    if len(label)>54:label=label[:52]+"…"
    index.insert_text((63,y),label,fontname="FS",fontsize=9.6)
    num=str(start_pages[name])
    index.insert_text((W-63-font.text_length(num,fontsize=9.6),y),num,fontname="FS",fontsize=9.6)
    y+=23
index.insert_text((W/2-2.5,566),"3",fontname="FS",fontsize=10.5)
P.set_metadata({"title":"Cuanto mejor, peor - REV03 (edicion de lectura)","author":"Victor Salesa Sanz","subject":"Version textual revisada con imagenes de referencia, no certificada para imprenta"})
pdf=OUT/"Cuanto_mejor_peor_V4_06_1_REV03_LECTURA_GITHUB.pdf"
P.save(pdf,garbage=4,deflate=True,clean=True)
pages=len(P);P.close()
summary={"pdf":str(pdf.relative_to(ROOT)),"pages":pages,"sha256":hashlib.sha256(pdf.read_bytes()).hexdigest(),"size":pdf.stat().st_size,"illustrations":"Canva page thumbnails, low resolution","prepress_approved":False,"chapters":start_pages}
(OUT/"MANIFEST_COMPILACION_GITHUB.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2),"utf-8")
print(json.dumps({k:v for k,v in summary.items() if k!="chapters"},ensure_ascii=False))
