---
title: "Prediction-Powered Inference Across Many Tasks for AI Evaluation & Social Science Research"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.29249
priority: medium
status: unread
interest: medium
next_step: skim
---
# Prediction-Powered Inference Across Many Tasks for AI Evaluation & Social Science Research
> 原文: [https://arxiv.org/abs/2605.29249](https://arxiv.org/abs/2605.29249)

arXiv:2605.29249v1 Announce Type: new
Abstract: Many applications require statistically valid inference across many related tasks, while using only a handful of high-quality labels per hypothesis. In AI evaluation, these tasks may correspond to model behaviors across prompts, subgroups, or hypotheses; in social science surveys, they may correspond to related questions, populations, or measurement conditions. Prediction-powered inference (PPI) uses abundant but inexpensive proxy measurements to improve inference from limited, ground-truth labels, but commonly used methods treat tasks independently and therefore fail to exploit shared structure across related tasks. This limitation is especially important in settings where only a small number of labels are available per task. To address this issue, we introduce a multi-task prediction-powered inference framework that uses labeled data from related tasks to improve power while preserving task-specific inference. Our methods exploit the shared structure in the proxy-ground-truth relationship through cross-task recalibration, while retaining within-task rectification and power tuning to construct accurate point estimates and confidence intervals. We prove that efficiency gains beyond power-tuned PPI are only possible when the proxy-ground-truth relationship contains nonlinear structure; affine cross-task recalibrations are asymptotically equivalent to using the original proxy. We complement our theoretical findings with experiments on synthetic and semi-synthetic datasets, as well as a case study auditing language models on election-related information during the 2024 U.S. presidential election. Using a large human-annotation study, we show that cross-task recalibration can substantially reduce confidence interval widths when labels are scarce.
