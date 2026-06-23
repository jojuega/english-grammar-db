import json

with open('data/english_grammar_cefr.json') as f:
    cefr = json.load(f)

with open('data/english_grammar_american.json') as f:
    ame = json.load(f)

# Check structure
print('=== CEFR ===')
print('Top keys:', list(cefr.keys()))
print('Level keys:', list(cefr['levels'].keys()))
for lk, lv in cefr['levels'].items():
    cats = lv.get('categories', [])
    total_pts = sum(len(c.get('points', [])) for c in cats)
    print(f'  {lk}: {len(cats)} categories, {total_pts} total points')
    if cats and cats[0].get('points'):
        sample_pt = cats[0]['points'][0]
        print(f'    Sample point keys: {list(sample_pt.keys())}')
        print(f'    Sample: {json.dumps(sample_pt, ensure_ascii=False)[:300]}')

print()
print('=== AMERICAN ===')
print('Top keys:', list(ame.keys()))
print('Level keys:', list(ame['levels'].keys()))
for lk, lv in ame['levels'].items():
    cats = lv.get('categories', [])
    total_pts = sum(len(c.get('points', [])) for c in cats)
    print(f'  {lk}: {len(cats)} categories, {total_pts} total points')
    if cats and cats[0].get('points'):
        sample_pt = cats[0]['points'][0]
        print(f'    Sample point keys: {list(sample_pt.keys())}')
        print(f'    Sample: {json.dumps(sample_pt, ensure_ascii=False)[:300]}')
