---
interest: medium
link: https://arxiv.org/abs/2606.28432
next_step: skim
priority: medium
slack_ts: '1782792825.627689'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Spectral Perturbation of the Empirical Fisher Information Matrix under Weight
  Quantization
---
# Spectral Perturbation of the Empirical Fisher Information Matrix under Weight Quantization
> 原文: [https://arxiv.org/abs/2606.28432](https://arxiv.org/abs/2606.28432)

arXiv:2606.28432v1 Announce Type: new
Abstract: We study the spectral perturbation of the empirical Fisher Information Matrix (FIM) of a parametric statistical model under two structured perturbations: departure of the input from a reference (in-distribution) ensemble, and finite-precision (quantized) perturbation of the model's parameters. For the first, under an explicit local curvature-monotonicity hypothesis on the dominant eigenvalue lambda\_max of the FIM, we show departure from a reference manifold provably elevates lambda\_max relative to a calibration baseline (Proposition 3.2), and discuss why this hypothesis is required, since curvature need not increase monotonically under every perturbation. Our principal result is a directional eigenvalue perturbation bound, via Weyl's inequality, showing lambda\_max under a quantization noise perturbation is lower bounded by its unperturbed value up to a third-order remainder, and, under a mild genericity condition, strictly exceeds it at leading order (Theorem 4.3). We give two tractable approximations to lambda\_max -- one heuristic, one with a rigorous two-sided bound -- and a completeness result for a threshold-based partition of an augmented state space. These results motivate using sigma\_t = lambda\_max(F\_t)/lambda\_base as a runtime monitoring statistic for deployed language models: the quantization result offers a mechanism for an empirical observation of our own, where a calibration threshold for this statistic was approximately 244 times larger than a preliminary full-precision estimate on a 4-bit quantized model, a single measurement rather than a value derived in closed form. We report supporting measurements (twelve models, n=1,080 trajectories) broadly consistent with our predictions, discuss the scope and limitations of every result, and state as an open problem the closed-form prediction of the quantization inflation magnitude our bound does not supply.
