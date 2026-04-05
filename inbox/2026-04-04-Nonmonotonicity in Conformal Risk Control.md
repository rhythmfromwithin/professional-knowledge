---
interest: medium
link: https://arxiv.org/abs/2604.01502
next_step: skim
priority: medium
slack_ts: '1775359533.249499'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Non-monotonicity in Conformal Risk Control
---
# Non-monotonicity in Conformal Risk Control
> 原文: [https://arxiv.org/abs/2604.01502](https://arxiv.org/abs/2604.01502)

arXiv:2604.01502v1 Announce Type: new
Abstract: Conformal risk control (CRC) provides distribution-free guarantees for controlling the expected loss at a user-specified level. Existing theory typically assumes that the loss decreases monotonically with a tuning parameter that governs the size of the prediction set. This assumption is often violated in practice, where losses may behave non-monotonically due to competing objectives such as coverage and efficiency.
We study CRC under non-monotone loss functions when the tuning parameter is selected from a finite grid, a common scenario in thresholding or discretized decision rules. Revisiting a known counterexample, we show that the validity of CRC without monotonicity depends on the relationship between the calibration sample size and the grid resolution. In particular, risk control can still be achieved when the calibration sample is sufficiently large relative to the grid.
We provide a finite-sample guarantee for bounded losses over a grid of size $m$, showing that the excess risk above the target level $\alpha$ is of order $\sqrt{\log(m)/n}$, where $n$ is the calibration sample size. A matching lower bound shows that this rate is minimax optimal. We also derive refined guarantees under additional structural conditions, including Lipschitz continuity and monotonicity, and extend the analysis to settings with distribution shift via importance weighting.
Numerical experiments on synthetic multilabel classification and real object detection data illustrate the practical impact of non-monotonicity. Methods that account for finite-sample deviations achieve more stable risk control than approaches based on monotonicity transformations, while maintaining competitive prediction-set sizes.
