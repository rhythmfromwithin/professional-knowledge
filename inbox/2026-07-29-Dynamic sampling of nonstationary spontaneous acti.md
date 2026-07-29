---
title: "Dynamic sampling of non-stationary spontaneous activity in dissociated neuronal networks"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2607.24269
priority: low
status: unread
interest: medium
next_step: skim
---
# Dynamic sampling of non-stationary spontaneous activity in dissociated neuronal networks
> 原文: [https://arxiv.org/abs/2607.24269](https://arxiv.org/abs/2607.24269)

arXiv:2607.24269v1 Announce Type: new
Abstract: Objective. To develop and evaluate an adaptive electrode-selection method for tracking non-stationary spontaneous activity during long-term high-density microelectrode array (HD-MEA) recordings under a fixed channel budget.
Approach. We formulated electrode allocation as a sequential subset-selection problem and used a discounted Poisson-Gamma model with Thompson sampling. The method updated electrode-specific activity estimates from observed spike counts and reallocated a fixed channel budget over time. We evaluated it by offline replay of nine 34 h HD-MEA recordings, selecting 100 electrodes from 529 densely routed candidates, and in a representative online recording using 1,024 routed electrodes.
Main results. Across offline recordings, the top 100 active-electrode set changed substantially, reaching 47.8% turnover at 34 h. The Bayesian method captured the largest fraction of the spikes available to an oracle selector among the tested strategies and exceeded static selection by 17.2 percentage points at the final time point. In the online recording, adaptive selection captured the first synchronized burst and supported center-of-activity trajectory analysis.
Significance. Uncertainty-aware exploration and temporal discounting can improve HD-MEA recording efficiency under fixed readout constraints, providing a basis for adaptive sensing of evolving neural activity.
