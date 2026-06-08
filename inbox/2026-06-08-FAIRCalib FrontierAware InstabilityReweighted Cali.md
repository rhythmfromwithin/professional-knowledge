---
interest: medium
link: https://arxiv.org/abs/2606.06547
next_step: skim
priority: high
slack_ts: '1780894165.969289'
source: cs.LG - Machine Learning
status: unread
title: 'FAIR-Calib: Frontier-Aware Instability-Reweighted Calibration for Post-Training
  Quantization of Diffusion Large Language Models'
---
# FAIR-Calib: Frontier-Aware Instability-Reweighted Calibration for Post-Training Quantization of Diffusion Large Language Models
> 原文: [https://arxiv.org/abs/2606.06547](https://arxiv.org/abs/2606.06547)

arXiv:2606.06547v1 Announce Type: new
Abstract: Diffusion Large Language Models (dLLMs) refine tokens iteratively but commit them irreversibly, leading to a "stability lag" where early decisions remain fragile even after being written. We reveal that Post-Training Quantization (PTQ) error easily flips these borderline decisions at the write frontier, which are then permanently locked in and amplified. To address this, we propose Frontier-Aware Instability-Reweighted Calibration (FAIR-Calib), a two-stage PTQ framework for dLLMs. Stage I probes a full-precision teacher to estimate a position prior that combines frontier hits and masked-stage reliability. Stage II performs off-policy, layer-wise calibration by minimizing a reweighted hidden-state MSE, effectively prioritizing the protection of fragile frontier states without requiring expensive end-to-end diffusion rollouts. We further theoretically justify our weighted objective as a surrogate for output KL divergence. Empirically, FAIR-Calib consistently outperforms state-of-the-art baselines on LLaDA and Dream (W4A4), significantly reducing frontier decision flips and suppressing post-commit mismatches across diverse benchmarks.
