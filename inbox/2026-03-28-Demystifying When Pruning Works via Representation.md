---
interest: medium
link: https://arxiv.org/abs/2603.24652
next_step: skim
priority: high
slack_ts: '1774841189.442059'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Demystifying When Pruning Works via Representation Hierarchies
---
# Demystifying When Pruning Works via Representation Hierarchies
> 原文: [https://arxiv.org/abs/2603.24652](https://arxiv.org/abs/2603.24652)

arXiv:2603.24652v1 Announce Type: new
Abstract: Network pruning, which removes less important parameters or architectures, is often expected to improve efficiency while preserving performance. However, this expectation does not consistently hold across language tasks: pruned models can perform well on non-generative tasks but frequently fail in generative settings. To understand this discrepancy, we analyze network pruning from a representation-hierarchy perspective, decomposing the internal computation of language models into three sequential spaces: embedding (hidden representations), logit (pre-softmax outputs), and probability (post-softmax distributions). We find that representations in the embedding and logit spaces are largely robust to pruning-induced perturbations. However, the nonlinear transformation from logits to probabilities amplifies these deviations, which accumulate across time steps and lead to substantial degradation during generation. In contrast, the stability of the categorical-token probability subspace, together with the robustness of the embedding space, supports the effectiveness of pruning for non-generative tasks such as retrieval and multiple-choice selection. Our analysis disentangles the effects of pruning across tasks and provides practical guidance for its application. Code is available at https://github.com/CASE-Lab-UMD/Pruning-on-Representations
