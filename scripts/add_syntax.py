#!/usr/bin/env python3
"""Add Syntax & Sentence Structure category to both CEFR and American databases.
Sources: British Council LearnEnglish, Cambridge Grammar of English, Khan Academy, Azar-Hagen.
"""

import json

with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "r") as f:
    db = json.load(f)

# ============================================================
# SYNTAX & SENTENCE STRUCTURE — Points per level
# ============================================================

syntax = {
    "A1": {
        "name": "A1 Syntax — Basic Sentence Structure",
        "description": "Simple sentence formation, sentence types, subject-verb-object. Source: British Council, Cambridge Grammar.",
        "points": [
            "Sentence types: statements/declarative (Subject + Verb + Object: I like coffee, She lives in London)",
            "Sentence types: yes/no questions with inversion (Are you tired?, Do you like tea?)",
            "Sentence types: Wh- questions (Where do you live?, What is your name?)",
            "Sentence types: imperatives/commands (Sit down!, Don't run!, Let's go)",
            "Sentence types: exclamations (What a beautiful day!, How nice!)",
            "Basic SVO word order: Subject + Verb + Object as the fundamental English pattern",
            "Subject identification: the subject is a noun or pronoun that performs the action (She runs, The cat sleeps)",
            "Verb identification: the action or state word (run, is, have, like)",
            "Object identification: the receiver of the action (I like coffee, She reads books)",
            "Every English clause must have a subject (NOT: Is late. → He is late)",
            "Imperative exception: the subject is implied/omitted (Come here! = You come here!)",
            "Simple sentences: one independent clause with one subject and one predicate (I went to the store)",
            "Affirmative vs negative sentences: using not, don't, doesn't, isn't, aren't (I don't like tea, She isn't here)",
            "There is/are as dummy subject for existence (There is a book on the table)"
        ]
    },
    "A2": {
        "name": "A2 Syntax — Compound Sentences & Clause Elements",
        "description": "Compound sentences, clause elements (S,V,O), direct/indirect objects. Source: British Council, Azar-Hagen Fundamentals.",
        "points": [
            "Compound sentences: joining two independent clauses with coordinating conjunctions FANBOYS (for, and, nor, but, or, yet, so)",
            "Compound sentences with 'and' for addition (I like tea and I like coffee)",
            "Compound sentences with 'but' for contrast (She is tired but she is happy)",
            "Compound sentences with 'or' for alternatives (You can stay or you can leave)",
            "Compound sentences with 'so' for result (It was raining, so we stayed home)",
            "Clause elements: Subject (S) — who or what the sentence is about",
            "Clause elements: Verb (V) — the action or state",
            "Clause elements: Object (O) — who or what receives the action (direct object)",
            "Clause elements: Indirect Object (IO) — who benefits from the action (She gave me a book)",
            "Direct vs indirect objects: word order (She gave a book to me = She gave me a book)",
            "Transitive verbs: verbs that require a direct object (I bought a car, She likes music)",
            "Intransitive verbs: verbs that do not take an object (He arrived, She smiled, They laughed)",
            "Verbs that can be both transitive and intransitive (She sang / She sang a song; We ate / We ate pizza)",
            "Subject-verb agreement in compound sentences (He runs and she walks / They run and walk)",
            "Adverbials (A): adding time, place, manner to clauses (I went to the park yesterday, She speaks softly)"
        ]
    },
    "B1": {
        "name": "B1 Syntax — Complex Sentences & Verb Patterns",
        "description": "Complex sentences with subordination, linking verbs, complements. Source: British Council, Azar-Hagen Fundamentals.",
        "points": [
            "Complex sentences: independent clause + dependent/subordinate clause (I stayed home because it rained)",
            "Subordinating conjunctions for reason: because, since, as (I left because I was tired)",
            "Subordinating conjunctions for time: when, while, before, after, until, as soon as (I'll call you when I arrive)",
            "Subordinating conjunctions for condition: if, unless (If it rains, I'll stay home)",
            "Subordinating conjunctions for contrast: although, even though (Although it was cold, we went out)",
            "Linking verbs (copular verbs): be, become, seem, appear, look, sound, smell, taste, feel + adjective/noun complement",
            "Subject complements after linking verbs (She is a doctor, He seems tired, The soup tastes delicious)",
            "Object complements: adjectives/nouns that describe the object (They painted the wall blue, We elected her president)",
            "Ditransitive verbs: verbs that take two objects — direct and indirect (She gave me a gift, He told us a story)",
            "Verb + indirect object + direct object vs Verb + direct object + to/for + indirect (She gave me a book / She gave a book to me)",
            "Common ditransitive verbs: give, send, tell, show, offer, lend, pass, throw, buy, make",
            "There + be patterns for existence (There is/are, There was/were, There will be, There has been)",
            "It as dummy/empty subject (It is raining, It is important to study, It takes time)",
            "Cleft-like emphasis with 'it' (It was John who called, not Mary) — introductory"
        ]
    },
    "B2": {
        "name": "B2 Syntax — Advanced Clause Types & Complementation",
        "description": "Coordination vs subordination, verb complementation, ergative verbs, clause reduction. Source: Cambridge Grammar, Azar-Hagen Understanding & Using.",
        "points": [
            "Coordination vs subordination: independent clauses joined equally (coordination) vs one clause depending on another (subordination)",
            "Correlative conjunctions: both...and, either...or, neither...nor, not only...but also",
            "Complex-compound sentences: two or more independent clauses + at least one dependent clause",
            "Ergative verbs: verbs where the object of the transitive use becomes the subject of the intransitive use (She opened the door / The door opened; I boiled the water / The water boiled)",
            "Common ergative verbs: begin, break, change, close, cook, drop, end, finish, grow, improve, increase, melt, move, open, shut, start, stop, turn",
            "Verb complementation: verb + that-clause (I believe that he is right, She suggested that we leave)",
            "Verb complementation: verb + wh-clause (I don't know where she lives, He explained what happened)",
            "Verb complementation: verb + if/whether clause (I wonder if she will come, She asked whether I was free)",
            "Verb complementation: verb + to-infinitive vs verb + -ing (patterns by verb category)",
            "Reduced clauses: using participles instead of full clauses (The man sitting there / The house built in 1900)",
            "Adjective complements: adjective + that-clause (I'm happy that you came), adjective + to-infinitive (It's easy to use)",
            "Noun complements: noun + that-clause (the fact that..., the idea that..., the belief that...)",
            "Prepositional complements: preposition + wh-clause (It depends on what you mean), preposition + -ing (She's good at singing)",
            "Existential 'there' in all tenses and with modals (There must be a mistake, There used to be a shop here, There is going to be a party)"
        ]
    },
    "C1": {
        "name": "C1 Syntax — Complex Complementation & Phrase Structure",
        "description": "Extraposition, complex complementation, phrase structure analysis, post-modification. Source: Cambridge Grammar, British Council.",
        "points": [
            "Extraposition: moving a heavy subject to the end with 'it' (That he resigned surprised us → It surprised us that he resigned)",
            "Extraposition patterns: It + be + adjective + that-clause (It is clear that...), It + be + adjective + to-infinitive (It is important to...)",
            "It-cleft sentences for focus: It + be + focused element + that/who (It was the manager who made the final decision)",
            "Wh-cleft (pseudo-cleft) sentences: What + clause + be + focus (What I need is more time, What bothers me is his attitude)",
            "Phrase structure: Noun Phrase (NP) — determiner + pre-modifiers + head noun + post-modifiers (the three very old wooden chairs in the corner)",
            "Phrase structure: Verb Phrase (VP) — auxiliary + main verb + complements (has been working, might have been taken)",
            "Phrase structure: Adjective Phrase (AdjP) — intensifier + adjective + complement (very happy about the result, quite different from before)",
            "Phrase structure: Adverb Phrase (AdvP) — intensifier + adverb (very quickly, much more carefully)",
            "Phrase structure: Prepositional Phrase (PP) — preposition + NP complement (in the garden, after the meeting, on top of the hill)",
            "Post-modification in noun phrases: prepositional phrases (the man in the corner), relative clauses (the book that I read), participle clauses (the woman waiting outside)",
            "Multiple post-modification: stacking modifiers after the head noun (a study of the effects of pollution on urban populations in developing countries)",
            "Apposition: two noun phrases side by side referring to the same entity (My brother, a doctor, lives in Paris; The city of London)",
            "Complement clauses within phrases: I like the idea that we might win, There's a chance she'll come",
            "Stylistic fronting for emphasis and cohesion (That I cannot accept; Into the room walked a stranger)"
        ]
    },
    "C2": {
        "name": "C2 Syntax — Information Structure & Stylistic Syntax",
        "description": "Theme/rheme, given/new, marked structures, syntactic choice for effect. Source: Cambridge Grammar, academic syntax references.",
        "points": [
            "Information structure: theme (topic, what the sentence is about) vs rheme (comment, what is said about the theme)",
            "Given-before-new principle: placing familiar/known information before new information for natural flow",
            "End-focus principle: the most important or new information naturally falls at the end of the clause in English",
            "End-weight principle: longer, heavier phrases tend to be placed at the end of the sentence (I gave the book to the girl in the red dress who was sitting by the window)",
            "Marked vs unmarked word order: deviations from SVO for emphasis, contrast, or cohesion (Never have I seen such beauty — marked)",
            "Left-dislocation: moving a topic to the front with a pronoun copy (That film, I really enjoyed it; John, he's always late)",
            "Right-dislocation: adding a clarifying NP at the end (He's a nice guy, John; I found it fascinating, that book)",
            "Passive for information structure: using passive to move the agent to end-focus or to make the patient the theme",
            "Existential 'there' for introducing new information (There's a man at the door who wants to see you)",
            "Cleft and pseudo-cleft as information-structuring devices: choosing what to emphasize and what to background",
            "Ellipsis and substitution for cohesion: omitting recoverable elements (I can [come] if you want me to [come])",
            "Parallelism for rhetorical effect: matching syntactic structures across phrases/clauses (We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields)",
            "Syntactic ambiguity: sentences with multiple possible structures (I saw the man with the telescope — ambiguous: I used a telescope / the man had a telescope)",
            "Stylistic syntax choices: formal vs informal clause structures, academic nominalization vs conversational phrasing"
        ]
    }
}

# American levels map to same content
am_map = {
    "Level 1 - Beginner": "A1",
    "Level 2 - High Beginner": "A2",
    "Level 3 - Intermediate": "B1",
    "Level 4 - High Intermediate": "B2",
    "Level 5 - Advanced": "C1",
    "Level 6 - High Advanced": "C2"
}

def add_syntax(db_obj, level_name, cefr_key, system_name):
    """Add syntax category to a level in a database."""
    if cefr_key not in syntax:
        return 0
    
    syn_data = syntax[cefr_key]
    lvl_data = db_obj["levels"][level_name]
    
    # Check if category already exists
    syn_cat = None
    for cat in lvl_data["categories"]:
        if "Syntax" in cat["category"] and "Sentence Structure" in cat["category"]:
            syn_cat = cat
            break
    
    if syn_cat is None:
        syn_cat = {
            "category": "Syntax & Sentence Structure",
            "subs": []
        }
        lvl_data["categories"].append(syn_cat)
    
    # Add or update subcategory
    found = False
    for sub in syn_cat["subs"]:
        if sub["subcategory"] == syn_data["name"]:
            sub["points"] = syn_data["points"]
            found = True
            break
    
    if not found:
        syn_cat["subs"].append({
            "subcategory": syn_data["name"],
            "description": syn_data["description"],
            "points": syn_data["points"]
        })
    
    return len(syn_data["points"])


# Add to CEFR
print("Adding Syntax to CEFR...")
cefr_total = 0
for lvl_name, lvl_data in db["systems"]["CEFR"]["levels"].items():
    cefr_key = lvl_name.split(" - ")[0]
    n = add_syntax(db["systems"]["CEFR"], lvl_name, cefr_key, "CEFR")
    if n:
        print(f"  {lvl_name}: +{n} syntax points")
        cefr_total += n

# Add to American
print("\nAdding Syntax to American...")
am_total = 0
for lvl_name, lvl_data in db["systems"]["American"]["levels"].items():
    cefr_key = am_map.get(lvl_name, "A1")
    n = add_syntax(db["systems"]["American"], lvl_name, cefr_key, "American")
    if n:
        print(f"  {lvl_name}: +{n} syntax points")
        am_total += n

# Save combined
with open("/root/projects/english-grammar-db/data/english_grammar_database.json", "w") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# Also save separate files
cefr_db = db["systems"]["CEFR"]
cefr_db["meta"] = {
    "title": "CEFR English Grammar Database — British/European System",
    "version": "2.1",
    "system": "CEFR",
    "source": "Cambridge EGP, British Council/EAQUALS"
}
am_db = db["systems"]["American"]
am_db["meta"] = {
    "title": "American ESL Grammar Database — US University IEP System",
    "version": "2.1",
    "system": "American ESL",
    "source": "Pearson GSE, Azar-Hagen, US IEPs"
}

with open("/root/projects/english-grammar-db/data/english_grammar_cefr.json", "w") as f:
    json.dump(cefr_db, f, indent=2, ensure_ascii=False)
with open("/root/projects/english-grammar-db/data/english_grammar_american.json", "w") as f:
    json.dump(am_db, f, indent=2, ensure_ascii=False)

# Stats
cefr_pts = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["CEFR"]["levels"].values())
am_pts = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["American"]["levels"].values())

print(f"\n✅ Syntax added: {cefr_total} CEFR + {am_total} American")
print(f"   CEFR total: {cefr_pts} points")
print(f"   American total: {am_pts} points")
print(f"   Grand total: {cefr_pts + am_pts}")
