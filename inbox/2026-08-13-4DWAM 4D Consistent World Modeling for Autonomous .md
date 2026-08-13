---
title: "4D-WAM: 4D Consistent World Modeling for Autonomous Driving"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.10107
priority: medium
status: unread
interest: medium
next_step: skim
---
# 4D-WAM: 4D Consistent World Modeling for Autonomous Driving
> 原文: [https://arxiv.org/abs/2608.10107](https://arxiv.org/abs/2608.10107)

arXiv:2608.10107v1 Announce Type: new
Abstract: Emerging World-Action Models (WAMs) have demonstrated promising performance in autonomous driving by jointly modeling future driving scene evolution and trajectory planning. However, existing WAMs are typically trained with video data, which is only 2D projections of the underlying 4D driving scene. Consequently, WAMs fail to understand and capture the structure of 4D scenes and thus generate visually plausible yet 4D inconsistent future predictions that mislead downstream planning. To alleviate this issue, we present 4D-WAM, a model that leverages geometric foundation models for training-time supervision to enable 4D consistent world modeling. Specifically, we feed WAM-predicted future frames into a geometric foundation model, and use 4D-aware responses to define a 4D consistency loss. This loss encourages the model to understand, represent, and predict physically consistent 4D scenes during training, without additional inference cost. Moreover, we identify an early-decision phenomenon in WAMs and propose a decision-oriented timestep sampling strategy that emphasizes supervision at early, high-noise stages, where driving decisions are primarily formed. By propagating 4D supervision to this critical decision-formation phase, the proposed strategy further improves trajectory planning. Extensive experiments demonstrate that 4D-WAM effectively models 4D consistent scene evolution and achieves state-of-the-art performance on challenging NAVSIM-v1 and NAVSIM-v2 benchmarks.
