---
interest: medium
link: https://arxiv.org/abs/2608.19231
next_step: skim
priority: medium
slack_ts: '1787362759.542329'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'TorchDCM: A Unified PyTorch-Native Package for Discrete Choice Modeling'
---
# TorchDCM: A Unified PyTorch-Native Package for Discrete Choice Modeling
> 原文: [https://arxiv.org/abs/2608.19231](https://arxiv.org/abs/2608.19231)

arXiv:2608.19231v1 Announce Type: new
Abstract: Estimating large and simulation-intensive discrete choice models (DCMs) requires repeated evaluation of utilities, probabilities, derivatives, and simulated likelihoods over many observations, alternatives, and draws. Existing DCM software provides mature econometric workflows, while recent GPU-oriented tools accelerate selected models, leaving a gap between econometric coverage and scalable differentiable computation. We introduce TorchDCM, an open Python package for discrete choice modeling that compiles choice data and model specifications into a unified PyTorch-native likelihood engine for estimation, inference, prediction, and structured reporting on CPU or CUDA devices. The package covers the principal econometric functionality available across Biogeme and Apollo, including multinomial, nested, mixed, ordered, latent-variable, and panel likelihoods. It also supports ragged choice sets, constrained parameters, covariance estimation, willingness-to-pay analysis, elasticities, and extensible likelihood components. We evaluate TorchDCM against seven other estimation packages in aligned synthetic and real-data full-estimation experiments. TorchDCM completes all 45 synthetic cases, runs fastest in every comparable synthetic case, and satisfies the prespecified final-log-likelihood tolerance in every comparison with at least two comparable solutions. More precisely, it reduces median runtime by 89.1%-99.7% relative to Biogeme and Apollo across model-data settings. CUDA provides an additional 12.0-71.0x speedup over single-core TorchDCM. These results establish a scalable and reproducible foundation for econometric estimation and differentiable choice-model development. The open-source package and executed examples are available at https://github.com/mbc96325/torchdcm.
