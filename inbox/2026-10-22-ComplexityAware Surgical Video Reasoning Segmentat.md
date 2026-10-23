---
interest: medium
link: https://arxiv.org/abs/2610.28776
next_step: skim
priority: medium
slack_ts: '1792729425.073179'
source: cs.CV - Computer Vision
status: unread
title: Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and
  Context Memory
---
# Complexity-Aware Surgical Video Reasoning Segmentation with Digital Twin and Context Memory
> 原文: [https://arxiv.org/abs/2610.28776](https://arxiv.org/abs/2610.28776)

arXiv:2610.28776v1 Announce Type: new
Abstract: Conventional surgical segmentation relies on closed-set categories or explicit text queries, which cannot resolve implicit queries that require reasoning about workflows, instrument functions, and temporal relationships. To address these limitations, we propose SurgReasonSeg, a complexity-aware method that brings reasoning segmentation over digital twin (DT) representations to surgical video. Specifically, SurgReasonSeg constructs DT representations from surgical foundation models and trains two low-rank adapters (LoRA) of one large language model with reinforcement learning (RL), each specialized for a different query complexity. A lightweight router, also trained with RL, selects between the two adapters to balance latency against accuracy. SurgReasonSeg also sets the temporal context with an adaptive sliding window conditioned on query complexity and workflow phase, and retrieves relevant historical cases from a surgical context memory by workflow similarity and procedural relevance. We further introduce EndoVis-ReasonSeg, a surgical reasoning segmentation benchmark with 1,460 training and 961 test samples across semantic, spatial, and temporal categories. On EndoVis-ReasonSeg, SurgReasonSeg improves J&F over the strongest baseline, ReSurgSAM2, by 0.178, 0.237, and 0.297 on semantic, spatial, and temporal queries, and it also achieves the best results on the Ref-EndoVis17 and Ref-EndoVis18 referring segmentation benchmarks. A backbone-matched attribution protocol separates the contribution of the upstream segmenter from that of the reasoning modules. Our method runs at 18.8 FPS averaged over the query distribution, enabling real-time reasoning segmentation in surgical videos.
