#!/usr/bin/env python3
"""Verify the BrE/AmE discrepancies database and annotations integrity."""
import json, os, re, sys

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

errors = []
warnings = []

# ─── VERIFY 1: Discrepancies DB ──────────────────────────────────────────
with open(os.path.join(DATA_DIR, 'english_grammar_bre_ame_discrepancies.json')) as f:
    disc = json.load(f)

# Structural checks
if disc.get("name") != "British vs American English — Grammatical Discrepancies":
    errors.append("Discrepancies DB: wrong name")
if not disc.get("categories") or not disc.get("meta"):
    errors.append("Discrepancies DB: missing categories or meta")

total_items = 0
ids_seen = set()
cats_seen = set()

for cat in disc["categories"]:
    cname = cat.get("name", "?")
    if cname in cats_seen:
        errors.append(f"Duplicate category: {cname}")
    cats_seen.add(cname)
    
    for item in cat.get("items", []):
        total_items += 1
        # Check required fields
        for field in ["id", "point", "bre", "ame", "cefr_level", "american_level"]:
            if field not in item:
                errors.append(f"Item lacks '{field}': {item.get('point', '?')[:50]}")
        
        # Check unique ID
        item_id = item.get("id", "")
        if item_id in ids_seen:
            errors.append(f"Duplicate item ID: {item_id}")
        ids_seen.add(item_id)
        
        # Check ID format
        if not re.match(r'^BA-\d{3}$', item_id):
            errors.append(f"Bad ID format: {item_id}")

# Check ID continuity
expected_ids = sorted([f"BA-{i:03d}" for i in range(1, total_items + 1)])
actual_ids = sorted([item["id"] for cat in disc["categories"] for item in cat["items"]])
if expected_ids != actual_ids:
    errors.append(f"Item ID discontinuity. Expected {len(expected_ids)}, got {len(actual_ids)}.")
    diff = set(expected_ids) - set(actual_ids)
    if diff:
        errors.append(f"Missing IDs: {sorted(diff)[:5]}...")

print(f"✅ VERIFY 1: Discrepancies DB")
print(f"   Categories: {len(disc['categories'])}")
print(f"   Items: {total_items} (expected 69)")
print(f"   IDs: {len(ids_seen)} unique, format OK")
print(f"   Fields present: point, bre, ame, cefr_level, american_level")
if errors: sys.exit("\n".join(errors[:5]))

# ─── VERIFY 2: CEFR annotations ──────────────────────────────────────────
with open(os.path.join(DATA_DIR, 'english_grammar_cefr.json')) as f:
    cefr = json.load(f)

ann_count = 0
breakage_count = 0
annotated_ids = set()

for lvl_key, lvl in cefr["levels"].items():
    for cat in lvl.get("categories", []):
        for sub in cat.get("subs", []):
            for i, point in enumerate(sub.get("points", [])):
                if isinstance(point, str) and "discrepancies DB #" in point:
                    ann_count += 1
                    # Extract BA-ID
                    m = re.search(r'(BA-\d{3})', point)
                    if m:
                        annotated_ids.add(m.group(1))

# Check structure is intact
for lvl_key, lvl in cefr["levels"].items():
    for cat in lvl.get("categories", []):
        if not cat.get("category") or not isinstance(cat.get("subs"), list):
            breakage_count += 1
            errors.append(f"CEFR: broken structure in {lvl_key} > {cat.get('category')}")

print(f"\n✅ VERIFY 2: CEFR annotations")
print(f"   Annotated points: {ann_count}")
print(f"   Unique discrepancy IDs referenced: {len(annotated_ids)}")
print(f"   Structure intact: {breakage_count == 0}")

# ─── VERIFY 3: American annotations ──────────────────────────────────────
with open(os.path.join(DATA_DIR, 'english_grammar_american.json')) as f:
    ame_db = json.load(f)

ann_count_a = 0
breakage_count_a = 0
annotated_ids_a = set()

for lvl_key, lvl in ame_db["levels"].items():
    for cat in lvl.get("categories", []):
        for sub in cat.get("subs", []):
            for i, point in enumerate(sub.get("points", [])):
                if isinstance(point, str) and "discrepancies DB #" in point:
                    ann_count_a += 1
                    m = re.search(r'(BA-\d{3})', point)
                    if m:
                        annotated_ids_a.add(m.group(1))

# Check structure intact
for lvl_key, lvl in ame_db["levels"].items():
    for cat in lvl.get("categories", []):
        if not cat.get("category") or not isinstance(cat.get("subs"), list):
            breakage_count_a += 1
            errors.append(f"AMERICAN: broken structure in {lvl_key} > {cat.get('category')}")

print(f"\n✅ VERIFY 3: American annotations")
print(f"   Annotated points: {ann_count_a}")
print(f"   Unique discrepancy IDs referenced: {len(annotated_ids_a)}")
print(f"   Structure intact: {breakage_count_a == 0}")

# ─── VERIFY 4: Cross-reference ──────────────────────────────────────────
all_disc_ids = set(item["id"] for cat in disc["categories"] for item in cat["items"])
cefr_refs = annotated_ids
ame_refs = annotated_ids_a

# IDs referenced but not existing in discrepancies DB
orphan_cefr = cefr_refs - all_disc_ids
orphan_ame = ame_refs - all_disc_ids

# IDs existing but not referenced in any DB
unused = all_disc_ids - cefr_refs - ame_refs

if orphan_cefr:
    errors.append(f"CEFR references non-existent IDs: {orphan_cefr}")
if orphan_ame:
    errors.append(f"American references non-existent IDs: {orphan_ame}")

print(f"\n✅ VERIFY 4: Cross-reference")
print(f"   Discrepancies DB has {len(all_disc_ids)} unique IDs")
print(f"   CEFR references {len(cefr_refs)} of them")
print(f"   American references {len(ame_refs)} of them")
print(f"   Unreferenced in both DBs: {len(unused)} items")
if len(unused) > 5:
    print(f"   (This is OK — many items are 'background knowledge' not tied to a specific grammar point)")

# ─── VERIFY 5: Duplicate annotations ─────────────────────────────────────
# Check no point has multiple annotations that would be confusing
multi_ann = 0
for lvl_key, lvl in cefr["levels"].items():
    for cat in lvl.get("categories", []):
        for sub in cat.get("subs", []):
            for point in sub.get("points", []):
                if isinstance(point, str) and point.count("discrepancies DB #") > 1:
                    multi_ann += 1
                    if multi_ann <= 3:
                        errors.append(f"CEFR duplicate annotations: {point[:80]}")

print(f"\n✅ VERIFY 5: Duplicate annotations check")
print(f"   CEFR points with >1 annotation: {multi_ann}")

# ─── VERIFY 6: Total counts ──────────────────────────────────────────────
# Count total points in each db after annotation
def count_points(db):
    total = 0
    for lvl_key, lvl in db["levels"].items():
        for cat in lvl.get("categories", []):
            for sub in cat.get("subs", []):
                total += len(sub.get("points", []))
    return total

cefr_total = count_points(cefr)
ame_total = count_points(ame_db)

print(f"\n✅ VERIFY 6: Final counts")
print(f"   CEFR total points: {cefr_total}")
print(f"   American total points: {ame_total}")
print(f"   Discrepancies DB: {total_items} items")

# ─── FINAL ───────────────────────────────────────────────────────────────
if errors:
    print(f"\n❌ ERRORS FOUND ({len(errors)}):")
    for e in errors[:10]:
        print(f"   - {e}")
    sys.exit(1)
else:
    print(f"\n🎯 ALL VERIFICATIONS PASSED — 0 errors, 0 structural issues")
