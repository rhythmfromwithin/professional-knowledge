---
interest: medium
link: https://arxiv.org/abs/2605.05436
next_step: skim
priority: medium
slack_ts: '1778472598.830229'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Estimating Implicit Regularization in Deep Learning
---
# Estimating Implicit Regularization in Deep Learning
> 原文: [https://arxiv.org/abs/2605.05436](https://arxiv.org/abs/2605.05436)

arXiv:2605.05436v1 Announce Type: new
Abstract: Deep learning systems are known to exhibit implicit regularization (alt. implicit bias), favoring simple solutions instead of merely minimizing the loss function. In some cases, we can analytically derive the implicit regularization -- connecting it to an equivalent penalty that augments the learning objective. However, modern deep learning systems are complex, carrying modifications to the training procedure and architecture (e.g. early stopping, minibatching, dropout) whose effects are not always directly interpretable. Although estimating the resulting implicit regularization could aid theorists in algorithm design and practitioners in interpreting their hyperparameter choices, this problem has received little direct attention. It is also tractable: regularization makes weight updates deviate from loss gradients, promising a signal for identifying implicit bias. Here we provide gradient matching methods that can be used to empirically estimate the implicit regularization. Our method works on networks with known regularization, recovering popular explicit penalties like $\ell\_1$ and $\ell\_2$. It also replicates known implicit effects, like the quadratic weight penalty induced by early stopping in gradient descent, demonstrating that it can be used to test theories of implicit regularization. Crucially, because our method is empirical, it can handle implicit regularization in arbitrary networks. We demonstrate this use by characterizing the effects of dropout in deep networks, showing implicit $\ell\_2$ effects in this popular method. Our work shows that practitioners can use gradient matching to understand regularization in networks with implicit biases that are too complicated to derive analytically.
