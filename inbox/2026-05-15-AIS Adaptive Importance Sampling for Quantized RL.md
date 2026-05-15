---
title: "AIS: Adaptive Importance Sampling for Quantized RL"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2605.13907
priority: medium
status: unread
interest: medium
next_step: skim
---
# AIS: Adaptive Importance Sampling for Quantized RL
> 原文: [https://arxiv.org/abs/2605.13907](https://arxiv.org/abs/2605.13907)

arXiv:2605.13907v1 Announce Type: new
Abstract: Reinforcement learning (RL) for large language models (LLMs) is dominated by the cost of rollout generation, which has motivated the use of low-precision rollouts (e.g., FP8) paired with a BF16 trainer to improve throughput and reduce memory pressure. This introduces a rollout-training mismatch that biases the policy gradient and can cause training to collapse outright on reasoning benchmarks. We show that the mismatch is non-stationary and acts as a double-edged sword: early in training it provides a stochastic exploration bonus, exposing the gradient to trajectories the trainer would otherwise under-sample, but the same perturbation transitions into a destabilizing source of bias as the policy concentrates.
To solve this, we propose Adaptive Importance Sampling (AIS), a correction framework that adjusts the strength of its intervention on a per-batch basis. AIS combines three real-time diagnostics, namely weight reliability, divergence severity, and variance amplification, into a single mixing coefficient that interpolates between the uncorrected and fully importance-weighted gradients, suppressing the destabilizing component of the mismatch while preserving its exploratory benefit. We integrate AIS into GRPO and evaluate it on the diffusion-based LLaDA-8B-Instruct and the autoregressive Qwen3-8B and Qwen3.5-9B across mathematical reasoning and planning benchmarks. AIS matches the BF16 baseline on most tasks while retaining the 1.5 to 2.76x rollout speedup of FP8.
