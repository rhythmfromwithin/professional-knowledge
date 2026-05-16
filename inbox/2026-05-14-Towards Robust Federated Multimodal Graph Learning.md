---
interest: medium
link: https://arxiv.org/abs/2605.12584
next_step: skim
priority: high
slack_ts: '1778903333.208029'
source: cs.LG - Machine Learning
status: unread
title: Towards Robust Federated Multimodal Graph Learning under Modality Heterogeneity
---
# Towards Robust Federated Multimodal Graph Learning under Modality Heterogeneity
> 原文: [https://arxiv.org/abs/2605.12584](https://arxiv.org/abs/2605.12584)

arXiv:2605.12584v1 Announce Type: new
Abstract: Recently, multimodal graph learning (MGL) has garnered significant attention for integrating diverse modality information and structured context to support various network applications. However, real-world graphs are often isolated due to data-sharing limitations across multiple parties, and their modalities are frequently incomplete. This highlights an urgent need to develop a robust federated approach. However, we find that existing methods remain insufficient. On the one hand, centralized MGL methods that handle missing modalities overlook the knowledge sharing and generalization in federated scenarios. On the other hand, while federated MGL methods have become increasingly mature, they primarily target non-graph data. Based on these technologies, we identify a two-stage pipeline wherein client-side completion reconstructs missing modalities, and server-side aggregation integrates the client-updated parameters of both the modality generator and the backbone models. Although this serves as a general solution, we identify two primary challenges in achieving greater robustness: (1) Topology-Isolated Local Completion: Client-side modality generation struggles to effectively leverage global semantics. (2) Reliability-Imbalanced Global Aggregation: Server-side multi-party collaboration is hindered by client updates with varying modality availability and recovery reliability. To address these challenges, we propose \textsc{FedMPO}, which utilizes topology-aware cross-modal generation to recover missing features using comprehensive graph context, missing-aware expert routing to locally filter out noisy recovered signals, and reliability-aware aggregation to appropriately down-weight unreliable updates. Extensive experiments on 3 tasks across 6 datasets demonstrate that FedMPO outperforms baselines, achieving performance gains of up to 4.10% and 5.65% in high-missing and non-IID settings.
