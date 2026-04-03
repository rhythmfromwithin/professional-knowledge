---
interest: medium
link: https://arxiv.org/abs/2603.26749
next_step: skim
priority: low
slack_ts: '1775185059.940709'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Training-Free Diffusion-Driven Modeling of Pareto Set Evolution for Dynamic
  Multiobjective Optimization
---
# Training-Free Diffusion-Driven Modeling of Pareto Set Evolution for Dynamic Multiobjective Optimization
> 原文: [https://arxiv.org/abs/2603.26749](https://arxiv.org/abs/2603.26749)

arXiv:2603.26749v1 Announce Type: new
Abstract: Dynamic multiobjective optimization problems (DMOPs) feature time-varying objectives, which cause the Pareto optimal solution (POS) set to drift over time and make it difficult to maintain both convergence and diversity under limited response time. Many existing prediction-based dynamic multiobjective evolutionary algorithms (DMOEAs) either depend on learned models with nontrivial training cost or employ one-step population mapping, which may overlook the gradual nature of POS evolution. This paper proposes DD-DMOEA, a training-free diffusion-based dynamic response mechanism for DMOPs. The key idea is to treat the POS obtained in the previous environment as a "noisy" sample set and to guide its evolution toward the current POS through an analytically constructed multi-step denoising process. A knee-point-based auxiliary strategy is used to specify the target region in the new environment, and an explicit probability-density formulation is derived to compute the denoising update without neural training. To reduce the risk of misleading guidance caused by knee-point prediction errors, an uncertainty-aware scheme adaptively adjusts the guidance strength according to the historical prediction deviation. Experiments on the CEC2018 dynamic multiobjective benchmarks show that DD-DMOEA achieves competitive or better convergence-diversity performance and provides faster dynamic response than several state-of-the-art DMOEAs.
