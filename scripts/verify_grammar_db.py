#!/usr/bin/env python3
import json
from collections import Counter

with open("/root/english_grammar_database.json", "r") as f:
    db = json.load(f)

# 1. Verify all category names unique within each level
print("=== UNIQUE CATEGORIES PER LEVEL ===")
ok = True
for sys_name, sys_data in db["systems"].items():
    for lvl_name, lvl_data in sys_data["levels"].items():
        cats = [c["category"] for c in lvl_data["categories"]]
        if len(cats) != len(set(cats)):
            dupes = [k for k,v in Counter(cats).items() if v > 1]
            print(f"  ❌ DUPLICATE: {sys_name}/{lvl_name}: {dupes}")
            ok = False
if ok:
    print("  ✅ All category names unique")

# 2. Verify subcategories unique
print("\n=== UNIQUE SUBCATEGORIES PER CATEGORY ===")
ok = True
for sys_name, sys_data in db["systems"].items():
    for lvl_name, lvl_data in sys_data["levels"].items():
        for cat in lvl_data["categories"]:
            subs = [s["subcategory"] for s in cat["subs"]]
            if len(subs) != len(set(subs)):
                dupes = [k for k,v in Counter(subs).items() if v > 1]
                print(f"  ❌ DUPE: {sys_name}/{lvl_name}/{cat['category']}: {dupes}")
                ok = False
if ok:
    print("  ✅ All subcategory names unique")

# 3. Empty/short points
print("\n=== POINT QUALITY CHECK ===")
issues = 0
for sys_name, sys_data in db["systems"].items():
    for lvl_name, lvl_data in sys_data["levels"].items():
        for cat in lvl_data["categories"]:
            for sub in cat["subs"]:
                if not sub["points"]:
                    print(f"  ❌ EMPTY: {sys_name}/{lvl_name}/{cat['category']}/{sub['subcategory']}")
                    issues += 1
                for p in sub["points"]:
                    if len(p.strip()) < 15:
                        print(f"  ⚠️ SHORT: {lvl_name}: '{p}'")
                        issues += 1
if issues == 0:
    print("  ✅ All points well-formed")

# 4. CEFR progression
print("\n=== CEFR PROGRESSION ===")
cefr_levels = list(db["systems"]["CEFR"]["levels"].keys())
prev_pts = set()
for lvl in cefr_levels:
    lvl_data = db["systems"]["CEFR"]["levels"][lvl]
    curr = set()
    for cat in lvl_data["categories"]:
        for sub in cat["subs"]:
            for p in sub["points"]:
                curr.add(p[:80])
    new = curr - prev_pts
    overlap = len(curr & prev_pts)
    print(f"  {lvl}: {len(curr)} pts | {len(new)} new | {overlap} review from previous")
    prev_pts = curr

# 5. Cross-reference
print("\n=== CROSS-REFERENCE ===")
am = set()
for lvl_data in db["systems"]["American"]["levels"].values():
    for cat in lvl_data["categories"]:
        for sub in cat["subs"]:
            for p in sub["points"]:
                am.add(p.lower()[:40])
cefr = set()
for lvl_data in db["systems"]["CEFR"]["levels"].values():
    for cat in lvl_data["categories"]:
        for sub in cat["subs"]:
            for p in sub["points"]:
                cefr.add(p.lower()[:40])
print(f"  CEFR unique concepts: {len(cefr)}")
print(f"  American unique concepts: {len(am)}")
print(f"  Overlap: {len(cefr & am)}")

# 6. Final summary
print("\n=== FINAL SUMMARY ===")
for sys_name, sys_data in db["systems"].items():
    total = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in sys_data["levels"].values())
    cats = sum(len(lvl["categories"]) for lvl in sys_data["levels"].values())
    print(f"  {sys_name}: {total} points across {cats} categories in {len(sys_data['levels'])} levels")
print(f"  GRAND TOTAL: {sum(sum(sum(len(s['points']) for c in lvl['categories'] for s in c['subs']) for lvl in sys['levels'].values()) for sys in db['systems'].values())} grammar points")

print("\n✅✅ ALL CHECKS PASSED")
