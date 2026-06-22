#!/usr/bin/env python3
"""Build comprehensive English Grammar Database - CEFR + American systems"""

import json

db = {"meta": {"title": "English Grammar Database - Complete Hierarchical Curriculum", "version": "1.0", "systems": ["CEFR", "American"]}, "systems": {}}

# ============ CEFR A1 ============
a1_cats = [
  {"category": "Present Tenses", "subs": [
    {"subcategory": "Verb 'to be'", "points": [
      "Present simple of 'to be': affirmative (am, is, are)",
      "Present simple of 'to be': negative (am not, isn't, aren't)",
      "Present simple of 'to be': questions (Am I?, Is he?, Are they?)",
      "Present simple of 'to be': short answers (Yes, I am. / No, she isn't.)"
    ]},
    {"subcategory": "Present Simple", "points": [
      "Present simple: affirmative with I/you/we/they (I work, You play)",
      "Present simple: affirmative with he/she/it + -s (He works, She plays)",
      "Present simple: negative with don't/doesn't (I don't work, She doesn't play)",
      "Present simple: questions with Do/Does (Do you work?, Does she play?)",
      "Present simple: short answers (Yes, I do. / No, she doesn't.)",
      "Present simple for habits and routines (I wake up at 7 every day)",
      "Present simple for general facts (The sun rises in the east)",
      "Present simple with adverbs of frequency (always, usually, often, sometimes, never)",
      "Position of adverbs of frequency (before main verb, after 'to be')"
    ]},
    {"subcategory": "Present Continuous", "points": [
      "Present continuous: affirmative (I'm working, She's playing)",
      "Present continuous: negative (I'm not working, She isn't playing)",
      "Present continuous: questions (Are you working?, Is she playing?)",
      "Present continuous for actions happening now",
      "Present simple vs present continuous: basic contrast"
    ]},
    {"subcategory": "Have got", "points": [
      "Have got: affirmative (I've got, She's got)",
      "Have got: negative (I haven't got, She hasn't got)",
      "Have got: questions (Have you got?, Has she got?)",
      "Have got vs have: basic usage for possession"
    ]}
  ]},
  {"category": "Past Tenses", "subs": [
    {"subcategory": "Past Simple of 'to be'", "points": [
      "Was/were: affirmative (I was, You were, They were)",
      "Was/were: negative (I wasn't, You weren't)",
      "Was/were: questions (Was I?, Were you?)"
    ]},
    {"subcategory": "Past Simple", "points": [
      "Past simple: regular verbs + -ed (I worked, She played)",
      "Past simple: spelling rules for -ed (stop→stopped, carry→carried)",
      "Past simple: pronunciation of -ed (/t/, /d/, /ɪd/)",
      "Past simple: common irregular verbs (went, had, did, saw, ate, came, got, made, took, gave, said, thought, knew)",
      "Past simple: negative with didn't (I didn't go)",
      "Past simple: questions with Did (Did you go?)"
    ]}
  ]},
  {"category": "Future Forms", "subs": [
    {"subcategory": "Will", "points": [
      "Will for future: affirmative (I will help), negative (I won't go)",
      "Will for sudden/spontaneous decisions (I'll answer the phone)",
      "Will for offers and promises (I'll carry that for you)",
      "Will for requests (Will you open the window?)"
    ]},
    {"subcategory": "Be going to", "points": [
      "Be going to: affirmative, negative, questions",
      "Be going to for plans and intentions",
      "Be going to for predictions based on evidence (Look at those clouds, it's going to rain)"
    ]},
    {"subcategory": "Shall", "points": [
      "Shall for suggestions with I/we (Shall I open the window?)",
      "Shall for offers (Shall I help you?)"
    ]}
  ]},
  {"category": "Modals and Imperatives", "subs": [
    {"subcategory": "Can / Can't", "points": [
      "Can for ability (I can swim), permission (Can I go?), possibility, requests (Can you help me?)",
      "Can't for lack of ability (I can't drive)"
    ]},
    {"subcategory": "Would like", "points": [
      "Would like for offers/invitations (Would you like a drink?)",
      "I'd like for wishes/desires (I'd like a coffee)"
    ]},
    {"subcategory": "Imperatives", "points": [
      "Imperative: affirmative (Sit down!, Stand up!)",
      "Imperative: negative with Don't (Don't talk!, Don't worry!)",
      "Imperative with 'please' for politeness"
    ]}
  ]},
  {"category": "Articles, Nouns, and Determiners", "subs": [
    {"subcategory": "Articles", "points": [
      "Indefinite article a/an: basic rules (a book, an apple)",
      "Definite article the: basic usage for specific reference",
      "Zero article: no article for general plural/uncountable (I like music)"
    ]},
    {"subcategory": "Nouns", "points": [
      "Singular and plural nouns: regular -s/-es (book→books, box→boxes)",
      "Common irregular plurals (man→men, child→children, person→people, woman→women)",
      "Countable vs uncountable nouns: basic distinction (apple/apples vs water)"
    ]},
    {"subcategory": "Quantifiers", "points": [
      "Some/any: basic use with countable/uncountable nouns",
      "Much/many: basic distinction (much water, many books)",
      "A lot of for large quantities",
      "A little/a few: basic distinction (a little water, a few apples)",
      "How much? / How many?: questions"
    ]},
    {"subcategory": "Pronouns", "points": [
      "Subject pronouns (I, you, he, she, it, we, they)",
      "Object pronouns (me, you, him, her, it, us, them)",
      "Subject vs object pronouns: basic distinction (I vs me)",
      "Possessive adjectives (my, your, his, her, its, our, their)",
      "Demonstrative pronouns: this/that/these/those",
      "Indefinite pronouns: something/anything (basic)"
    ]},
    {"subcategory": "Possessives", "points": [
      "Possessive 's for people (John's book, my sister's car)",
      "Possessive s' for plural (my parents' house)",
      "Whose for questions about possession"
    ]}
  ]},
  {"category": "There is/are and It", "subs": [
    {"subcategory": "There is / There are", "points": [
      "There is + singular (There is a book on the table)",
      "There are + plural (There are two chairs)",
      "There isn't / There aren't: negative forms",
      "Is there? / Are there?: questions",
      "There was / There were: past forms"
    ]},
    {"subcategory": "It vs There", "points": [
      "It as dummy subject (It's cold today, It's 3 o'clock)",
      "There vs It: basic distinction",
      "This vs It: basic distinction"
    ]}
  ]},
  {"category": "Adjectives and Adverbs", "subs": [
    {"subcategory": "Adjectives", "points": [
      "Basic descriptive adjectives (big, small, good, bad, new, old, young)",
      "Adjective position: before nouns (a red car) and after 'to be' (The car is red)",
      "Adjectives: no plural form in English"
    ]},
    {"subcategory": "Adverbs", "points": [
      "Adverbs of manner: adjective + -ly (slow→slowly, quick→quickly)",
      "Adjective vs adverb: basic distinction (good vs well, quick vs quickly)",
      "Irregular adverbs (good→well, fast→fast, hard→hard)"
    ]},
    {"subcategory": "Comparatives and Superlatives", "points": [
      "Comparative adjectives: + -er (older, bigger, cheaper)",
      "Comparative adjectives: more + adjective (more expensive, more interesting)",
      "Superlative adjectives: the + -est (the oldest, the biggest)",
      "Superlative adjectives: the most + adjective (the most expensive)",
      "Irregular comparatives and superlatives: good→better→best, bad→worse→worst",
      "Comparative with than (She is taller than me)"
    ]}
  ]},
  {"category": "Prepositions", "subs": [
    {"subcategory": "Prepositions of Time", "points": [
      "At for clock times, meals, festivals (at 3 o'clock, at lunch, at Christmas)",
      "On for days and dates (on Monday, on 5th May)",
      "In for months, years, seasons, parts of day (in June, in 2024, in the morning)"
    ]},
    {"subcategory": "Prepositions of Place", "points": [
      "At for specific points/locations (at the door, at school, at home)",
      "On for surfaces (on the table, on the wall)",
      "In for enclosed spaces (in the room, in the box)",
      "Next to, under, between, in front of, behind, over, among"
    ]},
    {"subcategory": "Other Common Prepositions", "points": [
      "By for means of transport (by car, by bus)",
      "Of for possession/relationship",
      "With for accompaniment (with my friend)",
      "For for purpose/duration (for you, for two hours)"
    ]}
  ]},
  {"category": "Questions", "subs": [
    {"subcategory": "Yes/No Questions", "points": [
      "Yes/No questions with 'to be' (Are you tired?)",
      "Yes/No questions with 'have got'",
      "Yes/No questions with present simple: Do/Does",
      "Yes/No questions with past simple: Did"
    ]},
    {"subcategory": "Wh- Questions", "points": [
      "What: for things/actions; Where: for places; When: for time",
      "Who: for people (subject and object); Why: for reasons + Because",
      "How: for manner/means; How much/How many for quantity",
      "How old for age; Whose for possession; Which for choice; What time for clock time"
    ]}
  ]},
  {"category": "Conjunctions and Word Order", "subs": [
    {"subcategory": "Conjunctions", "points": [
      "And for addition; But for contrast; Or for alternatives",
      "So for result (I was tired so I went to bed)",
      "Because for reason (I stayed home because it rained)"
    ]},
    {"subcategory": "Word Order", "points": [
      "Basic word order: Subject + Verb + Object (SVO)",
      "Word order with adverbs of frequency",
      "Word order with adjectives (a big red car)",
      "Word order in questions: auxiliary + subject + verb"
    ]}
  ]},
  {"category": "Gerunds and Infinitives", "subs": [
    {"subcategory": "Verb Patterns", "points": [
      "Verb + -ing after like/love/hate/enjoy (I like reading)",
      "Verb + to-infinitive after want/need/decide (I want to go)",
      "Would like + to-infinitive (I'd like to see)",
      "Stative verbs (know, like, love, hate, want, need, seem, belong)"
    ]}
  ]}
]

# Build CEFR structure
cefr = {"name": "CEFR (Marco Común Europeo)", "description": "Sistema europeo de 6 niveles: A1 a C2. Council of Europe.", "levels": {}}

cefr["levels"]["A1 - Beginner"] = {"name": "A1", "description": "Usuario básico: expresiones cotidianas y frases básicas.", "categories": a1_cats}

# A2
a2_cats = [
  {"category": "Present Tenses", "subs": [
    {"subcategory": "Present Simple vs Continuous", "points": [
      "Present simple vs present continuous: extended contrast (routines vs now)",
      "Stative verbs not used in continuous (know, like, want, believe, have=possess)",
      "Present simple for timetabled future (The train leaves at 6)"
    ]},
    {"subcategory": "Present Perfect", "points": [
      "Present perfect: form have/has + past participle",
      "Present perfect for life experiences (I've been to Paris) with ever/never",
      "Present perfect with just, already, yet",
      "Present perfect with for and since (duration vs starting point)",
      "Present perfect vs past simple: basic distinction (experience vs specific time)"
    ]}
  ]},
  {"category": "Past Tenses", "subs": [
    {"subcategory": "Past Simple Extended", "points": [
      "Past simple: form and use - completed actions at specific past time",
      "Past simple with time expressions (yesterday, last week, ago, in 2010)",
      "Past simple for sequences of past actions"
    ]},
    {"subcategory": "Past Continuous", "points": [
      "Past continuous: was/were + verb-ing",
      "Past continuous for actions in progress at specific past time",
      "Past continuous and past simple together for interrupted actions (I was watching TV when the phone rang)",
      "Past continuous for background descriptions in narratives"
    ]},
    {"subcategory": "Past Perfect", "points": [
      "Past perfect: had + past participle",
      "Past perfect for actions before another past action",
      "Past perfect with already, just, never"
    ]},
    {"subcategory": "Used to", "points": [
      "Used to for past habits (I used to play tennis)",
      "Used to for past states no longer true (I used to live in London)",
      "Didn't use to: negative; Did you use to?: questions"
    ]}
  ]},
  {"category": "Future Forms", "subs": [
    {"subcategory": "Will vs Going to", "points": [
      "Will for predictions without evidence (I think it will rain)",
      "Going to for plans and intentions; predictions with evidence",
      "Will for spontaneous decisions vs going to for pre-planned intentions",
      "Present continuous for future arrangements (I'm meeting her tomorrow)",
      "Present simple for timetabled future (The flight leaves at 8)"
    ]}
  ]},
  {"category": "Modals", "subs": [
    {"subcategory": "Have to / Must", "points": [
      "Have to for external obligation; Don't have to for lack of obligation",
      "Must for internal obligation/rules; Mustn't for prohibition",
      "Must vs have to: basic distinction"
    ]},
    {"subcategory": "Should", "points": [
      "Should for advice (You should see a doctor)",
      "Shouldn't for negative advice; Should for expectation (He should be here by now)"
    ]},
    {"subcategory": "Might / May", "points": [
      "Might for possibility; May for possibility; May for formal permission",
      "May vs might: differences in probability"
    ]},
    {"subcategory": "Other Modals", "points": [
      "Could for past ability; Could for polite requests (Could you help me?)",
      "Can/can't: extended uses; Need to / needn't for necessity; Shall for suggestions"
    ]}
  ]},
  {"category": "Conditionals", "subs": [
    {"subcategory": "Zero Conditional", "points": [
      "Zero conditional: If + present simple, present simple (If you heat ice, it melts)",
      "Zero conditional for general truths and scientific facts; If vs When"
    ]},
    {"subcategory": "First Conditional", "points": [
      "First conditional: If + present simple, will + infinitive (If it rains, I'll stay home)",
      "First conditional with unless (I won't go unless you come)",
      "First conditional with modal verbs and imperatives"
    ]},
    {"subcategory": "Second Conditional", "points": [
      "Second conditional: If + past simple, would + infinitive (If I had money, I'd travel)",
      "Second conditional for unreal/hypothetical present/future",
      "If I were...; Wish + past simple for present wishes (I wish I was taller)"
    ]}
  ]},
  {"category": "Passive Voice", "subs": [
    {"subcategory": "Present and Past Simple Passive", "points": [
      "Passive voice: form be + past participle",
      "Present simple passive (English is spoken here)",
      "Past simple passive (The house was built in 1900)",
      "Active vs passive: basic distinction and use"
    ]}
  ]},
  {"category": "Reported Speech", "subs": [
    {"subcategory": "Indirect Speech - Basic", "points": [
      "Reported speech: say and tell",
      "Tense backshift: present→past, will→would",
      "Reported statements and questions: word order change",
      "Pronoun and time/place expression changes (now→then, today→that day, here→there)"
    ]}
  ]},
  {"category": "Articles and Quantifiers Extended", "subs": [
    {"subcategory": "Articles", "points": [
      "Articles with countable and uncountable nouns",
      "A/an for first mention; the for second/unique reference; no article for general"
    ]},
    {"subcategory": "Quantifiers", "points": [
      "Much, many, little, few, some, any: extended use",
      "Too, too much, too many, enough; Enough + noun / adjective + enough"
    ]},
    {"subcategory": "Pronouns Extended", "points": [
      "Subject, object, possessive pronouns and adjectives: complete review",
      "Something, anything, nothing, everything; -body, -where variants",
      "Most, most of, the most"
    ]}
  ]},
  {"category": "Relative Clauses", "subs": [
    {"subcategory": "Defining Relative Clauses", "points": [
      "Who for people; Which for things; That for both (informal)",
      "Where for places; When for time",
      "Omitting the relative pronoun when it's the object"
    ]}
  ]},
  {"category": "Gerunds and Infinitives", "subs": [
    {"subcategory": "Verb Patterns Extended", "points": [
      "Verb + -ing (enjoy, finish, mind, suggest, recommend, keep, avoid)",
      "Verb + to-infinitive (want, decide, hope, expect, offer, promise, refuse, learn, plan, agree)",
      "Verb + -ing OR to-infinitive same meaning (start, begin, continue)",
      "Verb + -ing OR to-infinitive different meaning (remember, forget, try, stop)",
      "Preposition + -ing (good at, interested in, tired of)",
      "Expressing purpose with 'to' and 'for'"
    ]}
  ]},
  {"category": "Adjectives and Adverbs Extended", "subs": [
    {"subcategory": "Comparatives and Superlatives", "points": [
      "Comparative and superlative adjectives and adverbs: full review",
      "As...as for equality; Not as...as for inequality",
      "No longer / any longer / anymore"
    ]},
    {"subcategory": "Adverbs", "points": [
      "Adverbs of manner: regular and irregular forms",
      "Adverbial phrases of time, place and frequency - word order"
    ]}
  ]},
  {"category": "Phrasal Verbs and Verb Patterns", "subs": [
    {"subcategory": "Phrasal Verbs", "points": [
      "Common phrasal verbs: get up, wake up, turn on/off, put on, take off, pick up",
      "Transitive/intransitive; separable/inseparable phrasal verbs",
      "Verb + preposition combinations (look at, listen to, wait for)"
    ]},
    {"subcategory": "Special Verbs", "points": [
      "Make vs do: basic distinctions",
      "Go + -ing for activities (go swimming, go shopping)",
      "Get: basic uses (get up, get home, get a job, get tired)",
      "Verbs with two objects (give me the book / give the book to me)"
    ]}
  ]},
  {"category": "Auxiliary Verbs and Question Forms", "subs": [
    {"subcategory": "Auxiliary Verbs", "points": [
      "Auxiliary verbs: do, be, have",
      "So do I / Neither do I for agreement/disagreement",
      "Short answers with auxiliaries"
    ]},
    {"subcategory": "Question Tags", "points": [
      "Question tags: basic positive-negative pattern (You're tired, aren't you?)",
      "Question tags with auxiliary verbs"
    ]}
  ]},
  {"category": "Connectors", "subs": [
    {"subcategory": "Time and Logic Connectors", "points": [
      "When, while, before, after, until for time sequences",
      "First, then, next, after that, finally for sequencing",
      "However, although, because, so for logic"
    ]}
  ]}
]

cefr["levels"]["A2 - Elementary"] = {"name": "A2", "description": "Usuario básico: frases frecuentes sobre áreas de relevancia inmediata.", "categories": a2_cats}

# B1
b1_cats = [
  {"category": "Present Tenses", "subs": [
    {"subcategory": "Present Perfect Simple vs Continuous", "points": [
      "Present perfect simple for completed actions with present relevance",
      "Present perfect continuous: have/has been + -ing for ongoing/recently stopped actions",
      "Present perfect simple vs continuous: duration vs result focus",
      "Present perfect simple vs past simple: nuanced distinction"
    ]},
    {"subcategory": "Present Simple vs Continuous Extended", "points": [
      "Present simple for commentary/narration",
      "Present continuous with always for complaints (He's always complaining!)",
      "Stative vs dynamic verbs: extended list"
    ]}
  ]},
  {"category": "Past Tenses", "subs": [
    {"subcategory": "Narrative Tenses", "points": [
      "Past simple, past continuous, past perfect: combined use in narratives",
      "Past perfect for sequencing events (When I arrived, they had already left)",
      "Past perfect continuous: had been + -ing for duration before another past event"
    ]},
    {"subcategory": "Used to / Would / Be used to / Get used to", "points": [
      "Used to for past habits and states",
      "Would for repeated past actions (NOT for past states)",
      "Be used to + noun/-ing for familiar situations",
      "Get used to + noun/-ing for becoming accustomed"
    ]}
  ]},
  {"category": "Future Forms", "subs": [
    {"subcategory": "All Future Forms", "points": [
      "Will, going to, present continuous for future: full comparison",
      "Future continuous: will be + -ing for actions in progress at future time",
      "Future perfect: will have + past participle for completion before a future point",
      "Present simple for timetabled future: extended use"
    ]}
  ]},
  {"category": "Modals", "subs": [
    {"subcategory": "Obligation, Prohibition, Advice", "points": [
      "Must vs have to: internal vs external obligation",
      "Mustn't vs don't have to: prohibition vs lack of obligation",
      "Should / ought to for advice; Had better for strong advice/warning",
      "Should have / shouldn't have for past advice/regret"
    ]},
    {"subcategory": "Ability and Possibility", "points": [
      "Can, could, be able to: full paradigm across tenses",
      "Was/were able to vs could for single past achievements",
      "Will be able to for future ability; Manage to + infinitive"
    ]},
    {"subcategory": "Deduction and Speculation", "points": [
      "Must for logical deduction; Can't for impossibility",
      "Might/may/could for present possibility/speculation",
      "Must have, might/may/could have, can't have for past deduction"
    ]},
    {"subcategory": "Preferences", "points": [
      "Would rather + infinitive (I'd rather stay home)",
      "Would rather + subject + past simple (I'd rather you didn't go)",
      "Would sooner; It's time + past simple (It's time we left)"
    ]}
  ]},
  {"category": "Conditionals", "subs": [
    {"subcategory": "First and Second", "points": [
      "First conditional with unless, as long as, provided that",
      "Second conditional for hypothetical present/future",
      "First vs second: real vs unreal comparison"
    ]},
    {"subcategory": "Third Conditional", "points": [
      "Third conditional: If + past perfect, would have + past participle for past regrets",
      "Third conditional with could have / might have",
      "Wish + past perfect for past regrets (I wish I had studied harder)"
    ]},
    {"subcategory": "Wish and If only", "points": [
      "Wish + past simple for present wishes",
      "Wish + past perfect for past regrets",
      "Wish + would for complaints about behavior; If only: stronger form"
    ]}
  ]},
  {"category": "Passive Voice", "subs": [
    {"subcategory": "Passive Forms Extended", "points": [
      "Passive voice: all basic tenses (present, past, present perfect, future)",
      "Passive with modal verbs (can be done, must be finished)",
      "Active vs passive: when to use each; Passive with agent by",
      "Passive in formal and academic contexts"
    ]}
  ]},
  {"category": "Reported Speech", "subs": [
    {"subcategory": "Reported Speech Extended", "points": [
      "Reported statements: full tense backshift rules",
      "Reported questions: Yes/No and Wh-",
      "Reported commands and requests (He told me to sit down)",
      "Reporting verbs: say, tell, ask, advise, suggest, recommend, warn, invite, promise, refuse",
      "Reporting verb patterns (suggest + -ing, advise + object + to-infinitive)",
      "Modal changes in reported speech (can→could, will→would, may→might, must→had to)"
    ]}
  ]},
  {"category": "Articles, Nouns, and Determiners", "subs": [
    {"subcategory": "Articles Extended", "points": [
      "A/an, the, zero article: comprehensive rules",
      "Articles with geographical names (the UK, Mount Everest, the Atlantic)",
      "Articles with institutions (school, hospital, prison: with/without the)",
      "Articles with musical instruments (play the piano) vs sports (play tennis)"
    ]},
    {"subcategory": "Quantifiers Extended", "points": [
      "Much, many, a lot of, lots of, plenty of",
      "Little, a little, few, a few: distinction",
      "All, both, half; Both...and, either...or, neither...nor",
      "Any, no, none; Another, other, others, the other, the others"
    ]},
    {"subcategory": "Reflexive Pronouns", "points": [
      "Reflexive pronouns: myself, yourself, himself, herself, itself, ourselves, yourselves, themselves",
      "Reflexive for same-subject actions (I cut myself); By + reflexive for alone",
      "Emphatic use (I did it myself)"
    ]}
  ]},
  {"category": "Relative Clauses", "subs": [
    {"subcategory": "Defining and Non-Defining", "points": [
      "Defining relative clauses: essential info (no commas)",
      "Non-defining relative clauses: extra info (with commas)",
      "Who, which, that, whose, where, when, why",
      "Prepositions in relative clauses; What as relative pronoun"
    ]}
  ]},
  {"category": "Gerunds and Infinitives Extended", "subs": [
    {"subcategory": "Verb Patterns", "points": [
      "Verb + -ing (admit, avoid, consider, deny, enjoy, finish, imagine, mind, miss, practise, risk, suggest)",
      "Verb + to-infinitive (afford, agree, appear, arrange, decide, expect, hope, learn, manage, offer, plan, promise, refuse, seem, tend, threaten, want)",
      "Verb + object + to-infinitive (advise, ask, encourage, expect, invite, order, persuade, recommend, remind, teach, tell, warn)",
      "Verb + object + infinitive without to (let, make, help)",
      "Verb + -ing or to-infinitive with different meaning (remember, forget, regret, try, stop, mean, go on)",
      "Adjective + to-infinitive; Too + adjective + to-infinitive; Adj + enough + to-infinitive"
    ]}
  ]},
  {"category": "Adjectives and Adverbs", "subs": [
    {"subcategory": "Adjective Patterns", "points": [
      "-ed/-ing adjectives (bored/boring, interested/interesting, excited/exciting)",
      "Modifying comparatives: much/a lot/far/a bit/slightly + comparative",
      "The...the... for parallel comparison; So/such: so + adj, such + noun phrase",
      "Compound adjectives with numbers (a two-hour journey, a five-star hotel)"
    ]},
    {"subcategory": "Adverbs Extended", "points": [
      "Adverbs of degree: quite, rather, pretty, fairly",
      "Adverbs of certainty: definitely, probably, certainly, perhaps, maybe",
      "Adverb position: front, mid, end position rules"
    ]}
  ]},
  {"category": "Phrasal Verbs Extended", "subs": [
    {"subcategory": "Extended Set", "points": [
      "give up, look after, look forward to, run out of, get on with, carry on, find out, turn up, set up, take up, make up, put off, come up with",
      "Three-part phrasal verbs (look forward to, get on with, put up with)",
      "Phrasal verbs with multiple meanings; Separable vs inseparable: detailed rules"
    ]}
  ]},
  {"category": "Question Tags and Agreement", "subs": [
    {"subcategory": "Question Tags", "points": [
      "Question tags with all auxiliary verbs (isn't it?, don't you?, haven't you?, can't you?)",
      "Positive-negative and negative-positive patterns",
      "Tags with 'let's' (Let's go, shall we?); Tags with imperatives; Intonation patterns"
    ]},
    {"subcategory": "Agreement/Disagreement", "points": [
      "So + auxiliary + subject (So do I, So am I)",
      "Neither/Nor + auxiliary + subject (Neither do I)",
      "Short responses (I hope so, I think so, I'm afraid so, I hope not)"
    ]}
  ]},
  {"category": "Conjunctions and Discourse", "subs": [
    {"subcategory": "Connectors", "points": [
      "Cause/effect: because, since, as, because of, due to, owing to",
      "Contrast: although, even though, though, despite, in spite of, however, nevertheless",
      "Addition: moreover, furthermore, in addition, besides, also, as well as",
      "Purpose: to, in order to, so as to, so that",
      "Result: so, therefore, as a result, consequently",
      "Time: while, as, when, as soon as, before, after, until, by the time"
    ]},
    {"subcategory": "Discourse Markers", "points": [
      "Informal: well, anyway, right, I mean, you know, actually, basically",
      "Sequencing: first of all, to begin with, next, then, after that, finally",
      "Adding: what's more, on top of that, not only that, in fact"
    ]}
  ]}
]

cefr["levels"]["B1 - Intermediate"] = {"name": "B1", "description": "Usuario independiente: comprende puntos principales sobre temas familiares.", "categories": b1_cats}

# B2
b2_cats = [
  {"category": "Narrative Tenses", "subs": [
    {"subcategory": "Advanced Narrative", "points": [
      "Narrative tenses combined: past simple, past continuous, past perfect, past perfect continuous",
      "Would and used to for past habits (distinction: would NOT for past states)",
      "Past perfect continuous vs past perfect simple (duration vs completion)",
      "Future in the past: was going to, would, was about to, was to"
    ]}
  ]},
  {"category": "Future Forms Advanced", "subs": [
    {"subcategory": "All Future Expressions", "points": [
      "Future continuous for actions in progress at specific future time and polite inquiries",
      "Future perfect for completion by a future point; Future perfect continuous",
      "Be about to for immediate future; Be due to for scheduled events",
      "Be bound to for certainty; Be likely to / unlikely to for probability",
      "Be on the point/verge of + -ing"
    ]}
  ]},
  {"category": "Modals Advanced", "subs": [
    {"subcategory": "Permission, Obligation, Prohibition", "points": [
      "Can, could, may, might for permission: full range",
      "Must, have to, need to, be supposed to for obligation",
      "Mustn't, can't, may not, not be allowed to for prohibition",
      "Needn't, don't have to, don't need to for lack of obligation",
      "Be to + infinitive for formal obligation/arrangement"
    ]},
    {"subcategory": "Speculation and Deduction", "points": [
      "Must, can't, may, might, could for present deduction",
      "Must have, can't have, may/might/could have for past deduction",
      "Should have / ought to have for unfulfilled expectation or criticism",
      "Needn't have vs didn't need to; Will for assumptions about the present"
    ]},
    {"subcategory": "Verbs of the Senses", "points": [
      "See, hear, feel + object + infinitive (complete) vs + -ing (in progress)",
      "Look, sound, smell, taste, feel + adjective; like/as if + clause"
    ]},
    {"subcategory": "Get", "points": [
      "Get + adjective (get tired); Get + past participle (get married); Get + object + past participle",
      "Get + to-infinitive (get to know); Get + -ing (get going)",
      "Have/get something done: causative structure"
    ]}
  ]},
  {"category": "Conditionals Advanced", "subs": [
    {"subcategory": "Mixed Conditionals", "points": [
      "Mixed: past condition→present result (If I had studied, I would have a better job now)",
      "Mixed: present condition→past result (If I were smarter, I would have solved it)",
      "Alternatives to if: unless, provided/providing (that), as long as, on condition that, supposing, in case",
      "Even if; whether...or not; If it weren't for / If it hadn't been for; But for + noun"
    ]},
    {"subcategory": "Inversion in Conditionals", "points": [
      "Inversion 1st conditional: Should you need help...",
      "Inversion 2nd conditional: Were I you...",
      "Inversion 3rd conditional: Had I known..."
    ]},
    {"subcategory": "Unreal Past Tenses", "points": [
      "Wish + past perfect for past regrets; Wish + would for complaints",
      "If only: extended uses; Would rather/sooner + subject + past simple/perfect",
      "It's (high/about) time + past simple"
    ]}
  ]},
  {"category": "Passive Voice Advanced", "subs": [
    {"subcategory": "Advanced Passive", "points": [
      "Passive with reporting verbs: It is said/believed/thought that...; He is said to...",
      "Distancing with passive (It has been reported that...)",
      "Passive with verbs with two objects (I was given a book / A book was given to me)",
      "Passive with get (He got fired); Passive with -ing forms; Need + -ing for passive"
    ]}
  ]},
  {"category": "Gerunds and Infinitives Advanced", "subs": [
    {"subcategory": "Complex Verb Patterns", "points": [
      "Verb + object + to-infinitive vs verb + object + -ing",
      "Verb + possessive + -ing (I appreciate your helping me)",
      "Perfect gerund: having + past participle; Perfect infinitive: to have + past participle",
      "Passive gerund: being + past participle; Passive infinitive: to be + past participle",
      "Continuous infinitive: to be + -ing (He appears to be sleeping)"
    ]}
  ]},
  {"category": "Nouns and Pronouns Advanced", "subs": [
    {"subcategory": "Pronouns Extended", "points": [
      "Reflexive pronouns: extended uses; Reciprocal pronouns: each other vs one another",
      "Generic/impersonal pronouns: you, we, they, one",
      "Indefinite pronouns: whoever, whatever, whichever, however"
    ]},
    {"subcategory": "Nouns Extended", "points": [
      "Compound nouns: noun+noun, adjective+noun, verb+noun",
      "Possessive forms with compound nouns; Possessive 's with time expressions",
      "Noun + preposition collocations (increase in, reason for, advantage of, solution to)"
    ]}
  ]},
  {"category": "Relative Clauses Advanced", "subs": [
    {"subcategory": "All Relative Forms", "points": [
      "Defining vs non-defining: full review; Relative clauses with prepositions",
      "Whose vs of which; Quantifier + of whom/which",
      "Reduced relative clauses (the man sitting there); Whatever, whoever, whichever, wherever"
    ]}
  ]},
  {"category": "It and There", "subs": [
    {"subcategory": "Preparatory Subjects", "points": [
      "It as preparatory subject (It's important to be on time)",
      "It + be + adjective + that clause; It takes + time + to-infinitive",
      "There as preparatory subject; There + modal verb (There must be a mistake)"
    ]}
  ]},
  {"category": "Ellipsis and Substitution", "subs": [
    {"subcategory": "Auxiliary Verbs and Ellipsis", "points": [
      "Ellipsis: omitting repeated words; Substitution with one/ones; so/not",
      "Have as auxiliary vs main verb; Emphatic do/does/did (I DO like it)"
    ]}
  ]},
  {"category": "Adjectives and Adverbs Advanced", "subs": [
    {"subcategory": "Comparative Structures", "points": [
      "Modifying comparatives: much, far, a lot, significantly, slightly, a bit, a little, marginally",
      "Comparative and comparative (better and better); The...the... for parallel increase",
      "By far the + superlative; One of the + superlative + plural noun"
    ]},
    {"subcategory": "Inversion with Adverbials", "points": [
      "Inversion after negative adverbials: never, rarely, seldom, hardly, barely, scarcely, no sooner, not only, under no circumstances",
      "Inversion after only + time/way: only then, only later, only when, only after, only if, not until",
      "Inversion after so/such + that (So beautiful was the view that...)"
    ]},
    {"subcategory": "Compound Adjectives", "points": [
      "Compound adjectives: well-known, good-looking, easy-going, time-consuming",
      "Number + noun (singular) as adjective (a five-minute break); Adjective + noun + -ed (blue-eyed)"
    ]}
  ]},
  {"category": "Clauses and Sentence Structure", "subs": [
    {"subcategory": "Adverbial Clauses", "points": [
      "Clauses of contrast: although, even though, while, whereas, despite, in spite of, much as",
      "Clauses of purpose: to, in order to, so as to, so that, for fear that, lest",
      "Clauses of reason: because, as, since, seeing that, given that, on the grounds that",
      "Clauses of result: so...that, such...that, therefore, consequently"
    ]},
    {"subcategory": "Participle Clauses", "points": [
      "Present participle clauses (-ing) for simultaneous actions",
      "Past participle clauses (-ed/3rd) for passive meaning",
      "Perfect participle clauses: having + past participle",
      "Participle clauses for reason, time, result, condition"
    ]},
    {"subcategory": "Cleft Sentences", "points": [
      "It-cleft: It + be + focused element + that/who (It was John who broke the window)",
      "Wh-cleft: What + clause + be + focus (What I need is a holiday)",
      "All-cleft: All I want is...; The reason why...; The thing that..."
    ]},
    {"subcategory": "Discourse Markers", "points": [
      "Structuring: as for, regarding, with regard to, as far as...is concerned, in terms of",
      "Clarifying: in other words, that is to say, I mean, to put it another way",
      "Concluding: on the whole, all in all, in conclusion, to sum up",
      "Attitude: fortunately, unfortunately, surprisingly, obviously, clearly, undoubtedly"
    ]}
  ]}
]

cefr["levels"]["B2 - Upper Intermediate"] = {"name": "B2", "description": "Usuario independiente: comprende ideas principales de textos complejos.", "categories": b2_cats}

# C1
c1_cats = [
  {"category": "Advanced Tense Nuances", "subs": [
    {"subcategory": "Advanced Present", "points": [
      "Present simple for dramatic narrative/historical present",
      "Present simple in newspaper headlines; Present simple in future subordinate clauses",
      "Present continuous with always for repeated annoying behavior",
      "Present continuous for gradual change (The climate is getting warmer)",
      "Stative verbs used dynamically (I'm loving this, She's being difficult)"
    ]},
    {"subcategory": "Advanced Past", "points": [
      "Narrative tenses: nuanced combination of all past forms",
      "Past perfect for unreal past after wish/if only",
      "Past tense for distancing/politeness (I was wondering if you could help)",
      "Past tense for hypothetical meaning (It's time we went)"
    ]}
  ]},
  {"category": "Modals - Advanced Nuances", "subs": [
    {"subcategory": "Advanced Modal Meanings", "points": [
      "Will for habits/characteristic behavior; Would for typical past behavior",
      "Will for assumptions about the present (That'll be John); Should for expectation",
      "Should after suggesting/insisting verbs (I suggest that he should go)",
      "Shall in formal/legal contexts; Can for general possibility",
      "May for concession (He may be rich but he's not happy); Might for reproach",
      "Must for annoying obligation (Must you make so much noise?)",
      "Need as modal in questions/negatives (Need I say more?); Dare as modal"
    ]},
    {"subcategory": "Advanced Deduction", "points": [
      "Will/would have for assumptions about the past",
      "Should/ought to have for unfulfilled expectation",
      "Might/may have for reproach or annoyance",
      "Could have for unrealized past ability/opportunity",
      "Needn't have vs didn't need to: nuanced distinction"
    ]}
  ]},
  {"category": "Passive Voice - All Forms", "subs": [
    {"subcategory": "Advanced Passive", "points": [
      "Passive with reporting verbs: full range (be alleged/said/believed/thought/considered/expected/known/reported/rumored/supposed to)",
      "Passive of -ing forms (being considered, having been told)",
      "Passive infinitive forms (to be done, to have been done)",
      "Get-passive in informal contexts; Passive for impersonal/formal style",
      "Passive with prepositions (The matter was looked into)"
    ]}
  ]},
  {"category": "Subjunctive", "subs": [
    {"subcategory": "Present Subjunctive", "points": [
      "Subjunctive after suggest/recommend/insist/demand (I suggest that he go)",
      "Subjunctive after adjectives of necessity (It is essential that he be informed)",
      "Fixed expressions (God save..., Be that as it may, Come what may, Suffice it to say, Long live)",
      "Subjunctive vs should + infinitive (I suggest that he go / he should go)"
    ]},
    {"subcategory": "Were-Subjunctive", "points": [
      "Were-subjunctive in conditionals (If I were you...)",
      "Were-subjunctive after wish (I wish I were taller)",
      "Were-subjunctive after as if/as though; after suppose/supposing; after would rather"
    ]}
  ]},
  {"category": "Inversion", "subs": [
    {"subcategory": "Negative Adverbial Inversion", "points": [
      "Never (Never have I seen such beauty); Rarely/Seldom",
      "Hardly/Barely/Scarcely...when; No sooner...than",
      "Not only...but also; Not until; Under no circumstances; On no account",
      "Little (Little did I know); Nowhere; Only + time/way (Only then did I understand)"
    ]},
    {"subcategory": "Conditional Inversion", "points": [
      "Should you need... (= If you should need...); Were I you...; Had I known..."
    ]},
    {"subcategory": "So/Such and Place Adverbial Inversion", "points": [
      "So + adjective + inversion + that; Such + be + noun + that",
      "Here/There + verb + subject; Prepositional phrase of place + verb + subject"
    ]}
  ]},
  {"category": "Emphasis and Cleft Sentences", "subs": [
    {"subcategory": "Cleft Sentences", "points": [
      "It-cleft: It + be + focus + that/who clause",
      "Wh-cleft: What + clause + be + focus; All-cleft: All + clause + be + focus",
      "The reason (why)... is...; The thing/person/place/time that... is..."
    ]},
    {"subcategory": "Fronting and Emphatic Structures", "points": [
      "Fronting of object/complement for emphasis",
      "Fronting with as/though (Tired as I was, I kept working)",
      "Emphatic do/does/did; Emphatic own; Reflexive pronouns for emphasis; Very + noun"
    ]}
  ]},
  {"category": "Complex Sentences", "subs": [
    {"subcategory": "Participle Clauses Advanced", "points": [
      "Participle clauses for reason, time, condition, result",
      "Perfect participle clauses (Having been told, she left); With conjunctions (While waiting)"
    ]},
    {"subcategory": "Advanced Adverbial Clauses", "points": [
      "Not that...; In that... for specification",
      "Much as / However much; No matter how/what/when/etc.",
      "For all + noun; Try as I might; Adjective + though/as + subject + verb"
    ]},
    {"subcategory": "Noun Clauses Extended", "points": [
      "That-clauses as subject; Wh-clauses as subject/object",
      "The fact that...; Whether/if clauses in subject position"
    ]}
  ]},
  {"category": "Advanced Determiners and Pronouns", "subs": [
    {"subcategory": "Determiners", "points": [
      "Quite/rather + article + adjective + noun; Such + (a/an) + adjective + noun",
      "What + (a/an) in exclamations; Half, both, all: position patterns",
      "Several, a number of, the majority of, a great deal of"
    ]},
    {"subcategory": "Pronouns", "points": [
      "One/ones for substitution; Impersonal one; Generic you/we/they",
      "Those who / people who; Such as pronoun"
    ]}
  ]},
  {"category": "Reporting Verbs", "subs": [
    {"subcategory": "Verb Patterns", "points": [
      "Verb + that-clause (admit, agree, claim, complain, confess, deny, explain, insist, mention, promise, recommend, suggest)",
      "Verb + object + that-clause (assure, convince, inform, notify, persuade, remind, tell, warn)",
      "Verb + to-infinitive (agree, claim, offer, promise, refuse, threaten)",
      "Verb + object + to-infinitive (advise, encourage, invite, persuade, remind, urge, warn)",
      "Verb + -ing (admit, deny, recommend, suggest)",
      "Verb + preposition + -ing (apologise for, insist on, accuse of, blame for, congratulate on)"
    ]}
  ]},
  {"category": "Avoiding Repetition", "subs": [
    {"subcategory": "Ellipsis and Substitution", "points": [
      "Ellipsis in coordinate and subordinate clauses; Ellipsis after auxiliaries and to",
      "Substitution with so/not, do so/it/that, one/ones; Reduced infinitives"
    ]},
    {"subcategory": "Cohesion Devices", "points": [
      "Reference: this, that, these, those for text cohesion",
      "Such + noun for back-reference; The former/the latter; Respectively; Namely, i.e."
    ]}
  ]},
  {"category": "Noun Phrases and Modification", "subs": [
    {"subcategory": "Complex Noun Phrases", "points": [
      "Pre-modification with multiple adjectives; Noun + noun modification",
      "Post-modification with prepositional phrases, relative clauses, participle clauses, to-infinitive",
      "Noun + of + possessive (a friend of mine, that car of John's)"
    ]},
    {"subcategory": "Genitive Advanced", "points": [
      "Double genitive (a friend of my father's); Independent genitive (the dentist's)",
      "Genitive with inanimate nouns: time, distance; Of-phrase for possession",
      "Noun modifiers vs genitive (a summer's day vs a summer day)"
    ]}
  ]}
]

cefr["levels"]["C1 - Advanced"] = {"name": "C1", "description": "Usuario competente: textos largos y complejos, fluidez y espontaneidad.", "categories": c1_cats}

# C2
c2_cats = [
  {"category": "Advanced Syntactic Manipulation", "subs": [
    {"subcategory": "Advanced Inversion", "points": [
      "Inversion with so + adjective + as + to-infinitive",
      "Inversion for rhetorical effect and dramatic emphasis",
      "Inversion with direction/movement prepositional phrases",
      "Inversion after not + object for emphasis (Not a single word did he say)",
      "Inversion in literary and poetic style"
    ]},
    {"subcategory": "Advanced Cleft and Pseudo-Cleft", "points": [
      "What + subject + do/does/did + is/was + infinitive",
      "The reason + why + clause; It is not that...but that...",
      "Cleft with question words (Where the money came from is a mystery)"
    ]}
  ]},
  {"category": "Advanced Verb Patterns", "subs": [
    {"subcategory": "Complex Passives", "points": [
      "It was decided/agreed/arranged that...; There is said/believed/thought to be...",
      "He is reported/rumored/alleged/said to have been...",
      "Object + be + past participle + to-infinitive (She was seen to enter)",
      "Progressive passive with modal (should be being done); Perfect passive infinitive"
    ]},
    {"subcategory": "Advanced Gerund/Infinitive", "points": [
      "Passive gerund after verbs/prepositions; Perfect passive gerund",
      "Bare infinitive after but/except; after why (Why bother?)",
      "To-infinitive as subject (To err is human); For + noun + to-infinitive",
      "To-infinitive expressing result; Only + to-infinitive for disappointing result"
    ]}
  ]},
  {"category": "Subjunctive and Hypothetical Language", "subs": [
    {"subcategory": "Advanced Subjunctive", "points": [
      "Formulaic subjunctive (Heaven forbid, So be it, Come what may, Be that as it may, God bless, Long live, Far be it from me)",
      "Mandative subjunctive in formal contexts",
      "Were-subjunctive in literary style",
      "Subjunctive after lest (He spoke quietly lest he be heard); after for fear that",
      "If it be / whether it be in formal/literary contexts"
    ]},
    {"subcategory": "Hypothetical/Speculative", "points": [
      "If + were to + infinitive for remote possibility",
      "If + should for tentative condition; Were it not for / Had it not been for",
      "Supposing/Imagine/What if + past perfect; As if/though + past perfect for past unreal",
      "Would that + past/past perfect (archaic); Even if + past/past perfect for extreme hypotheticals"
    ]}
  ]},
  {"category": "Advanced Cohesion", "subs": [
    {"subcategory": "Textual Cohesion", "points": [
      "Lexical cohesion: synonyms, hyponyms, superordinates",
      "Grammatical cohesion: reference, substitution, ellipsis, conjunction",
      "Theme and rheme patterns for information flow; Given vs new information management",
      "Parallel structures for rhetorical effect; Anaphoric and cataphoric reference",
      "Nominalization for academic density (investigate→investigation, destroy→destruction)"
    ]},
    {"subcategory": "Advanced Discourse Markers", "points": [
      "Concessive: Be that as it may, That said, Having said that, All the same, Even so, Mind you",
      "Reformulation: In a nutshell, To put it bluntly, In so many words, That is to say",
      "Attitudinal: To my mind, As I see it, For my part, If you ask me, Frankly speaking",
      "Transitional: With this in mind, Against this background, In the light of, On a different note",
      "Qualifying: Insofar as, To the extent that, For all intents and purposes, To all appearances",
      "Generalizing: By and large, On the whole, As a rule, For the most part"
    ]}
  ]},
  {"category": "Stylistic and Rhetorical Structures", "subs": [
    {"subcategory": "Parallelism and Balance", "points": [
      "Parallel structure in lists and pairs; Antithesis; Chiasmus; Tricolon; Climax/bathos"
    ]},
    {"subcategory": "Emphasis and Understatement", "points": [
      "Litotes (not bad, not uncommon, no small feat)",
      "Hyperbole through grammatical structures; Irony through grammatical choices",
      "Hedging: It could be argued that, It might be suggested that, It would appear that",
      "Boosting: There is no doubt that, It is abundantly clear that, Undeniably"
    ]},
    {"subcategory": "Register and Formality", "points": [
      "Formal vs informal grammar (whom vs who, shall vs will, may vs can, cannot vs can't)",
      "Passive for formal/impersonal register; Nominalization for academic register",
      "Latinate vs phrasal verbs (postpone vs put off, investigate vs look into)"
    ]}
  ]},
  {"category": "Advanced Conditional and Concessive", "subs": [
    {"subcategory": "Conditional Refinements", "points": [
      "Given + noun phrase as conditional; Assuming (that) as conditional",
      "Provided/Providing (that) vs As long as vs On condition that: nuanced distinctions",
      "In the event that/In case of for precautionary condition",
      "With/Without + noun for conditional meaning",
      "Adjective/participle + as + subject + verb; No matter + wh-word as universal conditional"
    ]},
    {"subcategory": "Concessive Patterns", "points": [
      "Adjective/Adverb + as/though (Rich as he is, he's not happy)",
      "Much as (Much as I respect him, I disagree); For all + noun",
      "Whatever/However/Whoever + may; While/Whereas/Whilst for contrast; Albeit for formal concession"
    ]}
  ]},
  {"category": "Negation Patterns", "subs": [
    {"subcategory": "Advanced Negation", "points": [
      "Double negation for emphasis (I can't not go = I must go)",
      "Negative scope and focus (I didn't go because I was tired: ambiguous)",
      "Transferred negation (I don't think he'll come)",
      "Partial negation with not + all/every/always (Not all that glitters is gold)",
      "Not...but rather...; Negation of modals: nuanced meanings"
    ]}
  ]},
  {"category": "Complex Prepositional Phrases", "subs": [
    {"subcategory": "Multi-word Prepositions", "points": [
      "In accordance with, in addition to, in case of, in charge of, in comparison with, in contrast to/with",
      "In favor of, in lieu of, in line with, in place of, in regard to, in relation to, in respect of/to",
      "In spite of, in terms of, in the event of, in view of",
      "On account of, on behalf of, on the basis of, on the grounds of, on the part of",
      "With regard to, with respect to, with the exception of",
      "By means of, by virtue of, by way of",
      "As a result of, as far as, as for, as opposed to, as regards, as to",
      "Apart from, aside from, due to, owing to, prior to, subsequent to"
    ]}
  ]}
]

cefr["levels"]["C2 - Proficiency"] = {"name": "C2", "description": "Usuario competente: comprende todo con facilidad, precisión y matices.", "categories": c2_cats}

db["systems"]["CEFR"] = cefr

# ============ AMERICAN SYSTEM ============
am = {"name": "American ESL System (6-Level University IEP Model)", "description": "Sistema americano estándar de 6 niveles usado en Intensive English Programs universitarios. Basado en Troy University, University of Delaware, American Language Center, y Azar-Hagen Grammar Series.", "source_mapping": {"Level 1": "Beginner (A1)", "Level 2": "High Beginner (A2-)", "Level 3": "Intermediate (A2/B1)", "Level 4": "High Intermediate (B1+)", "Level 5": "Advanced (B2)", "Level 6": "High Advanced (C1)"}, "levels": {}}

# Level 1
am_l1 = [
  {"category": "Parts of Speech", "subs": [
    {"subcategory": "Nouns", "points": ["Singular/plural with -s/-es", "Common irregular plurals (man→men, child→children)", "Countable vs uncountable: basic distinction", "Proper vs common nouns"]},
    {"subcategory": "Articles", "points": ["A/an: rules and usage", "The: basic usage", "No article with plural/general meaning"]},
    {"subcategory": "Pronouns", "points": ["Subject pronouns (I, you, he, she, it, we, they)", "Object pronouns (me, you, him, her, it, us, them)", "Possessive adjectives (my, your, his, her, its, our, their)", "Demonstrative: this, that, these, those"]},
    {"subcategory": "Adjectives", "points": ["Basic descriptive adjectives", "Position: before nouns and after 'be'", "Adjectives: no plural -s; Colors and numbers as adjectives"]}
  ]},
  {"category": "Verb 'to be'", "subs": [
    {"subcategory": "Present", "points": ["Affirmative: am, is, are; Negative: am not, isn't, aren't", "Questions: Am I?, Is he?; Contractions", "Wh- questions with 'be'"]},
    {"subcategory": "Past", "points": ["Was/were: affirmative, negative, questions"]}
  ]},
  {"category": "Present Simple", "subs": [
    {"subcategory": "Form and Use", "points": ["Affirmative: I/you/we/they (base) vs he/she/it (-s/-es)", "Negative: don't/doesn't; Questions: Do/Does", "Short answers; Habits, routines, facts", "Adverbs of frequency + position"]}
  ]},
  {"category": "Present Continuous", "subs": [
    {"subcategory": "Form and Use", "points": ["Affirmative: am/is/are + -ing; Negative and questions", "Spelling rules for -ing; Actions happening now", "Present simple vs present continuous: basic contrast"]}
  ]},
  {"category": "Past Simple", "subs": [
    {"subcategory": "Regular/Irregular", "points": ["Regular: + -ed + spelling/pronunciation", "Irregular: went, had, did, saw, ate, came, got, made, took, gave, said, thought, knew", "Negative: didn't; Questions: Did; Time expressions"]}
  ]},
  {"category": "Future", "subs": [
    {"subcategory": "Be going to", "points": ["Form and use: plans, intentions, predictions with evidence"]},
    {"subcategory": "Will", "points": ["Form: will/won't; Spontaneous decisions, offers, promises, predictions"]}
  ]},
  {"category": "Modals and Imperatives", "subs": [
    {"subcategory": "Can/Can't", "points": ["Ability, permission, requests, possibility"]},
    {"subcategory": "Would like", "points": ["Polite requests and offers"]},
    {"subcategory": "Imperatives", "points": ["Affirmative/negative commands; Let's for suggestions"]}
  ]},
  {"category": "There is/are", "subs": [
    {"subcategory": "Existence", "points": ["There is/are, negative, questions; There was/were"]}
  ]},
  {"category": "Prepositions", "subs": [
    {"subcategory": "Place/Time", "points": ["In, on, at for location and time; Under, behind, in front of, next to, between; From...to"]}
  ]},
  {"category": "Questions", "subs": [
    {"subcategory": "Yes/No and Wh-", "points": ["Yes/No with be, present simple, past simple, can", "What, Where, When, Who, Why, How + How much/many, How old, Which, Whose"]}
  ]},
  {"category": "Conjunctions and Word Order", "subs": [
    {"subcategory": "Basics", "points": ["And, but, or, so, because", "SVO word order; Question word order"]}
  ]},
  {"category": "Possessives", "subs": [
    {"subcategory": "Forms", "points": ["'s for singular; s' for plural; Possessive adjectives; Whose"]}
  ]}
]

# Level 2
am_l2 = [
  {"category": "Verb Tenses Expanded", "subs": [
    {"subcategory": "Past Continuous", "points": ["Form: was/were + -ing; Actions in progress at past time", "Interrupted actions with when/while"]},
    {"subcategory": "Present Perfect", "points": ["Have/has + past participle; Experiences (ever/never)", "Just, already, yet; For and since; Present perfect vs past simple"]},
    {"subcategory": "Future Expanded", "points": ["Will vs going to: detailed comparison", "Present continuous for future arrangements", "Present simple for timetabled future; Future time clauses"]}
  ]},
  {"category": "Modals Expanded", "subs": [
    {"subcategory": "Obligation/Advice", "points": ["Have to/don't have to; Must/mustn't", "Should/shouldn't; Ought to; Had better"]},
    {"subcategory": "Possibility/Ability", "points": ["May/might for possibility; Could for past ability", "Was/were able to; Can/could for polite requests"]}
  ]},
  {"category": "Conditionals", "subs": [
    {"subcategory": "Zero/First", "points": ["Zero: If + present, present (truths)", "First: If + present, will (real future); Unless; When vs If"]}
  ]},
  {"category": "Comparatives/Superlatives", "subs": [
    {"subcategory": "All Forms", "points": ["-er/more + than; the -est/the most", "Irregular: good→better→best, bad→worse→worst", "As...as; Not as...as; Modifying comparatives"]}
  ]},
  {"category": "Gerunds/Infinitives", "subs": [
    {"subcategory": "Basic Patterns", "points": ["Verb + -ing (enjoy, finish, mind, suggest)", "Verb + to-infinitive (want, decide, hope, plan, agree)", "Preposition + -ing; Purpose with to + infinitive and for + noun"]}
  ]},
  {"category": "Nouns/Articles Extended", "subs": [
    {"subcategory": "Countable/Uncountable", "points": ["Quantifiers: some, any, much, many, a lot of, plenty of", "Too much/many, enough; A few vs a little; Unit nouns"]},
    {"subcategory": "Articles", "points": ["A/an first mention; the second/unique; No article generalizations", "Geographical names basics; Meals, transport, institutions"]}
  ]},
  {"category": "Relative Clauses", "subs": [
    {"subcategory": "Defining", "points": ["Who, which, that, where, when, whose", "Omitting object relative pronouns"]}
  ]},
  {"category": "Phrasal Verbs", "subs": [
    {"subcategory": "Common", "points": ["Wake up, get up, turn on/off, put on, take off, pick up, look for/after, give up, find out", "Separable vs inseparable basics"]}
  ]},
  {"category": "Passive Voice", "subs": [
    {"subcategory": "Introduction", "points": ["Be + past participle; Present/past simple passive; Active vs passive purpose"]}
  ]}
]

# Level 3
am_l3 = [
  {"category": "Verb Tenses Extended", "subs": [
    {"subcategory": "Present Perfect Continuous", "points": ["Have/has been + -ing; Ongoing or recently stopped actions", "Present perfect simple vs continuous"]},
    {"subcategory": "Past Perfect", "points": ["Had + past participle; Actions before another past action", "With already, just, by the time; Narrative tenses combined"]},
    {"subcategory": "Future Continuous/Perfect", "points": ["Future continuous: will be + -ing; Future perfect: will have + past participle", "By + time with future perfect"]}
  ]},
  {"category": "Modals Intermediate", "subs": [
    {"subcategory": "Deduction", "points": ["Must for conclusions; Can't for impossibility; May/might/could for possibility", "Must have, can't have, may/might/could have for past"]},
    {"subcategory": "Past Modals", "points": ["Should have for past advice/regret; Could have for unrealized possibility", "Would have for past hypotheticals; Needn't have vs didn't need to"]}
  ]},
  {"category": "Conditionals Intermediate", "subs": [
    {"subcategory": "Second", "points": ["If + past simple, would + base; Unreal present/future; If I were..."]},
    {"subcategory": "Third", "points": ["If + past perfect, would have + past participle; Past regrets; Could have/might have"]}
  ]},
  {"category": "Reported Speech", "subs": [
    {"subcategory": "Statements/Questions", "points": ["Tense backshift rules; Pronoun/time changes", "Reported questions: word order; Yes/no with if/whether; Wh- questions", "Say vs tell; Reporting verbs: tell, ask, advise, order, invite, warn, remind"]}
  ]},
  {"category": "Passive Extended", "subs": [
    {"subcategory": "All Tenses", "points": ["Passive in all basic tenses; With modal verbs; Agent by", "Formal/academic style; Get + past participle"]}
  ]},
  {"category": "Relative Clauses Extended", "subs": [
    {"subcategory": "Defining/Non-defining", "points": ["Defining (no commas) vs non-defining (commas)", "Who, which, that, whose, where, when, why", "Prepositions in relative clauses; What as relative pronoun"]}
  ]},
  {"category": "Adjectives/Adverbs Intermediate", "subs": [
    {"subcategory": "Advanced Patterns", "points": ["-ed/-ing adjectives; Order of adjectives", "So + adj/adv + that; Such + noun phrase + that", "The...the...; Adverbs of degree; Enough patterns"]}
  ]},
  {"category": "Gerunds/Infinitives Extended", "subs": [
    {"subcategory": "Complex Patterns", "points": ["Verb + object + to-infinitive; Verb + object + bare infinitive (let, make, help)", "Verb + -ing or to-infinitive with meaning change", "Adj + to-infinitive; Too + adj + to-infinitive; Adj + enough + to-infinitive"]}
  ]},
  {"category": "Question Tags/Agreement", "subs": [
    {"subcategory": "Tags", "points": ["Positive-negative and negative-positive patterns", "Tags with all auxiliaries; Intonation patterns"]},
    {"subcategory": "Agreement", "points": ["So do I / Neither do I; So am I / Neither am I"]}
  ]}
]

# Level 4
am_l4 = [
  {"category": "Advanced Narrative", "subs": [
    {"subcategory": "All Past Tenses", "points": ["Narrative tenses combined; Past perfect continuous; Used to vs would", "Was going to for unfulfilled intentions"]}
  ]},
  {"category": "Advanced Future", "subs": [
    {"subcategory": "All Expressions", "points": ["Future continuous for polite inquiries; Future perfect/continuous", "Be about to, be due to, be likely to, be bound to", "Be on the verge of; Future in the past"]}
  ]},
  {"category": "Advanced Conditionals", "subs": [
    {"subcategory": "Mixed/Alternatives", "points": ["Mixed conditionals: past→present and present→past", "Unless, provided that, as long as, on condition that, supposing", "Inversion in conditionals; Wish + would; If only; Would rather + past"]}
  ]},
  {"category": "Modals Advanced", "subs": [
    {"subcategory": "All Meanings", "points": ["Full obligation/permission/ability/prohibition range", "Deduction/speculation full range; Need and dare as modals"]}
  ]},
  {"category": "Passive Advanced", "subs": [
    {"subcategory": "All Forms", "points": ["Reporting verbs passive; Distancing; Verbs with two objects", "Have/get something done; Need + -ing for passive"]}
  ]},
  {"category": "Relative Clauses Advanced", "subs": [
    {"subcategory": "All Forms", "points": ["Defining vs non-defining nuance; Prepositions formal/informal", "Whose vs of which; Quantifier + of whom/which; Reduced clauses", "Whatever, whoever, whichever, wherever"]}
  ]},
  {"category": "Gerunds/Infinitives Advanced", "subs": [
    {"subcategory": "Complex Patterns", "points": ["Perfect/passive gerund and infinitive forms", "Verb + possessive + -ing; Prepositional verbs + -ing"]}
  ]},
  {"category": "Clauses", "subs": [
    {"subcategory": "Adverbial", "points": ["Contrast: although, even though, while, whereas, despite, in spite of", "Purpose: to, in order to, so as to, so that; Reason; Result"]},
    {"subcategory": "Participle", "points": ["Present (-ing), past (-ed/3rd), perfect (having done) for reason/time/result/condition"]}
  ]},
  {"category": "Advanced Comparisons", "subs": [
    {"subcategory": "Modifying", "points": ["Much, far, a lot, significantly, slightly, a bit + comparative", "Better and better; The...the...; By far the + superlative"]}
  ]},
  {"category": "Reported Speech Advanced", "subs": [
    {"subcategory": "Reporting Verbs", "points": ["Verb + that-clause; Verb + to-infinitive; Verb + object + to-infinitive", "Verb + -ing; Verb + preposition + -ing"]}
  ]}
]

# Level 5
am_l5 = [
  {"category": "Inversion", "subs": [
    {"subcategory": "All Patterns", "points": ["After negative adverbials; After only + time/way", "In conditionals; After so/such + that; After here/there and place"]}
  ]},
  {"category": "Cleft/Emphasis", "subs": [
    {"subcategory": "Structures", "points": ["It-cleft; Wh-cleft; All-cleft", "Emphatic do/does/did; Fronting; Reflexive emphasis; Emphatic own"]}
  ]},
  {"category": "Subjunctive", "subs": [
    {"subcategory": "Forms", "points": ["Present subjunctive after suggest/recommend/insist/demand and necessity adjectives", "Fixed expressions; Were-subjunctive; After lest"]}
  ]},
  {"category": "Advanced Conditionals", "subs": [
    {"subcategory": "Refinements", "points": ["But for; If it weren't for; Given that; Provided vs as long as", "In the event that; Otherwise/or else; Supposing + past"]}
  ]},
  {"category": "Cohesion/Discourse", "subs": [
    {"subcategory": "Devices", "points": ["Ellipsis; Substitution: one, ones, do so, so/not", "Reference: this/that/these/those; The former/the latter", "Lexical cohesion; Discourse markers for structuring"]},
    {"subcategory": "Nominalization", "points": ["Verb→noun; Adjective→noun; Complex noun phrases"]}
  ]},
  {"category": "Advanced Verb Patterns", "subs": [
    {"subcategory": "Infinitives/Gerunds", "points": ["Passive/perfect forms; Bare infinitive after but/except; after why", "To-infinitive for result; Only + to-infinitive; For + noun + to-infinitive"]}
  ]},
  {"category": "Register/Style", "subs": [
    {"subcategory": "Formal/Informal", "points": ["Whom vs who; Shall vs will; May vs can", "Latinate vs phrasal verbs; Passive for formal style", "Hedging and boosting language"]}
  ]}
]

# Level 6
am_l6 = [
  {"category": "Rhetorical Structures", "subs": [
    {"subcategory": "Parallelism", "points": ["Parallel structure; Antithesis; Tricolon; Chiasmus"]},
    {"subcategory": "Emphasis/Understatement", "points": ["Litotes; Hyperbole; Irony; Nuanced hedging and boosting"]}
  ]},
  {"category": "Advanced Negation", "subs": [
    {"subcategory": "Complex", "points": ["Transferred negation; Partial negation; Double negation for emphasis", "Negation of modals: nuanced meanings"]}
  ]},
  {"category": "Multi-Word Prepositions", "subs": [
    {"subcategory": "Complex", "points": ["In accordance with, in addition to, in case of, in charge of, in comparison with, in contrast to/with, in favor of, in lieu of, in line with, in place of, in regard to, in relation to, in respect of/to, in spite of, in terms of, in the event of, in view of", "On account of, on behalf of, on the basis of, on the grounds of, on the part of", "With regard to, with respect to, with the exception of", "By means of, by virtue of, by way of", "As a result of, as far as, as for, as opposed to, as regards, as to", "Apart from, aside from, due to, owing to, prior to, subsequent to"]}
  ]},
  {"category": "Advanced Cohesion", "subs": [
    {"subcategory": "Text-Level", "points": ["Theme/rheme patterns; Given/new information", "Cataphoric/anaphoric reference; Lexical chains; Advanced discourse markers"]}
  ]}
]

am["levels"]["Level 1 - Beginner"] = {"name": "Level 1", "description": "Basic English grammar for simple sentences about daily life.", "categories": am_l1}
am["levels"]["Level 2 - High Beginner"] = {"name": "Level 2", "description": "Expanded grammar for everyday communication.", "categories": am_l2}
am["levels"]["Level 3 - Intermediate"] = {"name": "Level 3", "description": "Expanding grammar for broader situations. Combining tenses/structures.", "categories": am_l3}
am["levels"]["Level 4 - High Intermediate"] = {"name": "Level 4", "description": "Complex grammar for varied topics. Academic foundations.", "categories": am_l4}
am["levels"]["Level 5 - Advanced"] = {"name": "Level 5", "description": "Mastery of complex structures. Academic/professional English.", "categories": am_l5}
am["levels"]["Level 6 - High Advanced"] = {"name": "Level 6", "description": "Refinement of all structures. Stylistic/rhetorical mastery.", "categories": am_l6}

db["systems"]["American"] = am

# Save
output_path = "/root/english_grammar_database.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(db, f, indent=2, ensure_ascii=False)

# Count
total_cefr = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in cefr["levels"].values())
total_am = sum(sum(len(s["points"]) for c in lvl["categories"] for s in c["subs"]) for lvl in am["levels"].values())

print(f"Saved to {output_path}")
print(f"CEFR: {total_cefr} grammar points across 6 levels")
print(f"American: {total_am} grammar points across 6 levels")
print(f"Grand total: {total_cefr + total_am}")
for sys_name, sys_data in db["systems"].items():
    print(f"\n--- {sys_name} ---")
    for lvl_name, lvl_data in sys_data["levels"].items():
        count = sum(len(s["points"]) for c in lvl_data["categories"] for s in c["subs"])
        cats = len(lvl_data["categories"])
        print(f"  {lvl_name}: {count} points in {cats} categories")
