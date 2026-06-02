---
title: "HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.00271
priority: medium
status: unread
interest: medium
next_step: skim
---
# HeLoCo: Efficient asynchronous low-communication training under data and device heterogeneity
> 原文: [https://arxiv.org/abs/2606.00271](https://arxiv.org/abs/2606.00271)

arXiv:2606.00271v1 Announce Type: new
Abstract: Distributed Low-Communication (DiLoCo) training reduces communication overhead by allowing workers to perform multiple local optimization steps before sending pseudo-gradients to a global outer update. Its asynchronous variant further improves hardware utilization by removing synchronization barriers, but at the cost of stale pseudo-gradients computed from outdated model states. As a result, these updates can become misaligned with the current global optimization direction, particularly in heterogeneous systems. This issue becomes even more pronounced when data are non-IID, a setting that has not been well studied in asynchronous low-communication training. To address this limitation, we propose \textbf{HeLoCo}, a direction-aware correction method for asynchronous low-communication training that uses outer momentum as a reference for the current optimization trajectory and selectively adjusts incoming pseudo-gradients before the outer update. Updates that remain aligned are preserved, while directionally conflicting components are corrected. On multilingual language-model training with heterogeneous workers and non-IID data, HeLoCo consistently improves validation loss. It outperforms existing asynchronous DiLoCo-based baselines by up to 7.5\% at a fixed token budget, exceeds asynchronous momentum look-ahead by up to 3.3\% at a fixed wall-clock budget, and surpasses the synchronous baseline by up to 22.1\% under severe system heterogeneity. Our analysis further shows how staleness, worker speed, and data heterogeneity shape update quality and convergence in highly decentralized and heterogeneous training setups.
