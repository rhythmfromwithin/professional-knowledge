---
interest: medium
link: https://arxiv.org/abs/2609.36227
next_step: skim
priority: medium
slack_ts: '1790745149.156049'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: One-Step Next-Latent Prediction Is Not a World Model
---
# One-Step Next-Latent Prediction Is Not a World Model
> 原文: [https://arxiv.org/abs/2609.36227](https://arxiv.org/abs/2609.36227)

arXiv:2609.36227v1 Announce Type: new
Abstract: Next-latent prediction fits a map from the current embedding to the next one. LeNEPA carries this objective to time series, replacing the stop-gradient of next-embedding prediction with the isotropy penalty of LeJEPA. A world model is a transition kernel that can be rolled out. The one-step regression identifies a conditional mean, and a mean is a kernel only in special cases. For a linear-Gaussian Markov latent, the mean transition and the innovation covariance are fixed by the one-step problem, and the open-loop squared error at horizon $K$ equals the trace of the sum of the pushed-forward innovation covariances. That error grows with $K$ after the one-step fit is exact. If the conditional mean is nonlinear, composing it is not the multi-step conditional mean. If the observation is a non-injective function of a Markov state, a memoryless one-step map does not determine future observations, while a short window can. An isotropy penalty is a function of the embedding marginal, so its partial derivative in the transition weights is zero. On a scalar autoregression with coefficient $0.9$, the one-step mean squared error is $0.998$ and the $16$-step open-loop error is $5.10$. On a hidden rotation, an eight-step window reaches $16$-step error $0.056$, while the current scalar alone reaches $0.778$. Raising the isotropy weight from $0.1$ to $10$ leaves eight-step latent error inside $[0.78,0.85]$ on three seeds.
