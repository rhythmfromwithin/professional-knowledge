---
interest: medium
link: https://arxiv.org/abs/2605.23048
next_step: skim
priority: low
slack_ts: '1779856026.149599'
source: cs.HC - Human-Computer Interaction
status: unread
title: 'StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing'
---
# StanBKT: Rethinking Parameter Estimation in Bayesian Knowledge Tracing
> 原文: [https://arxiv.org/abs/2605.23048](https://arxiv.org/abs/2605.23048)

arXiv:2605.23048v1 Announce Type: new
Abstract: Bayesian Knowledge Tracing (BKT) is a widely used and interpretable student modeling approach in intelligent tutoring systems and educational data mining. However, most implementations rely on expectation-maximization or related optimization methods that yield only point estimates, limiting uncertainty quantification and principled comparisons across learners and conditions. We introduce StanBKT, an open-source Python package for estimating BKT models using Bayesian inference in Stan. StanBKT provides a unified framework supporting Hamiltonian Monte Carlo, variational inference, Pathfinder, and optimization-based estimation while preserving the hidden Markov structure and interpretability of classical BKT. It supports standard, grouped, and hierarchical BKT models, flexible prior specification, posterior predictive inference, and utilities for visualization and diagnostics. We evaluate StanBKT on large-scale observational and controlled educational datasets. On the ASSISTments 2020 dataset, we show that supported inference methods achieve comparable predictive performance while differing in computational efficiency and posterior fidelity. We further demonstrate how posterior inference enables principled comparison of condition-specific parameters in an educational intervention involving perceptual cue manipulations. Results illustrate how uncertainty quantification facilitates more reliable interpretation of differences in learning, forgetting, guessing, and slipping parameters across experimental conditions. Overall, StanBKT extends BKT beyond point estimation by providing a flexible framework for probabilistic student modeling, uncertainty quantification, and hierarchical inference in educational data mining.
