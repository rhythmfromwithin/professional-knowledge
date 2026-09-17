---
interest: medium
link: https://arxiv.org/abs/2609.16054
next_step: skim
priority: high
slack_ts: '1789619654.413809'
source: cs.LG - Machine Learning
status: unread
title: Causal neural set filtering for online multi-target tracking
---
# Causal neural set filtering for online multi-target tracking
> 原文: [https://arxiv.org/abs/2609.16054](https://arxiv.org/abs/2609.16054)

arXiv:2609.16054v1 Announce Type: new
Abstract: Transformer-based multi-target tracking (MTT) jointly learns data association and state estimation, but MT3/Track-MT3-style trackers repeatedly re-encode measurement windows, incurring redundant computation. We propose Causal Neural Set Filtering (CNSF)\footnote{\href{https://github.com/daihuangyu/CNSF}{Code: https://github.com/daihuangyu/CNSF}}, a neural set filter that encodes only current measurements while carrying past evidence in a structured recursive track state. CNSF combines exclusive Sinkhorn association, association-conditioned Kalman-shaped updates with moment matching, and recurrent Bernoulli lifecycle modeling with measurement-driven birth. These mechanisms impose soft one-to-one constraints, propagate association-induced state uncertainty, and support existence estimation under missed detections and birth--death transitions. On a held-out three-regime simulated test set, CNSF reduces mean GOSPA and T-GOSPA relative to Track-MT3 by 19.3\% and 30.4\%, with 55.9\% fewer parameters and a $3.76\times$ speedup in single-thread CPU inference.
