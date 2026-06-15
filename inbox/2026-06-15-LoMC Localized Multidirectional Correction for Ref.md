---
interest: medium
link: https://arxiv.org/abs/2606.13709
next_step: skim
priority: medium
slack_ts: '1781500245.672429'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'LoMC: Localized Multidirectional Correction for Refusal Suppression in Routed
  Foundation Models'
---
# LoMC: Localized Multidirectional Correction for Refusal Suppression in Routed Foundation Models
> 原文: [https://arxiv.org/abs/2606.13709](https://arxiv.org/abs/2606.13709)

arXiv:2606.13709v1 Announce Type: new
Abstract: We study controlled post-training refusal suppression in routed MoE and hybrid-MoE foundation models, aiming to increase non-refusal target-response behavior while preserving general capability under a compact intervention footprint. Existing broad direction-based edits can perturb general-purpose computation, whereas support-only expert edits often lack sufficient capacity to correct heterogeneous refusal representations. To address this limitation, we introduce Localized Multidirectional Correction (LoMC), a support-gated intervention framework that follows a support-then-correction execution order: it first identifies a compact edit support, then aggregates prototype correction directions into layer-wise correction directions, and finally applies rank-one layer-wise correction only within the selected support. By using the edit support as a structural gating constraint, LoMC increases correction capacity without expanding the intervention scope. Experiments on text-only and multimodal safety benchmarks across four routed backbones show that LoMC substantially improves non-refusal target-response behavior while maintaining general capability under a compact intervention footprint.
