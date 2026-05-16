---
interest: medium
link: https://arxiv.org/abs/2605.13859
next_step: skim
priority: low
slack_ts: '1778903338.626199'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'BiSpikCLM: A Spiking Language Model integrating Softmax-Free Spiking Attention
  and Spike-Aware Alignment Distillation'
---
# BiSpikCLM: A Spiking Language Model integrating Softmax-Free Spiking Attention and Spike-Aware Alignment Distillation
> 原文: [https://arxiv.org/abs/2605.13859](https://arxiv.org/abs/2605.13859)

arXiv:2605.13859v1 Announce Type: new
Abstract: Spiking Neural Networks (SNNs) offer promising energy-efficient alternatives to large language models (LLMs) due to their event-driven nature and ultra-low power consumption. However, to preserve capacity, most existing spiking LLMs still incur intensive floating-point matrix multiplication (MatMul) and nonlinearities, or training difficulties arising from the complex spatiotemporal dynamics. To address these challenges, we propose BiSpikCLM, the first fully binary spiking MatMul-free causal language model. BiSpikCLM introduces Softmax-Free Spiking Attention (SFSA), eliminating softmax and floating-point operations in autoregressive language modeling. For efficient training, we introduce Spike-Aware Alignment Distillation (SpAD), which aligns ANN teacher and SNN student across embeddings, attention maps, intermediate features, and output logits. SpAD framework allows BiSpikCLM to reach comparable performance to ANN counterparts using substantially fewer training tokens (e.g., only 5.6% of the tokens for the 1.3B model). As a result, BiSpikCLM achieves competitive performance at only 4.16% - 5.87% of the computational cost on natural language generation tasks. Our results highlight the feasibility and effectiveness of fully binary spike-driven LLMs and establish the distillation as a promising pathway for brain-inspired spiking NLP.
