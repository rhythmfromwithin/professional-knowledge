---
interest: medium
link: https://arxiv.org/abs/2611.03775
next_step: skim
priority: medium
slack_ts: '1793859284.156119'
source: cs.CV - Computer Vision
status: unread
title: 'FlowRig: Unified Skeleton Generation for 3D and 4D Meshes via Flow Matching'
---
# FlowRig: Unified Skeleton Generation for 3D and 4D Meshes via Flow Matching
> 原文: [https://arxiv.org/abs/2611.03775](https://arxiv.org/abs/2611.03775)

arXiv:2611.03775v1 Announce Type: new
Abstract: Automatic rigging is a fundamental task for both static 3D and dynamic 4D mesh animation, yet existing methods do not provide a unified feedforward solution for these two settings. While static 3D riggers achieve strong quality, they often provide limited control over bone count and become temporally unstable when applied frame by frame to dynamic meshes. Existing 4D methods, in contrast, typically rely on expensive per-sequence optimization. We propose MoTWorld, a template-free, data-efficient framework for unified 3D and 4D skeleton generation. Built on flow matching, MoTWorld generates temporally aligned skeletons for an entire sequence in a single feedforward pass, while naturally handling single-mesh 3D rigging. The model further supports explicit skeleton-count control, uncertainty estimation for candidate selection, and masking-based interpolation, forecasting, and backcasting. To address limited paired 4D rigging data, we adopt a curriculum that initializes from large-scale 3D rigging data and adapts to mid-scale 4D mesh-skeleton data. Experiments show that MoTWorld achieves strong static 3D rigging performance with controllable bone complexity, as well as high-quality and temporally consistent 4D reconstruction and prediction results.
