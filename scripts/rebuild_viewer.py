#!/usr/bin/env python3
"""Regenerate pre-rendered viewer with syntax data."""

import json

with open("/root/projects/english-grammar-db/data/english_grammar_cefr.json") as f: cefr = json.load(f)
with open("/root/projects/english-grammar-db/data/english_grammar_american.json") as f: am = json.load(f)

def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def build_tree(db_obj, sys_name):
    LC = ['l1','l2','l3','l4','l5','l6']; BC = ['b1','b2','b3','b4','b5','b6']
    h = f'<div class="sys-section" id="sys-{sys_name}">\n'
    for li, (ln, ld) in enumerate(db_obj["levels"].items()):
        lc, bc = LC[li] if li<6 else 'l1', BC[li] if li<6 else 'b1'
        pts = sum(len(s["points"]) for c in ld["categories"] for s in c["subs"])
        h += f'<div class="tn"><div class="tr {lc}" style="padding-left:0" onclick="tog(this)"><span class="tw">▶</span><span class="ti">📊</span><span class="tl"><strong>{esc(ln)}</strong></span><span class="tb {bc}">{pts} pts</span></div><div class="tc hidden">'
        for cat in ld["categories"]:
            is_ir="Irregular" in cat["category"]; is_pv="Phrasal" in cat["category"]; is_sy="Syntax" in cat["category"]
            icon = "🔄" if is_ir else ("📝" if is_pv else ("🔷" if is_sy else "📁"))
            rcls = "ir-row" if is_ir else ("pv-row" if is_pv else ("sy-row" if is_sy else ""))
            csubs = len(cat["subs"]); cpts = sum(len(s["points"]) for s in cat["subs"])
            h += f'<div class="tn"><div class="tr {rcls}" style="padding-left:18" onclick="tog(this)"><span class="tw">▶</span><span class="ti">{icon}</span><span class="tl">{esc(cat["category"])}</span><span class="tb {bc}">{csubs} sub</span></div><div class="tc hidden">'
            for sub in cat["subs"]:
                spts = len(sub["points"]); sn = sub.get("subcategory", sub.get("name",""))
                h += f'<div class="tn"><div class="tr {rcls}" style="padding-left:36" onclick="tog(this)"><span class="tw">▶</span><span class="ti">📋</span><span class="tl">{esc(sn)}</span><span class="tb {bc}">{spts} pts</span></div><div class="tc hidden">'
                for pt in sub["points"]:
                    h += f'<div class="tr" style="padding-left:54"><span class="ti">•</span><span class="tl">{esc(pt)}</span></div>'
                h += '</div></div>'
            h += '</div></div>'
        h += '</div></div>'
    h += '</div>'
    return h

cefr_html = build_tree(cefr, "CEFR")
am_html = build_tree(am, "American")

html = '''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>English Grammar Database</title><style>
:root{--bg:#0d1117;--s:#161b22;--b:#30363d;--t:#c9d1d9;--dim:#8b949e;--a:#58a6ff;--c1:#58a6ff;--c2:#3fb950;--c3:#d2991d;--c4:#db6d28;--c5:#f778ba;--c6:#bc8cff}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--t);display:flex;height:100vh;overflow:hidden}
aside{width:240px;min-width:240px;background:var(--s);border-right:1px solid var(--b);display:flex;flex-direction:column;overflow-y:auto;padding:12px}
aside h1{font-size:13px;color:var(--a);margin-bottom:10px}aside button{display:block;width:100%;padding:8px;margin:4px 0;background:var(--b);border:none;border-radius:5px;color:var(--t);cursor:pointer;font-size:11px;text-align:left}
aside button:hover{background:#3a4450}aside button.active{background:var(--a);color:#000;font-weight:600}
aside .ir{background:rgba(219,109,40,.2);color:var(--c4)}aside .pv{background:rgba(247,119,186,.2);color:var(--c5)}
aside .sy{background:rgba(88,166,255,.15);color:var(--a)}aside .info{font-size:9px;color:var(--dim);margin-top:8px;line-height:1.4}
main{flex:1;display:flex;flex-direction:column;overflow:hidden}header{padding:8px 14px;border-bottom:1px solid var(--b);background:var(--s);display:flex;gap:8px}
header input{flex:1;padding:8px 12px;background:var(--bg);border:1px solid var(--b);border-radius:6px;color:var(--t);font-size:13px}
header input::placeholder{color:var(--dim)}header span{font-size:11px;color:var(--dim);white-space:nowrap;align-self:center}
#tree{flex:1;overflow-y:auto;padding:6px 0;scroll-behavior:smooth}
.tr{display:flex;align-items:center;padding:3px 10px;cursor:pointer;border-left:3px solid transparent;min-height:26px;user-select:none}
.tr:hover{background:rgba(88,166,255,.07)}.tr.match{background:rgba(210,153,29,.1);border-left-color:var(--c3)}
.tw{width:14px;height:14px;display:inline-flex;align-items:center;justify-content:center;font-size:8px;color:var(--dim);flex-shrink:0;margin-right:3px;transition:transform .15s}
.tw.open{transform:rotate(90deg)}.ti{margin-right:3px;font-size:12px;flex-shrink:0}
.tl{font-size:11px;line-height:1.3;flex:1;overflow:hidden;text-overflow:ellipsis}.tl .hl{background:rgba(210,153,29,.5);border-radius:2px;padding:0 1px;font-weight:bold}
.tb{font-size:8px;padding:1px 4px;border-radius:3px;font-weight:600;margin-left:5px;flex-shrink:0}
.tc{overflow:hidden;transition:max-height .15s ease}.tc.hidden{max-height:0!important}
.l1{color:var(--c1)}.b1{background:rgba(88,166,255,.18);color:var(--c1)}.l2{color:var(--c2)}.b2{background:rgba(63,185,80,.18);color:var(--c2)}
.l3{color:var(--c3)}.b3{background:rgba(210,153,29,.18);color:var(--c3)}.l4{color:var(--c4)}.b4{background:rgba(219,109,40,.18);color:var(--c4)}
.l5{color:var(--c5)}.b5{background:rgba(247,119,186,.18);color:var(--c5)}.l6{color:var(--c6)}.b6{background:rgba(188,140,255,.18);color:var(--c6)}
.ir-row{border-left:3px solid var(--c4)!important;background:rgba(219,109,40,.04)}.pv-row{border-left:3px solid var(--c5)!important;background:rgba(247,119,186,.04)}
.sy-row{border-left:3px solid var(--a)!important;background:rgba(88,166,255,.04)}
#sys-American{display:none}@media(max-width:768px){body{flex-direction:column}aside{width:100%;min-width:100%;max-height:150px}}
::-webkit-scrollbar{width:4px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--b);border-radius:2px}
</style></head><body>
<aside><h1>📚 Grammar DB</h1>
<button class="active" onclick="switchSys('CEFR',this)">🇪🇺 CEFR (A1→C2)</button>
<button onclick="switchSys('American',this)">🇺🇸 American (L1→L6)</button>
<button onclick="expandAll()">📂 Expandir todo</button><button onclick="collapseAll()">📁 Colapsar todo</button>
<button class="sy" onclick="jump('syntax')">🔷 Syntax and Sentences</button>
<button class="ir" onclick="jump('irregular')">🔄 Irregular Verbs</button>
<button class="pv" onclick="jump('phrasal')">📝 Phrasal Verbs</button>
<div class="info">CEFR: 603 gr + 466 verb<br>American: 878 gr + 466 verb<br>Total: 2,413 items</div></aside>
<main><header><input id="q" placeholder="🔍 Buscar (Ctrl+K)..." oninput="search()"><span id="rc"></span></header><div id="tree">''' + cefr_html + am_html + '''</div></main>
<script>
function tog(el){var tc=el.closest(".tn").querySelector(":scope>.tc"),tw=el.querySelector(".tw");if(!tc)return;if(tc.classList.contains("hidden")){tc.classList.remove("hidden");tw.classList.add("open")}else{tc.classList.add("hidden");tw.classList.remove("open")}}
function switchSys(sys,btn){document.querySelectorAll("#tree>.sys-section").forEach(function(s){s.style.display="none"});document.getElementById("sys-"+sys).style.display="";document.querySelectorAll("aside button").forEach(function(b){b.classList.remove("active")});btn.classList.add("active");collapseAll()}
function search(){var q=document.getElementById("q").value.toLowerCase().trim();var vis=document.getElementById("sys-CEFR").style.display!=="none"?"CEFR":"American";var sec=document.getElementById("sys-"+vis);var all=sec.querySelectorAll(".tr");var c=0;all.forEach(function(t){t.classList.remove("match")});sec.querySelectorAll(".tc").forEach(function(t){t.classList.add("hidden")});sec.querySelectorAll(".tw").forEach(function(t){t.classList.remove("open")});if(!q){document.getElementById("rc").textContent="";return}var m=[];all.forEach(function(t){if((t.querySelector(".tl")?t.querySelector(".tl").textContent:"").toLowerCase().indexOf(q)>=0)m.push(t)});m.forEach(function(t){t.classList.add("match");var p=t.closest(".tn");while(p){var tc=p.querySelector(":scope>.tc");if(tc)tc.classList.remove("hidden");var tw=p.querySelector(":scope>.tr>.tw");if(tw)tw.classList.add("open");p=p.parentElement?p.parentElement.closest(".tn"):null}c++});document.getElementById("rc").textContent=c+" matches"}
function jump(type){var vis=document.getElementById("sys-CEFR").style.display!=="none"?"CEFR":"American";var sec=document.getElementById("sys-"+vis);var kw=type==="irregular"?"irregular verbs":(type==="phrasal"?"phrasal verbs":"syntax");sec.querySelectorAll(".tc").forEach(function(t){t.classList.remove("hidden")});sec.querySelectorAll(".tw").forEach(function(t){t.classList.add("open")});var all=sec.querySelectorAll(".tr");for(var i=0;i<all.length;i++){var t=all[i];var txt=(t.querySelector(".tl")?t.querySelector(".tl").textContent:"").toLowerCase();if(txt.indexOf(kw)>=0){t.scrollIntoView({behavior:"smooth",block:"center"});t.style.background="rgba(88,166,255,.2)";setTimeout(function(){t.style.background=""},1500);break}}}
function expandAll(){var vis=document.getElementById("sys-CEFR").style.display!=="none"?"CEFR":"American";document.getElementById("sys-"+vis).querySelectorAll(".tc").forEach(function(t){t.classList.remove("hidden")});document.getElementById("sys-"+vis).querySelectorAll(".tw").forEach(function(t){t.classList.add("open")})}
function collapseAll(){var vis=document.getElementById("sys-CEFR").style.display!=="none"?"CEFR":"American";document.getElementById("sys-"+vis).querySelectorAll(".tc").forEach(function(t){t.classList.add("hidden")});document.getElementById("sys-"+vis).querySelectorAll(".tw").forEach(function(t){t.classList.remove("open")})}
document.addEventListener("keydown",function(e){if((e.ctrlKey||e.metaKey)&&e.key==="k"){e.preventDefault();document.getElementById("q").focus()}if(e.key==="Escape"){document.getElementById("q").value="";search()}});
</script></body></html>'''

with open("/root/projects/english-grammar-db/viewer/pre-rendered.html", "w") as f:
    f.write(html)
print(f"✅ Pre-rendered viewer: {len(html)} bytes")
