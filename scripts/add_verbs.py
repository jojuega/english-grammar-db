#!/usr/bin/env python3
"""Add complete irregular verbs and phrasal verbs lists to grammar database.
Sources:
  - Cambridge Grammar: Table of Irregular Verbs (dictionary.cambridge.org)
  - Mango Languages: English Irregular Verbs by CEFR Level
  - Cambridge English Vocabulary Profile (EVP): phrasal verbs by level
     A1:4, A2:27, B1:135, B2:277, C1:99, C2:184
  - KotoEnglish: Phrasal Verbs by CEFR Level
"""

import json

with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "r") as f:
    db = json.load(f)

# ============================================================
# IRREGULAR VERBS BY CEFR LEVEL
# Source: Mango Languages / Cambridge Grammar
# ============================================================

irregular_verbs = {
    "A1": {
        "name": "A1 Irregular Verbs — Core Set",
        "description": "High-frequency irregular verbs essential for basic communication. First verbs encountered by beginners. Source: Cambridge Grammar, Mango Languages.",
        "verbs": [
            "be → was/were → been",
            "become → became → become",
            "begin → began → begun",
            "break → broke → broken",
            "bring → brought → brought",
            "build → built → built",
            "buy → bought → bought",
            "come → came → come",
            "cut → cut → cut",
            "do → did → done",
            "drive → drove → driven",
            "fall → fell → fallen",
            "feel → felt → felt",
            "find → found → found",
            "get → got → got/gotten (AmE: got for receiving, gotten otherwise; BrE: got)",
            "give → gave → given",
            "grow → grew → grown",
            "have → had → had",
            "hear → heard → heard",
            "hold → held → held",
            "keep → kept → kept",
            "know → knew → known",
            "lead → led → led",
            "learn → learned/learnt → learned/learnt (AmE: regular; BrE: both)",
            "leave → left → left",
            "let → let → let",
            "lose → lost → lost",
            "make → made → made",
            "mean → meant → meant",
            "meet → met → met",
            "pay → paid → paid",
            "put → put → put",
            "read → read /red/ → read /red/",
            "run → ran → run",
            "say → said → said",
            "see → saw → seen",
            "send → sent → sent",
            "sit → sat → sat",
            "sleep → slept → slept",
            "speak → spoke → spoken",
            "spend → spent → spent",
            "stand → stood → stood",
            "take → took → taken",
            "tell → told → told",
            "think → thought → thought",
            "understand → understood → understood",
            "wear → wore → worn",
            "write → wrote → written"
        ]
    },
    "A2": {
        "name": "A2 Irregular Verbs — Extended Set",
        "description": "Common irregular verbs for everyday topics and simple narratives. Source: Cambridge Grammar, Mango Languages.",
        "verbs": [
            "catch → caught → caught",
            "choose → chose → chosen",
            "cost → cost → cost",
            "draw → drew → drawn",
            "drink → drank → drunk",
            "feed → fed → fed",
            "fight → fought → fought",
            "fly → flew → flown",
            "forget → forgot → forgotten",
            "freeze → froze → frozen",
            "hide → hid → hidden",
            "hit → hit → hit",
            "hurt → hurt → hurt",
            "lend → lent → lent",
            "lie (recline) → lay → lain",
            "light → lit → lit",
            "ring → rang → rung",
            "rise → rose → risen",
            "sell → sold → sold",
            "shake → shook → shaken",
            "shoot → shot → shot",
            "shut → shut → shut",
            "sing → sang → sung",
            "sink → sank → sunk",
            "steal → stole → stolen",
            "stick → stuck → stuck",
            "strike → struck → struck",
            "sweep → swept → swept",
            "swim → swam → swum",
            "swing → swung → swung",
            "teach → taught → taught",
            "tear → tore → torn",
            "throw → threw → thrown",
            "wake → woke → woken",
            "win → won → won"
        ]
    },
    "B1": {
        "name": "B1 Irregular Verbs — Intermediate Set",
        "description": "Less common but still frequent irregular verbs for varied communication. Source: Cambridge Grammar, Mango Languages.",
        "verbs": [
            "bend → bent → bent",
            "bet → bet → bet",
            "bite → bit → bitten",
            "bleed → bled → bled",
            "blow → blew → blown",
            "broadcast → broadcast → broadcast",
            "burn → burned/burnt → burned/burnt (AmE: burned; BrE: both)",
            "burst → burst → burst",
            "creep → crept → crept",
            "deal → dealt → dealt",
            "dig → dug → dug",
            "dream → dreamed/dreamt → dreamed/dreamt",
            "flee → fled → fled",
            "forbid → forbade → forbidden",
            "forgive → forgave → forgiven",
            "hang → hung → hung (hanged only for executions)",
            "kneel → knelt/kneeled → knelt/kneeled",
            "lay → laid → laid",
            "lean → leaned/leant → leaned/leant",
            "quit → quit → quit",
            "ride → rode → ridden",
            "seek → sought → sought",
            "sew → sewed → sewn/sewed",
            "shine → shone → shone",
            "shrink → shrank → shrunk",
            "slide → slid → slid",
            "smell → smelled/smelt → smelled/smelt",
            "spell → spelled/spelt → spelled/spelt",
            "spill → spilled/spilt → spilled/spilt",
            "spin → spun → spun",
            "split → split → split",
            "spread → spread → spread",
            "spring → sprang → sprung",
            "sting → stung → stung",
            "stink → stank → stunk",
            "swear → swore → sworn",
            "swell → swelled → swollen/swelled",
            "tear → tore → torn",
            "weave → wove → woven",
            "weep → wept → wept",
            "wind → wound → wound",
            "withdraw → withdrew → withdrawn"
        ]
    },
    "B2": {
        "name": "B2 Irregular Verbs — Upper Intermediate Set",
        "description": "Lower-frequency irregular verbs for academic and professional contexts. Source: Cambridge Grammar.",
        "verbs": [
            "arise → arose → arisen",
            "awake → awoke → awoken",
            "bear → bore → borne (born for birth)",
            "beat → beat → beaten",
            "bind → bound → bound",
            "breed → bred → bred",
            "cling → clung → clung",
            "dive → dived/dove → dived (AmE: dove common as past)",
            "dwell → dwelt/dwelled → dwelt/dwelled",
            "fit → fit/fitted → fit/fitted (AmE: fit; BrE: fitted for past)",
            "forecast → forecast → forecast",
            "grind → ground → ground",
            "leap → leaped/leapt → leaped/leapt",
            "mislead → misled → misled",
            "overcome → overcame → overcome",
            "overtake → overtook → overtaken",
            "plead → pleaded/pled → pleaded/pled",
            "prove → proved → proved/proven (AmE: proven common)",
            "saw → sawed → sawn/sawed",
            "shed → shed → shed",
            "sow → sowed → sown/sowed",
            "spit → spat/spit → spat/spit",
            "stride → strode → stridden",
            "strive → strove/strived → striven/strived",
            "swell → swelled → swollen/swelled",
            "thrust → thrust → thrust",
            "tread → trod → trodden/trod",
            "undergo → underwent → undergone",
            "uphold → upheld → upheld",
            "upset → upset → upset",
            "withdraw → withdrew → withdrawn",
            "withhold → withheld → withheld",
            "withstand → withstood → withstood",
            "wring → wrung → wrung"
        ]
    },
    "C1": {
        "name": "C1/C2 Irregular Verbs — Advanced/Archaic Set",
        "description": "Rare, formal, or literary irregular verbs. Mostly passive recognition at C1, active at C2. Source: Cambridge Grammar.",
        "verbs": [
            "abide → abode/abided → abode/abided",
            "beget → begot → begotten",
            "bereave → bereft/bereaved → bereft/bereaved",
            "beseech → besought/beseeched → besought/beseeched",
            "bid (offer) → bid → bid",
            "bid (command) → bade → bidden",
            "cast → cast → cast",
            "cleave → clove/cleft → cloven/cleft",
            "forsake → forsook → forsaken",
            "gird → girded/girt → girded/girt",
            "heave → heaved/hove → heaved/hove",
            "hew → hewed → hewn/hewed",
            "mow → mowed → mown/mowed",
            "rend → rent → rent",
            "shear → sheared → shorn/sheared",
            "shoe → shod → shod",
            "slay → slew → slain",
            "sling → slung → slung",
            "slink → slunk → slunk",
            "smite → smote → smitten",
            "stave → staved/stove → staved/stove",
            "strew → strewed → strewn/strewed",
            "thrive → thrived/throve → thrived/thriven",
            "wreak → wreaked/wrought → wreaked/wrought"
        ]
    }
}

# ============================================================
# PHRASAL VERBS BY CEFR LEVEL  
# Source: Cambridge English Vocabulary Profile (EVP)
# A1:4, A2:27, B1:135, B2:277, C1:99, C2:184
# ============================================================

phrasal_verbs = {
    "A1": {
        "name": "A1 Phrasal Verbs — Physical Actions",
        "description": "Basic phrasal verbs describing visible, physical actions. Source: Cambridge EVP (4 at A1).",
        "verbs": [
            "get up — leave your bed after sleeping",
            "wake up — stop sleeping",
            "sit down — move into a sitting position",
            "stand up — rise to a standing position",
            "come in — enter a room or building",
            "go out — leave home for social reasons"
        ]
    },
    "A2": {
        "name": "A2 Phrasal Verbs — Daily Routines",
        "description": "Common phrasal verbs for everyday activities. Source: Cambridge EVP (27 at A2).",
        "verbs": [
            "turn on — start a machine, light, or device",
            "turn off — stop a machine, light, or device",
            "put on — dress yourself in clothing",
            "take off — remove clothing; leave the ground (plane)",
            "pick up — lift something; collect someone",
            "look for — try to find something",
            "look at — direct your eyes towards something",
            "look after — take care of someone or something",
            "listen to — pay attention to sound",
            "wait for — stay until something happens or someone arrives",
            "find out — discover information",
            "go back — return to a place",
            "come back — return to the speaker's location",
            "get on — enter a bus, train, plane; have good relationship",
            "get off — leave a bus, train, plane",
            "go on — continue; happen",
            "hurry up — do something more quickly",
            "lie down — put your body in a horizontal position",
            "run away — escape by running",
            "throw away — discard something",
            "try on — put on clothing to test fit",
            "write down — record in writing",
            "give back — return something to its owner",
            "take back — return something to where it was",
            "switch on/off — turn on/off (especially electrical)",
            "put away — store something in its proper place",
            "clean up — make a place clean and tidy"
        ]
    },
    "B1": {
        "name": "B1 Phrasal Verbs — Conversational Set",
        "description": "Phrasal verbs for more varied conversation. Source: Cambridge EVP (135 at B1). Representative sample.",
        "verbs": [
            "bring up — mention a topic; raise a child",
            "call off — cancel an event",
            "carry on — continue doing something",
            "come across — find by chance",
            "cut down (on) — reduce consumption",
            "deal with — handle a problem or situation",
            "drop off — deliver someone/something; fall asleep",
            "end up — finally be in a situation",
            "fall out (with) — have an argument and stop being friendly",
            "fill in — complete a form; give someone information",
            "get along (with) — have a good relationship",
            "get over — recover from illness or difficulty",
            "get through — successfully contact by phone; finish",
            "give up — stop doing something (quit)",
            "go through — experience a difficult situation",
            "grow up — become an adult",
            "hang up — end a phone call",
            "hold on — wait",
            "keep up (with) — stay at the same level",
            "let down — disappoint",
            "look forward to — anticipate with pleasure",
            "look up — search for information (dictionary/internet)",
            "make up — invent a story; reconcile after argument",
            "pass away — die (euphemism)",
            "point out — indicate or mention something",
            "put down — place something on a surface; criticize",
            "put up with — tolerate",
            "run out (of) — have no more of something",
            "set off — begin a journey",
            "set up — establish or arrange",
            "settle down — begin to live a stable life",
            "show off — try to impress others",
            "sort out — resolve a problem",
            "take over — assume control",
            "take up — begin a hobby or activity",
            "think over — consider carefully",
            "turn down — refuse an offer",
            "turn up — arrive or appear unexpectedly; increase volume",
            "work out — exercise; solve a problem; develop successfully"
        ]
    },
    "B2": {
        "name": "B2 Phrasal Verbs — Academic/Professional Set",
        "description": "Phrasal verbs for academic, professional, and formal contexts. Source: Cambridge EVP (277 at B2). Representative sample.",
        "verbs": [
            "account for — explain the reason for; constitute",
            "add up — calculate total; make sense",
            "back down — withdraw from a position",
            "blow up — explode; inflate",
            "break down — stop functioning; analyze into parts",
            "break out — start suddenly (war, fire, disease)",
            "bring about — cause to happen",
            "call for — require; demand",
            "carry out — perform a task or plan",
            "come up with — think of an idea or solution",
            "cut off — disconnect; isolate",
            "do without — manage without having something",
            "draw up — prepare a document or plan",
            "fall behind — fail to keep up",
            "figure out — understand or solve",
            "fill out — complete a form completely",
            "get away with — escape punishment",
            "get rid of — eliminate or discard",
            "give in — surrender or yield",
            "go ahead — proceed",
            "hand in — submit (homework, report)",
            "hold up — delay; rob",
            "keep off — stay away from",
            "lay off — dismiss from employment",
            "let off — excuse from punishment",
            "live up to — meet expectations",
            "look down on — regard as inferior",
            "look into — investigate",
            "make out — discern; pretend; kiss passionately",
            "pass on — transmit; die (euphemism)",
            "pick out — choose; identify",
            "pull off — succeed in doing something difficult",
            "put forward — propose an idea",
            "put off — postpone; discourage",
            "put out — extinguish; inconvenience",
            "rule out — exclude as a possibility",
            "run into — meet unexpectedly; encounter problems",
            "see off — say goodbye at departure",
            "stand for — represent; tolerate",
            "take after — resemble a family member",
            "take in — understand; deceive; accommodate",
            "talk into — persuade someone to do something",
            "think up — invent or devise",
            "turn over — give control; think about",
            "wear out — make tired; use until unusable",
            "wind up — end in a particular situation; tease",
            "wipe out — destroy completely"
        ]
    },
    "C1": {
        "name": "C1 Phrasal Verbs — Advanced Set",
        "description": "Advanced phrasal verbs for sophisticated expression. Source: Cambridge EVP (99 at C1). Representative sample.",
        "verbs": [
            "abide by — follow rules or decisions",
            "adhere to — stick to rules or principles",
            "amount to — be equivalent to; signify",
            "blurt out — say suddenly without thinking",
            "bounce back — recover quickly",
            "build on — develop from a previous idea/success",
            "capitalize on — take advantage of a situation",
            "cave in — collapse; finally agree under pressure",
            "chalk up — attribute or record",
            "clamp down on — take strong action to stop",
            "coincide with — happen at the same time",
            "conjure up — bring to mind; create magically",
            "crack down on — take severe measures against",
            "dawn on — become clear to someone",
            "detract from — reduce the quality or value",
            "dispense with — manage without; get rid of",
            "draw on — use as a resource",
            "dwell on — think about something too much",
            "embark on — begin a new project or journey",
            "fall through — fail to happen",
            "fathom out — understand something difficult",
            "fend off — defend against",
            "flesh out — add details to an idea",
            "fob off — deceive by giving something inferior",
            "gloss over — treat something superficially",
            "grapple with — struggle to deal with",
            "hinge on — depend on",
            "iron out — resolve small problems",
            "jot down — write quickly",
            "lag behind — move more slowly than others",
            "lapse into — gradually fall into a state",
            "mull over — think carefully about",
            "muster up — gather courage or energy",
            "opt for — choose",
            "pan out — develop in a particular way",
            "phase in/out — introduce/remove gradually",
            "pine for — yearn for",
            "play down — make something seem less important",
            "plough through — read/complete with difficulty",
            "press on — continue with determination",
            "prop up — support something weak",
            "resonate with — be meaningful to",
            "resort to — do something undesirable as last option",
            "scrape through — barely succeed",
            "set out — begin with a clear aim",
            "simmer down — become calm",
            "single out — choose one from a group",
            "size up — assess or evaluate",
            "skimp on — use too little of",
            "square up — settle a debt; prepare to fight",
            "stem from — originate from",
            "step down — resign from a position",
            "stumble across — find by chance",
            "sum up — summarize",
            "tamper with — interfere with something",
            "taper off — gradually decrease",
            "thrash out — discuss thoroughly to reach agreement",
            "tide over — help through a difficult period",
            "touch on — mention briefly",
            "toy with — consider casually; play with",
            "usher in — mark the beginning of",
            "veer towards — gradually move in a direction",
            "verge on — be very close to a state",
            "wade through — read or deal with something long/boring",
            "ward off — prevent or defend against",
            "wean off — gradually stop using",
            "whip up — create excitement; quickly prepare food",
            "zero in on — focus attention on"
        ]
    },
    "C2": {
        "name": "C2 Phrasal Verbs — Proficiency Set",
        "description": "Rare, formal, and highly nuanced phrasal verbs. Near-native mastery. Source: Cambridge EVP (184 at C2). Representative sample.",
        "verbs": [
            "accede to — agree to a demand",
            "acquiesce in — accept something reluctantly",
            "allude to — refer to indirectly",
            "appertain to — relate to or concern",
            "ascribe to — attribute to a cause",
            "avail of — make use of",
            "bear out — confirm or support",
            "bog down — become stuck and unable to progress",
            "broach — raise a sensitive subject",
            "buckle down — start working seriously",
            "chime in — join a conversation",
            "confide in — trust someone with secrets",
            "cotton on — begin to understand",
            "dabble in — take part casually",
            "defer to — submit to someone's authority",
            "delve into — explore in detail",
            "devolve upon — pass responsibility to",
            "disabuse of — free from a misconception",
            "divest of — take away from",
            "eke out — make limited resources last",
            "emanate from — come from a source",
            "endear to — make oneself liked",
            "entrust with — give responsibility for",
            "fawn over — flatter excessively",
            "fizzle out — end weakly",
            "gravitate towards — be naturally drawn to",
            "hanker after — desire strongly",
            "harp on — repeatedly talk about",
            "hive off — separate from a larger group",
            "impart to — communicate or transmit",
            "impinge on — have an effect on",
            "impute to — attribute (usually negative) to",
            "ingratiate with — try to gain favor",
            "inveigh against — speak critically about",
            "jockey for — compete for position",
            "kowtow to — obey slavishly",
            "lavish on — give generously to",
            "level with — be honest with",
            "lumber with — burden someone with",
            "make off with — steal and escape",
            "muse over — think about reflectively",
            "obtrude on — impose on",
            "partake of — share in; eat/drink",
            "pave the way for — create conditions for",
            "pepper with — repeatedly hit with small things",
            "pertain to — relate to",
            "pore over — study carefully",
            "predicate on — base on",
            "prevail upon — persuade",
            "prise out — extract with difficulty",
            "rake in — earn a lot of money",
            "rave about — praise enthusiastically",
            "read into — find meaning that isn't there",
            "reckon on — rely on",
            "reconcile to — come to accept",
            "refrain from — stop oneself from",
            "revel in — enjoy greatly",
            "revolve around — have as center focus",
            "rub off on — influence through contact",
            "savour of — have a quality of",
            "seize on — eagerly take advantage of",
            "set against — make someone oppose",
            "shore up — strengthen or support",
            "shrink from — avoid due to fear",
            "skate over — avoid dealing with",
            "slave away — work very hard",
            "smack of — have the quality of",
            "snap out of — quickly recover from a mood",
            "soldier on — continue despite difficulty",
            "spark off — cause to start",
            "sponge off — live at someone else's expense",
            "stake out — claim an area; watch secretly",
            "stamp out — eliminate completely",
            "stand by — support; be ready",
            "steep in — surround with a quality",
            "stick out — be noticeable; endure",
            "stoop to — lower oneself to do something",
            "strip away — remove layers",
            "succumb to — yield to pressure",
            "suss out — figure out",
            "swot up — study intensively",
            "tangle with — get into conflict with",
            "testify to — serve as evidence of",
            "tip off — give a warning secretly",
            "top up — refill to full",
            "tout as — promote as being good",
            "tuck away — store in a safe place; eat a lot",
            "vie for — compete eagerly for",
            "wade in — enter a discussion forcefully",
            "weigh up — consider carefully",
            "wheedle out — obtain through flattery",
            "winkle out — extract with difficulty",
            "wriggle out of — avoid by clever means",
            "yearn for — desire strongly",
            "yield to — submit to pressure",
            "zip through — do something very quickly"
        ]
    }
}

# ============================================================
# ADD TO DATABASE
# ============================================================

# Map American levels to CEFR
am_map = {
    "Level 1 - Beginner": "A1",
    "Level 2 - High Beginner": "A2",
    "Level 3 - Intermediate": "B1",
    "Level 4 - High Intermediate": "B2",
    "Level 5 - Advanced": "C1",
    "Level 6 - High Advanced": "C2"
}

# Add to CEFR
for lvl_name, lvl_data in db["systems"]["CEFR"]["levels"].items():
    cefr_key = lvl_name.split(" - ")[0]  # "A1 - Beginner" -> "A1"
    
    # Add irregular verbs
    if cefr_key in irregular_verbs:
        iv_data = irregular_verbs[cefr_key]
        # Check if category already exists
        iv_cat = None
        for cat in lvl_data["categories"]:
            if "Irregular Verbs" in cat["category"]:
                iv_cat = cat
                break
        
        if iv_cat is None:
            iv_cat = {
                "category": "Irregular Verbs — Complete List",
                "subs": []
            }
            lvl_data["categories"].append(iv_cat)
        
        # Check if subcategory exists
        found = False
        for sub in iv_cat["subs"]:
            if sub["subcategory"] == iv_data["name"]:
                sub["points"] = iv_data["verbs"]
                found = True
                break
        if not found:
            iv_cat["subs"].append({
                "subcategory": iv_data["name"],
                "description": iv_data["description"],
                "points": iv_data["verbs"]
            })
    
    # Add phrasal verbs  
    if cefr_key in phrasal_verbs:
        pv_data = phrasal_verbs[cefr_key]
        pv_cat = None
        for cat in lvl_data["categories"]:
            if "Phrasal Verbs" in cat["category"] and "Complete" in cat["category"]:
                pv_cat = cat
                break
        
        if pv_cat is None:
            pv_cat = {
                "category": "Phrasal Verbs — Complete List",
                "subs": []
            }
            lvl_data["categories"].append(pv_cat)
        
        found = False
        for sub in pv_cat["subs"]:
            if sub["subcategory"] == pv_data["name"]:
                sub["points"] = pv_data["verbs"]
                found = True
                break
        if not found:
            pv_cat["subs"].append({
                "subcategory": pv_data["name"],
                "description": pv_data["description"],
                "points": pv_data["verbs"]
            })

# Add to American
for lvl_name, lvl_data in db["systems"]["American"]["levels"].items():
    cefr_key = am_map.get(lvl_name, "A1")
    
    # Add irregular verbs
    if cefr_key in irregular_verbs:
        iv_data = irregular_verbs[cefr_key]
        iv_cat = None
        for cat in lvl_data["categories"]:
            if "Irregular Verbs" in cat["category"]:
                iv_cat = cat
                break
        if iv_cat is None:
            iv_cat = {"category": "Irregular Verbs — Complete List", "subs": []}
            lvl_data["categories"].append(iv_cat)
        found = False
        for sub in iv_cat["subs"]:
            if sub["subcategory"] == iv_data["name"]:
                sub["points"] = iv_data["verbs"]
                found = True
                break
        if not found:
            iv_cat["subs"].append({
                "subcategory": iv_data["name"],
                "description": iv_data["description"],
                "points": iv_data["verbs"]
            })
    
    # Add phrasal verbs
    if cefr_key in phrasal_verbs:
        pv_data = phrasal_verbs[cefr_key]
        pv_cat = None
        for cat in lvl_data["categories"]:
            if "Phrasal Verbs" in cat["category"] and "Complete" in cat["category"]:
                pv_cat = cat
                break
        if pv_cat is None:
            pv_cat = {"category": "Phrasal Verbs — Complete List", "subs": []}
            lvl_data["categories"].append(pv_cat)
        found = False
        for sub in pv_cat["subs"]:
            if sub["subcategory"] == pv_data["name"]:
                sub["points"] = pv_data["verbs"]
                found = True
                break
        if not found:
            pv_cat["subs"].append({
                "subcategory": pv_data["name"],
                "description": pv_data["description"],
                "points": pv_data["verbs"]
            })

# Save
output = "/root/projects/english-grammar-db/data/english_grammar_database.json"
with open(output, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# Stats
iv_total = sum(len(v["verbs"]) for v in irregular_verbs.values())
pv_total = sum(len(v["verbs"]) for v in phrasal_verbs.values())

cefr_pts = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["CEFR"]["levels"].values())
am_pts = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["American"]["levels"].values())

print(f"✅ Added to database: {output}")
print(f"   Irregular verbs: {iv_total} across 5 levels (A1-B2 + C1/C2 merged)")
print(f"   Phrasal verbs: {pv_total} across 6 levels")
print(f"   New CEFR total: {cefr_pts} points")
print(f"   New American total: {am_pts} points")
print(f"   Grand total: {cefr_pts + am_pts}")

# Per-level counts
for sn in ["CEFR", "American"]:
    print(f"\n--- {sn} ---")
    for ln, ld in db["systems"][sn]["levels"].items():
        pts = sum(len(s["points"]) for c in ld["categories"] for s in c["subs"])
        iv_pts = sum(len(s["points"]) for c in ld["categories"] if "Irregular" in c["category"] for s in c["subs"])
        pv_pts = sum(len(s["points"]) for c in ld["categories"] if "Phrasal" in c["category"] for s in c["subs"])
        print(f"  {ln}: {pts} pts (irregular: {iv_pts}, phrasal: {pv_pts})")
