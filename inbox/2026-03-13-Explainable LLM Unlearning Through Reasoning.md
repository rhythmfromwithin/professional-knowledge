---
title: "Explainable LLM Unlearning Through Reasoning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.09980
priority: high
status: unread
interest: medium
next_step: skim
---
# Explainable LLM Unlearning Through Reasoning
> 原文: [https://arxiv.org/abs/2603.09980](https://arxiv.org/abs/2603.09980)

arXiv:2603.09980v1 Announce Type: new
Abstract: LLM unlearning is essential for mitigating safety, copyright, and privacy concerns in pre-trained large language models (LLMs). Compared to preference alignment, it offers a more explicit way by removing undesirable knowledge characterized by specific unlearning datasets. In previous works, gradient ascent (GA) and its variants have shown promise for implementing unlearning, yet their untargeted nature results in unintended degradation of general capabilities, incomplete removal of knowledge, and the generation of incoherent responses, among many others. We argue that these issues stem from the absence of explicit guidance on what and how models should unlearn. To fill this gap, we introduce a novel unlearning target, reasoning-based unlearning target, which satisfies both the specified unlearning scope and the specified post-unlearning response. Building on this, we propose targeted reasoning unlearning (TRU), which leverages reasoning-based unlearning target as guidance. We employ the target using a cross-entropy supervised loss combined with a GA-based loss, enabling the model to learn reasoning ability for precise knowledge removal while preserving unrelated abilities. We evaluate TRU against strong baselines across multiple benchmarks and LLM backbones, and find that it achieves more reliable unlearning while preserving general capabilities. Moreover, TRU exhibits superior robustness under diverse attack scenarios, stemming from the reasoning ability learned through reasoning-based targets. Overall, our study establishes reasoning-augmented unlearning as a practical paradigm for reliable and explainable LLM unlearning.
