---
interest: medium
link: https://arxiv.org/abs/2610.26953
next_step: skim
priority: medium
slack_ts: '1792642776.636719'
source: cs.DC - Distributed Computing
status: unread
title: 'From Last-Layer to Cross-Layer: One-Shot Joint Classifier Reconstruction for
  Federated Learning'
---
# From Last-Layer to Cross-Layer: One-Shot Joint Classifier Reconstruction for Federated Learning
> 原文: [https://arxiv.org/abs/2610.26953](https://arxiv.org/abs/2610.26953)

arXiv:2610.26953v1 Announce Type: new
Abstract: Federated learning (FL) enables collaborative model training while preserving data privacy. However, non-independent and identically distributed (non-IID) data inevitably introduces classifier bias, leading to significant performance degradation. Existing studies primarily focus on calibrating or reconstructing the classifier after FL training to alleviate this bias. We find that the last-layer representations of the global model are often suboptimal for establishing a global decision boundary. Instead, classifiers constructed based on intermediate-layer representations can achieve superior performance. This finding provides a critical insight into overcoming the performance bottleneck inherent in existing paradigms. Nevertheless, identifying the optimal layer without auxiliary datasets or prior knowledge remains a formidable challenge. In this paper, we propose FLARE (Federated Cross-Layer Joint ClAssifier REconstruction) which rethinks classifier reconstruction from a cross-layer perspective and generalizes ridge regression to jointly exploit cross-layer representations, thereby surpassing the performance of any individual layer. Specifically, after FL training, clients perform only a single forward pass to extract class-conditional statistics from predefined layers. The server aggregates these statistics to construct a joint cross-layer ridge classifier, where an adaptive coupling coefficient regulates cross-layer correlations, thereby facilitating the integration of complementary discriminative information. Extensive experiments across 11 datasets, 8 model architectures, and diverse data heterogeneity scenarios demonstrate that FLARE, as a plug-and-play post-processing method, improves accuracy by 11.35% with only one additional communication round.
