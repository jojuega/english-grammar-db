#!/usr/bin/env python3
"""Add Causative (have/get something done) to both DBs at B2/L4 level."""

import json

with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "r") as f:
    db = json.load(f)

causative_points = [
    "Causative have: have + object + past participle — arrange for someone to do something for you (I had my car repaired, She had her hair cut, We had the house painted)",
    "Causative get: get + object + past participle — same meaning, more informal (I got my phone fixed, She got her nails done, We got the windows cleaned)",
    "Causative have for negative experiences: have + object + past participle (I had my wallet stolen, She had her car broken into, He had his application rejected)",
    "Causative get + object + to-infinitive: persuade someone to do something (I got him to help me with the project, She got her boss to approve the leave)",
    "Causative have + object + base form: tell/order someone to do something (I'll have my assistant send you the documents, She had everyone wait in the conference room)",
    "Causative make + object + base form: force someone to do something (My boss made me work late, The teacher made him rewrite the essay)",
    "Causative let + object + base form: allow someone to do something (My parents let me borrow the car, The rules don't let us take photos)",
    "Causative help + object + base form/to-infinitive: assist someone (She helped me carry the bags / She helped me to carry the bags)",
    "Causative get + object + past participle in questions and negatives (Where did you get your watch repaired? I couldn't get my computer fixed in time)",
    "Causative have + object + base form vs have + object + past participle: active vs passive meaning distinction (I had everyone clean the office vs I had the office cleaned)",
    "Causative need/want + -ing for passive meaning with things (The car needs washing = needs to be washed, The house wants painting = needs to be painted)",
    "Causative get + object + adjective/participle for state (I need to get my passport renewed, She got her eyes checked, We got everything ready)",
    "Causative all tenses: have/get something done in present, past, future, present perfect, and with modals (I have my hair cut every month; I had it done last week; I will have it done next week; I have already had it done; I must get it done)",
    "Difference between 'I cut my hair' (I did it myself) and 'I had my hair cut' (someone else did it) — fundamental meaning distinction"
]

def add_to_level(db_obj, level_name, category_name, point_list):
    lvl = db_obj["levels"][level_name]
    found_cat = None
    for cat in lvl["categories"]:
        if category_name in cat["category"]:
            found_cat = cat
            break
    if not found_cat:
        found_cat = {"category": category_name, "subs": []}
        lvl["categories"].append(found_cat)
    
    # Check if subcategory exists
    sub_name = "Causative Have/Get Structures — B2 Level"
    for sub in found_cat["subs"]:
        if sub_name in sub["subcategory"]:
            sub["points"] = point_list
            return len(point_list)
    
    found_cat["subs"].append({
        "subcategory": sub_name,
        "description": "Causative structures with have and get for expressing that someone else does something for you. Source: Azar-Hagen Understanding and Using English Grammar, Cambridge Grammar.",
        "points": point_list
    })
    return len(point_list)

n = add_to_level(db["systems"]["CEFR"], "B2 - Upper Intermediate", "Modals Advanced", causative_points)
print(f"CEFR B2: +{n} causative points")

n = add_to_level(db["systems"]["American"], "Level 4 - High Intermediate", "Modals: Complete Range", causative_points)
print(f"American L4: +{n} causative points")

# Also add to C1/L5 as review with advanced patterns
advanced = [
    "Causative in passive reporting: have/get something done in reporting structures (It is believed that he had his house renovated, She is said to have had her portrait painted)",
    "Causative get + reflexive + past participle for actions you need done to yourself (I need to get myself checked by a doctor, He got himself elected president, They got themselves invited to the ceremony)",
    "Causative have + object + present participle for ongoing actions by others (I'll have the assistant preparing the report while I'm away, She had the team working on the project all weekend)"
]
n2 = add_to_level(db["systems"]["CEFR"], "C1 - Advanced", "Inversion", advanced)
n2 += add_to_level(db["systems"]["American"], "Level 5 - Advanced", "Inversion: Complete Patterns", advanced)
print(f"C1/L5: +{n2} advanced causative points")

# Save
with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "w") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

cefr_db = db["systems"]["CEFR"]; cefr_db["meta"] = {"title":"CEFR English Grammar Database","version":"3.1","system":"CEFR"}
am_db = db["systems"]["American"]; am_db["meta"] = {"title":"American ESL Grammar Database","version":"3.1","system":"American ESL"}
with open("/root/projects/english-grammar-db/data/english_grammar_cefr.json","w") as f: json.dump(cefr_db, f, indent=2, ensure_ascii=False)
with open("/root/projects/english-grammar-db/data/english_grammar_american.json","w") as f: json.dump(am_db, f, indent=2, ensure_ascii=False)

cefr_t = sum(sum(len(s["points"]) for c in l["categories"] for s in c["subs"]) for l in db["systems"]["CEFR"]["levels"].values())
am_t = sum(sum(len(s["points"]) for c in l["categories"] for s in c["subs"]) for l in db["systems"]["American"]["levels"].values())
print(f"\n✅ Total: CEFR {cefr_t} | American {am_t} | Grand {cefr_t + am_t}")
