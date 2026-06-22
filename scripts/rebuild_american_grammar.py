#!/usr/bin/env python3
"""Rebuild American ESL system with FULL detail matching CEFR granularity"""

import json

# Load current DB to get CEFR portion
with open("/root/english_grammar_database.json", "r") as f:
    db = json.load(f)

# ============================================================
# AMERICAN ESL SYSTEM — Complete, same granularity as CEFR
# 6-level university IEP model (Troy, UDEL, ALC, Azar-Hagen)
# ============================================================

# LEVEL 1 — Beginner (equivalent to A1)
am_l1 = [
  {"category": "Verb 'to be'", "subs": [
    {"subcategory": "Present of 'to be'", "points": [
      "Present simple of 'to be': affirmative am/is/are",
      "Present simple of 'to be': negative am not/isn't/aren't",
      "Present simple of 'to be': yes/no questions (Am I?, Is he?, Are they?)",
      "Present simple of 'to be': short answers (Yes, I am. / No, she isn't.)",
      "Present simple of 'to be': Wh- questions (Where are you?, Who is she?)",
      "Contractions with 'to be' (I'm, you're, he's, she's, it's, we're, they're)"
    ]},
    {"subcategory": "Past of 'to be'", "points": [
      "Was/were: affirmative (I was, You were, They were)",
      "Was/were: negative (I wasn't, You weren't)",
      "Was/were: questions (Was I?, Were you?)"
    ]}
  ]},
  {"category": "Present Simple", "subs": [
    {"subcategory": "Form and Use", "points": [
      "Present simple: affirmative with I/you/we/they (I work, You play)",
      "Present simple: affirmative with he/she/it + -s (He works, She plays)",
      "Present simple: spelling rules for 3rd person singular -s/-es/-ies",
      "Present simple: negative with don't/doesn't (I don't work, She doesn't play)",
      "Present simple: questions with Do/Does (Do you work?, Does she play?)",
      "Present simple: short answers (Yes, I do. / No, she doesn't.)",
      "Present simple for habits and routines (I wake up at 7 every day)",
      "Present simple for general facts and permanent situations",
      "Present simple with adverbs of frequency (always, usually, often, sometimes, rarely, never)",
      "Position of adverbs of frequency (before main verb, after 'to be')"
    ]}
  ]},
  {"category": "Present Continuous", "subs": [
    {"subcategory": "Form and Use", "points": [
      "Present continuous: affirmative am/is/are + verb-ing",
      "Present continuous: negative am not/isn't/aren't + verb-ing",
      "Present continuous: questions (Are you working?, Is she playing?)",
      "Present continuous: spelling rules for -ing form (run→running, make→making)",
      "Present continuous for actions happening right now",
      "Present continuous for temporary situations",
      "Present simple vs present continuous: basic contrast"
    ]}
  ]},
  {"category": "Past Simple", "subs": [
    {"subcategory": "Regular Verbs", "points": [
      "Past simple: regular verbs + -ed (I worked, She played)",
      "Past simple: spelling rules for -ed (stop→stopped, carry→carried)",
      "Past simple: pronunciation of -ed endings (/t/ as in 'worked', /d/ as in 'played', /ɪd/ as in 'wanted')",
      "Past simple: negative with didn't + base form (I didn't go)",
      "Past simple: questions with Did + subject + base form (Did you go?)",
      "Past simple: short answers (Yes, I did. / No, I didn't.)"
    ]},
    {"subcategory": "Irregular Verbs", "points": [
      "Past simple: common irregular verbs (go→went, have→had, do→did, see→saw, eat→ate, come→came, get→got, make→made, take→took, give→gave, know→knew, think→thought, say→said, buy→bought, find→found, tell→told, put→put)"
    ]},
    {"subcategory": "Time Expressions", "points": [
      "Yesterday, last night/week/month/year",
      "Ago (two days ago, a year ago, three weeks ago)",
      "In + past year (in 2020, in 2015)"
    ]}
  ]},
  {"category": "Future Forms", "subs": [
    {"subcategory": "Be going to", "points": [
      "Be going to: affirmative am/is/are going to + base form",
      "Be going to: negative and questions",
      "Be going to for plans and intentions (I'm going to visit my family)",
      "Be going to for predictions based on present evidence (Look at those clouds! It's going to rain)"
    ]},
    {"subcategory": "Will", "points": [
      "Will for future: affirmative will + base form",
      "Will for future: negative won't + base form",
      "Will for future: questions (Will you come?)",
      "Will for spontaneous/sudden decisions (I'll answer the phone)",
      "Will for offers (I'll help you with that)",
      "Will for promises (I'll call you tomorrow)",
      "Will for requests (Will you open the window?)",
      "Will for predictions without evidence (I think it will rain)"
    ]},
    {"subcategory": "Shall", "points": [
      "Shall for suggestions with I/we (Shall I open the window?)",
      "Shall for offers (Shall we dance?)"
    ]}
  ]},
  {"category": "Modals and Imperatives", "subs": [
    {"subcategory": "Can / Can't", "points": [
      "Can for ability (I can swim, She can speak French)",
      "Can't for lack of ability (I can't drive)",
      "Can for permission (Can I go out?, Can I use your phone?)",
      "Can for possibility (It can get very cold here in winter)",
      "Can for requests (Can you help me?)"
    ]},
    {"subcategory": "Would like", "points": [
      "Would like + noun for polite requests (I'd like a coffee, please)",
      "Would you like...? for offers and invitations (Would you like some tea?)",
      "Would like + to-infinitive for desires (I'd like to visit Japan)"
    ]},
    {"subcategory": "Imperatives", "points": [
      "Imperative: affirmative commands and instructions (Sit down!, Stand up!, Open the door)",
      "Imperative: negative with Don't (Don't talk!, Don't worry!, Don't be late)",
      "Imperative with 'please' for politeness (Please sit down, Don't run please)",
      "Let's + base form for suggestions (Let's go, Let's eat)"
    ]}
  ]},
  {"category": "Articles, Nouns, and Determiners", "subs": [
    {"subcategory": "Articles", "points": [
      "Indefinite article a/an: basic rules (a book, an apple, a university, an hour)",
      "Definite article the: basic usage for specific/known reference",
      "Zero article: no article for general plural and uncountable nouns (I like music, Dogs are friendly)"
    ]},
    {"subcategory": "Nouns", "points": [
      "Singular and plural nouns: regular forms with -s/-es (book→books, box→boxes, baby→babies)",
      "Common irregular plurals (man→men, child→children, person→people, woman→women, foot→feet, tooth→teeth, mouse→mice)",
      "Countable vs uncountable nouns: basic distinction (apple/apples vs water, information)",
      "Proper nouns vs common nouns: capitalization rules"
    ]},
    {"subcategory": "Quantifiers", "points": [
      "Some and any: basic use with countable and uncountable nouns",
      "Much vs many: basic distinction (much water, many books)",
      "A lot of for large quantities (a lot of friends, a lot of money)",
      "A little vs a few: basic distinction (a little water = some, a few apples = some)",
      "How much? for uncountable and How many? for countable nouns"
    ]},
    {"subcategory": "Pronouns", "points": [
      "Subject pronouns (I, you, he, she, it, we, they)",
      "Object pronouns: direct and indirect objects (me, you, him, her, it, us, them)",
      "Subject vs object pronouns: basic distinction (I like her vs She likes me)",
      "Possessive adjectives (my, your, his, her, its, our, their)",
      "Demonstrative pronouns: this/that (singular) and these/those (plural)",
      "Indefinite pronouns: something/anything (basic use)"
    ]},
    {"subcategory": "Possessives", "points": [
      "Possessive 's for singular nouns (John's book, my sister's car, the teacher's desk)",
      "Possessive s' for plural nouns ending in -s (my parents' house, the students' classroom)",
      "Possessive 's for irregular plurals (the children's toys, the men's room)",
      "Whose for questions about possession (Whose book is this?)"
    ]}
  ]},
  {"category": "There is/are and It", "subs": [
    {"subcategory": "There is / There are", "points": [
      "There is + singular countable or uncountable noun (There is a book, There is water)",
      "There are + plural countable noun (There are two chairs, There are many people)",
      "There isn't / There aren't: negative forms",
      "Is there? / Are there?: yes/no questions",
      "There was / There were: past forms (There was a problem, There were issues)"
    ]},
    {"subcategory": "It vs There", "points": [
      "It as dummy subject for weather, time, distance (It's cold, It's 3 o'clock, It's far)",
      "There vs It: distinction (There is a book vs It is a book)",
      "This vs It: distinction for identification"
    ]}
  ]},
  {"category": "Adjectives and Adverbs", "subs": [
    {"subcategory": "Adjectives", "points": [
      "Basic descriptive adjectives (big, small, good, bad, new, old, young, tall, short, happy, sad)",
      "Adjective position: before nouns as modifiers (a red car, an interesting book)",
      "Adjective position: after linking verbs, especially 'to be' (The car is red, She seems happy)",
      "Adjectives have no plural form in English (three big cars, NOT three bigs cars)"
    ]},
    {"subcategory": "Adverbs of Manner", "points": [
      "Formation of adverbs from adjectives with -ly (slow→slowly, quick→quickly, careful→carefully)",
      "Adjective vs adverb: basic distinction and usage (He is good at tennis / He plays tennis well)",
      "Irregular adverbs: good→well, fast→fast, hard→hard, late→late, early→early"
    ]},
    {"subcategory": "Comparatives and Superlatives", "points": [
      "Comparative adjectives: short adjectives + -er (older, bigger, cheaper, happier)",
      "Comparative adjectives: long adjectives with more + adjective (more expensive, more interesting, more beautiful)",
      "Superlative adjectives: short adjectives with the + -est (the oldest, the biggest, the cheapest)",
      "Superlative adjectives: long adjectives with the most (the most expensive, the most interesting)",
      "Irregular comparatives and superlatives: good→better→best, bad→worse→worst, far→farther/further",
      "Comparative structures with than (She is taller than me, This book is more interesting than that one)",
      "Superlative structures (She is the tallest in the class)"
    ]}
  ]},
  {"category": "Prepositions", "subs": [
    {"subcategory": "Prepositions of Time", "points": [
      "At for clock times (at 3 o'clock, at noon, at midnight), meals (at breakfast), and festivals (at Christmas)",
      "On for days of the week and dates (on Monday, on May 5th, on my birthday)",
      "In for months, years, seasons, and parts of the day (in June, in 2024, in summer, in the morning)"
    ]},
    {"subcategory": "Prepositions of Place", "points": [
      "At for specific points and locations (at the door, at the bus stop, at home, at school, at work)",
      "On for surfaces and lines (on the table, on the wall, on the floor, on the street)",
      "In for enclosed spaces and areas (in the room, in the box, in the garden, in the city)",
      "Next to, under, between, in front of, behind, over, above, below, among, opposite, near"
    ]},
    {"subcategory": "Other Common Prepositions", "points": [
      "By for means of transport and communication (by car, by bus, by train, by email)",
      "With for accompaniment and instrument (with my friend, with a pen)",
      "For for purpose, recipient, and duration (a gift for you, for two hours)",
      "Of for possession and relationship (the door of the house, a cup of coffee, the city of London)",
      "From...to for origin and destination (from London to Paris, from 9 to 5)"
    ]}
  ]},
  {"category": "Questions", "subs": [
    {"subcategory": "Yes/No Questions", "points": [
      "Yes/No questions with 'to be' by inversion (Are you tired?, Is she ready?)",
      "Yes/No questions with present simple: Do/Does + subject + base form",
      "Yes/No questions with past simple: Did + subject + base form",
      "Yes/No questions with can (Can you swim?)"
    ]},
    {"subcategory": "Wh- Questions", "points": [
      "What: for things, actions, and general information",
      "Where: for places and locations",
      "When: for time and occasions",
      "Who: for people as subject (Who called?) and object (Who did you see?)",
      "Why: for reasons, answered with Because",
      "How: for manner, means, and condition",
      "How much / How many: for quantity (uncountable vs countable)",
      "How old: for age (How old are you?)",
      "How far: for distance (How far is the station?)",
      "How long: for duration (How long is the movie?)",
      "How often: for frequency (How often do you exercise?)",
      "Whose: for possession (Whose bag is this?)",
      "Which: for choice from a limited set (Which color do you prefer?)",
      "What time: for specific clock time (What time does the train leave?)"
    ]}
  ]},
  {"category": "Conjunctions", "subs": [
    {"subcategory": "Basic Coordinating Conjunctions", "points": [
      "And for addition and linking (I like tea and coffee, She sings and dances)",
      "But for contrast and opposition (I'm tired but happy, He's rich but not generous)",
      "Or for alternatives and choices (tea or coffee, now or later)",
      "So for result and consequence (I was tired so I went to bed early)",
      "Because for reason and cause (I stayed home because it rained)"
    ]}
  ]},
  {"category": "Word Order", "subs": [
    {"subcategory": "Sentence Structure", "points": [
      "Basic word order in English: Subject + Verb + Object (SVO) pattern",
      "Word order with adverbs of frequency: before main verb, after 'to be'",
      "Word order with adjectives: opinion→size→age→color→origin→material (a beautiful big old red Italian leather bag)",
      "Word order in questions: (Wh-word) + auxiliary + subject + main verb"
    ]}
  ]},
  {"category": "Gerunds and Infinitives (Basic)", "subs": [
    {"subcategory": "Verb Patterns", "points": [
      "Verb + -ing after like, love, hate, enjoy, prefer (I like reading, She loves swimming)",
      "Verb + to-infinitive after want, need, would like, decide, hope (I want to go, She hopes to visit)",
      "Stative/stative verbs: verbs not normally used in continuous (know, like, love, hate, want, need, believe, understand, seem, belong, own)"
    ]}
  ]}
]

# LEVEL 2 — High Beginner (A2)
am_l2 = [
  {"category": "Present Tenses Extended", "subs": [
    {"subcategory": "Present Simple vs Continuous", "points": [
      "Present simple vs present continuous: extended contrast (routines/general truths vs actions now/temporary)",
      "Stative verbs not used in continuous tenses: full list (know, like, love, hate, want, need, believe, understand, remember, forget, seem, belong, own, possess, consist, contain, matter, mean, prefer, realize, recognize, suppose)",
      "Present simple for timetabled/scheduled future events (The train leaves at 6, The movie starts at 8)"
    ]},
    {"subcategory": "Present Perfect", "points": [
      "Present perfect: form have/has + past participle (regular and irregular past participles)",
      "Present perfect: affirmative (I've visited, She's gone), negative (I haven't seen), questions (Have you ever...?)",
      "Present perfect for life experiences without specific time (I've been to Paris, She's never eaten sushi)",
      "Present perfect with ever (Have you ever been to...?) and never (I've never tried that)",
      "Present perfect with just for very recent actions (I've just finished my homework)",
      "Present perfect with already for earlier than expected (I've already eaten)",
      "Present perfect with yet in questions and negatives (Have you finished yet?, I haven't done it yet)",
      "Present perfect with for + duration (I've lived here for five years / since 2019)",
      "Present perfect with since + starting point (I've known her since 2010)",
      "Present perfect vs past simple: time reference distinction (experience/life vs specific completed past time)"
    ]}
  ]},
  {"category": "Past Tenses Extended", "subs": [
    {"subcategory": "Past Simple Extended", "points": [
      "Past simple: form and use for completed actions at a specific time in the past",
      "Past simple: extended irregular verbs (fly→flew, drink→drank, swim→swam, sing→sang, ring→rang, begin→began, break→broke, choose→chose, drive→drove, forget→forgot, grow→grew, hide→hid, ride→rode, rise→rose, shake→shook, speak→spoke, steal→stole, throw→threw, wear→wore, write→wrote)",
      "Past simple with time expressions: yesterday, last week, ...ago, in + year, when + clause",
      "Past simple for sequences of completed past actions (I got up, took a shower, and ate breakfast)"
    ]},
    {"subcategory": "Past Continuous", "points": [
      "Past continuous: form was/were + verb-ing",
      "Past continuous: affirmative (I was working), negative (She wasn't listening), questions (Were you sleeping?)",
      "Past continuous for actions in progress at a specific past time (At 8pm, I was watching TV)",
      "Past continuous and past simple together: interrupted actions (I was watching TV when the phone rang)",
      "Past continuous for two simultaneous past actions (I was cooking while she was setting the table)",
      "Past continuous for background descriptions and setting the scene in narratives"
    ]},
    {"subcategory": "Past Perfect", "points": [
      "Past perfect: form had + past participle for all subjects",
      "Past perfect for an action completed before another past action (When I arrived, they had already left)",
      "Past perfect with already, just, never (He had already eaten when I invited him)",
      "Past perfect for sequencing and clarifying the order of past events"
    ]},
    {"subcategory": "Used to", "points": [
      "Used to + base form for past habits that no longer happen (I used to play tennis every weekend)",
      "Used to for past states that are no longer true (I used to live in London, She used to be shy)",
      "Didn't use to: negative form for absence of past habit",
      "Did you use to...?: question form"
    ]}
  ]},
  {"category": "Future Forms Expanded", "subs": [
    {"subcategory": "All Future Expressions", "points": [
      "Will vs going to: detailed comparison of uses",
      "Will for predictions without present evidence (I think it will rain tomorrow)",
      "Going to for plans and intentions decided before speaking",
      "Going to for predictions based on present evidence (Look at those clouds, it's going to rain)",
      "Will for spontaneous decisions at the moment of speaking",
      "Present continuous for fixed future arrangements (I'm meeting her tomorrow at 3)",
      "Present simple for timetabled/scheduled future (The flight leaves at 8am, The course starts next Monday)",
      "Future time clauses: present tense after when/as soon as/after/before/until (I'll call you when I arrive)"
    ]}
  ]},
  {"category": "Modals Extended", "subs": [
    {"subcategory": "Have to / Must / Need to", "points": [
      "Have to / has to for external obligation from rules or circumstances (I have to wear a uniform at work)",
      "Don't have to / doesn't have to for lack of obligation (You don't have to pay, it's free)",
      "Must for strong personal obligation or rules the speaker believes in (I must finish this report today)",
      "Mustn't for strong prohibition (You mustn't smoke in here, it's illegal)",
      "Must vs have to: internal vs external obligation distinction",
      "Need to for necessity (I need to buy groceries)",
      "Don't need to / needn't for lack of necessity"
    ]},
    {"subcategory": "Should / Ought to", "points": [
      "Should for advice and recommendations (You should see a doctor, You should visit Paris)",
      "Shouldn't for negative advice (You shouldn't eat so much sugar)",
      "Should for expectation based on logic or schedule (He left an hour ago so he should be here soon)",
      "Ought to as a more formal alternative to should (You ought to apologize)"
    ]},
    {"subcategory": "May / Might", "points": [
      "May for possibility in the present/future (I may go to the party, It may rain later)",
      "Might for weaker possibility (I might join you, but I'm not sure)",
      "May for formal permission (May I come in? May I use your phone?)",
      "May vs might: might suggests lower probability than may",
      "Might not / may not for negative possibility (She might not come)"
    ]},
    {"subcategory": "Could and Can Extended", "points": [
      "Could for past ability (I could swim really well when I was young)",
      "Could for polite requests (Could you help me with this?, Could you open the window?)",
      "Could for possibility in the present/future (It could rain later, Be careful, you could fall)",
      "Can vs could for requests: could is more polite and formal",
      "Was/were able to for specific past achievements (I was able to fix the problem)"
    ]}
  ]},
  {"category": "Conditionals", "subs": [
    {"subcategory": "Zero Conditional", "points": [
      "Zero conditional for general truths and scientific facts: If + present simple, present simple (If you heat water to 100°C, it boils)",
      "Zero conditional for habits and routines (If I'm tired, I go to bed early)",
      "Zero conditional: If and When are often interchangeable for general truths",
      "Zero conditional with imperative in the main clause (If you're tired, go to bed)"
    ]},
    {"subcategory": "First Conditional", "points": [
      "First conditional: If + present simple, will + base form (If it rains tomorrow, I'll stay home)",
      "First conditional with modal verbs in the main clause: can, may, might, should (If you finish early, you can leave)",
      "First conditional with imperatives in the main clause (If you see John, tell him to call me)",
      "First conditional with unless = if not (I won't go unless you come with me)",
      "First conditional with as long as / provided that / on condition that (You can borrow my car as long as you drive carefully)"
    ]},
    {"subcategory": "Second Conditional", "points": [
      "Second conditional for unreal/hypothetical present or future: If + past simple, would + base form (If I had more money, I would travel the world)",
      "If I were... (were for all persons in formal/written English: If I were you, If she were here)",
      "Would in the main clause: could and might also possible (If I spoke French, I could work in Paris)",
      "Second conditional for giving advice: If I were you, I would...",
      "Wish + past simple for present wishes about unreal situations (I wish I was/were taller, I wish I lived by the beach)"
    ]}
  ]},
  {"category": "Passive Voice (Introduction)", "subs": [
    {"subcategory": "Present and Past Simple Passive", "points": [
      "Passive voice formation: be (conjugated) + past participle",
      "Present simple passive: am/is/are + past participle (English is spoken worldwide, Coffee is grown in Brazil)",
      "Past simple passive: was/were + past participle (The house was built in 1900, The windows were broken)",
      "Active vs passive: when the action is more important than the doer (agent unknown, obvious, or unimportant)",
      "Passive with by to introduce the agent when needed (The book was written by George Orwell)"
    ]}
  ]},
  {"category": "Reported Speech (Introduction)", "subs": [
    {"subcategory": "Basic Reported Speech", "points": [
      "Reported speech with say and tell: usage difference (say something, tell someone something)",
      "Tense backshift in reported speech: present simple→past simple (He said he was tired)",
      "Tense backshift: present continuous→past continuous (She said she was working)",
      "Tense backshift: will→would (He said he would call later)",
      "Tense backshift: can→could (She said she could help)",
      "Reported statements: basic transformations with pronoun changes",
      "Reported yes/no questions with if/whether (She asked if I was coming)",
      "Reported Wh- questions: word order changes to statement order (He asked where I lived)",
      "Time and place expression changes in reported speech (now→then, today→that day, here→there, tomorrow→the next day, yesterday→the day before)"
    ]}
  ]},
  {"category": "Articles and Quantifiers Extended", "subs": [
    {"subcategory": "Articles Extended", "points": [
      "A/an for first mention of singular countable nouns (I saw a dog. The dog was big.)",
      "The for second and subsequent mentions and for unique/known reference (the sun, the moon, the president)",
      "No article (zero article) for general plural countable nouns (Dogs are loyal animals)",
      "No article for general uncountable nouns (Music is important to me, I love coffee)",
      "Articles with countable vs uncountable nouns: comprehensive distinction"
    ]},
    {"subcategory": "Quantifiers Extended", "points": [
      "Much with uncountable nouns in questions and negatives (How much time?, I don't have much money)",
      "Many with plural countable nouns in questions and negatives (How many books?, There aren't many options)",
      "A lot of / lots of for large quantities in positive statements (a lot of people, lots of time)",
      "Too + adjective/adverb (too expensive, too quickly)",
      "Too much + uncountable noun (too much sugar)",
      "Too many + plural countable noun (too many people)",
      "Enough + noun (enough time, enough chairs)",
      "Adjective/adverb + enough (old enough, fast enough)",
      "A few + plural countable noun for a small number (a few friends = some)",
      "A little + uncountable noun for a small amount (a little help = some)",
      "Most, most of, the most: distinctions (most people agree / most of the students / the most expensive)",
      "Something, anything, nothing, everything",
      "Somebody/anybody/nobody/everybody, someone/anyone/no one/everyone",
      "Somewhere, anywhere, nowhere, everywhere"
    ]}
  ]},
  {"category": "Relative Clauses (Introduction)", "subs": [
    {"subcategory": "Defining Relative Clauses", "points": [
      "Who for people as subject of relative clause (The woman who lives next door is a doctor)",
      "Who/whom for people as object of relative clause (The man who/whom I met yesterday)",
      "Which for things and animals (The book which I bought is fascinating)",
      "That for people and things in informal/defining relative clauses (The book that I read, The woman that called)",
      "Where for places (The restaurant where we had dinner was amazing)",
      "When for times (I remember the day when we first met)",
      "Whose for possession (The man whose car was stolen)",
      "Omitting the relative pronoun when it functions as the object of the relative clause (The book I bought, The man I met)"
    ]}
  ]},
  {"category": "Gerunds and Infinitives Extended", "subs": [
    {"subcategory": "Verb + -ing", "points": [
      "Verbs always followed by -ing: enjoy, finish, mind (would you mind), suggest, recommend, keep (continue), avoid, consider, discuss, practise, miss, imagine, delay, postpone, admit, deny",
      "Verb + -ing after prepositions (good at singing, interested in learning, tired of waiting, afraid of flying, look forward to meeting, think about/of doing)",
      "Go + -ing for recreational activities (go swimming, go shopping, go running, go fishing, go skiing)"
    ]},
    {"subcategory": "Verb + to-infinitive", "points": [
      "Verbs followed by to-infinitive: want, decide, hope, expect, plan, agree, offer, promise, refuse, learn, need, would like, would love, would prefer, seem, appear, tend, manage, fail, afford, arrange, attempt",
      "Adjective + to-infinitive (happy to help, difficult to understand, easy to use, important to remember)",
      "Expressing purpose with to + infinitive (I went to the store to buy milk)",
      "Expressing purpose with for + noun/gerund (I went to the store for milk, this tool is for cutting)"
    ]},
    {"subcategory": "Verb + -ing or to-infinitive (same meaning)", "points": [
      "Like, love, hate, prefer: both -ing and to-infinitive possible with little difference",
      "Start, begin, continue: both -ing and to-infinitive possible with same meaning"
    ]},
    {"subcategory": "Verb + -ing or to-infinitive (different meaning)", "points": [
      "Remember + -ing (past memory) vs remember + to-infinitive (future obligation): I remember locking the door vs Remember to lock the door",
      "Forget + -ing (past action forgotten) vs forget + to-infinitive (fail to do): I'll never forget meeting her vs I forgot to call you",
      "Try + -ing (experiment) vs try + to-infinitive (attempt with effort): Try adding more salt vs I tried to open the door",
      "Stop + -ing (cease an activity) vs stop + to-infinitive (pause in order to): Stop smoking vs He stopped to smoke a cigarette"
    ]}
  ]},
  {"category": "Adjectives and Adverbs Extended", "subs": [
    {"subcategory": "Comparatives and Superlatives Extended", "points": [
      "Comparative and superlative adjectives: full review of short, long, and irregular forms",
      "Comparative adverbs: more + adverb (more quickly, more carefully, more often)",
      "Superlative adverbs: the most + adverb (the most quickly, the most carefully)",
      "As + adjective/adverb + as for equality (She's as tall as her brother, He runs as fast as me)",
      "Not as + adjective/adverb + as for inequality (This book is not as interesting as the other one)",
      "No longer / not any longer / not anymore for situations that have changed"
    ]},
    {"subcategory": "Adverbs Extended", "points": [
      "Adverbs of manner: regular formation with -ly and irregular forms",
      "Adverbs of frequency: always, usually, often, sometimes, occasionally, rarely, seldom, never — position rules",
      "Adverbial phrases of time (yesterday, last week, at the moment, these days)",
      "Adverbial phrases of place (at home, in the park, everywhere)",
      "Word order with multiple adverbs: manner + place + time (She sang beautifully at the concert last night)"
    ]}
  ]},
  {"category": "Phrasal Verbs and Verb Patterns", "subs": [
    {"subcategory": "Common Phrasal Verbs", "points": [
      "Wake up, get up, stand up, sit down, lie down",
      "Turn on/off (lights, TV), put on/take off (clothes), pick up (lift/collect)",
      "Look at, look for (search), look after (take care of)",
      "Come in, go out, come back, go back, get back (return)",
      "Give up (quit/stop), find out (discover), carry on (continue)",
      "Run out of (exhaust supply), get on with (have good relationship), look forward to (anticipate)",
      "Transitive vs intransitive phrasal verbs (I woke up vs I turned on the TV)",
      "Separable vs inseparable phrasal verbs: with pronouns, the object must go between (turn it on, NOT turn on it)"
    ]},
    {"subcategory": "Special Verbs", "points": [
      "Make vs do: common collocations (make a mistake, make a decision, make dinner / do homework, do the dishes, do business)",
      "Have vs take: common collocations (have a shower/bath, have breakfast/lunch, have a good time / take a break, take a walk, take a photo)",
      "Get: basic uses (get up, get home, get a job, get tired, get married, get ready, get the message)",
      "Verbs with two objects (direct and indirect): give someone something / give something to someone (She gave me a book / She gave a book to me)"
    ]}
  ]},
  {"category": "Auxiliary Verbs and Short Responses", "subs": [
    {"subcategory": "Auxiliary Verbs and Agreement", "points": [
      "Auxiliary verbs: do, be, have — their functions in forming questions, negatives, and short answers",
      "So + auxiliary + subject for positive agreement (I'm tired. — So am I.)",
      "Neither/Nor + auxiliary + subject for negative agreement (I can't swim. — Neither can I.)",
      "Short answers with auxiliaries: Yes, I do. / No, she isn't. / Yes, we have."
    ]},
    {"subcategory": "Question Tags (Introduction)", "points": [
      "Question tags with be: positive statement + negative tag (You're tired, aren't you?)",
      "Question tags: negative statement + positive tag (You aren't tired, are you?)",
      "Question tags with auxiliary verbs: do/does/did, have/has/had, can/could, will/would"
    ]}
  ]},
  {"category": "Connectors and Sequencers", "subs": [
    {"subcategory": "Time and Logic Connectors", "points": [
      "When, while, as for simultaneous and sequential time (When I arrived, they were eating / While I was cooking, she was reading)",
      "Before, after for time sequence (After I finish work, I'll call you)",
      "Until for an action continuing up to a point (I'll wait until you're ready)",
      "First, then, next, after that, finally for sequencing events",
      "However, although, even though for introducing contrast",
      "Because, since, as for giving reasons"
    ]}
  ]}
]

# LEVEL 3 — Intermediate (A2+/B1)
am_l3 = [
  {"category": "Present Tenses Advanced", "subs": [
    {"subcategory": "Present Perfect Continuous", "points": [
      "Present perfect continuous: form have/has been + verb-ing",
      "Present perfect continuous for actions that started in the past and continue to the present (I've been studying English for three years)",
      "Present perfect continuous for recently stopped actions with present evidence or results (You're out of breath! — I've been running)",
      "Present perfect simple vs present perfect continuous: result/focus on completion vs duration/ongoing action",
      "Present perfect continuous: questions with How long (How long have you been waiting?)"
    ]},
    {"subcategory": "Present Simple vs Continuous (Advanced)", "points": [
      "Present simple for live commentary and sports narration (He passes the ball... and scores!)",
      "Present continuous with always for repeated annoying or surprising behavior (He's always complaining about something!)",
      "Stative verbs used dynamically with a change in meaning: I think it's good (opinion) vs I'm thinking about it (considering)",
      "Stative verbs used dynamically: have (possess) vs having (eating/experiencing), see (perceive) vs seeing (meeting/dating), taste (flavor) vs tasting (testing)",
      "Present simple for newspaper headlines and plot summaries"
    ]}
  ]},
  {"category": "Past Tenses Advanced", "subs": [
    {"subcategory": "Narrative Tenses", "points": [
      "Narrative tenses combined: past simple (main events), past continuous (background/descriptions), past perfect (earlier past events)",
      "Past perfect for sequencing and clarifying the order of multiple past events (By the time I arrived, they had already eaten and had left)",
      "Past perfect continuous: form had been + verb-ing",
      "Past perfect continuous for actions that were in progress before another past event (She had been waiting for hours when the bus finally arrived)",
      "Past perfect continuous vs past perfect simple: duration/process vs completion/result"
    ]},
    {"subcategory": "Used to / Would / Be used to / Get used to", "points": [
      "Used to + base form for past habits and states that are no longer true",
      "Would + base form for repeated past actions and typical behavior (NOT for past states: NOT I would live in London)",
      "Be used to + noun/gerund for being accustomed to/familiar with something (I'm used to the noise now, She's used to getting up early)",
      "Get used to + noun/gerund for the process of becoming accustomed (It took me a while to get used to driving on the left)",
      "Used to vs be used to vs get used to: complete distinction (past habit vs current familiarity vs process of adaptation)"
    ]}
  ]},
  {"category": "Future Forms Advanced", "subs": [
    {"subcategory": "All Future Forms", "points": [
      "Will, going to, present continuous, present simple for future: complete comparison of use cases",
      "Future continuous: form will be + verb-ing",
      "Future continuous for actions that will be in progress at a specific future time (This time tomorrow, I'll be flying to Paris)",
      "Future continuous for planned or expected events (I'll be seeing John later — we work together)",
      "Future perfect: form will have + past participle",
      "Future perfect for actions completed before a specific future time (By Friday, I will have finished the report)",
      "Future perfect with by + time expression (By the end of this year, she will have saved enough money)",
      "Future perfect continuous: form will have been + verb-ing (By June, I'll have been working here for 10 years)"
    ]}
  ]},
  {"category": "Modals Advanced", "subs": [
    {"subcategory": "Obligation, Prohibition, Advice (All)", "points": [
      "Must vs have to: internal/personal obligation vs external/rules obligation (I must call my mom / I have to wear a uniform)",
      "Mustn't for prohibition vs don't have to for lack of obligation (You mustn't smoke here / You don't have to come if you don't want to)",
      "Should / ought to for advice (ought to is slightly more formal, less common in questions/negatives)",
      "Had better + base form for strong advice with warning of negative consequences (You'd better hurry or you'll miss the train)",
      "Should have + past participle for past advice/regret (You should have told me earlier!)",
      "Shouldn't have + past participle for past criticism (I shouldn't have eaten so much)"
    ]},
    {"subcategory": "Ability (All Tenses)", "points": [
      "Can for present ability (I can speak three languages)",
      "Could for general past ability (I could run fast when I was young)",
      "Was/were able to for specific past achievements on a particular occasion (I was able to fix the problem yesterday)",
      "Could vs was/were able to: general ability vs specific achievement distinction",
      "Will be able to for future ability (After the course, you'll be able to speak Spanish)",
      "Manage to + base form for succeeding in doing something difficult (I managed to finish on time)",
      "Succeed in + -ing as alternative for ability (She succeeded in passing the exam)"
    ]},
    {"subcategory": "Deduction and Speculation (Present)", "points": [
      "Must for strong logical deduction about the present (You must be exhausted after that 12-hour shift)",
      "Can't for strong negative deduction/impossibility (That can't be true — he would never do that)",
      "May/might/could for present possibility and speculation (She might be at home, I'm not sure)",
      "Must have + past participle for logical deduction about the past (He must have left already — his car isn't here)",
      "Might/may/could have + past participle for past possibility (She might have forgotten about the meeting)",
      "Can't have + past participle for past impossibility (He can't have said that — he wasn't even there)"
    ]},
    {"subcategory": "Preferences", "points": [
      "Would rather + base form for preference in the present/future (I'd rather stay home tonight)",
      "Would rather + subject + past simple for preference about another person's action (I'd rather you didn't smoke here)",
      "Would sooner + base form (less common variant of would rather)",
      "It's time + past simple for expressing that something should happen now/soon (It's time we left, It's high time you got a job)"
    ]}
  ]},
  {"category": "Conditionals Advanced", "subs": [
    {"subcategory": "Zero, First, and Second Conditionals (Review/Extension)", "points": [
      "Zero conditional: expanded use for instructions and imperatives",
      "First conditional: with unless (= if not), as long as, provided that, on condition that",
      "Second conditional: for hypothetical/unreal present and future situations",
      "First vs second conditional: real possibility vs unreal/hypothetical distinction",
      "Second conditional: If I were you for giving advice"
    ]},
    {"subcategory": "Third Conditional", "points": [
      "Third conditional for unreal/hypothetical past situations: If + past perfect, would have + past participle (If I had studied harder, I would have passed the exam)",
      "Third conditional for expressing regrets about the past (If I hadn't said that, we would still be friends)",
      "Third conditional with could have / might have for different past possibilities (If you had called, I could have helped)",
      "Conditionals review: comparing zero, first, second, and third conditionals side by side"
    ]},
    {"subcategory": "Wish and If only", "points": [
      "Wish + past simple for present wishes about unreal situations (I wish I had more free time)",
      "Wish + past perfect for past regrets (I wish I had studied harder at school)",
      "Wish + would for complaints about present behavior or situations you want to change (I wish you would stop interrupting me)",
      "If only as a stronger, more emphatic form of wish (If only I had more money!, If only I hadn't said that!)"
    ]}
  ]},
  {"category": "Passive Voice Extended", "subs": [
    {"subcategory": "Passive in All Basic Tenses", "points": [
      "Present simple passive: am/is/are + past participle",
      "Past simple passive: was/were + past participle",
      "Present perfect passive: have/has been + past participle (The house has been sold)",
      "Future simple passive: will be + past participle (The results will be announced tomorrow)",
      "Passive with modal verbs: can/must/should/might + be + past participle (This door must be kept closed)",
      "Active vs passive: when and why we choose the passive voice (agent unknown, obvious, unimportant, or to sound more formal/impersonal)",
      "Passive voice with the agent by when the agent is important information (The telephone was invented by Alexander Graham Bell)"
    ]}
  ]},
  {"category": "Reported Speech Extended", "subs": [
    {"subcategory": "Reported Statements, Questions, and Commands", "points": [
      "Reported statements: complete tense backshift rules with timeline",
      "Reported yes/no questions: if/whether with statement word order (She asked if I was coming)",
      "Reported Wh- questions: wh-word + subject + verb (He asked where I lived, She wanted to know what I was doing)",
      "Reported commands and requests: tell/ask + object + to-infinitive (He told me to sit down, She asked me to help)",
      "Reporting verbs: say, tell, ask (basic), advise, suggest, recommend, warn, invite, promise, offer, refuse, remind, persuade, convince",
      "Reporting verb patterns: suggest + -ing OR suggest + that + subject + (should) + base form",
      "Reporting verb patterns: advise/recommend + object + to-infinitive (She advised me to see a doctor)",
      "Modal verb changes in reported speech: can→could, will→would, may→might, must→had to, shall→should",
      "Time and place expression changes: now→then, today→that day, here→there, this→that, tomorrow→the next day, yesterday→the day before, last week→the week before, next month→the following month"
    ]}
  ]},
  {"category": "Articles, Nouns, and Quantifiers Advanced", "subs": [
    {"subcategory": "Articles: Complete Rules", "points": [
      "A/an: uses and rules including a before consonant sounds and an before vowel sounds (a university, an hour)",
      "The for unique items (the sun, the moon, the internet, the president), superlatives, and ordinal numbers",
      "The for shared/understood reference (Close the door, I'm going to the bank)",
      "Zero article: generalizations with plural and uncountable nouns, proper names, meals, sports, subjects",
      "Articles with geographical names: the + rivers/oceans/mountain ranges/deserts (the Thames, the Pacific, the Alps, the Sahara)",
      "Articles with geographical names: no article for countries (except those with plural/republic/kingdom: the UK, the USA, the Netherlands), cities, individual mountains, lakes",
      "Articles with institutions: go to school/hospital/prison/church (as a patient/student/inmate) vs go to the school (as a visitor)",
      "Articles with musical instruments (play the piano) vs sports (play tennis)"
    ]},
    {"subcategory": "Quantifiers: Complete Set", "points": [
      "Much, many, a lot of, lots of, plenty of — formality and sentence type distinctions",
      "Little, a little, few, a few — with vs without article meaning change (few = not enough, a few = some/small number)",
      "All, most, some, any, no, none as quantifiers",
      "Both, either, neither: both + plural noun (both books), either/neither + singular noun (either book)",
      "Both...and, either...or, neither...nor correlative conjunctions",
      "Another vs other vs others vs the other vs the others: complete distinctions"
    ]},
    {"subcategory": "Reflexive Pronouns", "points": [
      "Reflexive pronouns: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves",
      "Reflexive pronouns when the subject and object are the same person/thing (I cut myself, She taught herself)",
      "By + reflexive pronoun for doing something alone/without help (I did it by myself, He lives by himself)",
      "Reflexive pronouns for emphasis on the subject (The president himself attended, I'll do it myself)"
    ]}
  ]},
  {"category": "Relative Clauses Extended", "subs": [
    {"subcategory": "Defining and Non-Defining Relative Clauses", "points": [
      "Defining relative clauses: essential to identify which person/thing (no commas, that can replace who/which)",
      "Non-defining relative clauses: extra, non-essential information (commas required, that NOT allowed)",
      "Who, which, that, whose, where, when, why: all relative pronouns",
      "Prepositions in relative clauses: formal (the person to whom I spoke) vs informal (the person I spoke to)",
      "What as a relative pronoun meaning 'the thing(s) that' (I don't understand what you mean, What I need is a break)"
    ]}
  ]},
  {"category": "Gerunds and Infinitives: Complete Patterns", "subs": [
    {"subcategory": "Verb + -ing (Gerund)", "points": [
      "Verbs followed by gerund: admit, avoid, can't help, can't stand, consider, delay, deny, discuss, dislike, enjoy, feel like, finish, give up, imagine, involve, keep (on), mention, mind, miss, postpone, practise, recommend, regret, risk, suggest, tolerate, understand"
    ]},
    {"subcategory": "Verb + to-infinitive", "points": [
      "Verbs followed by to-infinitive: afford, agree, appear, arrange, ask, attempt, choose, claim, decide, demand, deserve, expect, fail, happen, help, hesitate, hope, intend, learn, manage, need, offer, plan, prepare, pretend, promise, refuse, seem, swear, tend, threaten, volunteer, wait, want, wish, would like, would love, yearn"
    ]},
    {"subcategory": "Verb + Object + to-infinitive", "points": [
      "Verbs taking object + to-infinitive: advise, allow, ask, beg, cause, challenge, convince, encourage, expect, forbid, force, get, help, invite, need, order, permit, persuade, prefer, recommend, remind, request, require, teach, tell, urge, want, warn, would like"
    ]},
    {"subcategory": "Verb + Object + Bare Infinitive (without to)", "points": [
      "Let + object + base form (Let me go, Let him speak)",
      "Make + object + base form for forcing (She made me do it)",
      "Help + object + base form OR to-infinitive (Help me carry this / Help me to carry this)",
      "Verbs of perception: see/hear/watch/notice/feel + object + base form for complete action (I saw him cross the street)",
      "Verbs of perception: see/hear/watch/notice/feel + object + -ing for action in progress (I saw him crossing the street)"
    ]},
    {"subcategory": "Verb + -ing or to-infinitive with Meaning Change", "points": [
      "Remember + -ing (recall past action) vs remember + to-infinitive (not forget future obligation)",
      "Forget + -ing (forget something that happened) vs forget + to-infinitive (fail to do something)",
      "Regret + -ing (feel sorry about past action) vs regret + to-infinitive (feel sorry to inform)",
      "Try + -ing (experiment, see what happens) vs try + to-infinitive (make an effort, attempt something difficult)",
      "Stop + -ing (cease an activity) vs stop + to-infinitive (stop in order to do something)",
      "Mean + -ing (involve, entail) vs mean + to-infinitive (intend)",
      "Go on + -ing (continue) vs go on + to-infinitive (move to the next stage)"
    ]}
  ]},
  {"category": "Adjectives and Adverbs Advanced", "subs": [
    {"subcategory": "-ed and -ing Adjectives", "points": [
      "-ed adjectives for how people feel (bored, interested, excited, tired, confused, surprised, disappointed, annoyed, frightened, satisfied)",
      "-ing adjectives for describing what causes the feeling (boring, interesting, exciting, tiring, confusing, surprising, disappointing, annoying, frightening, satisfying)",
      "Complete distinction: I am interested (feeling) vs The book is interesting (quality of the thing)"
    ]},
    {"subcategory": "Comparative and Superlative Structures", "points": [
      "Modifying comparatives for degree: much, far, a lot, considerably, significantly + comparative (much better, far more interesting)",
      "Modifying comparatives for small differences: a bit, a little, slightly, marginally + comparative (a bit better, slightly cheaper)",
      "The...the... for parallel increase (The more you practice, the better you get, The sooner, the better)",
      "So + adjective/adverb + that for result (It was so hot that we couldn't sleep)",
      "Such + (a/an) + adjective + noun + that for result (It was such a beautiful day that we decided to go out)",
      "So much / so many + that (There was so much noise that I couldn't concentrate)",
      "Compound adjectives with numbers: a two-hour meeting, a five-star hotel, a three-bedroom apartment, a ten-minute walk"
    ]},
    {"subcategory": "Adverbs of Degree and Certainty", "points": [
      "Adverbs of degree: quite, rather, pretty, fairly, extremely, incredibly, absolutely, completely, totally, slightly",
      "Adverbs of certainty: definitely, certainly, probably, possibly, maybe, perhaps, undoubtedly, surely",
      "Adverb position in sentences: front (Perhaps he's right), mid (He'll probably come), end (He'll come, probably)"
    ]}
  ]},
  {"category": "Phrasal Verbs Extended", "subs": [
    {"subcategory": "Extended Phrasal Verb Set", "points": [
      "Common extended phrasal verbs: give up, put off (postpone), take up (start hobby), make up (invent/reconcile), come up with (think of), run out of (exhaust), get on with (have good relationship), look forward to (anticipate), carry on (continue), find out (discover), turn up (arrive/appear), turn down (refuse), set up (establish), bring up (raise topic/children), call off (cancel), figure out (understand/solve), get over (recover), go through (experience), look into (investigate), point out (indicate)",
      "Three-part phrasal verbs: look forward to, get on with, put up with (tolerate), come up with, cut down on (reduce), get away with (escape punishment), live up to (meet expectations), run out of, stand up for (defend)",
      "Phrasal verbs with multiple meanings (take off: remove clothing, leave the ground/airplane, become successful)",
      "Separable vs inseparable phrasal verbs: detailed rules for pronoun object placement"
    ]}
  ]},
  {"category": "Question Tags and Agreement", "subs": [
    {"subcategory": "Question Tags", "points": [
      "Question tags with all auxiliary verbs (isn't it?, aren't you?, don't you?, didn't he?, haven't they?, can't you?, won't she?)",
      "Positive statement + negative tag (You're coming, aren't you?)",
      "Negative statement + positive tag (You don't like it, do you?)",
      "Question tags with 'let's': Let's go, shall we?",
      "Question tags with imperatives: Open the door, will you? / Don't be late, will you?",
      "Intonation in question tags: rising (genuine question, uncertain) vs falling (confirmation expected, rhetorical)",
      "Special tags: I am → aren't I?, There is → isn't there?, This is → isn't it?, Nobody → do they?"
    ]},
    {"subcategory": "Agreement and Disagreement", "points": [
      "So + auxiliary + subject for positive agreement (I like pizza. — So do I.)",
      "Neither/Nor + auxiliary + subject for negative agreement (I can't swim. — Neither can I.)",
      "Short responses with think/hope/believe/expect (Is it going to rain? — I hope not. / I think so.)"
    ]}
  ]},
  {"category": "Conjunctions and Discourse", "subs": [
    {"subcategory": "Cause, Contrast, Purpose, Result Connectors", "points": [
      "Cause/reason: because, since, as, because of + noun, due to + noun, owing to + noun (formal)",
      "Contrast: although, even though, though, despite + noun/-ing, in spite of + noun/-ing, however, nevertheless, nonetheless",
      "Purpose: to + infinitive, in order to + infinitive, so as to + infinitive, so that + clause (with can/could/will/would)",
      "Result: so, therefore, as a result, consequently, thus, hence (formal)",
      "Addition: moreover, furthermore, in addition, besides, also, as well, not only...but also",
      "Time: while, as, when, as soon as, before, after, until, by the time, once"
    ]},
    {"subcategory": "Informal Discourse Markers", "points": [
      "Conversation management: well, anyway, right, I mean, you know, actually, basically, so, look, listen",
      "Sequencing markers: first of all, to begin with, next, then, after that, finally, last but not least, to sum up",
      "Adding and emphasizing: what's more, on top of that, not only that, in fact, as a matter of fact, indeed"
    ]}
  ]}
]

# LEVEL 4 — High Intermediate (B1+)
am_l4 = [
  {"category": "Narrative Tenses Advanced", "subs": [
    {"subcategory": "All Past Tenses Combined", "points": [
      "Narrative tenses: past simple (main events), past continuous (background/setting), past perfect (earlier past), past perfect continuous (duration before past)",
      "Past perfect continuous: form had been + verb-ing for actions in progress up to a past moment (She had been crying and her eyes were red)",
      "Past perfect continuous vs past perfect simple: focus on duration/process vs completion/result (He had been running vs He had run 10 miles)",
      "Would for typical past behavior and repeated actions (NOT for states: NOT I would be tall)",
      "Used to + base form for past states and habits (I used to live in Paris, I used to smoke)",
      "Would vs used to for past habits: would for actions, used to for both actions and states"
    ]},
    {"subcategory": "Future in the Past", "points": [
      "Was/were going to + base form for intentions in the past that may or may not have happened (I was going to call you but I forgot)",
      "Would + base form as future from a past perspective (He said he would arrive at 6)",
      "Was/were about to + base form for actions that were imminent in the past (I was about to leave when the phone rang)",
      "Was/were to + base form for formal/destiny events in the past (He was to become one of the greatest artists of his generation)",
      "Was/were on the point/verge of + -ing for imminent past actions"
    ]}
  ]},
  {"category": "Future Forms: Complete Range", "subs": [
    {"subcategory": "All Future Expressions", "points": [
      "Future continuous: will be + verb-ing for actions in progress at a future time (This time next week I'll be lying on a beach)",
      "Future continuous for polite inquiries about plans (Will you be using the car this evening?)",
      "Future perfect: will have + past participle for actions completed before a future time (By Friday, I'll have finished the project)",
      "Future perfect continuous: will have been + verb-ing for duration up to a future point (By June, I'll have been working here for 10 years)",
      "Be about to + base form for immediate future (Hurry up! The train is about to leave)",
      "Be due to + base form for scheduled/expected events (The plane is due to arrive at 3:30)",
      "Be bound to + base form for certainty (With that attitude, you're bound to fail)",
      "Be likely to / be unlikely to + base form for probability (It's likely to rain, She's unlikely to agree)",
      "Be set to + base form for planned/expected events (The company is set to announce record profits)",
      "Be on the verge/point of + -ing (She was on the verge of tears, The country is on the point of economic collapse)"
    ]}
  ]},
  {"category": "Modals: Complete Range", "subs": [
    {"subcategory": "Permission, Obligation, Prohibition, Necessity", "points": [
      "Permission: can (informal), could (polite), may (formal), might (very formal/rare), be allowed to (all tenses)",
      "Obligation: must (internal/personal), have to (external/rules), need to (necessity), be supposed to (expectation), be to (formal instruction)",
      "Prohibition: mustn't (strong), can't (rule-based), may not (formal), not be allowed to (general), be forbidden to (very formal)",
      "Lack of obligation: don't have to, needn't (more formal), don't need to",
      "Need as a modal verb (restricted to negatives/questions): Need I say more? / You needn't have worried",
      "Dare as a modal verb (mainly in negatives): I dare not tell him / How dare you!"
    ]},
    {"subcategory": "Speculation and Deduction: Complete", "points": [
      "Must + base form for strong logical deduction about the present (He must be at least 60)",
      "Can't + base form for strong negative deduction (That can't be right)",
      "May/might/could + base form for possibility in the present/future",
      "Must have + past participle for deduction about the past (You must have been exhausted)",
      "Can't have + past participle for past impossibility (He can't have taken it, he wasn't there)",
      "May/might/could have + past participle for past possibility (She might have missed the bus)",
      "Should/ought to have + past participle for unfulfilled expectation or criticism (You should have told me!)",
      "Needn't have + past participle (something was done but was unnecessary) vs didn't need to (whether done or not is ambiguous)",
      "Will for assumptions about the present based on typical behavior (That'll be John at the door — he always comes at this time)",
      "Will have + past participle for assumptions about the past (You'll have heard the news by now)"
    ]},
    {"subcategory": "Verbs of the Senses", "points": [
      "See, hear, feel, smell, taste, notice, watch + object + base form for complete actions perceived (I saw him cross the street)",
      "See, hear, feel, smell, taste, notice, watch + object + -ing form for actions in progress when perceived (I saw him crossing the street)",
      "Look, sound, smell, taste, feel + adjective for describing sensations and impressions (That sounds interesting, This tastes delicious, You look tired)",
      "Look like, sound like, feel like + noun/clause for resemblance and impressions (He looks like his father, It sounds like you had a great time)",
      "As if / as though + clause after sense verbs (It looks as if it's going to rain, You sound as though you have a cold)"
    ]},
    {"subcategory": "Causative: Have/Get Something Done", "points": [
      "Have + object + past participle for arranging for someone to do something (I had my hair cut yesterday)",
      "Get + object + past participle for the same meaning (more informal) (I got my car fixed)",
      "Have + object + past participle for negative experiences (I had my wallet stolen)",
      "Get + object + to-infinitive for persuading someone to do something (I got him to help me)",
      "Have + object + base form for making/ordering someone (I'll have my assistant send you the details)"
    ]}
  ]},
  {"category": "Conditionals: Complete Range", "subs": [
    {"subcategory": "Mixed Conditionals", "points": [
      "Past condition → present result: If + past perfect, would + base form (If I had studied harder at school, I would have a better job now)",
      "Present condition → past result: If + past simple, would have + past participle (If I were more organized, I would have finished on time)",
      "Past condition → future result: If + past perfect, would + base form (If you had taken the course, you would be qualified for the promotion next year)"
    ]},
    {"subcategory": "Alternatives to If", "points": [
      "Unless (= if...not): I won't go unless you come (I won't go if you don't come)",
      "Provided/Providing (that) for conditions that must be met: You can borrow my car provided you fill it up with petrol",
      "As long as for conditions similar to provided that: You can stay as long as you're quiet",
      "On condition that (formal): They agreed on condition that the information remain confidential",
      "Supposing / Suppose / Imagine / What if for hypothetical scenarios",
      "Even if for conditions that don't affect the result: Even if it rains, I'll still go",
      "Whether...or not for alternatives: Whether you like it or not, you have to go",
      "In case for precautionary conditions: Take an umbrella in case it rains",
      "Otherwise / or else implying a negative condition: Hurry up, otherwise we'll miss the train"
    ]},
    {"subcategory": "Inversion in Conditionals", "points": [
      "Should + subject + base form in first conditional: Should you need any help, please call me",
      "Were + subject + to-infinitive in second conditional: Were I to win the lottery, I would travel the world",
      "Were + subject + noun/adjective in second conditional: Were I you, I would accept the offer",
      "Had + subject + past participle in third conditional: Had I known about the party, I would have come"
    ]},
    {"subcategory": "Unreal Past Tenses", "points": [
      "Wish + past simple for present unreal: I wish I had more free time",
      "Wish + past perfect for past regret: I wish I hadn't said that",
      "Wish + would for complaining: I wish you would stop interrupting",
      "If only: stronger/more emphatic than wish for all the above patterns",
      "Would rather/sooner + subject + past simple for preferences about others: I'd rather you didn't smoke here",
      "Would rather/sooner + subject + past perfect for past preference: I'd rather you had told me earlier",
      "It's time / It's high time / It's about time + past simple: It's time we left, It's high time you got a job",
      "As if / as though + past simple/past perfect for unreal comparison: He talks as if he knew everything, She looked as though she had seen a ghost"
    ]}
  ]},
  {"category": "Passive Voice: All Forms", "subs": [
    {"subcategory": "Passive with Reporting Verbs (Distancing)", "points": [
      "It is + reporting verb past participle + that: It is said/believed/thought/expected/reported/known that he is very wealthy",
      "Subject + be + reporting verb past participle + to-infinitive: He is said to be very wealthy",
      "Subject + be + reporting verb past participle + to have + past participle: She is believed to have left the country",
      "Passive of reporting verbs for distancing in formal/academic style: It has been suggested that..., It was agreed that...",
      "Passive with verbs with two objects: I was given a book (indirect object as subject) / A book was given to me (direct object as subject)",
      "Get + past participle as informal passive: He got fired, She got promoted, I got paid yesterday",
      "Need + -ing for passive meaning: The car needs washing (= needs to be washed), The house needs painting",
      "Passive with -ing forms: being + past participle (I hate being told what to do), having been + past participle (Having been warned, I was careful)"
    ]}
  ]},
  {"category": "Gerunds and Infinitives Advanced", "subs": [
    {"subcategory": "Advanced Gerund and Infinitive Forms", "points": [
      "Perfect gerund: having + past participle (Having studied all night, she was exhausted)",
      "Passive gerund: being + past participle (She hates being criticized)",
      "Perfect passive gerund: having been + past participle (He denied having been told about the problem)",
      "Perfect infinitive: to have + past participle (She seems to have forgotten about the meeting)",
      "Passive infinitive: to be + past participle (I expect to be promoted soon)",
      "Perfect passive infinitive: to have been + past participle (He is believed to have been kidnapped)",
      "Continuous infinitive: to be + verb-ing (He appears to be sleeping, She pretended to be reading)",
      "Verb + possessive adjective + gerund: I appreciate your helping me, I resent his being late",
      "Preposition + gerund in fixed expressions: be used to doing, look forward to doing, be accustomed to doing, object to doing, confess to doing"
    ]}
  ]},
  {"category": "Relative Clauses Advanced", "subs": [
    {"subcategory": "All Relative Clause Patterns", "points": [
      "Defining vs non-defining: commas, pronoun omission, use of that",
      "Relative clauses with prepositions: formal (the problem about which we spoke) vs informal (the problem we spoke about)",
      "Whose vs of which for possession (a writer whose books / a book the cover of which)",
      "Quantifier + of whom/which: all of whom, some of which, many of whom, none of which, each of which",
      "Reduced relative clauses with present participle: The man sitting over there vs The man who is sitting over there",
      "Reduced relative clauses with past participle: The house built in 1900 vs The house which was built in 1900",
      "Reduced relative clauses with to-infinitive: The first person to arrive vs The first person who arrived",
      "Whatever, whoever, whichever, wherever, whenever as relative pronouns: Take whatever you want, Whoever did this is a genius"
    ]}
  ]},
  {"category": "Adjective and Adverb Structures Advanced", "subs": [
    {"subcategory": "Advanced Comparative Structures", "points": [
      "Double comparatives with full clauses: The more I study, the more confused I get",
      "Progressive increase: better and better, more and more difficult, less and less interested",
      "Modifying superlatives: by far the best, easily the most important, the second largest, one of the most popular",
      "Compound adjectives: well-known, good-looking, easy-going, time-consuming, thought-provoking, mouth-watering, record-breaking, state-of-the-art"
    ]},
    {"subcategory": "Inversion after Negative Adverbials", "points": [
      "Never + auxiliary + subject + verb: Never have I seen such a beautiful sunset",
      "Rarely/Seldom + auxiliary + subject + verb: Rarely do we get such an opportunity, Seldom has he been so angry",
      "Hardly/Barely/Scarcely...when: Hardly had I sat down when the phone rang",
      "No sooner...than: No sooner had we arrived than it started to rain",
      "Not only...but also: Not only did he lie, but he also stole money",
      "Not until + time expression: Not until I got home did I realize I had lost my keys",
      "Under no circumstances/On no account: Under no circumstances should you open this door",
      "Little + auxiliary + subject + verb: Little did I know what was about to happen",
      "Only + time expression/way: Only then did I understand, Only by working hard can you succeed"
    ]}
  ]},
  {"category": "Clauses and Sentence Structure", "subs": [
    {"subcategory": "Adverbial Clauses: All Types", "points": [
      "Contrast: although, even though, while, whereas, whilst, despite + noun/-ing, in spite of + noun/-ing, much as + clause",
      "Purpose: to + inf, in order to, so as to, so that, for fear that, lest (formal): He spoke quietly lest he be overheard",
      "Reason: because, as, since, seeing that, given that, on the grounds that, in view of the fact that",
      "Result: so/such...that, therefore, consequently, as a result, with the result that"
    ]},
    {"subcategory": "Participle Clauses", "points": [
      "Present participle (-ing) for simultaneous actions: Walking down the street, I noticed a new shop",
      "Present participle (-ing) for reason: Being a doctor, she knew exactly what to do (=Because she was a doctor)",
      "Past participle (-ed/3rd) for passive meaning: Written in a hurry, the report contained many errors (=Because it was written in a hurry)",
      "Perfect participle (having + past participle) for earlier actions: Having finished her homework, she went out to play",
      "Participle clauses after conjunctions: While waiting for the bus, I read a book / After having eaten, they left",
      "Participle clauses for condition: Given more time, I could do better / Used correctly, this tool can save hours",
      "Participle clauses for result: The storm hit the coast, causing widespread damage"
    ]},
    {"subcategory": "Cleft Sentences (Introduction)", "points": [
      "It-cleft: It + be + focused element + that/who + rest of clause (It was John who broke the window)",
      "Wh-cleft (pseudo-cleft): What + clause + be + focused element (What I need is a holiday, What she said was interesting)",
      "All-cleft: All + (that) + clause + be + focused element (All I want is to be happy, All you need is love)"
    ]}
  ]},
  {"category": "Reported Speech: Reporting Verbs", "subs": [
    {"subcategory": "Reporting Verb Patterns", "points": [
      "Verb + that-clause: admit, agree, announce, argue, believe, claim, complain, confess, confirm, declare, deny, doubt, explain, feel, insist, mention, promise, recommend, remark, reply, report, say, state, suggest, think, warn",
      "Verb + (object) + that-clause: assure, convince, inform, notify, persuade, reassure, remind, tell, warn",
      "Verb + to-infinitive: agree, appear, arrange, ask, claim, decide, demand, expect, guarantee, hope, offer, pretend, promise, refuse, swear, threaten, volunteer, vow",
      "Verb + object + to-infinitive: advise, allow, ask, beg, command, encourage, expect, forbid, instruct, invite, order, permit, persuade, recommend, remind, request, tell, urge, warn",
      "Verb + -ing: admit, advise, apologize for, confess to, deny, forbid, propose, recommend, regret, report, suggest",
      "Verb + preposition + -ing: accuse of, apologise for, blame for, boast about/of, complain about/of, congratulate on, insist on, object to, thank for, warn about/against"
    ]}
  ]}
]

# LEVEL 5 — Advanced (B2/C1)
am_l5 = [
  {"category": "Tense Nuances", "subs": [
    {"subcategory": "Present Tenses Advanced", "points": [
      "Present simple for dramatic narrative and historical present to create immediacy",
      "Present simple in newspaper headlines for conciseness (President resigns, Storm hits coast)",
      "Present simple for future in subordinate clauses after time conjunctions (I'll call you when I arrive)",
      "Present continuous with always/constantly/forever for repeated annoying behavior (He's always losing his keys!)",
      "Present continuous for gradual change and developing situations (More people are working from home, The climate is getting warmer)",
      "Stative verbs used dynamically with meaning shift: I'm loving this series, She's being difficult (temporary behavior), I'm seeing someone (dating), We're having dinner (eating)"
    ]},
    {"subcategory": "Past Tenses Advanced", "points": [
      "Past simple for politeness and distancing (I wondered if you could help me, I was hoping you'd come)",
      "Past simple for hypothetical/unreal meaning (It's time we went, If only I knew, I'd rather you stayed)",
      "Past perfect for unreal past after wish/if only (I wish I had known, If only I hadn't said that)"
    ]}
  ]},
  {"category": "Modals: Advanced Nuances", "subs": [
    {"subcategory": "Extended Modal Meanings", "points": [
      "Will for characteristic/habitual behavior: He'll always help if you ask him",
      "Would for typical past behavior: Every summer we would go to the seaside",
      "Will for assumptions based on typical knowledge: That'll be John at the door (it's his usual time)",
      "Should for logical expectation/conclusion: The train should be here by now, They should have arrived yesterday",
      "Should after verbs of suggesting, recommending, insisting: I suggest that he should apply, It is important that you should attend",
      "Shall in formal/legal contexts: The tenant shall pay rent on the first of each month",
      "May for concession in formal style: He may be rich, but he's certainly not happy",
      "Might for reproach or annoyance: You might have told me! You might at least say thank you!",
      "Must for annoying obligation from the speaker's perspective: Must you always interrupt? Do we really must go?",
      "Need as a modal verb (restricted to questions and negatives): Need I say more? You needn't have bothered",
      "Dare as a modal verb (mainly in negatives/questions): I dare not think what might happen, How dare you speak to me like that!"
    ]},
    {"subcategory": "Advanced Past Modal Meanings", "points": [
      "Will have + past participle for assumption about the past: You'll have heard the news by now",
      "Would have + past participle for hypothetical past: I would have helped if I'd known",
      "Should/ought to have + past participle for unfulfilled expectations: The package should have arrived by now",
      "Might/may have + past participle for reproach: You might have warned me!",
      "Could have + past participle for unrealized past ability/opportunity: I could have been a doctor",
      "Needn't have vs didn't need to: You needn't have bought milk (you did buy it, unnecessarily) vs You didn't need to buy milk (whether you bought it or not is ambiguous)"
    ]}
  ]},
  {"category": "Passive Voice: All Advanced Forms", "subs": [
    {"subcategory": "Complete Passive Repertoire", "points": [
      "Passive with reporting verbs: full range — be alleged, assumed, believed, considered, expected, felt, known, reported, rumored, said, supposed, thought, understood + to-infinitive",
      "It + passive reporting verb + that clause: It is alleged that he stole the money",
      "Subject + passive reporting verb + to-infinitive: He is alleged to have stolen the money",
      "Passive of -ing forms: being considered, being built, having been told, having been invited",
      "Passive infinitive forms: to be given, to have been selected, to be being prepared",
      "Get-passive in informal contexts: He got caught, She got promoted, I got paid, The window got broken",
      "Passive for impersonal and formal register in academic, scientific, and business writing",
      "Passive with prepositional verbs: The matter was looked into, The children were taken care of, Such behavior won't be put up with"
    ]}
  ]},
  {"category": "Subjunctive", "subs": [
    {"subcategory": "Present Subjunctive (Mandative)", "points": [
      "Subjunctive after verbs of suggesting, recommending, demanding, insisting: base form for all persons (I suggest that he go, They demanded that she be present, The doctor recommended that I take more exercise)",
      "Subjunctive after adjectives of necessity, importance, urgency: It is essential/crucial/vital/important/necessary that he be informed immediately",
      "Subjunctive in formal resolutions and regulations: The committee recommends that the proposal be adopted",
      "Fixed formulaic subjunctive expressions: God save the Queen, Heaven forbid, So be it, Be that as it may, Come what may, Suffice it to say, Long live the king, God bless you, Far be it from me to criticize"
    ]},
    {"subcategory": "Were-Subjunctive (Past Subjunctive)", "points": [
      "Were-subjunctive in second conditional: If I were you, If she were here",
      "Were-subjunctive after wish: I wish I were taller, I wish it were summer",
      "Were-subjunctive after as if / as though: He acts as if he were the boss, She talks as though she were an expert",
      "Were-subjunctive after suppose/supposing: Suppose she were to find out, what then?",
      "Were-subjunctive after would rather/sooner: I'd rather she were here, I'd sooner you were honest"
    ]}
  ]},
  {"category": "Inversion: Complete Patterns", "subs": [
    {"subcategory": "Inversion after Negative and Restrictive Adverbials", "points": [
      "Never, Rarely, Seldom: Never have I felt so embarrassed, Rarely does one see such dedication",
      "Hardly/Barely/Scarcely...when: Hardly had we arrived when the trouble started",
      "No sooner...than: No sooner had I put the phone down than it rang again",
      "Not only...but also: Not only is she intelligent, but she is also very kind",
      "Not until: Not until I saw him did I remember the appointment",
      "At no time, Under no circumstances, On no account, In no way: Under no circumstances should you lend him money",
      "Little: Little did we suspect what was about to happen",
      "Nowhere: Nowhere else will you find such beautiful beaches",
      "Only + time expression: Only then did I realize my mistake, Only later did she understand, Only when I arrived did I discover the truth",
      "Only + by/through/with: Only by working together can we solve this problem, Only with patience will you succeed"
    ]},
    {"subcategory": "Inversion in Conditionals", "points": [
      "First conditional: Should you need any assistance, please contact reception",
      "Second conditional: Were I to win, I would donate half to charity",
      "Second conditional: Were she more experienced, she would be perfect for the job",
      "Third conditional: Had I known about the traffic, I would have left earlier"
    ]},
    {"subcategory": "Inversion after So/Such and Place Adverbials", "points": [
      "So + adjective/adverb + inversion + that: So exhausted was she that she fell asleep instantly, So quickly did he run that no one could catch him",
      "Such + be + noun + that: Such was the force of the explosion that windows shattered for miles",
      "Here/There + verb + subject: Here comes the bus, There goes our last chance",
      "Prepositional phrase of place + verb + subject: On the top of the hill stood an old castle, Round the corner came a speeding car, In the middle of the room lay a dead body"
    ]}
  ]},
  {"category": "Emphasis and Cleft Structures", "subs": [
    {"subcategory": "Cleft Sentences: Complete Set", "points": [
      "It-cleft: It + be + focused element + that/who (It was the manager who made the decision)",
      "Wh-cleft (pseudo-cleft): What + clause + be + focus (What really annoys me is his arrogance)",
      "Wh-cleft with do: What I did was (to) call the police",
      "All-cleft: All (that) + clause + be + focus (All I want is a peaceful life, All you need to do is ask)",
      "The reason why...is: The reason why I'm late is that I missed the bus",
      "The thing/person/place/time that...is: The thing that bothers me most is his attitude",
      "Cleft with question words: Where the money came from remains a mystery, How he escaped is still unknown"
    ]},
    {"subcategory": "Fronting and Emphatic Structures", "points": [
      "Fronting of object for emphasis: That I cannot accept!, A better solution I have never seen",
      "Fronting of complement: Strange as it may seem, Tired though I was",
      "Fronting of adverbial phrases for dramatic effect: Into the room burst a stranger, Down the hill rolled the boulder",
      "Emphatic do/does/did: I DO believe you, She DOES look tired, He DID try his best",
      "Emphatic own: my very own house, her own personal assistant",
      "Emphasis with reflexive pronouns: The president himself opened the ceremony",
      "Emphasis with very: That's the very thing I wanted, You're the very person I need to speak to"
    ]}
  ]},
  {"category": "Complex Sentences Advanced", "subs": [
    {"subcategory": "Advanced Participle Clauses", "points": [
      "Participle clauses for reason: Being the eldest, she took care of her siblings",
      "Participle clauses for time: Walking through the park, I ran into an old friend",
      "Participle clauses for condition: Treated with care, this shirt will last for years",
      "Participle clauses for result/consequence: The train broke down, causing long delays",
      "Perfect participle (having done/having been done): Having been told about the problem, she took immediate action",
      "Participle clauses with conjunctions: While waiting for the bus, After having eaten, Before leaving, When finished, If in doubt"
    ]},
    {"subcategory": "Advanced Adverbial Clauses", "points": [
      "Concessive: Much as I respect him, I must disagree, However hard I try, I can't seem to get it right",
      "Concessive: Adjective/Adverb + as/though: Tired as I was, I couldn't sleep, Hard though she tried, she couldn't solve it",
      "Concessive: For all + noun: For all his wealth, he wasn't happy, For all my efforts, nothing changed",
      "Concessive: No matter how + adjective: No matter how difficult it gets, don't give up",
      "Concessive: Try as I might: Try as I might, I couldn't remember her name",
      "Specification: In that: I was lucky in that I had some savings to fall back on",
      "Dismissal: Not that: Not that I care, but what did he say?",
      "Manner: As if/though, Like (informal): He treats me as if I were a child"
    ]}
  ]},
  {"category": "Determiners and Pronouns Advanced", "subs": [
    {"subcategory": "Advanced Determiner Patterns", "points": [
      "Quite/rather + a/an + adjective + noun: quite a difficult problem, rather a strange situation",
      "Such + (a/an) + adjective + noun: such a beautiful day, such terrible weather",
      "What + (a/an) + adjective + noun in exclamations: What a lovely surprise! What terrible news!",
      "Position patterns: all the people, both my parents, half the cake, twice the size",
      "Quantity determiners: several, a number of, the majority of, a great deal of, a large amount of"
    ]},
    {"subcategory": "Pronouns Extended", "points": [
      "One/ones for substitution: the red one, the big ones, I need a new phone — the one I have is broken",
      "Impersonal one for general statements: One should always be honest, One never knows",
      "Generic you/we/they for people in general: You never know what might happen, They say it's going to snow",
      "Those who / people who for groups: Those who arrived early got the best seats",
      "Such as a pronoun: Such was the situation when I arrived, More evidence, if such exists, will be presented"
    ]}
  ]},
  {"category": "Cohesion and Avoiding Repetition", "subs": [
    {"subcategory": "Ellipsis", "points": [
      "Ellipsis in coordinate clauses: I like tea and [I like] coffee, She can sing and [she can] dance",
      "Ellipsis in subordinate clauses: When [I am] in doubt, I ask, While [she was] in Paris, she visited the Louvre",
      "Ellipsis after auxiliary verbs: She can swim but I can't [swim], He didn't go but she did [go]",
      "Ellipsis after to: I didn't want to go but I had to [go], She asked me to help but I refused to [help]"
    ]},
    {"subcategory": "Substitution", "points": [
      "Substitution with so: I think so, I hope so, I'm afraid so, I suppose so, So it seems",
      "Substitution with not: I think not, I hope not, I'm afraid not, Apparently not",
      "Substitution with do so/it/that: If you want to leave, do so now, I'll clean the kitchen — I'll do it later",
      "Substitution with one/ones: I like the blue one, These ones are better, The new design is better than the old one",
      "The former/the latter for referencing two items: John and Mary arrived; the former was late, the latter was early"
    ]},
    {"subcategory": "Nominalization (Academic Writing)", "points": [
      "Converting verbs to nouns: investigate→investigation, analyze→analysis, discover→discovery, develop→development, improve→improvement, fail→failure, respond→response, decide→decision, destroy→destruction, reduce→reduction",
      "Converting adjectives to nouns: important→importance, relevant→relevance, able→ability, possible→possibility, complex→complexity, accurate→accuracy, significant→significance",
      "Complex noun phrases with pre- and post-modification for academic density and formality"
    ]}
  ]}
]

# LEVEL 6 — High Advanced (C1+/C2)
am_l6 = [
  {"category": "Advanced Syntactic Manipulation", "subs": [
    {"subcategory": "Advanced Inversion for Rhetorical Effect", "points": [
      "Inversion with so + adjective + as + to-infinitive: So bold was he as to challenge the king himself",
      "Inversion for dramatic emphasis in literary and persuasive writing",
      "Inversion with prepositional phrases of direction/movement for vivid description: Down came the rain, Up went the cheer, Out sprang the tiger",
      "Inversion after not + object for emphatic negation: Not a single word did he utter, Not one penny would they give",
      "Inversion in poetic and highly literary registers"
    ]},
    {"subcategory": "Advanced Cleft and Pseudo-Cleft Patterns", "points": [
      "What + subject + do/does/did + be + (to)-infinitive: What she did was (to) resign immediately, What the report fails to do is address the root cause",
      "It is not that...but that...: It's not that I don't like him, but that I don't trust him",
      "Cleft with question words as subjects: Where the money came from remains unknown, How he achieved it is a mystery",
      "It is not so much...as...: It's not so much that he's lazy as that he's unmotivated"
    ]}
  ]},
  {"category": "Advanced Verb and Noun Patterns", "subs": [
    {"subcategory": "Complex Passives", "points": [
      "It was decided/agreed/arranged/estimated/proposed/suggested/thought that...",
      "There is said/believed/thought/reported to be...",
      "Subject + be + reported/rumored/alleged/said/thought/believed + to have been + past participle",
      "Object + be + past participle + to-infinitive (She was seen to enter the building)",
      "Progressive passive with modal: should be being done, might be being considered",
      "Perfect passive infinitive: to have been done, to have been invited, to have been accepted"
    ]},
    {"subcategory": "Advanced Gerund and Infinitive Patterns", "points": [
      "Passive gerund after verbs and prepositions: He resents being told what to do, She's afraid of being attacked",
      "Perfect passive gerund: He denied having been warned, She admitted to having been influenced",
      "Bare infinitive after but/except: He does nothing but complain, She did everything except help",
      "Bare infinitive after why (not): Why bother? Why not go there yourself?",
      "To-infinitive as formal subject: To err is human, to forgive divine",
      "For + noun + to-infinitive as subject/complement: For him to admit his mistake was surprising, It's unusual for her to be late",
      "To-infinitive expressing unexpected result: He arrived at the station to find that the train had left",
      "Only + to-infinitive for disappointing or ironic result: I rushed to the store only to discover it was closed"
    ]}
  ]},
  {"category": "Subjunctive and Hypothetical (Full Range)", "subs": [
    {"subcategory": "Formal and Literary Subjunctive", "points": [
      "Formulaic subjunctive: Heaven forbid!, So be it, Be that as it may, Suffice it to say, Long live the King, God save the Queen, Far be it from me",
      "Mandative subjunctive in formal contexts: The regulations require that each applicant submit three references, The court ordered that the defendant pay restitution",
      "Subjunctive after lest: He spoke in a whisper lest he be overheard",
      "Subjunctive after for fear that: She hurried for fear that she be late",
      "If it be / whether it be in formal/literary context: If this be treason, make the most of it, Whether it be rain or shine, I'll be there",
      "Were-subjunctive in elevated literary style: Were I but the king for a day, all would change"
    ]},
    {"subcategory": "Hypothetical and Speculative Patterns", "points": [
      "If + were to + infinitive for remote/unlikely conditions: If she were to win the lottery, what would she do?",
      "If + should for tentative/tactful conditions: If you should see John, could you tell him I called?",
      "Were it not for / Had it not been for: Were it not for your help, I would have failed",
      "Supposing/Imagine/What if + past/past perfect for extreme hypotheticals: Supposing you had been there, what would you have done?",
      "As if/though + past perfect for unreal past comparisons: She looked as though she had been crying",
      "Would that + past/past perfect (archaic/literary): Would that I had known the truth sooner!",
      "Even if + past/past perfect for extreme hypothetical: Even if I had known, I couldn't have done anything"
    ]}
  ]},
  {"category": "Stylistic and Rhetorical Grammar", "subs": [
    {"subcategory": "Parallelism, Antithesis, and Chiasmus", "points": [
      "Parallel structure for rhetorical effect: matching grammatical forms in pairs and lists (Government of the people, by the people, for the people)",
      "Antithesis: contrasting two ideas in parallel structure (It was the best of times, it was the worst of times; To err is human, to forgive divine)",
      "Chiasmus: reversed/repeated structure (Ask not what your country can do for you, ask what you can do for your country; Fair is foul and foul is fair)",
      "Tricolon: three parallel elements building to a climax (Veni, vidi, vici; Life, liberty, and the pursuit of happiness)"
    ]},
    {"subcategory": "Litotes, Hyperbole, and Irony", "points": [
      "Litotes (understatement through double negative/negation): not bad (=good), not uncommon (=common), no small achievement (=a big achievement), I wouldn't say no (=I'd like that), He's not exactly poor (=he's very rich)",
      "Hyperbole through grammatical structures and intensifiers",
      "Irony through contrasting grammatical choices and register shifts",
      "Hedging for academic/professional caution: It could be argued that, It might be suggested that, It would appear that, It seems reasonable to assume, To some extent, In some respects",
      "Boosting for persuasive/confident stance: There is no doubt that, It is abundantly clear that, Undeniably, Without question, It is patently obvious"
    ]},
    {"subcategory": "Register: Formal vs Informal Grammar", "points": [
      "Whom vs who: the person to whom I spoke (formal) vs the person I spoke to (neutral/informal)",
      "Shall for first person future/obligation: I shall return (formal), You shall comply (legal)",
      "May vs can: May I be excused? (formal) vs Can I go? (informal)",
      "One should... vs You should... for general advice",
      "Latinate verbs vs phrasal verbs: postpone vs put off, investigate vs look into, tolerate vs put up with, encounter vs come across, extinguish vs put out, demolish vs tear down",
      "Full forms vs contractions in formal writing: cannot vs can't, do not vs don't, will not vs won't",
      "Passive for formal/impersonal register in academic and scientific English",
      "Nominalization for academic density: The implementation of the policy resulted in a reduction of costs (vs They put the policy into action and it cut costs)",
      "Complex prepositions for formal precision: in accordance with, with regard to, in respect of, pursuant to, in compliance with"
    ]}
  ]},
  {"category": "Advanced Conditional and Concessive Patterns", "subs": [
    {"subcategory": "Conditional Refinements", "points": [
      "Given + noun phrase as implicit condition: Given the circumstances, we had no choice but to proceed",
      "Assuming (that) as conditional: Assuming he agrees, we'll sign the contract tomorrow",
      "Provided/Providing (that) vs As long as vs On condition that: nuanced distinctions in formality and strength of condition",
      "In the event that / In case of for precautionary conditions",
      "With/Without + noun/noun phrase for conditional meaning: With luck, we'll finish today; Without your help, I wouldn't have succeeded",
      "Adjective/participle + as + subject + verb: Tired as he was, he carried on working; Exhausted as they were, they refused to give up"
    ]},
    {"subcategory": "Concessive Patterns (Full Range)", "points": [
      "Adjective/Adverb + as/though: Rich as he is, he lives modestly; Hard as I tried, I couldn't solve it",
      "Much as: Much as I admire her work, I find her personality difficult",
      "For all + noun phrase: For all his wealth and fame, he died alone",
      "Whatever/However/Wherever/Whoever + may: Whatever the cost may be, we must proceed",
      "While/Whereas/Whilst for contrast in formal writing: While some argue for change, others advocate stability",
      "Albeit for formal/factual concession: He finally accepted the offer, albeit reluctantly; It was an interesting, albeit flawed, argument",
      "No matter + wh-word as universal concessive: No matter what happens, I'll support you"
    ]}
  ]},
  {"category": "Advanced Negation", "subs": [
    {"subcategory": "Complex Negation Patterns", "points": [
      "Transferred negation: I don't think he'll come (rather than: I think he won't come)",
      "Negative scope ambiguity: I didn't go because I was tired (ambiguous: didn't go + reason vs went + not because tired)",
      "Partial negation with not + all/every/always: Not all that glitters is gold, Not every idea is a good one, I don't always agree with him",
      "Double negation for positive emphasis: I can't not go = I feel compelled to go, It's not uncommon = It's fairly common",
      "Not...but rather... for contrastive focus: The problem is not a lack of talent but rather a lack of opportunity",
      "Nuanced negation of modals: mustn't (prohibition), needn't (lack of necessity), can't (impossibility), won't (refusal), shan't (formal refusal)"
    ]}
  ]},
  {"category": "Complex Prepositional Phrases", "subs": [
    {"subcategory": "Full Inventory of Multi-Word Prepositions", "points": [
      "In: in accordance with, in addition to, in case of, in charge of, in comparison with/to, in compliance with, in connection with, in contrast to/with, in favor of, in front of, in lieu of, in line with, in place of, in regard to, in relation to, in respect of/to, in search of, in spite of, in terms of, in the event of, in the light of, in view of",
      "On: on account of, on behalf of, on the basis of, on the grounds of, on the part of, on the point of",
      "With: with regard to, with respect to, with the exception of, with a view to",
      "By: by means of, by virtue of, by way of, by dint of",
      "As: as a result of, as far as, as for, as opposed to, as regards, as to, as well as",
      "Other: apart from, aside from, away from, due to, owing to, thanks to, prior to, subsequent to, regardless of, irrespective of, contrary to, according to, along with, together with, as per"
    ]}
  ]},
  {"category": "Advanced Cohesion and Information Structure", "subs": [
    {"subcategory": "Theme/Rheme and Given/New", "points": [
      "Theme (topic) and rheme (comment) patterns for controlling information flow in paragraphs",
      "Given-before-new principle: placing familiar/known information before new information",
      "End-focus principle: placing the most important/new information at the end of the clause",
      "Cataphoric reference: forward reference with pronouns (This is what I mean: ...; Here's the thing: ...)",
      "Anaphoric reference: backward reference to previously mentioned items",
      "Lexical cohesion through synonymy, hyponymy, meronymy, and collocation chains",
      "Parallel structure across paragraphs for coherence and rhetorical impact",
      "Advanced discourse markers: Be that as it may, That said, Having said that, All the same, Even so, Mind you, In a nutshell, To put it bluntly, Insofar as, To the extent that, For all intents and purposes, To all appearances, By and large, On the whole, As a rule, For the most part"
    ]}
  ]}
]

# Assemble American system
am_system = {
    "name": "American ESL System (6-Level University IEP Model)",
    "description": "Sistema americano estándar de 6 niveles usado en Intensive English Programs universitarios. Basado en Troy University, University of Delaware, American Language Center, Azar-Hagen Grammar Series y Pearson GSE.",
    "source_mapping": {
        "Level 1 - Beginner": "Beginner (~A1 CEFR)",
        "Level 2 - High Beginner": "High Beginner (~A2- CEFR)",
        "Level 3 - Intermediate": "Intermediate (~A2+/B1 CEFR)",
        "Level 4 - High Intermediate": "High Intermediate (~B1+ CEFR)",
        "Level 5 - Advanced": "Advanced (~B2 CEFR)",
        "Level 6 - High Advanced": "High Advanced (~C1/C2 CEFR)"
    },
    "levels": {
        "Level 1 - Beginner": {"name": "Level 1", "description": "Basic English grammar for simple sentences about daily life. First contact with the language.", "categories": am_l1},
        "Level 2 - High Beginner": {"name": "Level 2", "description": "Expanded grammar for everyday communication. More verb tenses and sentence structures.", "categories": am_l2},
        "Level 3 - Intermediate": {"name": "Level 3", "description": "Expanding grammar for broader range of situations. Combining tenses and structures.", "categories": am_l3},
        "Level 4 - High Intermediate": {"name": "Level 4", "description": "Complex grammar for varied topics and expressing viewpoints. Academic English foundations.", "categories": am_l4},
        "Level 5 - Advanced": {"name": "Level 5", "description": "Mastery of complex structures. Academic and professional English. Near-native fluency.", "categories": am_l5},
        "Level 6 - High Advanced": {"name": "Level 6", "description": "Refinement of all structures. Stylistic mastery, rhetorical sophistication, nuanced expression.", "categories": am_l6}
    }
}

# Replace American system in DB
db["systems"]["American"] = am_system

# Save updated DB
with open("/root/english_grammar_database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# Count
cefr_total = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["CEFR"]["levels"].values())
am_total = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in db["systems"]["American"]["levels"].values())

print(f"CEFR: {cefr_total} grammar points")
print(f"American: {am_total} grammar points")
print(f"Grand total: {cefr_total + am_total}")

for lvl_name, lvl_data in db["systems"]["American"]["levels"].items():
    count = sum(len(s["points"]) for c in lvl_data["categories"] for s in c["subs"])
    cats = len(lvl_data["categories"])
    print(f"  {lvl_name}: {count} points in {cats} categories")
