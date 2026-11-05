---
interest: medium
link: https://arxiv.org/abs/2611.03652
next_step: skim
priority: high
slack_ts: '1793859287.178389'
source: cs.LG - Machine Learning
status: unread
title: Latent Cluster Separation as a Regularizer for Lifelong Anomaly Detection
---
# Latent Cluster Separation as a Regularizer for Lifelong Anomaly Detection
> 原文: [https://arxiv.org/abs/2611.03652](https://arxiv.org/abs/2611.03652)

arXiv:2611.03652v1 Announce Type: new
Abstract: Lifelong (continual) anomaly detection systems must learn a sequence of tasks without forgetting how to recognize anomaly types seen earlier -- a property known as backward transfer. A common way to try to improve backward transfer is to reshape a model's internal representation around learnable concept centroids, typically coupled with a new way of scoring anomalies based on distance to those centroids. Because these two design choices are usually introduced together, it is unclear which one is actually responsible for any performance gain. In this paper, we unbundle the two mechanisms within a VAE-based lifelong anomaly detector and study them separately. We find that used purely as a training-time regularizer -- while leaving anomaly scoring unchanged -- latent cluster separation can improve detection quality and backward transfer, though whether it outperforms the alternative scoring approach depends on the dataset's underlying representation. Switching to distance-based scoring is instead where most of the instability commonly associated with this class of method actually originates; we identify and explain the underlying mechanism. This benefit depends on the dataset's underlying representation, and we report this as practical guidance for choosing between the two design choices, rather than as a list of caveats.
