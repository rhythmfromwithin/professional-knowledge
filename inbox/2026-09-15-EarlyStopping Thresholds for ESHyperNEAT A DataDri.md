---
interest: medium
link: https://arxiv.org/abs/2609.13533
next_step: skim
priority: low
slack_ts: '1789446773.167619'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Early-Stopping Thresholds for ES-HyperNEAT: A Data-Driven Approach from Fitness
  Dynamics'
---
# Early-Stopping Thresholds for ES-HyperNEAT: A Data-Driven Approach from Fitness Dynamics
> 原文: [https://arxiv.org/abs/2609.13533](https://arxiv.org/abs/2609.13533)

arXiv:2609.13533v1 Announce Type: new
Abstract: Most hyperparameter configurations for Evolvable-Substrate HyperNEAT (ES-HyperNEAT) produce networks that stagnate at random-guessing performance, wasting computational resources. We frame early stopping as binary classification on early fitness trajectories: for each trial, we compute the cumulative median of best-per-generation fitness and test it against a threshold derived by maximizing the F1 score on an initial 90-trial dataset. The resulting rule (generation G\* = 3, threshold T\* = 0.140) achieves F1 = 0.872 on 180 independent validation trials, retaining over 90% of successful trials while cutting computational cost by 41.6%. Compared to Hyperband, our domain-specific rule is 64% more efficient with higher mean fitness, though Hyperband occasionally discovers higher peak solutions. On a converged search population the rule becomes too aggressive (recall 31.1%), motivating adaptive thresholds. The specific thresholds are ES-HyperNEAT-specific, but the methodology, deriving stopping criteria from fitness dynamics classification, is applicable to other evolutionary algorithms with stagnation-prone hyperparameter spaces.
