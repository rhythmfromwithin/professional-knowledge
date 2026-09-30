---
title: "LOCO-AdaMP: Built-in LOCO Inference for Adaptive Minipatch Ensembles with Enhanced Prediction"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2609.36396
priority: medium
status: unread
interest: medium
next_step: skim
---
# LOCO-AdaMP: Built-in LOCO Inference for Adaptive Minipatch Ensembles with Enhanced Prediction
> 原文: [https://arxiv.org/abs/2609.36396](https://arxiv.org/abs/2609.36396)

arXiv:2609.36396v1 Announce Type: new
Abstract: As black-box machine learning models become increasingly common, extracting interpretations with uncertainty quantification has become a critical challenge. One popular type of interpretation is leave-one-covariate-out (LOCO) feature importance, while prior LOCO inference methods often require data-splitting or model-refitting. A recent ensemble framework, LOCO-MP, addresses these challenges using minipatches that subsample both observations and features, but massive feature subsampling can hurt prediction in high-dimensional sparse settings. Motivated by this limitation, we consider minipatch ensembles with adaptive feature sampling guided by LOCO importance, and propose LOCO-AdaMP, which enables free LOCO inference for the resulting adaptive minipatch ensemble. We show that LOCO-AdaMP yields substantially improved predictive models while retaining asymptotically valid feature importance inference without data-splitting, despite the complex dependence between the adaptive sampling distribution and the LOCO importance statistics. Our analysis relies on a careful leave-two-out perturbation bound for the iteratively updated sampling probabilities together with the stability of LOCO scores induced by observation subsampling. Empirical results on synthetic and real datasets demonstrate advantages of LOCO-AdaMP over existing methods in predictive performance, inferential power, and stability. Overall, LOCO-AdaMP provides a flexible ensemble framework (agnostic to base models) that delivers both strong predictive performance and asymptotically valid, powerful feature importance inference for regression.
