---
interest: medium
link: https://arxiv.org/abs/2606.02623
next_step: skim
priority: low
slack_ts: '1780633550.023249'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Oscillatory State-Space Models as Inductive Biases for Physics-Informed Neural
  PDE Solvers
---
# Oscillatory State-Space Models as Inductive Biases for Physics-Informed Neural PDE Solvers
> 原文: [https://arxiv.org/abs/2606.02623](https://arxiv.org/abs/2606.02623)

arXiv:2606.02623v1 Announce Type: new
Abstract: Solving time-dependent partial differential equations (PDEs) is an important problem in computational science and engineering. Physics-informed neural networks (PINNs) learn PDE solutions from governing equations. However, accurately capturing temporal evolution remains challenging. Recent sequence-model-based approaches parameterize time evolution using general-purpose sequence models, which capture temporal dependencies but do not explicitly encode the structured dynamics of PDE solutions. In addition, their memory requirements can scale unfavorably with sequence length and resolution, limiting applicability in large-scale or high-dimensional settings. This work introduces a PINN approach that incorporates oscillatory state-space dynamics to represent the modal structure of PDE solutions. The proposed method leverages a linear-oscillator-based temporal evolution, together with a PDE-aware spectral basis in space. This design enables closed-form spatial differentiation and consistent enforcement of boundary conditions. The method is evaluated on forward, inverse, and high-dimensional PDE problems, including cases up to 100 spatial dimensions. The results show improved accuracy and reduced memory usage compared to recent sequence-model-based PINN approaches. Overall, this work highlights the benefits of incorporating structured dynamical priors into the temporal evolution of neural PDE solvers and suggests designing more physics-aligned and computationally efficient PINN architectures.
