---
interest: medium
link: https://arxiv.org/abs/2606.19587
next_step: skim
priority: medium
slack_ts: '1781847256.267019'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: A Solver-Free Training Method for Predict-then-Optimize
---
# A Solver-Free Training Method for Predict-then-Optimize
> 原文: [https://arxiv.org/abs/2606.19587](https://arxiv.org/abs/2606.19587)

arXiv:2606.19587v1 Announce Type: new
Abstract: We propose a scalable method for training prediction (machine learning) models in the predict-then-optimize paradigm, where model outputs serve as coefficients for a subsequent linear optimization task. Directly minimizing the empirical decision regret is intractable for linear programming and combinatorial optimization since the decision mapping is piecewise constant, and the gradients are zero almost everywhere. While existing methods address this by smoothing the differentiation process, they suffer from scalability issues, since a computationally expensive solver call is required for every gradient evaluation. To address this, we propose a decision-focused learning pipeline based on a measure transformation principle, which yields a new surrogate loss that is completely optimization-solver-free during training. We establish theoretical guarantees, including Fisher consistency and excess risk bounds. Empirically, our method achieves decision quality competitive with state-of-the-art methods while reducing training time by orders of magnitude.
