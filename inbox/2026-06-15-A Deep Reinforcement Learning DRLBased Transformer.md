---
interest: medium
link: https://arxiv.org/abs/2606.13682
next_step: skim
priority: high
slack_ts: '1781500239.180889'
source: cs.AI - Artificial Intelligence
status: unread
title: A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the
  Open Shop Scheduling Problem
---
# A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem
> 原文: [https://arxiv.org/abs/2606.13682](https://arxiv.org/abs/2606.13682)

arXiv:2606.13682v1 Announce Type: new
Abstract: The open shop scheduling problem (OSSP) arises in many industrial and service settings but remains computationally challenging as the number of jobs and machines increases. While exact methods quickly become intractable, classical dispatching rules and metaheuristics may require substantial tuning to maintain solution quality at large scales. This study develops a Transformer-based scheduling policy for OSSP using an encoder-decoder architecture with multi-head attention. The model is trained on Taillard benchmark instances (4x4, 5x5, 7x7, and 10x10) using only the processing-time matrix as input and produces feasible schedules with makespans typically within 15-30% of best-known values. To evaluate scalability, the trained policy is applied without retraining to randomly generated instances from 40x40 to 100x100 and compared against classical dispatching heuristics, including SPT, LPT, MWKR, and EST. Across these large instances, the Transformer achieved average gaps of 12.89-15.12% relative to a standard lower bound. Compared with EST, the Transformer remained competitive, typically within a modest margin, while substantially outperforming SPT and LPT. These results indicate that a Transformer policy trained on small OSSP instances can generalize to substantially larger problems and provide a feature-light, learning-based alternative to classical dispatching rules.
