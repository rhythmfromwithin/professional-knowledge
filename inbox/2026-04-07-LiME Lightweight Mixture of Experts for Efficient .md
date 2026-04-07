---
interest: medium
link: https://arxiv.org/abs/2604.02338
next_step: skim
priority: high
slack_ts: '1775531931.037919'
source: cs.LG - Machine Learning
status: unread
title: 'LiME: Lightweight Mixture of Experts for Efficient Multimodal Multi-task Learning'
---
# LiME: Lightweight Mixture of Experts for Efficient Multimodal Multi-task Learning
> 原文: [https://arxiv.org/abs/2604.02338](https://arxiv.org/abs/2604.02338)

arXiv:2604.02338v1 Announce Type: new
Abstract: MoE-PEFT methods combine Mixture of Experts with parameter-efficient fine-tuning for multi-task adaptation, but require separate adapters per expert causing trainable parameters to scale linearly with expert count and limiting applicability to adapter-based architectures. We propose LiME (Lightweight Mixture of Experts), which achieves expert specialization through lightweight modulation rather than adapter replication. Instead of separate adapters, LiME uses a single shared PEFT module and modulates its output with lightweight expert vectors, reducing expert parameters while generalizing to any PEFT method. Notably, LiME introduces zero-parameter routing by leveraging existing frozen and adapted representations eliminating learned router parameters typically required per layer. Theoretically, we prove that (i) more experts preserve more task-relevant information and (ii) modulation approximates full expert-specific PEFT with bounded error. LiME further incorporates n-gram windowed routing and adaptive expert selection (Auto Top-K) based on routing confidence. Experiments on MMT-47, a multimodal multi-task benchmark with 47 tasks spanning text, image, and video, demonstrate that LiME achieves competitive or superior performance while using up to 4x fewer trainable parameters and up to 29% faster training compared to corresponding MoE-PEFT baselines.
