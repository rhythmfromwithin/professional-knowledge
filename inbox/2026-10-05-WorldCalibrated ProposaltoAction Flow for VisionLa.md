---
interest: medium
link: https://arxiv.org/abs/2610.02323
next_step: skim
priority: medium
slack_ts: '1791351182.231919'
source: cs.RO - Robotics
status: unread
title: World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models
---
# World-Calibrated Proposal-to-Action Flow for Vision-Language-Action Models
> 原文: [https://arxiv.org/abs/2610.02323](https://arxiv.org/abs/2610.02323)

arXiv:2610.02323v1 Announce Type: new
Abstract: Flow-based Vision-Language-Action (VLA) policies generate action chunks by transporting samples from a task-agnostic isotropic Gaussian source. As this source is conditioned on neither recent execution nor predicted future evolution, (i) it discards the local continuity established by recently executed motion. (ii) Even when predictive world representations are introduced, they often only condition the transport dynamics rather than determine where generation starts, how far it may deviate, or along which action directions it may expand. Building on this observation, we introduce ProAct, a world-calibrated proposal-to-action framework that makes the generative source itself predictable. (i) To preserve motion continuity, a lightweight Proposal Expert converts recent actions into a scene-aware hypothesis via one motion-anchored endpoint flow-matching step, initializing generation near the demonstrated action manifold. (ii) To jointly capture intended scene evolution and proposal-future compatibility, a prospective World Expert treats the hypothesis as a soft motion prior while predicting the task-consistent latent future. (iii) From this compatibility, the model calibrates a proposal-centered anisotropic source, where a bounded per-step extent controls the allowed deviation and a trace-normalized low-rank geometry under a condition-number budget allocates refinement over coupled translation, rotation, and gripper directions. Compared with $\pi\_{0.5}$, ProAct improves performance across simulation and real-world tasks while reducing denoising steps by 50%, inference latency by up to 25.8%, and increasing throughput by up to 34.8%.
