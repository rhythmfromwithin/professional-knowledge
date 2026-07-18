---
interest: medium
link: https://arxiv.org/abs/2607.13042
next_step: skim
priority: high
slack_ts: '1784344397.039959'
source: cs.LG - Machine Learning
status: unread
title: 'Automatic Differentiation from Scratch: How PyTorch Computes Gradients in
  Physics-Informed Neural Networks'
---
# Automatic Differentiation from Scratch: How PyTorch Computes Gradients in Physics-Informed Neural Networks
> 原文: [https://arxiv.org/abs/2607.13042](https://arxiv.org/abs/2607.13042)

arXiv:2607.13042v1 Announce Type: new
Abstract: This paper traces, with explicit numerical values, how PyTorch's automatic differentiation (AD) engine computes gradients for Physics-Informed Neural Network (PINN) training -- a setting that requires two levels of differentiation: computing the physics derivative $\hat{y}'(t)=d\hat{y}/dt$ through the network, and computing parameter gradients $\nabla\_\theta L$ of a loss that itself depends on $\hat{y}'(t)$. Using a 1-3-3-1 multilayer perceptron and the initial value problem $y'(t)+y(t)=0$, $y(0)=1$, we trace the complete pipeline at every node: the computational graph built during the forward pass, the reverse-mode backward traversal that computes all 22 parameter gradients in a single pass, and the graph-on-graph mechanism by which \texttt{create\\_graph=True} enables correct differentiation through the physics-informed residual. Every adjoint value is verified against the hand derivations of Tahimi (2026), connecting the $P/Q$ sensitivity framework to the vector--Jacobian products used by PyTorch's autograd engine.
