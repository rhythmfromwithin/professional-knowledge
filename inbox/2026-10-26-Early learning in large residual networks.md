---
interest: medium
link: https://arxiv.org/abs/2610.31783
next_step: skim
priority: medium
slack_ts: '1793076019.605739'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Early learning in large residual networks
---
# Early learning in large residual networks
> 原文: [https://arxiv.org/abs/2610.31783](https://arxiv.org/abs/2610.31783)

arXiv:2610.31783v1 Announce Type: new
Abstract: We study the early training dynamics of nonlinear residual networks with blocks of zero hidden layers as a model of more general residual networks. We analyze networks in a sequential limit where first width and depth diverge, then the number of training data points diverges, and finally the input dimension diverges. This is a more refined setup compared to the typical mean-field theory analysis in which depth and width diverge but the number of training datapoints and input dimension are fixed. Our main technical result is a diagrammatic computation of both the network output and the hidden representations after the few steps of gradient descent in terms of the statistics of inner products of inputs from the training set. One of our principle conceptual findings is a negative result: in the limit of large input dimension the network output can learn only a linear function of its inputs early in training since higher learned monomials are more and more suppressed in the input dimension and vanish in the large dimension limit. This suggests that mean-field limits of ResNets are surprisingly rigid in the regime of high input dimension and may not be sufficient toy models for understanding feature learning. Finally, we investigate how to ensure hyperparameter transfer for the learning rate as a function of dataset size and input dimension. We test our predictions numerically and find excellent agreement with our theory.
