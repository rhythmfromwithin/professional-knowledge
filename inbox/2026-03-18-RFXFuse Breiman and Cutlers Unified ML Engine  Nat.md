---
title: "RFX-Fuse: Breiman and Cutler's Unified ML Engine + Native Explainable Similarity"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.13234
priority: high
status: unread
interest: medium
next_step: skim
---
# RFX-Fuse: Breiman and Cutler's Unified ML Engine + Native Explainable Similarity
> 原文: [https://arxiv.org/abs/2603.13234](https://arxiv.org/abs/2603.13234)

arXiv:2603.13234v1 Announce Type: new
Abstract: Breiman and Cutler's original Random Forest was designed as a unified ML engine -- not merely an ensemble predictor. Their implementation included classification, regression, unsupervised learning, proximity-based similarity, outlier
detection, missing value imputation, and visualization -- capabilities that modern libraries like scikit-learn never implemented. RFX-Fuse (Random Forests X [X=compression] -- Forest Unified Learning and Similarity Engine) delivers
Breiman and Cutler's complete vision with native GPU/CPU support. Modern ML pipelines require 5+ separate tools -- XGBoost for prediction, FAISS for similarity, SHAP for explanations, Isolation Forest for outliers, custom code for
importance. RFX-Fuse provides a 1 to 2 model object alternative -- a single set of trees grown once. Novel Contributions: (1) Proximity Importance -- native explainable similarity: proximity measures that samples are similar;
proximity importance explains why. (2) Dataset-specific imputation validation for general tabular data -- ranking imputation methods by how real the imputed data looks, without ground truth labels.
