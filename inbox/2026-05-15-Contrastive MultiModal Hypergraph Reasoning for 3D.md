---
interest: medium
link: https://arxiv.org/abs/2605.13854
next_step: skim
priority: medium
slack_ts: '1778903340.194809'
source: cs.CV - Computer Vision
status: unread
title: Contrastive Multi-Modal Hypergraph Reasoning for 3D Crowd Mesh Recovery
---
# Contrastive Multi-Modal Hypergraph Reasoning for 3D Crowd Mesh Recovery
> 原文: [https://arxiv.org/abs/2605.13854](https://arxiv.org/abs/2605.13854)

arXiv:2605.13854v1 Announce Type: new
Abstract: Multi-person 3D reconstruction is pivotal for real-world interaction analysis, yet remains challenging due to severe occlusions and depth ambiguity. Current approaches typically rely on single-modality inputs, which inherently lack geometric guidance. Furthermore, these methods often reconstruct subjects in isolation, neglecting the collective group context essential for resolving ambiguities in crowded scenes. To address these limitations, we propose Contrastive Multi-modal Hypergraph Reasoning to synergize semantic, geometric, and pose cues for crowd reconstruction. We first initialize robust node representations by combining RGB features, geometric priors, and occlusion-aware incomplete poses. Additionally, we introduce a pelvis depth indicator as a global spatial anchor, aligning visual features with a metric-scale-agnostic depth ordering. Subsequently, we construct a shared-topology hypergraph that moves beyond pairwise constraints to model higher-order crowd dynamics. To improve feature fusion, we design a hypergraph-based contrastive learning scheme that jointly enhances intra-modal discriminability and enforces cross-modal orthogonality. This mechanism enables the network to propagate global context effectively, allowing it to infer missing information even under severe occlusion. Extensive experiments on the Panoptic and GigaCrowd benchmarks confirm that our method achieves new state-of-the-art performance. Code and pre-trained models are available at https://github.com/SunMH-try/CoMHR.
