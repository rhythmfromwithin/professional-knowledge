---
title: "Transfer learning for causal forest"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2606.07693
priority: medium
status: unread
interest: medium
next_step: skim
---
# Transfer learning for causal forest
> 原文: [https://arxiv.org/abs/2606.07693](https://arxiv.org/abs/2606.07693)

arXiv:2606.07693v1 Announce Type: new
Abstract: Transfer learning addresses the challenge of transfering knowledge from one domain to another. Traditional transfer learning focuses on adapting models trained on a source domain (with a lot of observations) to improve performance on a target domain (with few observations). In this work we consider the case of a model shift and we focus on the transfer learning applied to a causal forest namely HTERF. This causal forest aims to estimate the Conditional Average Treatment Effect (CATE). The approach considered is the offset method presented by Wang (2016) adapted to a causal context. This method relies on the use of intermediate models in order to estimate the offset between source and target distributions. Our main result is a bound on the CATE error of HTERF on target depending on the error of the intermediate models. Simulation studies show the good performances of this approach in different settings on simulations and on a real-world dataset.
