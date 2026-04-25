---
title: "Micro-DualNet: Dual-Path Spatio-Temporal Network for Micro-Action Recognition"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.21011
priority: medium
status: unread
interest: medium
next_step: skim
---
# Micro-DualNet: Dual-Path Spatio-Temporal Network for Micro-Action Recognition
> 原文: [https://arxiv.org/abs/2604.21011](https://arxiv.org/abs/2604.21011)

arXiv:2604.21011v1 Announce Type: new
Abstract: Micro-actions are subtle, localized movements lasting 1-3 seconds such as scratching one's head or tapping fingers. Such subtle actions are essential for social communication, ubiquitously used in natural interactions, and thus critical for fine-grained video understanding, yet remain poorly understood by current computer vision systems. We identify a fundamental challenge: micro-actions exhibit diverse spatio-temporal characteristics where some are defined by spatial configurations while others manifest through temporal dynamics. Existing methods that commit to a single spatio-temporal decomposition cannot accommodate this diversity. We propose a dual-path network that processes anatomically-grounded spatial entities through parallel Spatial-Temporal (ST) and Temporal-Spatial (TS) pathways. The ST path captures spatial configurations before modeling temporal dynamics, while the TS path inverts this order to prioritize temporal dynamics. Rather than fixed fusion, we introduce entity-level adaptive routing where each body part learns its optimal processing preference, complemented by Mutual Action Consistency (MAC) loss that enforces cross-path coherence. Extensive experiments demonstrate competitive performance on MA-52 dataset and state-of-the-art results on iMiGUE dataset. Our work reveals that architectural adaptation to the inherent complexity of micro-actions is essential for advancing fine-grained video understanding.
