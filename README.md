# English Grammar Database 🗂️

Base de datos jerárquica completa de gramática del inglés con **1,311 puntos gramaticales exactos**, organizados en dos sistemas de niveles:

| Sistema | Niveles | Puntos | Fuente primaria |
|---------|---------|--------|-----------------|
| **CEFR** (A1→C2) | 6 | 518 | Cambridge EGP + British Council/EAQUALS |
| **American ESL** (L1→L6) | 6 | 793 | Pearson GSE + Azar-Hagen + US University IEPs |

## Estructura

```
Sistema → Nivel → Categoría → Subcategoría → Punto Gramatical Exacto
```

Ejemplo:
```
CEFR → A1 → Present Tenses → Present Simple → "Present simple: affirmative with he/she/it + -s"
```

## Archivos

- `data/english_grammar_database.json` — Base de datos completa (JSON)
- `scripts/build_grammar_db.py` — Generador CEFR
- `scripts/rebuild_american_grammar.py` — Generador American ESL
- `scripts/verify_grammar_db.py` — Validador estructural
- `docs/` — Reportes

## Fuentes verificadas

1. **Cambridge English Grammar Profile** (1222+ statements empíricos)
2. **British Council / EAQUALS Core Inventory** (A1-C1)
3. **Pearson GSE Grammar Guide** (450+ objetivos gramaticales)
4. **Azar-Hagen Grammar Series** (3 libros, estándar US)
5. **Troy University, UDEL, ALC** — Currículos IEP
