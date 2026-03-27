---
interest: medium
link: https://arxiv.org/abs/2603.20296
next_step: skim
priority: high
slack_ts: '1774581542.791019'
source: cs.LG - Machine Learning
status: unread
title: Collaborative Adaptive Curriculum for Progressive Knowledge Distillation
---
# Collaborative Adaptive Curriculum for Progressive Knowledge Distillation
> 原文: [https://arxiv.org/abs/2603.20296](https://arxiv.org/abs/2603.20296)

arXiv:2603.20296v1 Announce Type: new
Abstract: Recent advances in collaborative knowledge distillation have demonstrated cutting-edge performance for resource-constrained distributed multimedia learning scenarios. However, achieving such competitiveness requires addressing a fundamental mismatch: high-dimensional teacher knowledge complexity versus heterogeneous client learning capacities, which currently prohibits deployment in edge-based visual analytics systems. Drawing inspiration from curriculum learning principles, we introduce Federated Adaptive Progressive Distillation (FAPD), a consensus-driven framework that orchestrates adaptive knowledge transfer. FAPD hierarchically decomposes teacher features via PCA-based structuring, extracting principal components ordered by variance contribution to establish a natural visual knowledge hierarchy. Clients progressively receive knowledge of increasing complexity through dimension-adaptive projection matrices. Meanwhile, the server monitors network-wide learning stability by tracking global accuracy fluctuations across a temporal consensus window, advancing curriculum dimensionality only when collective consensus emerges. Consequently, FAPD provably adapts knowledge transfer pace while achieving superior convergence over fixed-complexity approaches. Extensive experiments on three datasets validate FAPD's effectiveness: it attains 3.64% accuracy improvement over FedAvg on CIFAR-10, demonstrates 2x faster convergence, and maintains robust performance under extreme data heterogeneity ({\alpha}=0.1), outperforming baselines by over 4.5%.
