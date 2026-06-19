---
title: "When to Trust, How to Distill: Multi-Foundation Model Guidance for Lightweight, Robust Scientific Time Series Forecasting"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2606.19363
priority: high
status: unread
interest: medium
next_step: skim
---
# When to Trust, How to Distill: Multi-Foundation Model Guidance for Lightweight, Robust Scientific Time Series Forecasting
> 原文: [https://arxiv.org/abs/2606.19363](https://arxiv.org/abs/2606.19363)

arXiv:2606.19363v1 Announce Type: new
Abstract: The deployment of Time-Series Foundation Models (TSFMs) in physical sciences is hindered by a critical trade-off: while these models encode rich, universal temporal dynamics, they suffer from severe distributional misalignment when applied zero-shot to specific scientific domains, and their computational cost prohibits deployment in edge-computing sensor networks. We address a fundamental challenge: How can we extract latent structural knowledge from misaligned foundation models (FM) to train lightweight, specialized forecasters? We propose Gated Uncertainty-Aware Routing for Distillation (Guard), a novel framework that reframes multiteacher distillation as an instance-wise decision process with two adaptive mechanisms: (1) a Contextual Router that dynamically selects the most relevant teacher based on local input statistics, exploiting complementarity across diverse foundation models; and (2) an Uncertainty-Gated Temperature mechanism that acts as a "circuit-breaker," automatically attenuating distillation strength when teacher confidence diverges from domain reality. We evaluate our proposed lightweight framework on four climate-critical domains: meteorology, ecosystem carbon flux, soil moisture, and energy grids. Our method significantly reduces RMSE relative to a fixed-weight multi-teacher distillation baseline, successfully distilling knowledge from pretrained FMs (teachers) even when they exhibit suboptimal zero-shot accuracy due to distribution shift between the original and target data domains. We demonstrate that these domain-misaligned teachers can still serve as critical correctives, outperforming the globally superior FMs on 28.5% of the hardest instances. Ultimately, this enables high-precision scientific forecasting suitable for resource-constrained edge deployment. Code is available at https://github.com/RupasreeDey/GUARD-KDD2026.
