---
interest: medium
link: https://arxiv.org/abs/2610.00149
next_step: skim
priority: low
slack_ts: '1791091835.307439'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Per-Node Activation Function Evolution in Indirectly Encoded Substrates: Solvability,
  Limits, and Emergent Diversity'
---
# Per-Node Activation Function Evolution in Indirectly Encoded Substrates: Solvability, Limits, and Emergent Diversity
> 原文: [https://arxiv.org/abs/2610.00149](https://arxiv.org/abs/2610.00149)

arXiv:2610.00149v1 Announce Type: new
Abstract: Biological neurons achieve computational diversity through specialized types: tonic, bursting, adapting, and fast-spiking cells coexist within the same circuit. Artificial neural networks, by contrast, apply a single activation function uniformly to all nodes, which limits what they can represent. We show that this uniformity creates hard limits for evolutionary search: across sparse evolved substrates, monotonic functions fail to solve parity beyond its smallest instance, XOR, while a single oscillatory unit suffices at all tested scales. The gap is one of search and sparsity, not representation: monotonic networks can represent parity with a modest number of hidden units, and gradient descent recovers that solution. We evolve, to our knowledge for the first time in indirect encoding, per-node activation function assignments from an 18-function palette across more than 4,500 experimental runs spanning Boolean logic, regression, and spatial classification.
Testing each of the 18 functions individually on Parity-4 reveals a three-tier solvability structure: oscillatory functions achieve 100%, intermediate functions 6.7-80%, and all 9 monotonic functions 0%. This divide is not universal. Recurrence collapses it, and gradient descent inverts it entirely, showing that the barrier is specific to evolutionary search in sparse substrates. What activation functions a network can use, beyond its topology and weights, determines what evolutionary search can solve. Indirect encoding discovers heterogeneous per-node activation assignments unlikely to be chosen by hand.
