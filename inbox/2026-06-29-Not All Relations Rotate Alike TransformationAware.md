---
interest: medium
link: https://arxiv.org/abs/2606.27412
next_step: skim
priority: medium
slack_ts: '1782708429.301029'
source: cs.CV - Computer Vision
status: unread
title: 'Not All Relations Rotate Alike: Transformation-Aware Decoupling for Viewpoint-Robust
  3D Scene Graph Generation'
---
# Not All Relations Rotate Alike: Transformation-Aware Decoupling for Viewpoint-Robust 3D Scene Graph Generation
> 原文: [https://arxiv.org/abs/2606.27412](https://arxiv.org/abs/2606.27412)

arXiv:2606.27412v1 Announce Type: new
Abstract: 3D Scene Graph Generation (3DSGG) represents 3D scenes as structured object-relation-object graphs, providing a compact relational abstraction for spatial understanding. In embodied intelligence settings, the same 3D scene may be observed by agents from viewpoints that differ by yaw rotations. However, current 3DSGG models often fail to produce relation predictions that follow the expected transformation behavior under such viewpoint shifts. This behavior reveals an empirical mismatch related to predicate-level transformation heterogeneity: directional predicates such as left, front, right, and behind should transform with the observation frame, whereas most contact, support, and semantic predicates such as standing on and attached to should remain stable. To reduce this mismatch, we propose Transformation-Aware Decoupling (TAD), a viewpoint-robust 3DSGG framework that decouples relation reasoning according to predicate transformation behavior and is supported by viewpoint-stable object representations. TAD decomposes relation reasoning into two parts: one learns cues that should stay stable across viewpoints, while the other learns directional cues that should change with the observation frame. The two parts are merged for standard multi-label predicate prediction. Transformation-specific descriptors and group-aware auxiliary supervision encourage the two branches to capture complementary relation cues. Extensive experiments on 3DSSG show that TAD achieves state-of-the-art robustness under yaw viewpoint changes without training-time rotation augmentation, while maintaining competitive performance under the standard benchmark. The project page is available at https://tad-predicate.github.io/.
