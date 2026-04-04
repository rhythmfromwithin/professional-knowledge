---
interest: medium
link: https://arxiv.org/abs/2603.29597
next_step: skim
priority: low
slack_ts: '1775270895.273569'
source: q-bio.NC - Neurons and Cognition
status: unread
title: Structural and dynamical strategies to prevent runaway excitation in reservoir
  computing
---
# Structural and dynamical strategies to prevent runaway excitation in reservoir computing
> 原文: [https://arxiv.org/abs/2603.29597](https://arxiv.org/abs/2603.29597)

arXiv:2603.29597v1 Announce Type: new
Abstract: Reservoirs, typically implemented as recurrent neural networks with fixed random connection weights, can be combined with a simple trained readout layer to perform a wide range of computational tasks. However, increasing the magnitude of reservoir connection weights to exploit nonlinear dynamics can cause the network to develop strong spontaneous activity that drives neurons into saturation, dramatically degrading performance. In this work, we investigate two distinct countermeasures against such runaway excitation. The first approach introduces a subtle non-homogeneous structure into the matrix of connection weigths $w\_{ij}$, without altering the overall probability distribution $p(w)$. We identify several favorable structuring principles, such as creating a small subset of neurons with weaker-than-average input connections. Even if the rest of the reservoir falls into runaway saturating behavior, this weakly coupled subset remains in a mildly nonlinear regime whose dynamics can still be exploited by the readout layer. The second approach implements a form of automatic gain control, in which a dedicated control unit dynamically regulates the reservoir's average global activation toward an optimal setpoint. Although the control unit modulates the excitability of the reservoir only via a global gain factor, this mechanism substantially enlarges the dynamical regime favorable for computation and renders performance largely independent of the underlying connection statistics.
