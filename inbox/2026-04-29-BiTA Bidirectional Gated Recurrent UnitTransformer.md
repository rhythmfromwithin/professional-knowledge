---
title: "BiTA: Bidirectional Gated Recurrent Unit-Transformer Aggregator in a Temporal Graph Network Framework for Alert Prediction in Computer Networks"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.22781
priority: high
status: unread
interest: medium
next_step: skim
---
# BiTA: Bidirectional Gated Recurrent Unit-Transformer Aggregator in a Temporal Graph Network Framework for Alert Prediction in Computer Networks
> 原文: [https://arxiv.org/abs/2604.22781](https://arxiv.org/abs/2604.22781)

arXiv:2604.22781v1 Announce Type: new
Abstract: Proactive alert prediction in computer networks is critical for mitigating evolving cyber threats and enabling timely defensive actions. Temporal Graph Neural Networks (TGNs) provide a principled framework for modeling time-evolving interactions; however, existing TGN-based methods predominantly rely on unidirectional or single-mechanism temporal aggregation, which limits their ability to capture recursive, multi-scale temporal patterns commonly observed in real-world attack behaviors. In this paper, we propose BiTA, a Bidirectional Gated Recurrent Unit-Transformer Aggregator for temporal graph learning. Rather than introducing a deeper or higher-capacity model, BiTA redesigns the temporal aggregation function within the TGN framework by jointly encoding bidirectional sequential dependencies and long-range contextual relations over each node's temporal neighborhood. This aggregation strategy enables complementary temporal reasoning at different scales while preserving the original TGN memory and message-passing structure. We evaluate BiTA on real-world alert datasets, demonstrating significant improvements in key performance metrics such as area under the curve, average precision, mean reciprocal rank, and per-category prediction accuracy when compared to state-of-the-art temporal graph models. BiTA outperforms baseline methods under both transductive and inductive settings, highlighting its robustness and generalization capabilities in dynamic network environments. BiTA is a scalable and interpretable framework for real-time cyber threat anticipation, paving the way toward more intelligent and adaptive intrusion detection systems.
