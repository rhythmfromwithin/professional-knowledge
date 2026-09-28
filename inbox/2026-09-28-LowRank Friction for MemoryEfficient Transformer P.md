---
interest: medium
link: https://arxiv.org/abs/2609.30342
next_step: skim
priority: medium
slack_ts: '1790571563.811669'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Low-Rank Friction for Memory-Efficient Transformer Pretraining
---
# Low-Rank Friction for Memory-Efficient Transformer Pretraining
> 原文: [https://arxiv.org/abs/2609.30342](https://arxiv.org/abs/2609.30342)

arXiv:2609.30342v1 Announce Type: new
Abstract: iKFAD is a recently proposed optimiser that replaces adaptive learning rates with adaptive friction in the momentum dynamics, yet performs as well as Adam. Its limitation is that the full friction tensor $\xi\in\mathbb{R}^{m\times n}$ carries the same $\mathcal{O}(mn)$ memory overhead per layer as Adam's second-moment buffer. Here we replace iKFAD's friction tensor $\xi$ with a rank-1 outer-product factorisation built from row and column momentum statistics, resulting in Rank-1 iKFAD (R-iKFAD). This reduces the friction memory footprint from $\mathcal{O}(mn)$ to $\mathcal{O}(m+n)$ per layer, which approximately halves iKFAD's total optimiser state. Despite this reduction, R-iKFAD maintains parity in performance with iKFAD: experiments on GPT2-Nano, TinyViT, DistilBERT and GPT2-S confirm that it matches or exceeds iKFAD while nearly halving the memory footprint and remaining comparably robust to hyperparameters. We analyse the continuous-time dynamics in two damping regimes. For linear damping ($\gamma>0$) we prove exponential convergence under strong convexity. For $\gamma=0$, the preferred option in our experiments, the friction is generated entirely from past momentum and switches off as the momentum vanishes, so geometric convergence cannot be shown. We nonetheless prove convergence to the minimiser, together with matching upper and lower bounds on the energy: of order $t^{-1}$ when the regularisation scale $\epsilon\_{\mathrm{stab}}$ is zero, and of order $t^{-1/2}$ when it is positive. To our knowledge this is the first convergence rate for a rank-1 factored optimiser in continuous time, and the first such result that does not require positive damping.
