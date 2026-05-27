---
interest: medium
link: https://arxiv.org/abs/2605.26155
next_step: skim
priority: medium
slack_ts: '1779856041.023659'
source: cs.RO - Robotics
status: unread
title: When Does Adaptive Guidance Help? Belief-Aware Privileged Distillation for
  Autonomous Driving Under Partial Observability
---
# When Does Adaptive Guidance Help? Belief-Aware Privileged Distillation for Autonomous Driving Under Partial Observability
> 原文: [https://arxiv.org/abs/2605.26155](https://arxiv.org/abs/2605.26155)

arXiv:2605.26155v1 Announce Type: new
Abstract: Guided Soft Actor-Critic (GSAC) distills knowledge from a privileged full-state teacher to a partial-observation student for autonomous driving, but uses a fixed distillation coefficient lambda regardless of the agent's uncertainty. We present Belief-Aware GSAC (BA-GSAC), which modulates lambda via ensemble disagreement, and use it as a testbed for a systematic empirical study asking: when does adaptive guidance actually help? Evaluating five strategies (fixed lambda in {0.01, 0.1}, adaptive, linear decay, and vanilla SAC) across three POMDP difficulty levels on Highway-Env, we find that preliminary single-seed runs suggest benefits under mild and moderate partial observability, but under severe occlusion (evaluated with 3 seeds for all methods) the adaptive coefficient collapses to lambda\_min within about 3K steps. We trace this to an observability blindness phenomenon: because the ensemble predicts partial observations, it achieves low disagreement even under heavy occlusion, modeling what is visible but unable to detect what is missing. We diagnose the root cause and propose an architectural fix (training the ensemble on full-state predictions using the guiding actor's privileged access); while not validated here, we show that even with current limitations, the warmup phase provides measurable stabilization (CV=13.3% vs. 29.8% for constant lambda=0.01). In fact, a simple deterministic linear decay schedule achieves the best severe-POMDP performance across all metrics (mean 116.5, CV=8.9%), suggesting that the scheduling effect, not the ensemble, drives the stability benefit. These findings provide practical guidance for designing uncertainty-aware teacher-student frameworks and highlight ensemble prediction targets as an important design choice.
