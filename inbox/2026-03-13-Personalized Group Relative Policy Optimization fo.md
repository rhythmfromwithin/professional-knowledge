---
interest: medium
link: https://arxiv.org/abs/2603.10009
next_step: skim
priority: high
slack_ts: '1773974637.303549'
source: cs.LG - Machine Learning
status: unread
title: Personalized Group Relative Policy Optimization for Heterogenous Preference
  Alignment
---
# Personalized Group Relative Policy Optimization for Heterogenous Preference Alignment
> 原文: [https://arxiv.org/abs/2603.10009](https://arxiv.org/abs/2603.10009)

arXiv:2603.10009v1 Announce Type: new
Abstract: Despite their sophisticated general-purpose capabilities, Large Language Models (LLMs) often fail to align with diverse individual preferences because standard post-training methods, like Reinforcement Learning with Human Feedback (RLHF), optimize for a single, global objective. While Group Relative Policy Optimization (GRPO) is a widely adopted on-policy reinforcement learning framework, its group-based normalization implicitly assumes that all samples are exchangeable, inheriting this limitation in personalized settings. This assumption conflates distinct user reward distributions and systematically biases learning toward dominant preferences while suppressing minority signals. To address this, we introduce Personalized GRPO (P-GRPO), a novel alignment framework that decouples advantage estimation from immediate batch statistics. By normalizing advantages against preference-group-specific reward histories rather than the concurrent generation group, P-GRPO preserves the contrastive signal necessary for learning distinct preferences. We evaluate P-GRPO across diverse tasks and find that it consistently achieves faster convergence and higher rewards than standard GRPO, thereby enhancing its ability to recover and align with heterogeneous preference signals. Our results demonstrate that accounting for reward heterogeneity at the optimization level is essential for building models that faithfully align with diverse human preferences without sacrificing general capabilities.
