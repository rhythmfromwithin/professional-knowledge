---
title: "Enhancing Web Application Firewalls with BERT-GNN for SQL Injection Detection"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.28882
priority: low
status: unread
interest: medium
next_step: skim
---
# Enhancing Web Application Firewalls with BERT-GNN for SQL Injection Detection
> 原文: [https://arxiv.org/abs/2608.28882](https://arxiv.org/abs/2608.28882)

arXiv:2608.28882v1 Announce Type: new
Abstract: Detecting sophisticated SQL Injection (SQLi) attacks remains among the most critical challenges in web applications security. This research study has resulted in an optimised hybrid BERT-GNN pipeline with improved detection accuracy and robustness while reducing false-positive and false-negative rates. SQL queries are tokenised and encoded into contextual BERT embeddings, which then initialise the node features of a Graph Neural Network (GNN) trained to classify each query, with the architecture tuned by Optuna over accuracy, precision, recall, and F1-score. The proposed model achieved 99.67% accuracy, with 99.71% precision, 99.39% recall, and 99.55% F1-score on the attack class. A sensitivity analysis, performed by perturbing graph inputs, further assessed the model robustness and yielded a low mean sensitivity score of 0.0037, indicating stable predictions under such perturbations. The results have demonstrated the potential of a novel hybrid model that couples BERT contextual understanding with the GNN structural modelling to detect sophisticated SQLi attack vectors. For open validation, the dataset, test sets and models are made available at https://github.com/mlily2024/Final-project-SQL-injection-pipeline.
