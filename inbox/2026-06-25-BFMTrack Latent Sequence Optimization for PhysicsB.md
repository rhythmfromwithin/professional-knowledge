---
interest: medium
link: https://arxiv.org/abs/2606.25056
next_step: skim
priority: medium
slack_ts: '1782360755.726599'
source: cs.RO - Robotics
status: unread
title: 'BFMTrack: Latent Sequence Optimization for Physics-Based Motion Tracking with
  Behavioral Foundation Models'
---
# BFMTrack: Latent Sequence Optimization for Physics-Based Motion Tracking with Behavioral Foundation Models
> 原文: [https://arxiv.org/abs/2606.25056](https://arxiv.org/abs/2606.25056)

arXiv:2606.25056v1 Announce Type: new
Abstract: Behavioral Foundation Models (BFMs) offer a promising path toward universal physics-based character control by organizing a rich repertoire of physically plausible behaviors into a latent space, guided by a large-scale motion dataset. While these models excel at time-invariant tasks, such as goal-reaching and state-based reward optimization, their latent space does not directly support time-varying objectives, such as tracking a motion sequence. For tracking, existing heuristics rely on moving-window-averaging that fails to capture the nuances of highly dynamic motions. In this work, we propose a novel Latent Sequence Optimization (LSO) to address these shortcomings. Our approach combines simulation rollouts with a policy gradient update to optimize over a sequence of latents, extending the capabilities of BFMs toward precise motion tracking without requiring reward engineering and tuning. To guide the optimization toward smooth, coherent latent trajectories, we model the latent sequence using temporally correlated noise. We validate our approach across dense tracking, sparse keyframing, and direct deployment onto a real humanoid robot.
