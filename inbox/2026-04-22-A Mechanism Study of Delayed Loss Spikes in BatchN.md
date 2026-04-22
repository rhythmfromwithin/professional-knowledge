---
interest: medium
link: https://arxiv.org/abs/2604.16809
next_step: skim
priority: medium
slack_ts: '1776828596.593319'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: A Mechanism Study of Delayed Loss Spikes in Batch-Normalized Linear Models
---
# A Mechanism Study of Delayed Loss Spikes in Batch-Normalized Linear Models
> 原文: [https://arxiv.org/abs/2604.16809](https://arxiv.org/abs/2604.16809)

arXiv:2604.16809v1 Announce Type: new
Abstract: Delayed loss spikes have been reported in neural-network training, but existing theory mainly explains earlier non-monotone behavior caused by overly large fixed learning rates. We study one stylized hypothesis: normalization can postpone instability by gradually increasing the effective learning rate during otherwise stable descent. To test this hypothesis at theorem level, we analyze batch-normalized linear models. Our flagship result concerns whitened square-loss linear regression, where we derive explicit no-rising-edge and delayed-onset conditions, bound the waiting time to directional onset, and show that the rising edge self-stabilizes within finitely many iterations. Combined with a square-loss decomposition, this yields a concrete delayed-spike mechanism in the whitened regime. For logistic regression, under highly restrictive active-margin assumptions, we prove only a supporting finite-horizon directional precursor in a knife-edge regime, with an optional appendix-only loss lower bound under an extra non-degeneracy condition. The paper should therefore be read as a stylized mechanism study rather than a general explanation of neural-network loss spikes. Within that scope, the results isolate one concrete delayed-instability pathway induced by batch normalization.
