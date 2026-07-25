---
interest: medium
link: https://arxiv.org/abs/2607.20505
next_step: skim
priority: medium
slack_ts: '1784949903.609009'
source: cs.RO - Robotics
status: unread
title: 'HERMES: Heterogeneous Edge-Relational Multi-Head Embedded SSM Attention for
  Traffic Conflict Prediction at Signalized Intersections'
---
# HERMES: Heterogeneous Edge-Relational Multi-Head Embedded SSM Attention for Traffic Conflict Prediction at Signalized Intersections
> 原文: [https://arxiv.org/abs/2607.20505](https://arxiv.org/abs/2607.20505)

arXiv:2607.20505v1 Announce Type: new
Abstract: Surrogate safety measures (SSMs) enable proactive traffic safety assessment, but many existing methods evaluate pairwise interactions independently or flatten multi-agent scenes into fixed feature vectors, limiting their ability to represent heterogeneous interaction structure and evolving scene-level risk. This study formulates traffic conflict assessment as temporal heterogeneous scene-graph classification and proposes HERMES, a heterogeneous edge-relational graph neural network with SSM-informed multi-head attention. Vehicles and pedestrians are represented as heterogeneous nodes, while vehicle-vehicle, vehicle-pedestrian, and pedestrian-pedestrian interactions are encoded as relation-specific edges with continuous kinematic and surrogate-safety descriptors. Relation-specific attention, dynamic node-edge updates, safety-aware graph pooling, and temporal sequence learning are jointly used to estimate scene-level conflict probability. HERMES was evaluated using 109,028 trajectory-derived sequences from a signalized urban intersection and tested on an independently collected comparable intersection dataset. Enhanced HERMES achieved an AUC-ROC of 0.9898 +/- 0.0013, an AUC-PR of 0.9412 +/- 0.0067, and an F1 score of 0.8449 +/- 0.0103. At a 5% false-alarm rate, it detected 95.7% of conflict sequences, outperforming the strongest Transformer baseline and XGBoost. In zero-shot external evaluation, HERMES achieved an AUC-ROC of 0.9752 and an AUC-PR of 0.7829. Joint source-target training further improved target-site performance with limited target-site data. These findings show that preserving heterogeneous interaction topology, safety-informed edge semantics, and short-term temporal evolution improves scene-level conflict classification and supports transferable roadside safety monitoring at signalized intersections.
