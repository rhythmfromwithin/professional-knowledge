---
title: "Refining Compositional Diffusion for Reliable Long-Horizon Planning"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.03075
priority: medium
status: unread
interest: medium
next_step: skim
---
# Refining Compositional Diffusion for Reliable Long-Horizon Planning
> 原文: [https://arxiv.org/abs/2605.03075](https://arxiv.org/abs/2605.03075)

arXiv:2605.03075v1 Announce Type: new
Abstract: Compositional diffusion planning generates long-horizon trajectories by stitching together overlapping short-horizon segments through score composition. However, when local plan distributions are multimodal, existing compositional methods suffer from mode-averaging, where averaging incompatible local modes leads to plans that are neither locally feasible nor globally coherent. We propose Refining Compositional Diffusion (RCD), a training-free guidance method that steers compositional sampling toward high-density, globally coherent plans. RCD leverages the self-reconstruction error of a pretrained diffusion model as a proxy for the log-density of composed plans, combined with an overlap consistency term that enforces consistency at segment boundaries. We show that the combined guidance concentrates sampling on high-density plans that mitigate mode-averaging. Experiments on challenging long-horizon tasks from OGBench, including locomotion, object manipulation, and pixel-based observations, demonstrate that RCD consistently outperforms existing methods.
