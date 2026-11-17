---
interest: medium
link: https://arxiv.org/abs/2611.17503
next_step: skim
priority: medium
slack_ts: '1794900947.570479'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Multifidelity Operator Inference for Dynamical Systems
---
# Multifidelity Operator Inference for Dynamical Systems
> 原文: [https://arxiv.org/abs/2611.17503](https://arxiv.org/abs/2611.17503)

arXiv:2611.17503v1 Announce Type: new
Abstract: This paper presents a multifidelity (MF) formulation of Operator Inference (OpInf) for learning non-intrusive, physics-based reduced-order models (ROMs) of nonlinear dynamical systems. OpInf learns reduced operators from projections of snapshot data by solving a least squares regression problem. However, generating high-fidelity snapshots can be computationally expensive, limiting parameter coverage and the temporal extent of training trajectories for many aerospace applications, which can lead to inaccurate or unstable ROM predictions. This work proposes MF-OpInf, which combines limited high-fidelity snapshots with more plentiful low-fidelity snapshots through a control-variates-inspired MF least squares formulation to learn a single set of reduced operators across multiple trajectories. Low-fidelity trajectories provide additional parameter coverage and extend beyond the high-fidelity training time horizon. The low-fidelity snapshots are also used to construct an improved reduced basis through weighted proper orthogonal decomposition. We demonstrate MF-OpInf on a nonlinear reaction-diffusion problem with parametrized sinusoidal forcing and a two-dimensional incompressible flow past a cylinder with a parametrized inlet pulse. In these experiments, under an equal training simulation budget, MF-OpInf reduces the mean relative prediction error at unseen parameters by up to $87\%$ for the reaction-diffusion problem and $28\%$ for the cylinder flow problem over the test time regime, which extends beyond the high-fidelity training time horizon. These results demonstrate that MF-OpInf can improve temporal extrapolation and prediction at unseen parameters without increasing the training simulation budget.
