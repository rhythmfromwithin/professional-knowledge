---
interest: medium
link: https://arxiv.org/abs/2610.20628
next_step: skim
priority: high
slack_ts: '1792296496.645089'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design'
---
# PRISM: PRIvileged Sibling-guided Multi-Agent Topology Design
> 原文: [https://arxiv.org/abs/2610.20628](https://arxiv.org/abs/2610.20628)

arXiv:2610.20628v1 Announce Type: new
Abstract: Multi-agent systems (MAS) based on large language models (LLMs) have become a powerful way to address complex problems, and their effectiveness depends critically on the collaboration topology that decides which agents participate and how they communicate. Recent work learns to generate this topology from the task query, fitting the generator to corpora of execution-verified graphs. The post-training method for such generators remains a limitation: a corpus lists the graphs that solved a query but never ranks them, leaving continued supervised fine-tuning (SFT) with no per-query preference to exploit. Without such a preference, the generator drifts toward the topologies the corpus contains most often rather than those that suit each query, so a gain on one task can come at a cost on another. We propose PRISM, which recovers per-query signal from the same corpus by learning with privileged information: a teacher reads, through a zero-initialized low-rank branch, a sibling graph that also solved the query and is unavailable at deployment, and the student matches its per-decision targets on trajectories the student samples itself. Across six diverse benchmarks PRISM improves over every topology-design baseline evaluated, and matched-teacher controls support the contribution of privileged query information. Code is available in this link.
