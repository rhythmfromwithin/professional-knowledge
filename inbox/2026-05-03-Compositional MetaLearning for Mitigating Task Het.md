---
interest: medium
link: https://arxiv.org/abs/2604.26999
next_step: skim
priority: high
slack_ts: '1777866897.426519'
source: cs.AI - Artificial Intelligence
status: unread
title: Compositional Meta-Learning for Mitigating Task Heterogeneity in Physics-Informed
  Neural Networks
---
# Compositional Meta-Learning for Mitigating Task Heterogeneity in Physics-Informed Neural Networks
> 原文: [https://arxiv.org/abs/2604.26999](https://arxiv.org/abs/2604.26999)

arXiv:2604.26999v1 Announce Type: new
Abstract: Physics-informed neural networks (PINNs) approximate solutions of partial differential equations (PDEs) by embedding physical laws into the loss function. In parameterized PDE families, variations in coefficients or boundary/initial conditions define distinct tasks. This makes training individual PINNs for each task computationally prohibitive, while cross-task transfer can be sensitive to task heterogeneity. While meta-learning can reduce retraining cost, existing methods often rely on a single global initialization and may suffer from negative transfer, particularly under feature-scarce coordinate inputs and limited training-task availability. We propose the Learning-Affinity Adaptive Modular Physics-Informed Neural Network (LAM-PINN), a compositional framework that leverages task-specific learning dynamics. LAM-PINN combines PDE parameters with learning-affinity metrics from brief transfer sessions to construct a task representation and cluster tasks even with coordinate-only inputs. It decomposes the model into cluster-specialized subnetworks and a shared meta network, and learns routing weights to selectively reuse modules instead of relying on a single global initialization. Across three PDE benchmarks, LAM-PINN achieves an average 19.7-fold reduction in mean squared error (MSE) on unseen tasks using only 10% of the training iterations required by conventional PINNs. These results indicate its effectiveness for generalization to unseen configurations within bounded design spaces of parameterized PDE families in resource-constrained engineering settings.
