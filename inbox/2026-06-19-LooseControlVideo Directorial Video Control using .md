---
interest: medium
link: https://arxiv.org/abs/2606.19495
next_step: skim
priority: medium
slack_ts: '1781847260.836869'
source: cs.CV - Computer Vision
status: unread
title: 'LooseControlVideo: Directorial Video Control using Spatial Blocking'
---
# LooseControlVideo: Directorial Video Control using Spatial Blocking
> 原文: [https://arxiv.org/abs/2606.19495](https://arxiv.org/abs/2606.19495)

arXiv:2606.19495v1 Announce Type: new
Abstract: Precise 3D spatial orchestration in text-to-video generation remains a significant challenge, particularly for multi-object scenes where semantic layout and temporal dynamics are often entangled. While existing depth-conditioned models achieve good structural fidelity, they necessitate dense, frame-accurate guidance that is labor-intensive to author for dynamic events involving deformable objects. We present LooseControlVideo, a framework that enables intuitive and expressive control by using sparse, oriented 3D boxes as a "blocking" proxy. This allows users to author high-level layout and trajectory while leveraging a video generative model to generate realistic occlusions, dynamics and interactions. We achieve this by fine-tuning a Wan 2.2 backbone on a video dataset annotated with DNOCS, a novel encoding for 3D size, orientation and depth-ordered occlusions. Furthermore, our method allows for localized refinement, such as adjusting a jump trajectory or adding an interaction, with minimal disruption to the global scene context. Extensive evaluations on the nuScenes, HO-3D, and BEHAVE benchmarks demonstrate that LooseControlVideo significantly outperforms existing 2D-box and flow-based baselines. Our findings indicate a 1.2x to 3x improvement in Trajectory Error; 2x improvement in Rigid Motion Consistency; and a 1.5x to 2x increase in Occlusion Accuracy over current state-of-the-art layout-conditioned models, demonstrating that oriented 3D primitives provide good geometric prior for complex, multi-agent video authoring.
