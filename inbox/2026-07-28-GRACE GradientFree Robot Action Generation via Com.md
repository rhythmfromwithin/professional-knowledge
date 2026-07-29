---
interest: medium
link: https://arxiv.org/abs/2607.21661
next_step: skim
priority: medium
slack_ts: '1785295222.383829'
source: cs.RO - Robotics
status: unread
title: 'GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior
  Mean Estimation'
---
# GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation
> 原文: [https://arxiv.org/abs/2607.21661](https://arxiv.org/abs/2607.21661)

arXiv:2607.21661v1 Announce Type: new
Abstract: Diffusion policies generate multimodal robot action sequences from demonstrations, but steering them toward deployment-time constraints typically relies on differentiable guidance costs. This excludes many practical safety constraints, such as binary collision checks, joint limits, and black-box rollout costs that are nondifferentiable. We propose Gradient-free Robot Action generation via Combined diffusion-MPPI posterior mean Estimation (GRACE), which guides a pretrained diffusion policy with Model Predictive Path Integral (MPPI) control using only forward cost evaluations. Building on the common score-ascent structure of diffusion and MPPI, GRACE constructs a cost-conditioned guidance posterior at each reverse step and estimates its mean with a single MPPI update centered at the diffusion reverse mean. For differentiable costs, GRACE recovers conventional gradient guidance under a first-order, matched-covariance approximation. GRACE attains higher success rates than diffusion-based and sampling-based baselines in simulation. On a real 7-DoF manipulator, GRACE avoids a deployment-time obstacle that the unguided prior collides with in every trial. Code and experiment videos are available at https://anonymous.4open.science/w/grace-70BB/.
