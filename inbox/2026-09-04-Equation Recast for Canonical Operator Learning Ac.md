---
interest: medium
link: https://arxiv.org/abs/2609.02982
next_step: skim
priority: high
slack_ts: '1788581043.282779'
source: cs.LG - Machine Learning
status: unread
title: Equation Recast for Canonical Operator Learning Across Parametric PDEs
---
# Equation Recast for Canonical Operator Learning Across Parametric PDEs
> 原文: [https://arxiv.org/abs/2609.02982](https://arxiv.org/abs/2609.02982)

arXiv:2609.02982v1 Announce Type: new
Abstract: Learning solution operators across broad parameter ranges can require substantial coverage of both input functions and physical parameters, particularly for purely data-driven parametric models. In addition, the resulting models may fail silently outside the training distribution. We introduce equation recast, which reformulates parametric operator learning as the learning of a single canonical operator. Parameter-induced operator variations are derived analytically from the governing equation and absorbed into effective sources, enabling zero-shot prediction across new parameter regimes. Across multi-parameter, nonlinear, and singular PDE settings, equation recast supports extrapolation, integrates sparse heterogeneous datasets in a shared canonical representation, and uses loss of convergence as an internal warning signal for failure of the recast iteration. In high-fidelity tokamak simulations for nuclear fusion, the framework unifies electron-temperature data across four device geometries through canonical-domain mapping within one jointly trained operator. Equation recast provides a route toward reusable neural PDE solvers combining equation-guided transfer, data efficiency, and monitorable inference.
