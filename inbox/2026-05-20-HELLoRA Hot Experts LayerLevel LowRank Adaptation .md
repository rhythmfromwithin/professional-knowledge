---
interest: medium
link: https://arxiv.org/abs/2605.18795
next_step: skim
priority: high
slack_ts: '1779423486.593629'
source: cs.LG - Machine Learning
status: unread
title: 'HELLoRA: Hot Experts Layer-Level Low-Rank Adaptation for Mixture-of-Experts
  Models'
---
# HELLoRA: Hot Experts Layer-Level Low-Rank Adaptation for Mixture-of-Experts Models
> 原文: [https://arxiv.org/abs/2605.18795](https://arxiv.org/abs/2605.18795)

arXiv:2605.18795v1 Announce Type: new
Abstract: Low-Rank Adaptation (LoRA) dominates parameter-efficient fine-tuning of large language models, yet most variants target dense architectures. Mixture-of-Experts (MoE) models scale parameters at near-constant per-token compute, and their sparse activation patterns create untapped opportunities for more efficient adaptation. We propose Hot-Experts Layer-level Low-Rank Adaptation (HELLoRA), which attaches LoRA modules only to the most frequently activated experts at each layer. This simple mechanism reduces trainable parameters and adapter-induced FLOPs while improving downstream performance, an effect we attribute to a form of structured regularization that preserves pretrained expert specialization. To stress-test HELLoRA under extreme parameter budgets, we further compose it with LoRI to form HELLoRI, which freezes the up-projection and sparsifies the down-projection. Across three MoE backbones, namely OlMoE-1B-7B, Mixtral-8x7B, and DeepSeekMoE, and three task families covering mathematical reasoning, code generation, and safety alignment, HELLoRA consistently outperforms strong PEFT baselines. Relative to vanilla LoRA on OlMoE, HELLoRA uses 15.7% of the trainable parameters, reduces adapter FLOPs by 38.7%, achieves 1.9x the training throughput, and improves accuracy by 9.2%. On DeepSeekMoE, HELLoRA outperforms LoRA while using only 23.2% of its trainable parameters. These results demonstrate that activation-aware adapter placement is an effective and practical route to scaling PEFT for MoE language models.
