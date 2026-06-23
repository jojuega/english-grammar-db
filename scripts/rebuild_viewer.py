#!/usr/bin/env python3
"""
Regenerate viewer with:
- CEFR + American + BrE/AmE Discrepancies embedded
- BA-XXX references in points → clickable tooltips
- Third tab for discrepancies DB
"""
import json, re

DATA = "/root/projects/english-grammar-db/data"
OUT = "/root/projects/english-grammar-db/viewer/pre-rendered.html"

with open(f"{DATA}/english_grammar_cefr.json") as f: cefr = json.load(f)
with open(f"{DATA}/english_grammar_american.json") as f: am = json.load(f)
with open(f"{DATA}/english_grammar_bre_ame_discrepancies.json") as f: disc = json.load(f)

def esc(text):
    return text.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

# Build a lookup: ba_id → html snippet with details
disc_lookup = {}
for cat in disc["categories"]:
    for item in cat["items"]:
        ba_id = item["id"]
        ex = "".join(f"<div class=\"d-ex\">{esc(e)}</div>" for e in item.get("example_pair",[]))
        kd = f"<div class=\"d-kd\">{esc(item.get('key_difference',''))}</div>" if item.get("key_difference") else ""
        disc_lookup[ba_id] = f"""
<div class=\"d-box\" id=\"d-{ba_id}\">
  <div class=\"d-close\" onclick=\"closeDisc()\">✕</div>
  <div class=\"d-id\">{ba_id}</div>
  <div class=\"d-pt\">{esc(item['point'])}</div>
  <div class=\"d-row\"><span class=\"d-lbl\">🇬🇧 BrE:</span><span class=\"d-val\">{esc(item['bre'])}</span></div>
  <div class=\"d-row\"><span class=\"d-lbl\">🇺🇸 AmE:</span><span class=\"d-val\">{esc(item['ame'])}</span></div>
  {ex}{kd}
  <div class=\"d-lvl\">CEFR: {item.get('cefr_level','?')} · Amer: {item.get('american_level','?')}</div>
</div>"""

def fmt_point(pt):
    """Convert point string to HTML, making BA-XXX references clickable."""
    def repl(m):
        ba = m.group(1)
        icon = "🔍"
        return f'<a class="bref" data-baid="{ba}" onclick="showDisc(\'{ba}\',event)">{icon}</a>'
    html = re.sub(r'#(BA-\d{3})', repl, esc(pt))
    return html

def build_tree(db_obj, sys_name):
    LC = ['l1','l2','l3','l4','l5','l6']; BC = ['b1','b2','b3','b4','b5','b6']
    h = f'<div class="sys-section" id="sys-{sys_name}">\n'
    for li, (ln, ld) in enumerate(db_obj["levels"].items()):
        lc, bc = LC[li] if li<6 else 'l1', BC[li] if li<6 else 'b1'
        pts = sum(len(s["points"]) for c in ld["categories"] for s in c["subs"])
        h += f'<div class="tn"><div class="tr {lc}" onclick="tog(this)"><span class="tw">▶</span><span class="ti">📊</span><span class="tl"><strong>{esc(ln)}</strong></span><span class="tb {bc}">{pts} pts</span></div><div class="tc hidden">'
        for cat in ld["categories"]:
            is_ir="Irregular" in cat["category"]; is_pv="Phrasal" in cat["category"]; is_sy="Syntax" in cat["category"]
            icon = "🔄" if is_ir else ("📝" if is_pv else ("🔷" if is_sy else "📁"))
            rcls = "ir-row" if is_ir else ("pv-row" if is_pv else ("sy-row" if is_sy else ""))
            csubs = len(cat["subs"]); cpts = sum(len(s["points"]) for s in cat["subs"])
            h += f'<div class="tn"><div class="tr {rcls}" onclick="tog(this)"><span class="tw">▶</span><span class="ti">{icon}</span><span class="tl">{esc(cat["category"])}</span><span class="tb {bc}">{csubs} sub</span></div><div class="tc hidden">'
            for sub in cat["subs"]:
                spts = len(sub["points"]); sn = sub.get("subcategory", sub.get("name",""))
                h += f'<div class="tn"><div class="tr {rcls}" onclick="tog(this)"><span class="tw">▶</span><span class="ti">📋</span><span class="tl">{esc(sn)}</span><span class="tb">{spts} pts</span></div><div class="tc hidden">'
                for pt in sub["points"]:
                    h += f'<div class="tr pt" style="padding-left:54"><span class="ti">•</span><span class="tl">{fmt_point(pt)}</span></div>'
                h += '</div></div>'
            h += '</div></div>'
        h += '</div></div>'
    h += '</div>'
    return h

def build_discrepancies_tree():
    h = '<div class="sys-section" id="sys-Discrepancies">\n'
    for cat in disc["categories"]:
        items = cat.get("items",[])
        h += f'<div class="tn"><div class="tr l3" onclick="tog(this)"><span class="tw">▶</span><span class="ti">🔬</span><span class="tl"><strong>{esc(cat["name"])}</strong></span><span class="tb b3">{len(items)}</span></div><div class="tc hidden">'
        for item in items:
            ba = item["id"]
            ex = "".join(f"<div class=\"d-ex\">{esc(e)}</div>" for e in item.get("example_pair",[]))
            kd = f"<div class=\"d-kd\">{esc(item.get('key_difference',''))}</div>" if item.get("key_difference") else ""
            h += f'''
<div class="tr pt" style="padding-left:18;flex-wrap:wrap;min-height:auto;padding:6px 10px 6px 18">
  <span class="ti">⚡</span>
  <span class="tl" style="font-weight:600;color:var(--c4)">#{ba}</span>
  <span class="tl" style="width:100%;margin-top:2px;font-size:10px;color:var(--t)">{esc(item["point"])}</span>
  <div style="width:100%;display:flex;gap:6px;margin-top:4px;font-size:10px;line-height:1.3">
    <span style="color:var(--c1);min-width:35px">🇬🇧</span><span>{esc(item["bre"])}</span>
  </div>
  <div style="width:100%;display:flex;gap:6px;font-size:10px;line-height:1.3">
    <span style="color:var(--c4);min-width:35px">🇺🇸</span><span>{esc(item["ame"])}</span>
  </div>
  {ex}{kd}
  <div style="width:100%;font-size:8px;color:var(--dim);margin-top:2px">{item.get("cefr_level","")} · {item.get("american_level","")}</div>
</div>'''
        h += '</div></div>'
    h += '</div>'
    return h

cefr_html = build_tree(cefr, "CEFR")
am_html = build_tree(am, "American")
disc_html = build_discrepancies_tree()

# Tooltip overlay HTML (all discrepancy boxes hidden by default)
tooltips = "".join(disc_lookup.values())
# Default hidden
tooltips = tooltips.replace('class="d-box"', 'class="d-box hidden"')

# Build stats
cefr_gr = sum(len(s["points"]) for l in cefr["levels"].values() for c in l["categories"] for s in c["subs"])
ame_gr = sum(len(s["points"]) for l in am["levels"].values() for c in l["categories"] for s in c["subs"])
disc_total = sum(len(c["items"]) for c in disc["categories"])

html = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>English Grammar Database</title>
<style>
:root{--bg:#0d1117;--s:#161b22;--b:#30363d;--t:#c9d1d9;--dim:#8b949e;--a:#58a6ff;--c1:#58a6ff;--c2:#3fb950;--c3:#d2991d;--c4:#db6d28;--c5:#f778ba;--c6:#bc8cff}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--t);display:flex;height:100vh;overflow:hidden}
aside{width:240px;min-width:240px;background:var(--s);border-right:1px solid var(--b);display:flex;flex-direction:column;overflow-y:auto;padding:12px}
aside h1{font-size:13px;color:var(--a);margin-bottom:10px}aside button{display:block;width:100%;padding:8px;margin:4px 0;background:var(--b);border:none;border-radius:5px;color:var(--t);cursor:pointer;font-size:11px;text-align:left}
aside button:hover{background:#3a4450}aside button.active{background:var(--a);color:#000;font-weight:600}
aside .ir{background:rgba(219,109,40,.2);color:var(--c4)}aside .pv{background:rgba(247,119,186,.2);color:var(--c5)}aside .sy{background:rgba(88,166,255,.15);color:var(--a)}aside .ba{background:rgba(188,140,255,.2);color:var(--c6)}aside .ba.active{background:var(--c6);color:#000}
aside .info{font-size:9px;color:var(--dim);margin-top:8px;line-height:1.4}
main{flex:1;display:flex;flex-direction:column;overflow:hidden}header{padding:8px 14px;border-bottom:1px solid var(--b);background:var(--s);display:flex;gap:8px}
header input{flex:1;padding:8px 12px;background:var(--bg);border:1px solid var(--b);border-radius:6px;color:var(--t);font-size:13px}
header input::placeholder{color:var(--dim)}header span{font-size:11px;color:var(--dim);white-space:nowrap;align-self:center}
#tree{flex:1;overflow-y:auto;padding:6px 0;scroll-behavior:smooth}
.tr{display:flex;align-items:center;padding:3px 10px;cursor:pointer;border-left:3px solid transparent;min-height:26px;user-select:none}
.tr:hover{background:rgba(88,166,255,.07)}.tr.match{background:rgba(210,153,29,.1);border-left-color:var(--c3)}
.tw{width:14px;height:14px;display:inline-flex;align-items:center;justify-content:center;font-size:8px;color:var(--dim);flex-shrink:0;margin-right:3px;transition:transform .15s}
.tw.open{transform:rotate(90deg)}.ti{margin-right:3px;font-size:12px;flex-shrink:0}
.tl{font-size:11px;line-height:1.3;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.tl .hl{background:rgba(210,153,29,.5);border-radius:2px;padding:0 1px;font-weight:bold}
/* Point rows with annotations: allow wrapping */
.tr.pt{white-space:normal;overflow:visible;min-height:auto}.tr.pt .tl{white-space:normal;overflow:visible;text-overflow:clip}
.tb{font-size:8px;padding:1px 4px;border-radius:3px;font-weight:600;margin-left:5px;flex-shrink:0}
.tc{overflow:hidden;transition:max-height .15s ease}.tc.hidden{max-height:0!important}
.l1{color:var(--c1)}.b1{background:rgba(88,166,255,.18);color:var(--c1)}.l2{color:var(--c2)}.b2{background:rgba(63,185,80,.18);color:var(--c2)}
.l3{color:var(--c3)}.b3{background:rgba(210,153,29,.18);color:var(--c3)}.l4{color:var(--c4)}.b4{background:rgba(219,109,40,.18);color:var(--c4)}
.l5{color:var(--c5)}.b5{background:rgba(247,119,186,.18);color:var(--c5)}.l6{color:var(--c6)}.b6{background:rgba(188,140,255,.18);color:var(--c6)}
.ir-row{border-left:3px solid var(--c4)!important;background:rgba(219,109,40,.04)}.pv-row{border-left:3px solid var(--c5)!important;background:rgba(247,119,186,.04)}
.sy-row{border-left:3px solid var(--a)!important;background:rgba(88,166,255,.04)}
#sys-American,#sys-Discrepancies{display:none}
/* BrE/AmE reference links */
.bref{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:rgba(188,140,255,.25);color:var(--c6);cursor:pointer;font-size:10px;margin:0 2px;text-decoration:none;vertical-align:middle}
.bref:hover{background:var(--c6);color:#000}
/* Tooltip overlay */
#d-overlay{position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.5);z-index:100;display:none}
.d-box{position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);width:500px;max-width:90%;max-height:80vh;overflow-y:auto;background:var(--s);border:1px solid var(--b);border-radius:8px;padding:16px;z-index:101;box-shadow:0 8px 32px rgba(0,0,0,.5)}
.d-box.hidden{display:none}.d-close{position:absolute;top:8px;right:10px;cursor:pointer;color:var(--dim);font-size:16px}.d-close:hover{color:var(--t)}
.d-id{color:var(--c4);font-weight:700;font-size:10px;margin-bottom:4px}.d-pt{font-size:12px;font-weight:600;margin-bottom:8px}
.d-row{display:flex;gap:8px;margin-bottom:6px;font-size:11px;line-height:1.4}.d-lbl{font-weight:600;white-space:nowrap;flex-shrink:0;min-width:35px}
.d-ex{background:rgba(88,166,255,.1);border-left:2px solid var(--a);padding:4px 8px;margin:3px 0;font-size:10px;font-family:monospace;border-radius:0 3px 3px 0}
.d-kd{background:rgba(210,153,29,.1);border-left:2px solid var(--c3);padding:4px 8px;margin:4px 0;font-size:10px;border-radius:0 3px 3px 0;line-height:1.4}
.d-lvl{font-size:9px;color:var(--dim);margin-top:6px}
@media(max-width:768px){.d-box{width:90%}}
/* Inline discrepancies view (in third tab) */
.d-tr{display:flex;align-items:center;padding:3px 10px;min-height:26px}
@media(max-width:768px){body{flex-direction:column}aside{width:100%;min-width:100%;max-height:150px}}
::-webkit-scrollbar{width:4px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--b);border-radius:2px}
</style></head><body>
<aside><h1>📚 Grammar DB</h1>
<button class="active" onclick="switchSys('CEFR',this)">🇪🇺 CEFR (A1→C2)</button>
<button onclick="switchSys('American',this)">🇺🇸 American (L1→L6)</button>
<button class="ba" onclick="switchSys('Discrepancies',this)">🔬 BrE vs AmE</button>
<button onclick="expandAll()">📂 Expandir todo</button><button onclick="collapseAll()">📁 Colapsar todo</button>
<button class="sy" onclick="jump('syntax')">🔷 Syntax and Sentences</button>
<button class="ir" onclick="jump('irregular')">🔄 Irregular Verbs</button>
<button class="pv" onclick="jump('phrasal')">📝 Phrasal Verbs</button>
<div class="info">CEFR: ''' + str(cefr_gr) + ''' gr + 466 verb<br>American: ''' + str(ame_gr) + ''' gr + 466 verb<br>BrE/AmE: ''' + str(disc_total) + ''' discrepancies<br>Total: ''' + str(cefr_gr + ame_gr + disc_total + 932) + ''' items</div></aside>
<main><header><input id="q" placeholder="🔍 Buscar (Ctrl+K)..." oninput="search()"><span id="rc"></span></header><div id="tree">''' + cefr_html + am_html + disc_html + '''</div></main>
<div id="d-overlay" onclick="closeDisc()"></div>''' + tooltips + '''
<script>
function tog(el){var tc=el.closest(".tn").querySelector(":scope>.tc"),tw=el.querySelector(".tw");if(!tc)return;if(tc.classList.contains("hidden")){tc.classList.remove("hidden");tw.classList.add("open")}else{tc.classList.add("hidden");tw.classList.remove("open")}}
function switchSys(sys,btn){document.querySelectorAll("#tree>.sys-section").forEach(function(s){s.style.display="none"});document.getElementById("sys-"+sys).style.display="";document.querySelectorAll("aside button").forEach(function(b){b.classList.remove("active")});btn.classList.add("active");collapseAll()}
function search(){var q=document.getElementById("q").value.toLowerCase().trim();var vis=["CEFR","American","Discrepancies"];var cur=null;for(var i=0;i<vis.length;i++){if(document.getElementById("sys-"+vis[i]).style.display!=="none"){cur=vis[i];break}}if(!cur)cur="CEFR";var sec=document.getElementById("sys-"+cur);var all=sec.querySelectorAll(".tr");var c=0;all.forEach(function(t){t.classList.remove("match")});sec.querySelectorAll(".tc").forEach(function(t){t.classList.add("hidden")});sec.querySelectorAll(".tw").forEach(function(t){t.classList.remove("open")});if(!q){document.getElementById("rc").textContent="";return}var m=[];all.forEach(function(t){if((t.querySelector(".tl")?t.querySelector(".tl").textContent:"").toLowerCase().indexOf(q)>=0)m.push(t)});m.forEach(function(t){t.classList.add("match");var p=t.closest(".tn");while(p){var tc=p.querySelector(":scope>.tc");if(tc)tc.classList.remove("hidden");var tw=p.querySelector(":scope>.tr>.tw");if(tw)tw.classList.add("open");p=p.parentElement?p.parentElement.closest(".tn"):null}c++});document.getElementById("rc").textContent=c+" matches"}
function jump(type){var vis=["CEFR","American"];var cur=null;for(var i=0;i<vis.length;i++){if(document.getElementById("sys-"+vis[i]).style.display!=="none"){cur=vis[i];break}}if(!cur)cur="CEFR";var kw=type==="irregular"?"irregular verbs":(type==="phrasal"?"phrasal verbs":"syntax");document.getElementById("sys-"+cur).querySelectorAll(".tc").forEach(function(t){t.classList.remove("hidden")});document.getElementById("sys-"+cur).querySelectorAll(".tw").forEach(function(t){t.classList.add("open")});var all=document.getElementById("sys-"+cur).querySelectorAll(".tr");for(var i=0;i<all.length;i++){var t=all[i];var txt=(t.querySelector(".tl")?t.querySelector(".tl").textContent:"").toLowerCase();if(txt.indexOf(kw)>=0){t.scrollIntoView({behavior:"smooth",block:"center"});t.style.background="rgba(88,166,255,.2)";setTimeout(function(){t.style.background=""},1500);break}}}
function expandAll(){var vis=["CEFR","American","Discrepancies"];for(var v=0;v<vis.length;v++){var s=document.getElementById("sys-"+vis[v]);if(s.style.display!=="none"){s.querySelectorAll(".tc").forEach(function(t){t.classList.remove("hidden")});s.querySelectorAll(".tw").forEach(function(t){t.classList.add("open")});break}}}
function collapseAll(){var vis=["CEFR","American","Discrepancies"];for(var v=0;v<vis.length;v++){var s=document.getElementById("sys-"+vis[v]);if(s.style.display!=="none"){s.querySelectorAll(".tc").forEach(function(t){t.classList.add("hidden")});s.querySelectorAll(".tw").forEach(function(t){t.classList.remove("open")});break}}}
function showDisc(baId,evt){evt.stopPropagation();var el=document.getElementById("d-"+baId);if(!el)return;document.getElementById("d-overlay").style.display="block";el.classList.remove("hidden")}
function closeDisc(){document.getElementById("d-overlay").style.display="none";document.querySelectorAll(".d-box").forEach(function(b){b.classList.add("hidden")})}
document.addEventListener("keydown",function(e){if((e.ctrlKey||e.metaKey)&&e.key==="k"){e.preventDefault();document.getElementById("q").focus()}if(e.key==="Escape"){closeDisc();document.getElementById("q").value="";search()}});
</script></body></html>'''

with open(OUT, "w") as f:
    f.write(html)

print(f"✅ Viewer: {len(html)} bytes")
print(f"   CEFR: {cefr_gr} gr · American: {ame_gr} gr · Discrepancies: {disc_total}")
