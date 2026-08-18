---
title: "Robust XGBoosting for Regression"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2608.13590
priority: high
status: unread
interest: medium
next_step: skim
---
# Robust XGBoosting for Regression
> 原文: [https://arxiv.org/abs/2608.13590](https://arxiv.org/abs/2608.13590)

arXiv:2608.13590v1 Announce Type: new
Abstract: XGBoost is a very popular and powerful method for prediction. It iteratively fits simple decision trees to the residuals of the previous step. An efficient and scalable implementation is available. The standard loss function for XGBoost is the quadratic loss, but a Huber loss can also be used. In this paper, we study the robustness of XGBoost and show that its performance can be affected by vertical outliers and leverage points. To address this, we explore alternative loss functions, based on M-, S-, and {\tau} -estimators from robust regression. Our results indicate that a two-step procedure, referred to as MM-XGBoost, provides the best trade-off between robustness and prediction accuracy.
