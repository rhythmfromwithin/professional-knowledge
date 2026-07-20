---
interest: medium
link: https://arxiv.org/abs/2607.14194
next_step: skim
priority: medium
slack_ts: '1784519278.044949'
source: cs.CV - Computer Vision
status: unread
title: Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video
  Models
---
# Inference-Time Concept Suppression and Video-Centric Evaluation for Text-to-Video Models
> 原文: [https://arxiv.org/abs/2607.14194](https://arxiv.org/abs/2607.14194)

arXiv:2607.14194v1 Announce Type: new
Abstract: Text-to-video (T2V) generators can synthesize realistic and temporally coherent videos, but controllably removing a target concept from a generator remains difficult.
Unlike text-to-image concept erasure, T2V unlearning must suppress a target concept that may persist across frames while preserving non-target subjects, actions, scenes, and temporal structure.
We propose \textbf{SIRUS}, a training-free inference-time framework for concept-level T2V unlearning.
Given textual aliases of a target concept, SIRUS localizes target-related prompt evidence and suppresses target expression during sampling, without updating the text encoder or denoising network.
We further introduce a video-oriented evaluation framework for T2V unlearning that separately measures target forgetting, non-target preservation, video quality, jailbreak robustness, and efficiency, using video-level failure criteria, frame-level residue statistics, paired preservation analysis, VBench-based quality diagnostics, and deployment overhead measurement.
Across five safety, object, and style concepts on CogVideoX, SIRUS reaches 70.4\% average forgetting success and 25.7\% average frame hit, compared with 44.4\% / 47.2\% for VideoEraser, while reducing the average VBench quality drop from -0.043 to -0.016, yielding the strongest forgetting-quality trade-off among fully evaluated baselines.
Transfer experiments on Wan2.2 further suggest that SIRUS generalizes across modern T2V backbones.
