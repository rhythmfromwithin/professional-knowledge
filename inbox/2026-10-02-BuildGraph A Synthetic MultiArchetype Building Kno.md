---
title: "BuildGraph: A Synthetic Multi-Archetype Building Knowledge Graph Dataset"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2610.00038
priority: low
status: unread
interest: medium
next_step: skim
---
# BuildGraph: A Synthetic Multi-Archetype Building Knowledge Graph Dataset
> 原文: [https://arxiv.org/abs/2610.00038](https://arxiv.org/abs/2610.00038)

arXiv:2610.00038v1 Announce Type: new
Abstract: Semantic querying of building knowledge graphs (KGs) underpins the integration of artificial intelligence into building operations, from natural-language access to cross-building analytics, but such KGs are rarely public owing to proprietary, security, and cost barriers. BuildGraph is a synthetic building KG dataset of 120 buildings in the Brick Schema ontology, grounded in U.S. Department of Energy prototype models and sensor-placement patterns from real buildings. It spans eight commercial building types across three ASHRAE energy-code vintages, with five realizations per archetype varying URI naming, sensor-attachment predicates, and topology. A 75-query SPARQL benchmark confirms structural completeness: BuildGraph reaches 91.5% Query Answerability Rate versus 35.8% for 59 real-world Brick files. Independently, it reproduces real buildings' sensor-type proportions on their shared vocabulary (cosine 0.86-0.94), evidence of realistic instrumentation where measurable. A downstream text-to-SPARQL experiment with Gemma 4 (26B) reaches 27.3% Row-Matching F1 (+17.5 pp over zero-shot) on 12 held-out buildings. BuildGraph gives facility managers and digital-twin developers a testbed for portable analytics and natural-language interfaces, and its dataset, generator, and benchmark are openly available at https://github.com/humanbuildingsynergy/BuildGraph.
