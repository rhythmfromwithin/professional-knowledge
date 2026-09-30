---
interest: medium
link: https://arxiv.org/abs/2609.30271
next_step: skim
priority: high
slack_ts: '1790745123.416039'
source: cs.LG - Machine Learning
status: unread
title: 'When the Preconditioning Exponent Turns Negative: Learning-Rate Coupling and
  Cross-Environment Generalization'
---
# When the Preconditioning Exponent Turns Negative: Learning-Rate Coupling and Cross-Environment Generalization
> 原文: [https://arxiv.org/abs/2609.30271](https://arxiv.org/abs/2609.30271)

arXiv:2609.30271v1 Announce Type: new
Abstract: Adaptive optimizers are commonly parameterized by a fixed power of the second-moment estimate. Existing partially adaptive methods study exponents between momentum-like updates and the standard Adam square root, while the interaction between this exponent and the global learning rate is less understood. We perform a controlled cross-environment study using a paired four-environment classification problem with stable sparse features, environment-dependent spurious sparse features, dense features, and high-dimensional noise. Across \NumRuns{} source-training runs covering 21 preconditioning exponents $p\in[-0.5,0.5]$ and five learning rates $\eta\in[10^{-4},10^{-2}]$, we find that the exponent maximizing cross-environment accuracy decreases almost linearly with $\log\_{10}\eta$. The fitted slopes range from $-0.270$ to $-0.300$, with $R^2$ between $0.972$ and $0.996$. At $\eta=10^{-2}$, source-validation selection still prefers positive exponents in all four environments, whereas cross-environment and worst-environment criteria prefer negative exponents. Checkpoint decomposition shows that lower $p$ reduces the learned spurious-to-stable and noise-to-stable weight ratios; under reversed correlation, it also reduces the magnitude of the harmful spurious margin. Negative $p$ is therefore not a universally optimal setting. It is a high-step-size allocation regime produced by the joint action of learning rate and preconditioning. The study also exposes a model-selection conflict: source-domain validation systematically selects a different preconditioning regime from the one that maximizes robustness to environmental change. The results are a single-seed, finite-budget mechanism study rather than a broad benchmark claim.
