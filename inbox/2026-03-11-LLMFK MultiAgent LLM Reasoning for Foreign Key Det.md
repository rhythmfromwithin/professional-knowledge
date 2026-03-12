---
interest: medium
link: https://arxiv.org/abs/2603.07278
next_step: skim
priority: low
slack_ts: '1773283547.241129'
source: cs.DB - Databases
status: unread
title: 'LLM-FK: Multi-Agent LLM Reasoning for Foreign Key Detection in Large-Scale
  Complex Databases'
---
# LLM-FK: Multi-Agent LLM Reasoning for Foreign Key Detection in Large-Scale Complex Databases
> 原文: [https://arxiv.org/abs/2603.07278](https://arxiv.org/abs/2603.07278)

arXiv:2603.07278v1 Announce Type: new
Abstract: Detecting missing foreign keys (FKs) requires accurately modeling semantic dependencies across database schemas, which conventional heuristic-based methods are fundamentally limited in capturing. We propose LLM-FK, the first fully automated multi-agent framework for FK detection, designed to address three core challenges that hinder naive LLM-based solutions in large-scale complex databases: combinatorial search space explosion, ambiguous inference under limited context, and global inconsistency arising from isolated local predictions. LLM-FK coordinates four specialized agents: a Profiler that decomposes the FK detection problem into the task of validating FK candidate column pairs and prunes the search space via a unique-key-driven schema decomposition strategy; an Interpreter that injects self-augmented domain knowledge; a Refiner that constructs compact structural representations and performs multi-perspective chain-of-thought reasoning; and a Verifier that enforces schema-wide consistency through a holistic conflict resolution strategy. Experiments on five benchmark datasets demonstrate that LLM-FK consistently achieves F1-scores above 93%, surpassing existing baselines by 15% on the large-scale MusicBrainz database, while reducing the candidate search space by two to three orders of magnitude without losing true FKs and maintaining robustness under challenging conditions like missing data. These results demonstrate the effectiveness and scalability of LLM-FK in real-world databases.
