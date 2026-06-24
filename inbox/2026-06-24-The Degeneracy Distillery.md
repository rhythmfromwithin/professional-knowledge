---
interest: medium
link: https://arxiv.org/abs/2606.23838
next_step: skim
priority: medium
slack_ts: '1782274340.077579'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: The Degeneracy Distillery
---
# The Degeneracy Distillery
> 原文: [https://arxiv.org/abs/2606.23838](https://arxiv.org/abs/2606.23838)

arXiv:2606.23838v1 Announce Type: cross
Abstract: When two or more parameters or labels produce similar data, they are degenerate, or hard to distinguish. Degeneracies render both label prediction and inverse problems difficult, since both machine learning algorithms and probabilistic samplers rely on the distinguishability of data and its gradients with respect to parameters. However, identifying degeneracies in physical models or real-world datasets can be elucidating about the choice of model or the underlying process that produces the data. We present the degeneracy distillery, a method that (1) detects and (2) resolves degenerate parameter combinations (a) automatically and (b) symbolically, from parameter-data (or parameter-simulation) pairs alone, through estimation and flattening of the Fisher information matrix. By exploring the information geometry of the likelihood, we characterize degeneracies as an intrinsic property of the physical model, requiring no realised data observation. We demonstrate our approach on a range of synthetic and real-world problems, discovering symbolic coordinate transformations that identify the combinations of parameters of a model which yield independent effects on the data. The resulting coordinates flatten the Fisher information in expectation globally, in contrast to posterior-based methods that flatten only at a single point, and substantially reduce the simulation budget required for downstream neural posterior estimation. In test cases we require up to $10\times$ fewer simulations for posterior estimation at matched validation calibration whilst simultaneously gaining physical insight on the system.
