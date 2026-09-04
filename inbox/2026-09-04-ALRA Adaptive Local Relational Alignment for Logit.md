---
title: "ALRA: Adaptive Local Relational Alignment for Logit-Based Pre-training Distillation of Autoregressive Language Models"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.03355
priority: medium
status: unread
interest: medium
next_step: skim
---
# ALRA: Adaptive Local Relational Alignment for Logit-Based Pre-training Distillation of Autoregressive Language Models
> 原文: [https://arxiv.org/abs/2609.03355](https://arxiv.org/abs/2609.03355)

arXiv:2609.03355v1 Announce Type: new
Abstract: Logit-based knowledge distillation for autoregressive language models usually aligns teacher and student next-token distributions over the entire vocabulary. However, this global objective overlooks relative preferences among likely token alternatives. Existing local approaches often select candidate tokens from either the teacher or the student alone. Teacher-only selection can miss tokens that the student considers likely, while student-only selection can rely on an inaccurate ranking early in training. We propose Adaptive Local Relational Alignment (ALRA), a position-specific framework combining student proposals with teacher guidance. At each valid prediction position, the student proposes likely tokens, while the teacher's most probable token is included as an anchor. ALRA adjusts the number of selected tokens according to how broadly the teacher distributes probability within this candidate set relative to the current batch. Adaptive Local Divergence retains the mass-matching term and separately matches the relative token distributions within the selected and remaining vocabulary regions. Unlike the exact full-vocabulary decomposition, it replaces the teacher-mass coefficients of the two conditional terms with unit coefficients, preventing either term from being downweighted solely because its region has low teacher probability. Student-Weighted Pairwise Relational Alignment emphasizes high-probability token pairs with small student probability gaps and gives less weight to unlikely or clearly separated pairs. Experiments on The Pile with randomly initialized 200M- and 500M-parameter students across nine zero-shot benchmarks yield average accuracies of 36.62% and 37.40%. ALRA exceeds the strongest competing distillation baseline by 0.94 and 0.83 percentage points and improves over pre-training without distillation by 2.31 and 2.91 points, respectively.
