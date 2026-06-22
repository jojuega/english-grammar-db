# 🗂️ English Grammar Database — Reporte

## Resumen Ejecutivo

Base de datos completa de gramática del inglés organizada jerárquicamente en **dos sistemas de niveles**:
- **CEFR** (Marco Común Europeo): A1→C2
- **American ESL** (Modelo universitario IEP): 6 niveles

**Total: 668 puntos gramaticales exactos**

---

## Fuentes Utilizadas

| # | Fuente | Tipo | Autoridad |
|---|--------|------|-----------|
| 1 | **Cambridge English Grammar Profile (EGP)** | 1222+ competence statements empíricos | Cambridge University Press |
| 2 | **British Council / EAQUALS Core Inventory** | Currículo oficial A1-C1 | British Council + EAQUALS |
| 3 | **Test-English Grammar Curriculum** | Lista completa A1-C1 por niveles | Test-English |
| 4 | **TrackTest English Core Exam** | Requisitos gramaticales A1-C2 | TrackTest |
| 5 | **Troy University ESL Curriculum** | Programa IEP 6 niveles | Troy University (USA) |
| 6 | **University of Delaware IEP** | Programa intensivo 6 niveles | UDEL (USA) |
| 7 | **American Language Center Curriculum** | 4 niveles (Pre-Beginner a Advanced) | ALC Philadelphia |
| 8 | **Azar-Hagen Grammar Series** | Serie estándar americana 3 libros | Pearson |
| 9 | **Pearson Global Scale of English (GSE)** | Learning Objectives por nivel | Pearson |

---

## Estructura Jerárquica

```
Sistema (CEFR | American)
  └── Nivel (A1, A2, B1, B2, C1, C2 | Level 1-6)
       └── Categoría (ej: "Present Tenses")
            └── Subcategoría (ej: "Present Simple")
                 └── Punto Gramatical Exacto (ej: "Present simple: affirmative with he/she/it + -s")
```

---

## CEFR: Distribución por Nivel

| Nivel | Puntos | Categorías | Enfoque |
|-------|--------|------------|---------|
| **A1 - Beginner** | 117 | 11 | Verbo to be, presente simple, pasado simple, artículos, preposiciones básicas, preguntas, adjetivos, imperativos, can, there is/are |
| **A2 - Elementary** | 87 | 14 | Present perfect, past continuous, will vs going to, used to, should/must/might, zero/1st/2nd conditional, passive básico, reported speech, relative clauses, phrasal verbs |
| **B1 - Intermediate** | 96 | 14 | Present perfect continuous, narrative tenses, future continuous/perfect, modales de deducción, 3rd conditional, wish/if only, pasiva extendida, reported speech completo |
| **B2 - Upper Intermediate** | 79 | 12 | Mixed conditionals, inversión condicional, distancing passive, causative, participle clauses, cleft sentences, ellipsis, inversión adverbial |
| **C1 - Advanced** | 74 | 11 | Subjuntivo, todos los tipos de inversión, cleft avanzado, fronting, reporting verb patterns, complex noun phrases, hedging |
| **C2 - Proficiency** | 65 | 8 | Inversión retórica, litotes, antítesis, quiasmo, transferred negation, multi-word prepositions, theme/rheme, registro formal/informal |

---

## American ESL: Distribución por Nivel

| Nivel | Puntos | Categorías | Equivalencia CEFR |
|-------|--------|------------|-------------------|
| **Level 1 - Beginner** | 40 | 12 | A1 |
| **Level 2 - High Beginner** | 28 | 9 | A2- |
| **Level 3 - Intermediate** | 29 | 9 | A2/B1 |
| **Level 4 - High Intermediate** | 24 | 10 | B1+ |
| **Level 5 - Advanced** | 17 | 7 | B2 |
| **Level 6 - High Advanced** | 12 | 4 | C1 |

---

## Archivos Generados

- **Base de datos JSON:** `/root/english_grammar_database.json` (668 puntos gramaticales)
- **Script generador:** `/root/build_grammar_db.py`

---

## Pendiente

- ⏳ Visualización del árbol gramatical (diagrama interactivo/visual)
