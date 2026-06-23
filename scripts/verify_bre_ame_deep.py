#!/usr/bin/env python3
"""Second verification: deep check annotations and data quality."""
import json, re

DATA_DIR = '../data'

with open(f'{DATA_DIR}/english_grammar_bre_ame_discrepancies.json') as f:
    disc = json.load(f)

with open(f'{DATA_DIR}/english_grammar_cefr.json') as f:
    cefr = json.load(f)

with open(f'{DATA_DIR}/english_grammar_american.json') as f:
    ame_db = json.load(f)

# ═══ VERIFY A: Annotation text quality ═══════════════════════════════════
# Check that annotation text doesn't contain truncated notes or missing IDs
bad_ann = []
for db_name, db in [("CEFR", cefr), ("American", ame_db)]:
    for lvl_key, lvl in db["levels"].items():
        for cat in lvl.get("categories", []):
            for sub in cat.get("subs", []):
                for i, point in enumerate(sub.get("points", [])):
                    if isinstance(point, str) and "discrepancies DB" in point:
                        # Check it has a valid BA-ID
                        if not re.search(r'BA-\d{3}', point):
                            bad_ann.append(f"{db_name}: missing BA-ID in '{point[:80]}'")
                        # Check it's not too long / malformed
                        if len(point) > 500:
                            bad_ann.append(f"{db_name}: overlong annotation: {point[:80]}...")

print(f"🧪 Deep Verify A — Annotation quality")
print(f"   Points checked: CEFR={sum(len(sub.get('points',[])) for l in cefr['levels'].values() for c in l.get('categories',[]) for sub in c.get('subs',[]))}")
print(f"   Bad annotations: {len(bad_ann)}")
if bad_ann:
    for b in bad_ann[:5]:
        print(f"   ❌ {b}")

# ═══ VERIFY B: Discrepancies DB item completeness ════════════════════════
# Every item should have examples_pair, key_difference (optional), and both variants
missing_field = []
for cat in disc["categories"]:
    for item in cat["items"]:
        if not item.get("example_pair"):
            missing_field.append(f"{item['id']}: missing example_pair")
        if not item.get("bre") or not item.get("ame"):
            missing_field.append(f"{item['id']}: missing bre/ame")

print(f"\n🧪 Deep Verify B — Discrepancies completeness")
print(f"   Items with incomplete fields: {len(missing_field)}")
if missing_field:
    for m in missing_field[:5]:
        print(f"   ⚠️  {m}")

# ═══ VERIFY C: Category coverage in discrepancies DB ═════════════════════
# Make sure all major grammar areas are represented
expected_cats = [
    "Verb Tenses", "Verb Forms", "Subject-Verb", "Modal", "Prepositions",
    "Articles", "Delexical", "Subjunctive", "Adverb", "Question Tag",
    "Pronoun", "Spelling", "Negation", "Clause", "Pragmatic"
]
found_cats = [c["name"] for c in disc["categories"]]
missed_cats = [e for e in expected_cats if not any(e.lower() in fc.lower() for fc in found_cats)]
covered_cats = [e for e in expected_cats if any(e.lower() in fc.lower() for fc in found_cats)]

print(f"\n🧪 Deep Verify C — Category coverage")
print(f"   Expected major areas covered: {len(covered_cats)}/{len(expected_cats)}")
if missed_cats:
    print(f"   Missing expected categories: {missed_cats}")

# ═══ VERIFY D: Annotation distribution ════════════════════════════════════
# Check annotations are spread across levels, not clustered in one
cefr_level_hits = {}
for lvl_key, lvl in cefr["levels"].items():
    count = 0
    for cat in lvl.get("categories", []):
        for sub in cat.get("subs", []):
            for point in sub.get("points", []):
                if isinstance(point, str) and "discrepancies DB" in point:
                    count += 1
    cefr_level_hits[lvl_key] = count

print(f"\n🧪 Deep Verify D — Annotation distribution across levels")
for lvl, cnt in cefr_level_hits.items():
    print(f"   {lvl}: {cnt} annotations")

# ═══ VERIFY E: No stray markers ──────────────────────────────────────────
# Check for any broken/malformed annotation markers
stray = []
for db_name, db in [("CEFR", cefr), ("American", ame_db)]:
    for lvl_key, lvl in db["levels"].items():
        for cat in lvl.get("categories", []):
            for sub in cat.get("subs", []):
                for point in sub.get("points", []):
                    if isinstance(point, str):
                        if "[🇬🇧→🇺🇸" in point and "discrepancies DB" not in point:
                            stray.append(f"{db_name}: partial annotation '{point[:60]}'")
                        elif "[🇺🇸→" in point and "discrepancies DB" not in point:
                            stray.append(f"{db_name}: partial annotation '{point[:60]}'")

print(f"\n🧪 Deep Verify E — Stray markers")
print(f"   Partial/broken annotations: {len(stray)}")

# ─── SUMMARY ─────────────────────────────────────────────────────────────
print(f"\n{'='*50}")
all_ok = not bad_ann and not missing_field and not missed_cats and not stray
if all_ok:
    print(f"✅ SECOND VERIFICATION PASSED — 0 issues found")
else:
    print(f"⚠️  Issues found — see above")
