---
title: "A Simple State Space Model Excels at Multivariate Time Series Classification"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.27406
priority: high
status: unread
interest: medium
next_step: skim
---
# A Simple State Space Model Excels at Multivariate Time Series Classification
> 原文: [https://arxiv.org/abs/2605.27406](https://arxiv.org/abs/2605.27406)

arXiv:2605.27406v1 Announce Type: new
Abstract: Structured state space models (SSMs) have recently emerged as a promising foundation for sequence modeling, with Mamba-based architectures demonstrating strong performance through input-dependent state transitions, albeit at considerable complexity. However, their application to time-series classification (TSC) has been largely limited to Mamba-style architectures, leaving the broader SSM design space underexplored. We present the first systematic study spanning diagonal SSMs (S4D) and input-dependent SSMs (Mamba family) on large-scale TSC benchmarks, asking whether such complexity is necessary for top performance. Our results reveal a surprising finding: S4D consistently outperforms Mamba-based variants in both accuracy and efficiency, challenging the assumption that increased complexity translates to meaningful gains in TSC. Building on this, we introduce MS4, lightweight modifications to S4D via a linear input projection and channel-mixing mechanism, and MS4N, a normalized variant that stabilizes state dynamics with negligible overhead. Evaluated on 59 datasets across MONSTER (up to 60 million samples, 50K timesteps, 82 classes) and the UEA benchmark, against 15 baselines, MS4 and MS4N consistently outperform Mamba-based models while remaining more efficient, and MS4N matches or surpasses competing deep learning models that are roughly 2x and 10x larger in parameters. These results position lightweight structured SSMs as a compelling alternative to scaling complexity for TSC.
