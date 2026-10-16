---
title: "Empirical Evaluation of Machine Learning for Cloud Cryptojacking Detection: Effects of Preprocessing and Evaluation Protocols"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.20658
priority: low
status: unread
interest: medium
next_step: skim
---
# Empirical Evaluation of Machine Learning for Cloud Cryptojacking Detection: Effects of Preprocessing and Evaluation Protocols
> 原文: [https://arxiv.org/abs/2610.20658](https://arxiv.org/abs/2610.20658)

arXiv:2610.20658v1 Announce Type: new
Abstract: Artificial intelligence (AI) has been widely applied to cloud cryptojacking detection. Classical machine learning models remain among the most widely used approaches for cloud cryptojacking detection. This paper presents an empirical evaluation of six widely used classical machine learning models for AI-based cloud cryptojacking detection under different preprocessing and evaluation settings. Because no public cloud-native cryptojacking dataset is currently available, experiments were conducted using two publicly available proxy datasets, DS2OS and NSL-KDD. The evaluated models include Random Forest, XGBoost, LightGBM, Gradient Boosting, Decision Tree, and K-Nearest Neighbors (KNN). Experimental results show that preprocessing choices and evaluation protocols have a measurable impact on model performance. On DS2OS, removing identifier-related features reduced the accuracy of most models to approximately 96%, while KNN achieved higher accuracy with lower attack recall. On NSL-KDD, models obtained 77 to 80\% accuracy on the official test set containing unseen attack types, compared with above 99.5% under a random train-test split. Attack-class precision, recall, and Matthews Correlation Coefficient (MCC) further provide complementary insights into classifier performance beyond overall accuracy. The results provide an empirical comparison of commonly used classical machine learning models under consistent experimental settings and offer insights into how preprocessing, dataset selection, and evaluation methodology influence reported performance.
