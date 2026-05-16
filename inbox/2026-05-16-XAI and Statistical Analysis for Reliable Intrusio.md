---
title: "XAI and Statistical Analysis for Reliable Intrusion Detection in the UAVIDS-2025 Dataset: From Tree to Hybrid and Tabular DNN Ensembles"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.13922
priority: low
status: unread
interest: medium
next_step: skim
---
# XAI and Statistical Analysis for Reliable Intrusion Detection in the UAVIDS-2025 Dataset: From Tree to Hybrid and Tabular DNN Ensembles
> 原文: [https://arxiv.org/abs/2605.13922](https://arxiv.org/abs/2605.13922)

arXiv:2605.13922v1 Announce Type: new
Abstract: During the last few years, the term Mechanistic Interpretability, a specific area, under the umbrella of explainable artificial intelligence (XAI), has been introduced, to explain the decisions made by complex machine learning (ML) models in critical systems like UAV intrusion detection systems (UAVIDS). In this paper, we apply best-practices for data pre-processing and examine a wide range of tree-ensembles, deep neural networks, hybrid stacking models and the latest ensemble neural networks to detect intrusions in UAV, with stratified 10-fold cross validation. With our top-performing model, XGBoost, we proceed to Shapley Additive explanations (SHAP), to analyze the global and local feature importances and understand which features, each attack targets, to mimic normal traffic and where the misclassifications occur. Furthermore a distribution analysis follows, by visually comparing violin plots and the curves of kernel density estimations. With the Westfall-Young permutation test for multiple comparisons, the Bandwidth optimization of the KDEs and the selection of Jensen-Shannon Distance for the test, we discover the true causes of false predictions, observed in Wormhole and Blackhole attacks in UAVIDS-2025. The findings provide robust, reliable and explainable models for UAV intrusion detection, along with statistical insights, which capture and clarify the masked nature of the attacks, regarding the challenge of Density Support Intersection, between these attacks, in this dataset.
