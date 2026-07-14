---
interest: medium
link: https://arxiv.org/abs/2607.08776
next_step: skim
priority: high
slack_ts: '1783998903.547869'
source: cs.LG - Machine Learning
status: unread
title: A Unified Approach to Interpreting Knowledge Distillation for Large Language
  Models via Interactions
---
# A Unified Approach to Interpreting Knowledge Distillation for Large Language Models via Interactions
> 原文: [https://arxiv.org/abs/2607.08776](https://arxiv.org/abs/2607.08776)

arXiv:2607.08776v1 Announce Type: new
Abstract: Despite the success of knowledge distillation (KD) in Large Language Models (LLMs), the underlying mechanism behind its efficacy remains unclear. In this paper, we propose a unified approach to explore the common mechanism of various KD methods using interactions. Specifically, we decompose the output score of the LLM into the sum of numerous interactions. Each interaction represents a nonlinear relationship involving a set of input variables (e.g., words). Based on the decomposed interactions, we discover that the common mechanism underlying various KD methods is the sparsification of interactions, i.e., student models retain fewer interactions for inference while suppressing other interactions to zero effects. Furthermore, we discover that the performance variance across different KD methods arises from their capabilities in handling complex interactions. A KD method typically yields better performance if it enables the student model to achieve higher sparsity of complex interactions. Motivated by these insights, we propose a plug-and-play loss function called Complex Interaction Penalty (CIP) to explicitly enforce the sparsity of complex interactions during the distillation process. Extensive experiments demonstrate that integrating CIP consistently improves the performance of diverse KD methods on both in-domain and out-of-distribution benchmarks.
