---
interest: medium
link: https://arxiv.org/abs/2609.09213
next_step: skim
priority: medium
slack_ts: '1789013734.940789'
source: cs.RO - Robotics
status: unread
title: 'Geometry Conditioning in an Embodied SLM: Training Controls and Robustness
  Diagnostics in a 0.8B Hybrid Model'
---
# Geometry Conditioning in an Embodied SLM: Training Controls and Robustness Diagnostics in a 0.8B Hybrid Model
> 原文: [https://arxiv.org/abs/2609.09213](https://arxiv.org/abs/2609.09213)

arXiv:2609.09213v1 Announce Type: new
Abstract: We study how physical-state inputs affect a 0.8B hybrid language model adapted for manipulation with 6.2M trainable parameters. Six conditions are trained on three LIBERO-Spatial tasks and evaluated over three seeds and 540 held-out rollouts. Conditioning recurrent decay gates on geometric increments yields 28.9% success, compared with 36.7% when those increments are shuffled during training and 24.4% without explicit object/goal geometry. Both geometry policies receive correct inputs at evaluation. A token adapter using the same increments scores 27.8%; differences vary across seeds and remain inconclusive. Token-clock conditioning scores 11.1%, including one seed that fails to converge. In separate robustness tests, a state-only relative-coordinate policy retains 7/10 success under frame relabeling, whereas all four tested visual policies fall to at most 3/20 after a 5 cm object displacement. These results show no reliable advantage from training-time geometric alignment under this recipe and illustrate the gap between coordinate invariance and physical-layout generalization. Episode records, seed-level analyses, and figure-generation code accompany the paper.
