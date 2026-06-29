---
interest: medium
link: https://arxiv.org/abs/2606.27797
next_step: skim
priority: medium
slack_ts: '1782708429.771939'
source: cs.DC - Distributed Computing
status: unread
title: Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation
  on HPC Systems
---
# Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems
> 原文: [https://arxiv.org/abs/2606.27797](https://arxiv.org/abs/2606.27797)

arXiv:2606.27797v1 Announce Type: new
Abstract: Knowledge Distillation (KD) enables training smaller student models under the guidance of larger teacher models, and the widely adopted TRL library implements it. Yet, TRL treats both models symmetrically, missing opportunities to exploit their pronounced asymmetry in memory footprint, and communication requirements. This paper presents an HPC-aware methodology for KD that decouples teacher and student partitioning efficiently. Our approach achieves up to 67% higher samples-per-second than TRL by avoiding unnecessary teacher-model data structures and selecting the best split strategy. We combine vertical and horizontal partitioning of models, deriving an analytical expression that identifies the existence of inflection points between splitting regimes. These results showed that exploiting teacher--student asymmetry through topology-aware parallelism notably accelerated GKD training on production HPC clusters at our company
