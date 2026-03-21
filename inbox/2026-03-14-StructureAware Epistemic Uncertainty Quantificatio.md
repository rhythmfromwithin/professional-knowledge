---
interest: medium
link: https://arxiv.org/abs/2603.11052
next_step: skim
priority: high
slack_ts: '1774060638.503709'
source: cs.LG - Machine Learning
status: unread
title: Structure-Aware Epistemic Uncertainty Quantification for Neural Operator PDE
  Surrogates
---
# Structure-Aware Epistemic Uncertainty Quantification for Neural Operator PDE Surrogates
> 原文: [https://arxiv.org/abs/2603.11052](https://arxiv.org/abs/2603.11052)

arXiv:2603.11052v1 Announce Type: new
Abstract: Neural operators (NOs) provide fast, resolution-invariant surrogates for mapping input fields to PDE solution fields, but their predictions can exhibit significant epistemic uncertainty due to finite data, imperfect optimization, and distribution shift. For practical deployment in scientific computing, uncertainty quantification (UQ) must be both computationally efficient and spatially faithful, i.e., uncertainty bands should align with the localized residual structures that matter for downstream risk management. We propose a structure-aware epistemic UQ scheme that exploits the modular anatomy common to modern NOs (lifting-propagation-recovering). Instead of applying unstructured weight perturbations (e.g., naive dropout) across the entire network, we restrict Monte Carlo sampling to a module-aligned subspace by injecting stochasticity only into the lifting module, and treat the learned solver dynamics (propagation and recovery) as deterministic. We instantiate this principle with two lightweight lifting-level perturbations, including channel-wise multiplicative feature dropout and a Gaussian feature perturbation with matched variance, followed by standard calibration to construct uncertainty bands. Experiments on challenging PDE benchmarks (including discontinuous-coefficient Darcy flow and geometry-shifted 3D car CFD surrogates) demonstrate that the proposed structure-aware design yields more reliable coverage, tighter bands, and improved residual-uncertainty alignment compared with common baselines, while remaining practical in runtime.
