---
interest: medium
link: https://arxiv.org/abs/2607.08773
next_step: skim
priority: high
slack_ts: '1784085264.300449'
source: cs.AI - Artificial Intelligence
status: unread
title: Interval Certifications for Multilayered Perceptrons via Lattice Traversal
---
# Interval Certifications for Multilayered Perceptrons via Lattice Traversal
> 原文: [https://arxiv.org/abs/2607.08773](https://arxiv.org/abs/2607.08773)

arXiv:2607.08773v1 Announce Type: new
Abstract: In this work we present a rigorous theoretical framework to a foundational problem of AI safety, namely adversarial robustness. In particular, we show that the adversarial robustness problem can be reduced to a lattice traversal problem. Each element of this lattice corresponds to an interval, i.e., an axis-aligned hyper-rectangle, containing an input point $\mathbf{x}$. Consider a multilayered perceptron classifier (MLP). An interval $I$ constitutes a sound certification if $\mathbf{x} \in I$ and $\mathbf{x}$ can be freely perturbed in $I$ without changing the MLP's prediction. Complementarily, an interval $I$ constitutes a complete certification if $\mathbf{x} \in I$ and when $\mathbf{x}$ moves outside of $I$ the MLP's prediction is guaranteed to change. While the sound certification problem corresponds to the well-studied adversarial robustness, complete certifications have not been examined in the literature. We develop lattice traversal operators, which we apply in a refine & verify iterative scheme. Using formal MLP verifiers, sound maximality and complete minimality are guaranteed. Moreover, we examine objective optimization problems. There we discover some interesting asymmetries. For complete certifications, the minimum solution is obtained in polynomial oracle calls. This does not hold for sound certifications, where we prove strong intractability results. Additionally, we examine optimization problems in symmetric intervals (i.e., $\ell\_\infty$-spheres), where we provide logarithmic algorithms. Finally, we present an empirical evaluation, using the novel ParallelepipedoNN system.
