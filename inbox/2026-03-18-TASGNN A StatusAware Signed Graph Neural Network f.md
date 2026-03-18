---
title: "TAS-GNN: A Status-Aware Signed Graph Neural Network for Anomaly Detection in Bitcoin Trust Systems"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.13290
priority: low
status: unread
interest: medium
next_step: skim
---
# TAS-GNN: A Status-Aware Signed Graph Neural Network for Anomaly Detection in Bitcoin Trust Systems
> 原文: [https://arxiv.org/abs/2603.13290](https://arxiv.org/abs/2603.13290)

arXiv:2603.13290v1 Announce Type: new
Abstract: Decentralized financial platforms rely heavily on Web of Trust reputation systems to mitigate counterparty risk in the absence of centralized identity verification. However, these pseudonymous networks are inherently vulnerable to adversarial behaviors, such as Sybil attacks and camouflaged fraud, where malicious actors cultivate artificial reputations before executing exit scams. Traditional anomaly detection in this domain faces two critical limitations. First, reliance on naive statistical heuristics (e.g., flagging the lowest 5% of rated users) fails to distinguish between victims of bad-mouthing attacks and actual fraudsters. Second, standard Graph Neural Networks (GNNs) operate on the assumption of homophily and cannot effectively process the semantic inversion inherent in signed (trust vs. distrust) and directed (status) edges. We propose TAS-GNN (Topology-Aware Signed Graph Neural Network), a novel framework designed for feature-sparse signed networks like Bitcoin-Alpha. TAS-GNN integrates recursive Web-of-Trust labeling and a dual-channel message-passing architecture that separately models trust and distrust signals, fused through a Status-Aware Attention mechanism. Experiments demonstrate that TAS-GNN achieves state-of-the-art performance, significantly outperforming existing signed GNN baselines.
