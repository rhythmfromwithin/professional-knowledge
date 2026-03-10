---
title: "Machine Learning for Complex Systems Dynamics: Detecting Bifurcations in Dynamical Systems with Deep Neural Networks"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.04420
priority: high
status: unread
interest: medium
next_step: skim
---
# Machine Learning for Complex Systems Dynamics: Detecting Bifurcations in Dynamical Systems with Deep Neural Networks
> 原文: [https://arxiv.org/abs/2603.04420](https://arxiv.org/abs/2603.04420)

arXiv:2603.04420v1 Announce Type: new
Abstract: Critical transitions are the abrupt shifts between qualitatively different states of a system, and they are crucial to understanding tipping points in complex dynamical systems across ecology, climate science, and biology. Detecting these shifts typically involves extensive forward simulations or bifurcation analyses, which are often computationally intensive and limited by parameter sampling. In this study, we propose a novel machine learning approach based on deep neural networks (DNNs) called equilibrium-informed neural networks (EINNs) to identify critical thresholds associated with catastrophic regime shifts. Rather than fixing parameters and searching for solutions, the EINN method reverses this process by using candidate equilibrium states as inputs and training a DNN to infer the corresponding system parameters that satisfy the equilibrium condition. By analyzing the learned parameter landscape and observing abrupt changes in the feasibility or continuity of equilibrium mappings, critical thresholds can be effectively detected. We demonstrate this capability on nonlinear systems exhibiting saddle-node bifurcations and multi-stability, showing that EINNs can recover the parameter regions associated with impending transitions. This method provides a flexible alternative to traditional techniques, offering new insights into the early detection and structure of critical shifts in high-dimensional and nonlinear systems.
