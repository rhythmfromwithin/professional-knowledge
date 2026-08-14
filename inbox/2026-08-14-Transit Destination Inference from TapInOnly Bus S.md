---
interest: medium
link: https://arxiv.org/abs/2608.11223
next_step: skim
priority: medium
slack_ts: '1786674586.834389'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'Transit Destination Inference from Tap-In-Only Bus Smart-Card Data: A Hierarchical
  Bayesian Approach'
---
# Transit Destination Inference from Tap-In-Only Bus Smart-Card Data: A Hierarchical Bayesian Approach
> 原文: [https://arxiv.org/abs/2608.11223](https://arxiv.org/abs/2608.11223)

arXiv:2608.11223v1 Announce Type: cross
Abstract: Entry-only automatic fare collection systems record boardings but not alightings, preventing direct construction of origin-destination (OD) matrices. This study develops a Hierarchical Bayesian Latent-Destination (HBLD) model that combines station-hour boarding and inferred alighting demand with passenger card histories. Trip-chain destinations are treated as noisy evidence with a reliability parameter, allowing destination uncertainty to propagate into OD flows. The model was applied to 838,305 bus tap-ins collected in Changzhou in May 2025 and linked to stop-network and hourly weather data. It estimates destination distributions over feasible downstream and reverse-direction through-terminal stops using network, time-of-day, weather, and smoothed historical demand effects. A Bayesian personalization layer uses prior card trips and reverts to the shared trip-level distribution when history is unavailable. Fitted by stochastic variational inference and evaluated on the final week, HBLD outperformed the strongest baseline. Observed boarding patterns consistently improved prediction, especially without card history, while inferred alighting patterns helped only when trip-chain evidence was strongly trusted. The model captured travel consistent with through-terminal riding and bus-assisted road crossing and estimated destinations for trips unresolved by deterministic chaining. Because true alightings were unavailable, scores measure agreement with trip-chain outputs rather than actual destination accuracy. HBLD provides uncertainty-aware destination predictions and OD matrices for service management, planning, scheduling, and resource allocation.
