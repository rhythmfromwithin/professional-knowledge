---
interest: medium
link: https://arxiv.org/abs/2606.30930
next_step: skim
priority: medium
slack_ts: '1782880936.887339'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'SGD at the Edge of Stability: Stochastic Stabilization with Large Learning
  Rates'
---
# SGD at the Edge of Stability: Stochastic Stabilization with Large Learning Rates
> 原文: [https://arxiv.org/abs/2606.30930](https://arxiv.org/abs/2606.30930)

arXiv:2606.30930v1 Announce Type: new
Abstract: Modern deep learning has been shown to operate at the edge of stability, routinely using learning rates far larger than those justified by classical optimization theory. Most prior analyses of the edge of stability phenomenon focus on deterministic gradient descent, leaving the stochastic setting largely unexplored. In this work, we provide sharp convergence guarantees for Stochastic Gradient Descent (SGD) applied to the multiclass cross-entropy loss, for both linear classifiers and two-layer neural networks. We show that the stochasticity of SGD may cause the dynamics to alternate between an edge-of-stability regime that is dominated by curvature-driven oscillations, and a stable regime in which the expected loss decreases at a controlled rate. Despite that, we prove that SGD self-stabilizes the dynamics, ensuring that the iterates return to stability in a fixed number of iterations and allowing convergence in the best-iterate sense even with large learning rates. Experiments validate our theoretical findings and illustrate the benefits of SGD in the large-stepsize regime.
