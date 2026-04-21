---
interest: medium
link: https://arxiv.org/abs/2604.15376
next_step: skim
priority: medium
slack_ts: '1776742312.057249'
source: cs.CV - Computer Vision
status: unread
title: 'Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding
  Pipelines'
---
# Zoom Consistency: A Free Confidence Signal in Multi-Step Visual Grounding Pipelines
> 原文: [https://arxiv.org/abs/2604.15376](https://arxiv.org/abs/2604.15376)

arXiv:2604.15376v1 Announce Type: new
Abstract: Multi-step zoom-in pipelines are widely used for GUI grounding, yet the intermediate predictions they produce are typically discarded after coordinate remapping. We observe that these intermediate outputs contain a useful confidence signal for free: zoom consistency, the distance between a model's step-2 prediction and the crop center. Unlike log-probabilities or token-level uncertainty, zoom consistency is a geometric quantity in a shared coordinate space, making it directly comparable across architecturally different VLMs without calibration. We prove this quantity is a linear estimator of step-1 spatial error under idealized conditions (perfect step-2, target within crop) and show it correlates with prediction correctness across two VLMs (AUC = 0.60; Spearman rho = -0.14, p < 10^{-6} for KV-Ground-8B; rho = -0.11, p = 0.0003 for Qwen3.5-27B). The correlation is small but consistent across models, application categories, and operating systems. As a proof-of-concept, we use zoom consistency to route between a specialist and generalist model, capturing 16.5% of the oracle headroom between them (+0.8%, McNemar p = 0.19). Code is available at https://github.com/omxyz/zoom-consistency-routing.
