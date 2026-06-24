---
interest: medium
link: https://arxiv.org/abs/2606.24166
next_step: skim
priority: low
slack_ts: '1782274336.088259'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Distributed Quality-Diversity Search for Toxicity in Large Language Models
---
# Distributed Quality-Diversity Search for Toxicity in Large Language Models
> 原文: [https://arxiv.org/abs/2606.24166](https://arxiv.org/abs/2606.24166)

arXiv:2606.24166v1 Announce Type: new
Abstract: Large Language Models remain vulnerable to adversarial prompts that elicit harmful responses, and scaling red-teaming to cover a broad range of failure modes is constrained by the cost of text generation and evaluation. We present \emph{ToxSearch-S}, a speciated extension of toxicity-focused evolutionary prompt search with incremental, embedding-driven niche maintenance, together with an MPI master-worker realization that centralizes population and species bookkeeping on rank~0 while offloading prompt evolution and evaluation to $n\_w$ parallel workers. Under a common budget, ToxSearch-S attains peak toxicity competitive with both ToxSearch and RainbowPlus while following a measurably less toxic best-so-far trajectory, indicating lower cumulative search pressure. Diversity is non-uni-dimensional: RainbowPlus yields greater embedding-level spread, whereas ToxSearch-S partitions high-toxicity prompts into more localized behavioral pockets, reflected by a higher DBSCAN cluster count. MPI distribution delivers substantial wall-clock gains, approximately $1.8\times$ with two workers and $3.2\times$ with four, while leaving Best@B statistically indistinguishable from sequential execution. Four-worker runs also produce significantly larger final species cardinality and more toxicity-bearing species, without a reliable gain in global peak toxicity. These results position incremental speciation as a practical quality-diversity mechanism for AI Safety and MPI as an effective means of compressing time-to-result while preserving measured search outcomes.
