---
interest: medium
link: https://arxiv.org/abs/2604.18644
next_step: skim
priority: high
slack_ts: '1777001709.259599'
source: cs.LG - Machine Learning
status: unread
title: 'FASE : A Fairness-Aware Spatiotemporal Event Graph Framework for Predictive
  Policing'
---
# FASE : A Fairness-Aware Spatiotemporal Event Graph Framework for Predictive Policing
> 原文: [https://arxiv.org/abs/2604.18644](https://arxiv.org/abs/2604.18644)

arXiv:2604.18644v2 Announce Type: new
Abstract: Predictive policing systems that allocate patrol resources based solely on predicted crime risk can unintentionally amplify racial disparities through feedback driven data bias. We present FASE, a Fairness Aware Spatiotemporal Event Graph framework, which integrates spatiotemporal crime prediction with fairness constrained patrol allocation and a closed loop deployment feedback simulator.
We model Baltimore as a graph of 25 ZIP Code Tabulation Areas and use 139,982 Part 1 crime incidents from 2017 to 2019 at hourly resolution, producing a sparse feature tensor. The prediction module combines a spatiotemporal graph neural network with a multivariate Hawkes process to capture spatial dependencies and self exciting temporal dynamics. Outputs are modeled using a Zero Inflated Negative Binomial distribution, suitable for overdispersed and zero heavy crime counts. The model achieves a validation loss of 0.4800 and a test loss of 0.4857.
Patrol allocation is formulated as a fairness constrained linear optimization problem that maximizes risk weighted coverage while enforcing a Demographic Impact Ratio constraint with deviation bounded by 0.05. Across six simulated deployment cycles, fairness remains within 0.9928 to 1.0262, and coverage ranges from 0.876 to 0.936. However, a persistent detection rate gap of approximately 3.5 percentage points remains between minority and non minority areas. This result shows that allocation level fairness constraints alone do not eliminate feedback induced bias in retraining data, highlighting the need for fairness interventions across the full pipeline.
