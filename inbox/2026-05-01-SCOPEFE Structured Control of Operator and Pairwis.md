---
interest: medium
link: https://arxiv.org/abs/2604.27025
next_step: skim
priority: medium
slack_ts: '1777780639.444189'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: 'SCOPE-FE: Structured Control of Operator and Pairwise Exploration for Feature
  Engineering'
---
# SCOPE-FE: Structured Control of Operator and Pairwise Exploration for Feature Engineering
> 原文: [https://arxiv.org/abs/2604.27025](https://arxiv.org/abs/2604.27025)

arXiv:2604.27025v1 Announce Type: new
Abstract: Automatic feature engineering is an effective approach for improving predictive performance in tabular learning. However, expand-and-reduce methods, such as OpenFE, become increasingly computationally expensive as the input dimensionality grows. This limitation arises primarily from the combinatorial explosion of candidate features generated through operator-feature combinations. To address this issue, we propose SCOPE-FE, a structured search space control framework that improves efficiency by reducing the candidate space prior to feature generation. SCOPE-FE jointly regulates two major sources of combinatorial growth: the operator space and feature-pair space. First, OperatorProbing estimates the dataset-specific utility of candidate operators and eliminates low-contribution operators in advance. Second, FeatureClustering employs spectral embedding and fuzzy c-means clustering to group structurally related features, thereby restricting candidate generation to relevant within-cluster combinations. In addition, we introduce ReliabilityScoring, which incorporates variance across subsamples to stabilize pruning decisions. Experiments on ten benchmark datasets demonstrate that SCOPE-FE substantially reduces feature engineering time while maintaining competitive predictive performance relative to existing baselines. The efficiency gains are particularly pronounced for high-dimensional datasets. These results indicate that structured control of the search space is an effective strategy for scalable automatic feature engineering. The code will be made publicly available upon acceptance.
