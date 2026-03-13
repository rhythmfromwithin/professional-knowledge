---
interest: medium
link: https://arxiv.org/abs/2603.05538
next_step: skim
priority: high
slack_ts: '1773369843.585559'
source: cs.LG - Machine Learning
status: unread
title: 'JAWS: Enhancing Long-term Rollout of Neural Operators via Spatially-Adaptive
  Jacobian Regularization'
---
# JAWS: Enhancing Long-term Rollout of Neural Operators via Spatially-Adaptive Jacobian Regularization
> 原文: [https://arxiv.org/abs/2603.05538](https://arxiv.org/abs/2603.05538)

arXiv:2603.05538v1 Announce Type: new
Abstract: Data-driven surrogate models improve the efficiency of simulating continuous dynamical systems, yet their autoregressive rollouts are often limited by instability and spectral blow-up. While global regularization techniques can enforce contractive dynamics, they uniformly damp high-frequency features, introducing a contraction-dissipation dilemma. Furthermore, long-horizon trajectory optimization methods that explicitly correct drift are bottlenecked by memory constraints. In this work, we propose Jacobian-Adaptive Weighting for Stability (JAWS), a probabilistic regularization strategy designed to mitigate these limitations. By framing operator learning as Maximum A Posteriori (MAP) estimation with spatially heteroscedastic uncertainty, JAWS dynamically modulates the regularization strength based on local physical complexity. This allows the model to enforce contraction in smooth regions to suppress noise, while relaxing constraints near singular features to preserve gradients, effectively realizing a behavior similar to numerical shock-capturing schemes. Experiments demonstrate that this spatially-adaptive prior serves as an effective spectral pre-conditioner, which reduces the base operator's burden of handling high-frequency instabilities. This reduction enables memory-efficient, short-horizon trajectory optimization to match or exceed the long-term accuracy of long-horizon baselines. Evaluated on the 1D viscous Burgers' equation, our hybrid approach improves long-term stability, shock fidelity, and out-of-distribution generalization while reducing training computational costs.
