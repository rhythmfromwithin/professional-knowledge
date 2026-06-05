---
interest: medium
link: https://arxiv.org/abs/2606.02596
next_step: skim
priority: high
slack_ts: '1780633550.791209'
source: cs.LG - Machine Learning
status: unread
title: 'Spectral Asymptotics of Neural Network Loss Landscapes: An Exact Decomposition
  of the Curvature Exponent'
---
# Spectral Asymptotics of Neural Network Loss Landscapes: An Exact Decomposition of the Curvature Exponent
> 原文: [https://arxiv.org/abs/2606.02596](https://arxiv.org/abs/2606.02596)

arXiv:2606.02596v1 Announce Type: new
Abstract: The curvature exponent $\alpha$ in $h\_k \propto \sigma\_k^\alpha$ -- governing how Hessian eigenvalues scale with gradient singular values -- varies systematically across layer types ($\alpha \approx 2$ for convolutions, $\approx 1$ for transformer attention, $< 1$ for MLP up-projections). Why? We prove the Spectral Alignment Decomposition: $\alpha = 2 + d\log\Phi\_k / d\log\sigma\_k$, where $\Phi\_k$ measures alignment between Kronecker factor eigenbases and gradient singular directions. This reduces "why does $\alpha$ vary?" to a geometric question we answer for LayerNorm, residual connections, and softmax heads. The decomposition implies a spectral transfer identity $s = \alpha\gamma$ linking curvature exponent, effective gradient rank-decay $\gamma$, and Hessian decay exponent $s$. The identity is algebraic; its empirical content is that $\alpha$ and $\gamma$, fit on independent data (HVPs vs. SVD), recover $s$ to ~2% median error across 93 layers, five architectures, and three datasets -- with no free parameters. A zeta-function bound on participation ratio shows curvature concentrates onto effectively one direction per layer. As a proof of concept, we derive the architecture-adaptive preconditioner $T(\sigma;\alpha)$ and show that Spectral Newton -- implementing $T$ in the gradient singular basis -- outperforms AdamW on vision benchmarks where $\alpha \approx 2$.
