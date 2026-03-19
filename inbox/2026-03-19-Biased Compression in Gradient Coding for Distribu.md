---
interest: medium
link: https://arxiv.org/abs/2603.16353
next_step: skim
priority: medium
slack_ts: '1773888847.547249'
source: cs.DC - Distributed Computing
status: unread
title: Biased Compression in Gradient Coding for Distributed Learning
---
# Biased Compression in Gradient Coding for Distributed Learning
> 原文: [https://arxiv.org/abs/2603.16353](https://arxiv.org/abs/2603.16353)

arXiv:2603.16353v1 Announce Type: new
Abstract: Communication bottlenecks and the presence of stragglers pose significant challenges in distributed learning (DL). To deal with these challenges, recent advances leverage unbiased compression functions and gradient coding. However, the significant benefits of biased compression remain largely unexplored. To close this gap, we propose Compressed Gradient Coding with Error Feedback (COCO-EF), a novel DL method that combines gradient coding with biased compression to mitigate straggler effects and reduce communication costs. In each iteration, non-straggler devices encode local gradients from redundantly allocated training data, incorporate prior compression errors, and compress the results using biased compression functions before transmission. The server aggregates these compressed messages from the non-stragglers to approximate the global gradient for model updates. We provide rigorous theoretical convergence guarantees for COCO-EF and validate its superior learning performance over baseline methods through empirical evaluations. As far as we know, we are among the first to rigorously demonstrate that biased compression has substantial benefits in DL, when gradient coding is employed to cope with stragglers.
