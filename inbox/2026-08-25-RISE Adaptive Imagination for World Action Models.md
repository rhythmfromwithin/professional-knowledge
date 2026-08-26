---
interest: medium
link: https://arxiv.org/abs/2608.20430
next_step: skim
priority: medium
slack_ts: '1787708797.547909'
source: cs.CV - Computer Vision
status: unread
title: 'RISE: Adaptive Imagination for World Action Models'
---
# RISE: Adaptive Imagination for World Action Models
> 原文: [https://arxiv.org/abs/2608.20430](https://arxiv.org/abs/2608.20430)

arXiv:2608.20430v1 Announce Type: new
Abstract: World Action Models (WAMs) improve planning by incorporating future world evolution into action generation, yet existing methods allocate a fixed imagination budget to every scene. We propose RISE (\textbf{R}efining \textbf{I}magination through \textbf{SE}lective Rollout), a system-level adaptive imagination framework that makes sequential \textsc{Roll}/\textsc{Stop} decisions according to the expected planning benefit of continued rollout. At each step, a Latent Evaluator estimates the risk revealed by the current prefix and how much planning could improve if imagination continues, while a Rollout Gate weighs this expected benefit against additional computation cost. Since factual driving logs expose only one realized future, we further construct \textbf{CounterDrive}, a counterfactual dataset with diverse outcomes and risk levels, to enrich future dynamics and provide localized risk supervision. Each retained sample undergoes expert verification and annotation of trajectory validity, incident onset, and causal category, providing a reusable resource for safety-critical world-modeling research. Experiments on NAVSIM and nuScenes show that RISE achieves the best overall planning performance while reducing unnecessary rollout, with additional transfer results supporting its plug-in generality across WAM architectures.
