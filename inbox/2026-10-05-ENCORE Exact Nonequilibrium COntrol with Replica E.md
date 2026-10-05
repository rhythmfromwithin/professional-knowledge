---
title: "ENCORE: Exact Non-equilibrium COntrol with Replica Exchange for Diffusion Generation"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.02538
priority: medium
status: unread
interest: medium
next_step: skim
---
# ENCORE: Exact Non-equilibrium COntrol with Replica Exchange for Diffusion Generation
> 原文: [https://arxiv.org/abs/2610.02538](https://arxiv.org/abs/2610.02538)

arXiv:2610.02538v1 Announce Type: new
Abstract: Inference-time control steers a pretrained generative model towards a target distribution without retraining. We study tilted targets $\pi\_0\propto G\_0\,p\_0$, where $p\_0$ is the sampler output distribution and $G\_0$ is an evaluable reweighting function. Existing approaches rely on sequential annealing with sequential Monte Carlo (SMC) or parallel annealing with replica exchange (RE). Sequential control is exact but needs large particle populations, whereas no exact parallel control method exists: existing RE corrections approximate an intractable time reversal and are biased. We propose Exact Non-equilibrium COntrol with Replica Exchange (ENCORE), the first exact parallel control method. Each replica stores its generation trajectory, so the upward move is a truncation and the intractable time reversal is never simulated. We prove target invariance and show that the resulting dynamics are those of non-equilibrium replica exchange with the exact time reversal as forward proposal. Under regularity conditions, our diffusion analysis shows that both sequential and parallel control become unstable under refinement of the time discretisation without guidance, whereas guided proposals remain stable and yield diagnostics for tuning the schedule and the computational budget. Across synthetic targets, Boltzmann sampling of biomolecules, and image generation, ENCORE achieves competitive accuracy and diversity, remains robust to sampler perturbations, and applies to distilled samplers where existing RE corrections are unavailable.
