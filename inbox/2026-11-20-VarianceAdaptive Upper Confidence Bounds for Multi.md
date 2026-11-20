---
interest: medium
link: https://arxiv.org/abs/2611.24988
next_step: skim
priority: medium
slack_ts: '1795157516.911319'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Variance-Adaptive Upper Confidence Bounds for Multi-Armed Bandits with Kaplan--Meier
  Survival Estimation
---
# Variance-Adaptive Upper Confidence Bounds for Multi-Armed Bandits with Kaplan--Meier Survival Estimation
> 原文: [https://arxiv.org/abs/2611.24988](https://arxiv.org/abs/2611.24988)

arXiv:2611.24988v1 Announce Type: new
Abstract: We study the stochastic multi-armed bandit problem in which the reward associated with each arm is the survival probability at a pre-specified time horizon, and the observed outcome is a right-censored time-to-event variable. Standard bandit algorithms face delayed and partial observations in this setting. Prior adaptations for the Kaplan--Meier (KM) estimator rely on Hoeffding-type bounds that ignore the inherent heteroscedasticity of continuous survival processes. To bridge this gap, we propose KM-UCB, a variance-adaptive policy that unites continuous-time survival analysis with discrete sequential decision-making. By leveraging martingale theory and continuous influence functions, we derive a fixed-cohort empirical Bernstein bound parameterized by Greenwood's variance formula. For realtime allocation, we retain the Greenwood index and use a survival bound from completed records to review the recommended arm. Under catch-up reporting, the policy has logarithmic expected regret with an arm-specific variance term in the exploration bound. We evaluate the original policy in a dual-layer delayed simulation and a retrospective replay of breast cancer trial data, and evaluate the correction in a separate paired simulation.
