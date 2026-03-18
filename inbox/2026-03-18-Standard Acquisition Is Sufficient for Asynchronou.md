---
title: "Standard Acquisition Is Sufficient for Asynchronous Bayesian Optimization"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.13501
priority: medium
status: unread
interest: medium
next_step: skim
---
# Standard Acquisition Is Sufficient for Asynchronous Bayesian Optimization
> 原文: [https://arxiv.org/abs/2603.13501](https://arxiv.org/abs/2603.13501)

arXiv:2603.13501v1 Announce Type: new
Abstract: Asynchronous Bayesian optimization is widely used for gradient-free optimization in domains with independent parallel experiments and varying evaluation times. Existing methods posit that standard acquisitions lead to redundant and repeated queries, proposing complex solutions to enforce diversity in queries. Challenging this fundamental premise, we show that methods, like the Upper Confidence Bound, can in fact achieve theoretical guarantees essentially equivalent to those of sequential Thompson sampling. A conceptual analysis of asynchronous Bayesian optimization reveals that existing works neglect intermediate posterior updates, which we find to be generally sufficient to avoid redundant queries. Further investigation shows that by penalizing busy locations, diversity-enforcing methods can over-explore in asynchronous settings, reducing their performance. Our extensive experiments demonstrate that simple standard acquisition functions match or outperform purpose-built asynchronous methods across synthetic and real-world tasks.
