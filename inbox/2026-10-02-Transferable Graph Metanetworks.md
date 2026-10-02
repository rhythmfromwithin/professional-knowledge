---
title: "Transferable Graph Metanetworks"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.00420
priority: medium
status: unread
interest: medium
next_step: skim
---
# Transferable Graph Metanetworks
> 原文: [https://arxiv.org/abs/2610.00420](https://arxiv.org/abs/2610.00420)

arXiv:2610.00420v1 Announce Type: new
Abstract: A weight space network (or metanetwork) takes the weights of another neural network as input and predicts properties of it. Most prior work trains such models on input networks of one or a few fixed sizes and evaluates them in-distribution. The few attempts at out-of-distribution size generalization remain limited in scope and have achieved only modest success. Consequently, the potential efficiency gains of training on small networks and evaluating on much larger ones remain largely unrealized. We propose Transferable Graph Metanetworks, which extend the graph metanetwork paradigm with a set of modifications that make performance transferable across input networks of different widths. The modifications follow two principles: invariance to the ways in which networks of different widths represent the same function, and continuity, such that weights representing similar functions receive similar predictions. We further study whether size generalization is possible for input networks trained independently from random initialization. Empirically, our modifications significantly improve size generalization on every task we consider. Performance is strongest on input networks trained under the maximal-update parameterization ($\mu$P), where it remains robust up to $42\times$ the training width. Theoretically, we explain these observations with infinite-width limit theory: we prove size-generalization guarantees for our model on $\mu$P-trained inputs, and explain why it can fail under other parameterizations.
