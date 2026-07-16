---
title: "TSCA-Net: Temporal-Spatial Clique Attention for Interpretable Multimodal Pedestrian Trajectory Prediction"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.11939
priority: medium
status: unread
interest: medium
next_step: skim
---
# TSCA-Net: Temporal-Spatial Clique Attention for Interpretable Multimodal Pedestrian Trajectory Prediction
> 原文: [https://arxiv.org/abs/2607.11939](https://arxiv.org/abs/2607.11939)

arXiv:2607.11939v1 Announce Type: new
Abstract: Accurate pedestrian trajectory prediction in crowded environments remains challenging due to the multimodal uncertainty of human motion and the variable complexity of motion dynamics across different scene contexts. Existing goal-conditioned models rely on static displacement structures that assign equal weight to all historical time steps, standard graph attention mechanisms, and fixed-capacity motion decoders that cannot adapt to local prediction complexity. To address these limitations, we propose TSCA-Net, a trajectory prediction framework built upon three complementary modules. The Temporal-Spatial Clique Attention (TSCA) module introduces learnable temporal gating into clique-based goal-history interaction, enabling time-aware modulation of historical observations relative to each candidate goal. The Cross-Pedestrian Clique Potential (CPCP) module models asymmetric pairwise agent relationships through a dynamic clique potential framework with a time-varying social graph. The Adaptive KAN Grid Refinement (AKGR) mechanism dynamically adjusts the B-spline grid resolution of a Kolmogorov-Arnold Network-augmented LSTM decoder based on per-agent goal distribution entropy, balancing model expressiveness against overfitting across varying motion complexities. Extensive experiments on the ETH/UCY and Stanford Drone Dataset benchmarks demonstrate that TSCA-Net achieves state-of-the-art performance, with average ADE/FDE of 0.13/0.20 m on ETH/UCY and 6.95/10.43 pixels on SDD. Comprehensive ablation studies confirm the complementary contributions of all three proposed modules.
