---
title: "Disentangling Structure and Semantics: How Schema Representation Affects LLM-Based SQL Generation"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.20356
priority: low
status: unread
interest: medium
next_step: skim
---
# Disentangling Structure and Semantics: How Schema Representation Affects LLM-Based SQL Generation
> 原文: [https://arxiv.org/abs/2608.20356](https://arxiv.org/abs/2608.20356)

arXiv:2608.20356v1 Announce Type: new
Abstract: LLM-based text-to-SQL pipelines read the database schema as text, which carries both structural cues (tables, keys, relationships) and semantic cues (table and column names); prior work has studied each axis in isolation, leaving open how they compare in magnitude and whether they substitute for one another. We present a controlled 6 times 3 factorial design crossing structural levels L\_1--L\_6 (from a denormalised wide table to a 3NF schema with foreign keys and explicit join paths) with semantic levels S\_1--S\_3 (anonymous, abbreviated, descriptive identifiers), evaluated on 397 corrected BIRD questions with identical gold queries throughout; we materialise 1NF and 2NF variants for nine BIRD databases to support the lowest structural levels. Across nine models from 0.5B to flagship scale we find an asymmetric substitution between the two axes, meaningful names compensate for missing structure but richer structural metadata does not recover performance when names are opaque, which reproduces in 8 of 9 databases and emerges with model scale (negligible below 3B). Within the structural axis the dominant lever is normalisation itself, not metadata layered on top of 3NF, suggesting that for current LLM-based text-to-SQL the practical bottleneck is semantic grounding rather than relational exposure.
