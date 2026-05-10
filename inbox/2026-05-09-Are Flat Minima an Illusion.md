---
interest: medium
link: https://arxiv.org/abs/2605.05209
next_step: skim
priority: high
slack_ts: '1778385544.991369'
source: cs.LG - Machine Learning
status: unread
title: Are Flat Minima an Illusion?
---
# Are Flat Minima an Illusion?
> 原文: [https://arxiv.org/abs/2605.05209](https://arxiv.org/abs/2605.05209)

arXiv:2605.05209v1 Announce Type: new
Abstract: Neural networks that land in flat regions of the loss landscape tend to generalise better than those in sharp regions. Sharpness-Aware Minimisation exploits this to improve generalisation. But function-preserving reparameterisation can inflate the Hessian of any minimum by two orders of magnitude without changing a single prediction. If the geometry of weight space can be manufactured from nothing, it cannot be the cause of anything. In other words, flat is simple and simplicity depends on encoding. Here I show that the actual driver is weakness, the volume of completions compatible with the learned function in the learner's embodied language. Weakness is reparameterisation-invariant because it is defined over what the network \emph{does}, not how it is parameterised. I prove weakness is minimax-optimal under exchangeable demands, and that PAC-Bayes bounds work because they correlate with it. On MNIST, the large-batch generalisation advantage \emph{vanishes} as training data grows, from $+1.6\%$ at $n = 2{,}000$ to $+0.02\%$ at $n = 60{,}000$. A quantity whose predictive power depends on how much data you have is not a cause but a confounder. I run head-to-heads on 100 networks with identical architecture and training. For MNIST weakness predicts generalisation ($\rho = +0.374$, $p = 0.00012$), sharpness anticorrelates ($\rho = -0.226$) and simplicity predicts nothing ($p = 0.848$). For Fashion-MNIST ($\rho = +0.384$, $p = 8.15 \times 10^{-5}$), though simplicity is at least somewhat predictive there. Simplicity is dataset dependent, whereas weakness is invariant. Flat minima were never the answer.
