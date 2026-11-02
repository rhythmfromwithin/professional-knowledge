---
interest: medium
link: https://arxiv.org/abs/2610.40728
next_step: skim
priority: high
slack_ts: '1793597878.129059'
source: cs.LG - Machine Learning
status: unread
title: Bayesian Distribution System State Estimation with Flow Matching
---
# Bayesian Distribution System State Estimation with Flow Matching
> 原文: [https://arxiv.org/abs/2610.40728](https://arxiv.org/abs/2610.40728)

arXiv:2610.40728v1 Announce Type: new
Abstract: Medium-voltage feeders have few real-time measurements, so distribution system state estimation (DSSE) rests on pseudo-measurements of the secondary substations, a prior in Bayesian terms. Weighted least squares keeps the power flow exact but reduces this prior to a mean and variance, while supervised deep learning estimators also learn the power flow and are tied to one measurement set. We propose PoSE (posterior sampling for state estimation), which keeps the Bayesian structure of DSSE and learns only what the distribution system operator does not know, namely the distribution of substation injections, modelled by a neural network trained with flow matching on historical data. The power flow equations, grid topology and measurements enter only at sampling, through a noise-aware Kalman-type correction. The neural network therefore never approximates the power flow, but every posterior sample is a physically consistent operating point, and one trained prior serves any measurement set, noise level and topology. On the IEEE 33-bus feeder, PoSE lowers the probabilistic injection error (CRPS) by 6.7-7.5% against a full-covariance Gaussian prior in all 12 tested settings. It provides reliable uncertainty: the 90% intervals contain the true injection almost exactly as often as exact posterior samples would, whereas those of supervised estimators contain it in only 37-78% of cases. On the 240-bus unbalanced three-phase Iowa feeder, it gives the lowest injection, voltage and branch-current errors of all estimators. A fast variant matches this accuracy at 0.2-0.6s per snapshot and, without retraining, beats Gaussian priors and retrained supervised estimators on seven reconfigured topologies.
