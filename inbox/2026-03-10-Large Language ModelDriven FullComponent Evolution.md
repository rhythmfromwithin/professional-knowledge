---
interest: medium
link: https://arxiv.org/abs/2603.06996
next_step: skim
priority: low
slack_ts: '1773715514.715379'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Large Language Model-Driven Full-Component Evolution of Adaptive Large Neighborhood
  Search
---
# Large Language Model-Driven Full-Component Evolution of Adaptive Large Neighborhood Search
> 原文: [https://arxiv.org/abs/2603.06996](https://arxiv.org/abs/2603.06996)

arXiv:2603.06996v1 Announce Type: new
Abstract: Adaptive Large Neighborhood Search (ALNS) is a prominent metaheuristic and a widely adopted approach for production and logistics optimization. However, it has long relied on hand-crafted components built on expert experience, which makes development slow and costly to adapt to new problems. This paper proposes a closed-loop, large-language-model-driven evolutionary framework that decouples ALNS and automatically rebuilds all of its components. We break ALNS into seven key modules: destroy, repair, operator selection, weight update, initial solution construction, acceptance rule, and destroy-rate control, and evolve each module through a dedicated task. By incorporating the MAP-Elites mechanism, the framework maintains a multi-dimensional elite archive to simultaneously drive the evolution of solution quality and strategic diversity. On TSPLIB benchmarks, the evolved algorithms consistently outperform optimized classic ALNS baselines under both fixed-iteration and fixed-time limits. The gains are especially clear on large-scale instances, where the average optimality gap drops from 3.18% to 0.74%. Code analysis also uncovers several counterintuitive yet meaningful design patterns that emerged naturally during evolution, offering practical and theoretical insights for future ALNS design. Finally, comparisons across multiple language models highlight clear differences in their ability to support evolutionary algorithm design, helping guide model selection for real-world engineering use.
