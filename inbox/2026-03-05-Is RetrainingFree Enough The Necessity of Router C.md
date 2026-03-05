---
title: "Is Retraining-Free Enough? The Necessity of Router Calibration for Efficient MoE Compression"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.02217
priority: high
status: unread
---
# Is Retraining-Free Enough? The Necessity of Router Calibration for Efficient MoE Compression
> 原文: [https://arxiv.org/abs/2603.02217](https://arxiv.org/abs/2603.02217)

arXiv:2603.02217v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) models scale capacity efficiently, but their massive parameter footprint creates a deployment-time memory bottleneck. We organize retraining-free MoE compression into three paradigms - Expert Pruning, Expert Editing, and Expert Merging - and show that persistent post-compression degradation largely stems from a neglected factor: router-expert mismatch when experts are changed but the router is left untouched. We argue that effective retraining-free compression should avoid updating expert parameters while allowing lightweight router calibration. To this end, we propose Router Knowledge Distillation (Router KD), which updates only a tiny fraction of parameters (the router) by distilling the original model's next-token distribution on unlabeled calibration data. Experiments across representative methods in all three paradigms demonstrate consistent performance recovery, with substantially larger gains in fine-grained MoEs (many small experts) than in coarse-grained MoEs due to their more complex routing decision boundaries.
