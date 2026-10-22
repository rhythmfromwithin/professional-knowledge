---
interest: medium
link: https://arxiv.org/abs/2610.23862
next_step: skim
priority: high
slack_ts: '1792642776.320179'
source: cs.LG - Machine Learning
status: unread
title: Forecasting Patient Trajectories from the Electronic Health Records with Action-Conditioned
  World Models
---
# Forecasting Patient Trajectories from the Electronic Health Records with Action-Conditioned World Models
> 原文: [https://arxiv.org/abs/2610.23862](https://arxiv.org/abs/2610.23862)

arXiv:2610.23862v1 Announce Type: new
Abstract: We introduce a predictive world model for electronic health records (EHR) that represents patient histories as action conditioned latent trajectories. Rather than modeling clinical events solely through autoregressive token prediction, our framework explicitly separates patient states from observed clinical actions and learns their evolution through a state and action conditioned transition operator. At its core is a state dependent linearization predictor that propagates local changes in latent patient state, enabling time resolved prediction, multi step rollout, and action conditioned simulation. Empirically, we show that generated latent trajectories preserve downstream predictive signal, temporal structure, and subgroup level statistical relationships present in encoder derived representations. We further decode free running rollouts into the original clinical feature space and evaluate future clinical measurements against observed values using task matched forecasting baselines, demonstrating that the learned dynamics retain predictive information beyond latent space agreement. Across binary classification and time to event tasks, EHR WM achieves competitive, though task dependent, performance relative to substantially larger EHR foundation models while using a 30x smaller parameter footprint. Finally, perturbing observed action sequences produces corresponding changes in generated trajectories, demonstrating the action sensitivity of the learned dynamics. Together, these results support world modeling as a complementary framework for learning explicit, time indexed representations of patient evolution from longitudinal EHR.
