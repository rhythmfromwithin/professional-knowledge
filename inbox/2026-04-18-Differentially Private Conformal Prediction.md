---
title: "Differentially Private Conformal Prediction"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.14621
priority: medium
status: unread
interest: medium
next_step: skim
---
# Differentially Private Conformal Prediction
> 原文: [https://arxiv.org/abs/2604.14621](https://arxiv.org/abs/2604.14621)

arXiv:2604.14621v1 Announce Type: new
Abstract: Conformal prediction (CP) has attracted broad attention as a simple and flexible framework for uncertainty quantification through prediction sets. In this work, we study how to deploy CP under differential privacy (DP) in a statistically efficient manner. We first introduce differential CP, a non-splitting conformal procedure that avoids the efficiency loss caused by data splitting and serves as a bridge between oracle CP and private conformal inference. By exploiting the stability properties of DP mechanisms, differential CP establishes a direct connection to oracle CP and inherits corresponding validity behavior. Building on this idea, we develop Differentially Private Conformal Prediction (DPCP), a fully private procedure that combines DP model training with a private quantile mechanism for calibration. We establish the end-to-end privacy guarantee of DPCP and investigate its coverage properties under additional regularity conditions. We further study the efficiency of both differential CP and DPCP under empirical risk minimization and general regression models, showing that DPCP can produce tighter prediction sets than existing private split conformal approaches under the same privacy budget. Numerical experiments on synthetic and real datasets demonstrate the practical effectiveness of the proposed methods.
