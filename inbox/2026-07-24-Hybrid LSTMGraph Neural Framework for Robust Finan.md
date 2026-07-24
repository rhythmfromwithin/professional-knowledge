---
title: "Hybrid LSTM-Graph Neural Framework for Robust Financial Fraud Detection and Adversarial Resilience"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2607.19350
priority: high
status: unread
interest: medium
next_step: skim
---
# Hybrid LSTM-Graph Neural Framework for Robust Financial Fraud Detection and Adversarial Resilience
> 原文: [https://arxiv.org/abs/2607.19350](https://arxiv.org/abs/2607.19350)

arXiv:2607.19350v1 Announce Type: new
Abstract: Financial institutions face significant challenges in detecting sophisticated money laundering patterns, such as smurfing and layering, due to extreme data imbalance (0.13% fraud rate) and evolving adversarial evasion tactics. This paper proposes FraudShield AI, a hybrid framework that integrates Long Short-Term Memory (LSTM) networks with hand-crafted Graph Topological Features to capture both temporal sequences and structural relational context. By engineering network-centric features including PageRank Centrality, In-Degree dynamics, and a custom Flow Ratio, the system shifts the detection paradigm from isolated transaction analysis to network-level forensics. A Focal Loss objective is used to address class imbalance, and a dynamic thresholding mechanism is introduced to improve resilience against low-value smurfing attacks. Experimental evaluation on the PaySim dataset shows that the proposed hybrid model substantially outperforms Logistic Regression and XGBoost baselines in Precision, Recall, and F1-Score, particularly on hard-to-detect micro-transaction fraud patterns. An ablation study confirms the complementary contribution of both the temporal and topological components.
