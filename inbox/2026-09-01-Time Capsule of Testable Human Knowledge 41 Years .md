---
interest: medium
link: https://arxiv.org/abs/2608.27459
next_step: skim
priority: high
slack_ts: '1788321940.328409'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Time Capsule of Testable Human Knowledge: 41 Years of Jeopardy! in a Single
  Free Local Model'
---
# Time Capsule of Testable Human Knowledge: 41 Years of Jeopardy! in a Single Free Local Model
> 原文: [https://arxiv.org/abs/2608.27459](https://arxiv.org/abs/2608.27459)

arXiv:2608.27459v1 Announce Type: new
Abstract: In 2011, IBM's Watson was something like a sealed capsule of its era's queryable knowledge. Its DeepQA system defeated the strongest human Jeopardy! champions, but the knowledge that let it do so lived in a curated billion-document corpus running on a cluster of POWER7 servers, frozen at build time and impossible to move or copy. We show that the same kind of artifact, a snapshot of what a culture can answer, is now portable and essentially free. We evaluate a single 9 GB open-weight model (Qwen2.5-14B, 4-bit) against the complete open Jeopardy! clue dataset, 529,939 clues across all 41 broadcast seasons from 1984 to 2025. To our knowledge this is the first time a model has been run over the full corpus. The 41 years mark only how long the questions were collected. What they test is far older and broader: the accumulated body of human general knowledge a culture considers worth knowing, from ancient history and dead languages to science, literature, and geography, with a verified answer for every item. The model answers 67.0% of all clues under a strict forced-response protocol with exact and fuzzy matching, and exceeds 85% on factoid categories. We treat training-data exposure as something both systems share rather than a flaw unique to language models. Watson's case is in fact the more extreme one. Its corpus was assembled to contain Jeopardy answers and it was tuned on past clues, and it could not answer anything outside that curated distribution. The decisive test is whether a model can answer clues that did not exist when it was built. On clues aired after its training cutoff, the local model holds 65% and Claude Opus 4.8 holds 95%, while Watson by construction scores zero. The capability survives the move from a server room to a file you could seal in a time capsule, and unlike Watson it is not frozen to its own moment.
