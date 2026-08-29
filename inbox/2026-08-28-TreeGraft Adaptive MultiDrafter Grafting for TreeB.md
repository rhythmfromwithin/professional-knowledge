---
interest: medium
link: https://arxiv.org/abs/2608.26112
next_step: skim
priority: high
slack_ts: '1787986077.508089'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding'
---
# TreeGraft: Adaptive Multi-Drafter Grafting for Tree-Based Speculative Decoding
> 原文: [https://arxiv.org/abs/2608.26112](https://arxiv.org/abs/2608.26112)

arXiv:2608.26112v1 Announce Type: new
Abstract: Speculative decoding accelerates large language model inference through a draft-then-verify paradigm. Building on this, tree-structured methods improve inference by organizing proposals into multiple candidate paths, increasing the accepted length. However, existing tree-structured methods use a single drafter for all drafting steps, creating a dilemma: a smaller drafter is fast but yields lower-quality trees, whereas a larger drafter improves tree quality but suffers from high latency. To address this, we propose TreeGraft, a multi-drafter framework in which drafters of different costs jointly construct a shared draft tree. TreeGraft uses the stronger drafter to rescore candidates by updating scores assigned by the weaker drafter, reselect grafting positions, and recover promising paths left unexplored. It also integrates stronger drafter expansions non-destructively, preserving existing branches that may still be accepted by the target model. Together, these designs improve the quality of the shared draft tree. To control the drafting cost, TreeGraft introduces a lightweight scheduler distilled from an offline value system to decide when to call the stronger drafter. Across 10 model pairs and 6 benchmarks, TreeGraft outperforms the better of the two fixed single-drafter endpoint strategies by 15.1% on average, reaching a maximum gain of 26.6%. Our code is available at https://anonymous.4open.science/r/TreeGraft-E983.
