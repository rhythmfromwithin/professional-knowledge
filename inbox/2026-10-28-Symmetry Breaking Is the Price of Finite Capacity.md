---
title: "Symmetry Breaking Is the Price of Finite Capacity"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.36138
priority: medium
status: unread
interest: medium
next_step: skim
---
# Symmetry Breaking Is the Price of Finite Capacity
> 原文: [https://arxiv.org/abs/2610.36138](https://arxiv.org/abs/2610.36138)

arXiv:2610.36138v1 Announce Type: new
Abstract: If rotating a problem never changes its answer, one might expect its best model to be rotation-invariant; we show that this fails, predictably and by an exact amount, when capacity is limited. A symmetry groups a model's directions into blocks of equally strong directions, a symmetric model must use each block whole, and when the budget cuts a block every optimal model breaks the symmetry. For a Gaussian problem with a $k$-unit bilinear predictor, the log-loss price of symmetry is exactly $(U\_k-I\_k)/(2\sigma^2)$, the signal of the best $k$ directions minus that of the best whole blocks. Because an attention head compares tokens through a similarity of rank at most its head dimension, whatever computation precedes it, the same price governs heads fitted to a symmetric similarity by squared error, and heads trained this way on three-dimensional directions break symmetry at exactly the predicted head dimensions, with the predicted rotation sensitivity (RMSE 0.004). Under softmax attention, flatter attention restores the predicted symmetric head where tested, while with peaked attention broken heads beat every whole-shell symmetric head at 16 of 20 head dimensions. We give a procedure that separates capacity-driven breaking from other causes.
