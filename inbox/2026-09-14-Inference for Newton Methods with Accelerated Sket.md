---
interest: medium
link: https://arxiv.org/abs/2609.12421
next_step: skim
priority: medium
slack_ts: '1789360373.329629'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Inference for Newton Methods with Accelerated Sketch-and-Project via Random
  Scaling
---
# Inference for Newton Methods with Accelerated Sketch-and-Project via Random Scaling
> 原文: [https://arxiv.org/abs/2609.12421](https://arxiv.org/abs/2609.12421)

arXiv:2609.12421v1 Announce Type: new
Abstract: We study an online sketched Newton method that approximates the Newton direction at each step via a state-of-the-art sketching solver, called the generalized accelerated sketch-and-project solver (GAS), thereby mitigating the computational bottleneck of classical second-order methods. The GAS solver improves upon vanilla, unaccelerated sketch-and-project solvers by achieving accelerated convergence through Nesterov momentum updates, and accommodates a flexible projection metric whose proper choice further reduces computational cost. Building on this design, we establish asymptotic normality of the averaged sketched Newton iterates and characterize their limiting covariance matrix. The resulting covariance recovers that of the unaccelerated sketched Newton method under a specific choice of acceleration parameters, converges more rapidly (in the number of sketching steps) to the minimax-optimal covariance in general, and is smaller than that of the last iterate produced by the accelerated method. Finally, we strengthen these results by establishing a functional central limit theorem for the Newton iterates, which allows us to bypass explicit covariance estimation and develop an online inference procedure based on random scaling. Specifically, we construct a pivotal test statistic by appropriately rescaling the averaged iterates, so that its limiting distribution is free of any unknown parameters, enabling asymptotically valid online inference. Numerical experiments demonstrate superior performance of the proposed inference procedure.
