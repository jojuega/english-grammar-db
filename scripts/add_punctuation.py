#!/usr/bin/env python3
"""T6: Add missing verb pattern gaps + T5: Add Punctuation & Capitalization category"""

import json

with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "r") as f:
    db = json.load(f)

# ============================================================
# T6: VERB PATTERNS — 8 missing points
# Add to existing Syntax & Sentence Structure (B1-B2) and Gerunds/Infinitives (B1-C1)
# ============================================================

# CEFR: Gerunds/Infinitives B1 — add prepositional verb patterns
for lvl_name in ["B1 - Intermediate", "B1"]:
    target_db = db["systems"]["CEFR"]["levels"] if "CEFR" in str(type(db)) else None
    pass

# Find B1 in CEFR and B1 in American
cefr_b1 = db["systems"]["CEFR"]["levels"]["B1 - Intermediate"]
cefr_b1_gerund = None
for cat in cefr_b1["categories"]:
    if "Gerunds" in cat["category"]:
        cefr_b1_gerund = cat
        break
if cefr_b1_gerund:
    for sub in cefr_b1_gerund["subs"]:
        if "Verb Patterns" in sub["subcategory"] and "preposition" not in sub.get("subcategory","").lower():
            sub["points"].append("Verb + preposition + gerund: insist on doing, apologize for being, succeed in doing, approve of doing, decide against doing")
            sub["points"].append("Verb + object + preposition + gerund: accuse someone of (doing), blame someone for (doing), congratulate someone on (doing), thank someone for (doing), prevent someone from (doing)")
            break

# CEFR C1 Syntax — add advanced verb patterns
cefr_c1_syn = None
for cat in db["systems"]["CEFR"]["levels"]["C1 - Advanced"]["categories"]:
    if "Syntax" in cat["category"]:
        cefr_c1_syn = cat
        break
if cefr_c1_syn:
    for sub in cefr_c1_syn["subs"]:
        sub["points"].append("Verb + it + complement + to-infinitive: find it difficult to..., make it easy to..., consider it important to..., think it necessary to...")
        sub["points"].append("Verb + object + as/for complement: regard her as a genius, see him as a leader, describe it as revolutionary, take him for a fool, mistake it for the real thing")
        sub["points"].append("Verb + reflexive pronoun: enjoy yourself, hurt yourself, teach yourself, cut yourself, introduce yourself, convince yourself, remind yourself")
        sub["points"].append("Verb + adjective + preposition patterns: be good at, be interested in, be afraid of, be famous for, be tired of, be proud of, be responsible for, be capable of")

# CEFR C2 — add prepositional vs phrasal verbs distinction
cefr_c2 = db["systems"]["CEFR"]["levels"]["C2 - Proficiency"]
for cat in cefr_c2["categories"]:
    if "Syntax" in cat["category"]:
        for sub in cat["subs"]:
            sub["points"].append("Prepositional verbs vs phrasal verbs distinction: prepositional verbs take an object immediately after the preposition (look at it, depend on it) and are always inseparable; phrasal verbs have a particle that can be separated (turn it off vs look into it)")
            break

# American: same additions at equivalent levels
am_levels = db["systems"]["American"]["levels"]
am_b1_gerund = None
for cat in am_levels["Level 3 - Intermediate"]["categories"]:
    if "Gerunds" in cat["category"]:
        am_b1_gerund = cat
        break
if am_b1_gerund:
    for sub in am_b1_gerund["subs"]:
        if "Verb + -ing" in sub["subcategory"]:
            sub["points"].append("Verb + preposition + gerund: insist on doing, apologize for being, succeed in doing, approve of doing")
            sub["points"].append("Verb + object + preposition + gerund: accuse someone of (doing), congratulate someone on (doing), thank someone for (doing), prevent someone from (doing)")
            break

am_l5_syn = None
for cat in am_levels["Level 5 - Advanced"]["categories"]:
    if "Syntax" in cat["category"]:
        am_l5_syn = cat
        break
if am_l5_syn:
    for sub in am_l5_syn["subs"]:
        sub["points"].append("Verb + it + complement + to-infinitive: find it difficult to, make it easy to, consider it important to")
        sub["points"].append("Verb + object + as/for complement: regard her as genius, see him as leader, describe it as revolutionary, mistake it for")
        sub["points"].append("Verb + reflexive pronoun: enjoy yourself, hurt yourself, teach yourself, introduce yourself")
        sub["points"].append("Verb + adjective + preposition patterns: be good at, be afraid of, be interested in, be famous for, be responsible for")

am_l6_syn = None
for cat in am_levels["Level 6 - High Advanced"]["categories"]:
    if "Syntax" in cat["category"] or "Cohesion" in cat["category"]:
        for sub in cat["subs"]:
            if "Register" in sub["subcategory"]:
                sub["points"].append("Prepositional verbs vs phrasal verbs: prepositional verbs are inseparable and lexicalized (depend on, believe in, consist of); phrasal verbs have separable particles (turn off, pick up, give away)")
                break

print("✅ T6: Verb pattern gaps filled")

# ============================================================
# T5: PUNCTUATION & CAPITALIZATION
# ============================================================

punctuation = {
    "A1": {
        "name": "A1 Punctuation and Capitalization — Basic Rules",
        "description": "Fundamental rules for sentence boundaries, proper nouns, and basic punctuation. Source: British Council, Cambridge Grammar.",
        "points": [
            "Capitalization: always capitalize the first word of a sentence (The cat is sleeping. She went home.)",
            "Capitalization: always capitalize the pronoun 'I' (I am happy, She and I went to the store)",
            "Capitalization: always capitalize proper nouns — names (John, Sarah, London, England, Monday, December)",
            "Period/full stop (.): used at the end of declarative sentences and statements (I like coffee. She lives in Paris.)",
            "Question mark (?): used at the end of direct questions (Where do you live? Are you tired?)",
            "Exclamation mark (!): used at the end of exclamations and strong commands (What a beautiful day! Sit down! Help!)",
            "Comma (,): used to separate items in a list of three or more (I bought apples, oranges, bananas and milk)",
            "Comma (,): used before 'and'/'but'/'or' when joining two independent clauses (I like tea, but she likes coffee)",
            "Capitalization: days of the week, months, and holidays (Monday, January, Christmas)",
            "Capitalization: nationalities, languages, and countries (Spanish, English, French, Germany, Japan, American)",
            "No capitalization for seasons (spring, summer, fall, winter) unless part of a title"
        ]
    },
    "A2": {
        "name": "A2 Punctuation — Apostrophes and Quotation Marks",
        "description": "Apostrophes for possession and contractions, basic quotation marks for speech. Source: British Council.",
        "points": [
            "Apostrophe (ʼ) for contractions: joining subject + verb (I'm, you're, he's, she's, it's, we're, they're)",
            "Apostrophe (ʼ) for negative contractions: don't, doesn't, didn't, can't, won't, isn't, aren't, wasn't, weren't, haven't, hasn't, hadn't",
            "Apostrophe (ʼ) for possessive singular nouns: add 's (John's book, the cat's tail, my mother's car)",
            "Apostrophe (ʼ) for possessive plural nouns ending in -s: add ' after the s (the students' books, my parents' house)",
            "Apostrophe (ʼ) for possessive plural nouns not ending in -s: add 's (the children's toys, the men's room)",
            "Quotation marks (\" \"): used to enclose direct speech or quotes (She said \"I'm tired.\" \"Come here,\" he said)",
            "Period/comma placement inside quotation marks in American English (She said \"I'm tired.\" He replied \"No,\" she said)",
            "Comma (,): after introductory words/phrases (Well, I think so. However, he was late. First, mix the ingredients.)",
            "Comma (,): used with direct address (John, can you help me? I'm sorry, sir. Thanks, Mary.)",
            "Comma (,): used in dates (June 5, 2024) and addresses (London, England, 10 Downing Street)",
            "Comma (,): used after 'Yes' and 'No' in responses (Yes, I do. No, I don't think so.)",
            "Capitalization: titles of books, movies, songs, TV shows (The Lord of the Rings, Titanic, Yesterday)",
            "Capitalization: capitalize the first and last words and all major words in titles; do not capitalize articles, conjunctions, or short prepositions in the middle (The Cat in the Hat, Gone with the Wind)"
        ]
    },
    "B1": {
        "name": "B1 Punctuation — Colons, Semicolons, and Advanced Commas",
        "description": "Colons and semicolons introduction, commas with subordinate clauses and non-restrictive elements. Source: Cambridge Grammar.",
        "points": [
            "Colon (:): used to introduce a list (You need the following items: a pen, paper, and a book)",
            "Colon (:): used to introduce an explanation or example (He had one goal: to win the championship)",
            "Colon (:): used to introduce a quotation (The president said: 'We will not give up')",
            "Semicolon (;): used to join two closely related independent clauses without a conjunction (I love Paris; it's my favorite city)",
            "Semicolon (;): used to separate items in a complex list that already contains commas (The winners were John, from London; Mary, from Paris; and Tom, from Berlin)",
            "Comma (,): used after subordinate clauses at the beginning of a sentence (When I arrived, they were already eating. If it rains, I'll stay home.)",
            "No comma when subordinate clause follows the main clause (I'll stay home if it rains. They were eating when I arrived.)",
            "Comma (,): with non-defining relative clauses that provide extra, non-essential information (My brother, who lives in Paris, is a doctor)",
            "Comma (,): after linking/adverbial words (however, therefore, moreover, furthermore, consequently, nevertheless — However, I disagree. Therefore, we must act.)",
            "Comma (,): to separate contrasting elements (She was happy, not sad. He arrived early, unlike the others.)",
            "Apostrophe: its vs it's — it's = contraction of it is or it has (It's raining, It's been a long day); its = possessive determiner (The dog wagged its tail)",
            "Quotation marks: single vs double quotes — American English uses double quotes first, single quotes for quotes within quotes (She said, \"He whispered, 'I'm scared.'\")",
            "Dash (—): used informally to indicate a pause, to set off additional information, or for emphasis (He finally arrived — three hours late)",
        ]
    },
    "B2": {
        "name": "B2 Punctuation — Semicolon, Dash, Ellipsis, and Parentheses",
        "description": "Advanced semicolon use, em dash and en dash, ellipsis, parentheses, hyphens, and brackets. Source: Cambridge Grammar, Chicago Manual of Style.",
        "points": [
            "Em dash (—): used to set off a parenthetical thought with more emphasis than commas or parentheses (The results — though unexpected — were conclusive)",
            "Em dash (—): used to indicate a sudden break in thought (I was going to — oh, never mind)",
            "En dash (–): used to indicate ranges of numbers, dates, or time (1990–2000, pages 10–25, 3:00–5:00 PM)",
            "Ellipsis (...): used to indicate omitted words in a quotation (The report stated that 'the findings... support the original hypothesis')",
            "Ellipsis (...): used to indicate a trailing off of thought or suspense (I just don't know... maybe you're right)",
            "Parentheses (()): used to enclose additional information, clarifications, or references (The study (published in 2024) found significant results)",
            "Brackets ([]): used to add clarification or commentary inside a quotation (He said 'it [the policy] was a mistake')",
            "Hyphen (-): used to form compound adjectives before a noun (well-known author, high-quality product, state-of-the-art technology, part-time job)",
            "Hyphen (-): used with prefixes in certain cases (ex-president, self-esteem, all-inclusive, twenty-five (numbers 21-99))",
            "Hyphen (-): used to avoid ambiguity or confusion (re-cover vs recover, re-sign vs resign, re-present vs represent)",
            "Semicolon (;): used before conjunctive adverbs (He was late; therefore, he missed the beginning. She studied hard; consequently, she passed.)",
            "Colon (:): used to introduce a formal list after a complete sentence (The conference had three main themes: sustainability, innovation, and inclusion)",
            "Parentheses (()): punctuation of parentheses — period goes inside if the entire sentence is parenthetical, outside if only part of the sentence is",
            "Comma (,): not used to separate a subject from its verb or a verb from its object (NOT: The team, won the game. / The study found, that the results were significant)",
            "Slashes (/) for alternatives: and/or, either/or, his/her, pass/fail"
        ]
    },
    "C1": {
        "name": "C1 Punctuation — Advanced and Stylistic Usage",
        "description": "Nuanced comma rules, quotation integration, register-specific punctuation, formatting conventions. Source: Chicago Manual of Style, Cambridge Grammar.",
        "points": [
            "Comma (,): with restrictive vs non-restrictive appositives (My brother, John, is visiting vs My brother John is visiting — appositive with vs without comma changes meaning)",
            "Comma (,): with introductory participial and absolute phrases (Having finished the report, she went home. The meeting concluded, we left the room.)",
            "Comma (,): to prevent misreading (In the valley below, the river flowed peacefully vs In the valley below the river flowed peacefully)",
            "Comma (,): with correlative conjunctions (not only...but also, either...or) is generally not needed, but may be used for clarity",
            "Quotation integration: how to integrate quotes smoothly with signal phrases and correct punctuation (According to Smith, 'the evidence is clear'; however, others disagree.)",
            "Quotations: block quotations — long quotes (over 40 words/4 lines) are set off as block quotes without quotation marks",
            "Colon (:): used to introduce a formal statement or lengthy quotation in academic writing (The author makes his position clear: 'We must act now or face the consequences.')",
            "Semicolon (;): used in academic writing to create sophisticated sentence connections and to balance contrasting ideas",
            "Capitalization: in titles following different style guides — APA, MLA, Chicago (sentence case vs title case conventions)",
            "Capitalization: after colons — lowercase when what follows is dependent on the preceding clause, capitalize when it's an independent clause or formal rule",
            "Numbers: spell out numbers one through nine/one hundred, use numerals for 10+ (with style guide variations)",
            "Slashes (/) in formal contexts: representing 'and' or 'or' should be avoided in formal academic writing; spell out instead",
            "Apostrophe: possessive of singular proper nouns ending in -s (James's car vs James' car — Chicago vs APA/MLA style variation)",
            "Punctuation conventions in scientific/technical writing: SI unit spacing, abbreviation punctuation, footnote markers"
        ]
    },
    "C2": {
        "name": "C2 Punctuation — Stylistic Choice and Rhetorical Expression",
        "description": "Punctuation as a stylistic tool, rhetorical effects, professional conventions, dialectical analysis of punctuation choices. Source: Chicago Manual of Style, Cambridge Grammar.",
        "points": [
            "Stylistic punctuation: using fragments for rhetorical effect (No. Never. Not in a million years.)",
            "Stylistic punctuation: dash vs parentheses vs commas — strategic choice based on degree of separation, emphasis, and formality",
            "Stylistic punctuation: using semicolons for balanced, parallel structures in formal and literary writing (The past is a foreign country; they do things differently there.)",
            "Stylistic punctuation: the colon for dramatic anticipation, introducing a punchline, or building suspense (The answer was simple: they had failed to prepare.)",
            "Ellipsis for stylistic effect: creating suspense, indicating hesitation, trailing off, or suggesting unspoken content",
            "Punctuation for tone and voice: exclamation marks for enthusiasm vs restraint, dashes for informality and conversational flow",
            "Parentheses vs dashes vs commas: subtle differences in tone — parentheses are more 'whispered', dashes more emphatic, commas more neutral",
            "Capitalization for emphasis: using all caps sparingly for very strong emphasis (I will NOT tolerate this) — generally discouraged in formal writing",
            "Punctuation with bulleted/vertical lists: capitalizing or not, using periods or not, parallel structure requirements",
            "British vs American punctuation differences: placement of periods/commas inside or outside quotation marks",
            "British vs American punctuation differences: colon after salutation (Dear Sir:) vs comma (Dear Sir,) or no punctuation",
            "Professional correspondence punctuation: meaning of comma splice vs semicolon vs period in email and business communication",
            "Legal and formal document punctuation conventions",
            "Punctuation in digital/online writing: conventions for text, email, social media, and informal contexts vs formal writing"
        ]
    }
}

# Map American levels
am_map = {
    "Level 1 - Beginner": "A1", "Level 2 - High Beginner": "A2",
    "Level 3 - Intermediate": "B1", "Level 4 - High Intermediate": "B2",
    "Level 5 - Advanced": "C1", "Level 6 - High Advanced": "C2"
}

def add_punctuation(db_obj, level_name, cefr_key):
    if cefr_key not in punctuation:
        return 0
    pdata = punctuation[cefr_key]
    lvl_data = db_obj["levels"][level_name]
    
    # Check if exists
    pcat = None
    for cat in lvl_data["categories"]:
        if "Punctuation" in cat["category"]:
            pcat = cat
            break
    if pcat is None:
        pcat = {"category": "Punctuation and Capitalization", "subs": []}
        lvl_data["categories"].append(pcat)
    
    found = False
    for sub in pcat["subs"]:
        if sub["subcategory"] == pdata["name"]:
            sub["points"] = pdata["points"]
            found = True
            break
    if not found:
        pcat["subs"].append({
            "subcategory": pdata["name"],
            "description": pdata["description"],
            "points": pdata["points"]
        })
    return len(pdata["points"])

# Add to CEFR
cefr_total = sum(add_punctuation(db["systems"]["CEFR"], ln, ln.split(" - ")[0]) for ln in db["systems"]["CEFR"]["levels"])
print(f"✅ T5: Punctuation added to CEFR ({cefr_total} points)")

# Add to American
am_total = sum(add_punctuation(db["systems"]["American"], ln, am_map.get(ln, "A1")) for ln in db["systems"]["American"]["levels"])
print(f"✅ T5: Punctuation added to American ({am_total} points)")

# Save
with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "w") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# Also separate files
cefr_db = db["systems"]["CEFR"]; cefr_db["meta"] = {"title": "CEFR English Grammar Database", "version": "3.0", "system": "CEFR"}
am_db = db["systems"]["American"]; am_db["meta"] = {"title": "American ESL Grammar Database", "version": "3.0", "system": "American ESL"}
with open("/root/projects/english-grammar-db/data/english_grammar_cefr.json", "w") as f:
    json.dump(cefr_db, f, indent=2, ensure_ascii=False)
with open("/root/projects/english-grammar-db/data/english_grammar_american.json", "w") as f:
    json.dump(am_db, f, indent=2, ensure_ascii=False)

cefr_pts = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["CEFR"]["levels"].values())
am_pts = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["American"]["levels"].values())
print(f"\n📊 CEFR total: {cefr_pts} | American total: {am_pts} | Grand total: {cefr_pts + am_pts}")
