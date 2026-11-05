---
interest: medium
link: https://arxiv.org/abs/2611.03741
next_step: skim
priority: medium
slack_ts: '1793859281.720589'
source: cs.CV - Computer Vision
status: unread
title: 'Beyond Proposals: Region-Consistent Open-Set Object Detection'
---
# Beyond Proposals: Region-Consistent Open-Set Object Detection
> 原文: [https://arxiv.org/abs/2611.03741](https://arxiv.org/abs/2611.03741)

arXiv:2611.03741v1 Announce Type: new
Abstract: Open-set object detection (OSOD) suffers from a fundamental limitation under dense proposal mechanisms: highly overlapping proposals associated with the same object are often assigned contradictory known/unknown predictions. Existing methods perform open-set reasoning independently for each proposal, while ignoring the shared semantics among correlated proposals, resulting in fragmented detections and unstable open-set decisions. In this paper, we reformulate OSOD as an object-centric semantic inference problem, where correlated proposals jointly support a coherent region-level semantic decision. Based on this perspective, we propose OCSI-Net, a unified framework that combines object-centric semantic consistency with geometry-aware uncertainty stabilization. Specifically, OCSI-Net aggregates correlated proposals into structured region clusters and infers region-level semantics from aggregated semantic evidence, thereby enforcing coherent open-set predictions within the same object region. Furthermore, a geometry-aware uncertainty mechanism is introduced to stabilize optimization near open-set transition boundaries. Extensive experiments on multiple benchmarks demonstrate that OCSI-Net consistently achieves state-of-the-art performance, improving the harmonic mean of known and unknown detection by an average of 6.83\% over the second-best method.
