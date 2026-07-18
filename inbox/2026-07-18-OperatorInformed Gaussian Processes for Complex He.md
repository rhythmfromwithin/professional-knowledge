---
title: "Operator-Informed Gaussian Processes for Complex Helmholtz Wavefields: From Synthetic Benchmarks to In Vivo Brain Elastography"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2607.14193
priority: medium
status: unread
interest: medium
next_step: skim
---
# Operator-Informed Gaussian Processes for Complex Helmholtz Wavefields: From Synthetic Benchmarks to In Vivo Brain Elastography
> 原文: [https://arxiv.org/abs/2607.14193](https://arxiv.org/abs/2607.14193)

arXiv:2607.14193v1 Announce Type: new
Abstract: The Helmholtz equation governs time-harmonic wave propagation, and in dissipative media a complex modulus renders its squared wavenumber $\kappa^2$ complex. Inferring such fields from sparse, noisy data calls for solvers that also quantify their own uncertainty. Physics-informed Gaussian-process (GP) regression supplies this by returning a posterior over the solution, yet operator-conditioned formulations have been developed almost exclusively for real-valued fields. We extend operator-informed GP regression to complex-valued Helmholtz problems by realifying the complex operator into an equivalent coupled real block, which enables inference with standard real-valued GP conditioning. The construction admits a family of priors, from a proper diagonal prior to coregionalized and multiscale variants, and conditions on PDE residuals and boundary traces. On benchmark problems in one to three dimensions, the solver is competitive with finite-difference and neural-network baselines at a far smaller interior-constraint budget. Unlike those deterministic baselines, it returns a posterior over the complex wavefield rather than a point estimate. Applied to \textit{in vivo} brain magnetic resonance elastography, a proper multiscale prior reconstructs the shear curl field to a correlation of $0.77$ with measurement, above a $0.75$ target. The gain arises from the multiscale kernel rather than from real--imaginary coupling. We further identify a low-frequency accuracy ceiling set by model mismatch and a posterior uncertainty that is not yet calibrated. Calibrated uncertainty therefore emerges as the central next step for probabilistic wavefield inference in dissipative media.
