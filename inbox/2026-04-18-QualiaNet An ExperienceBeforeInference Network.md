---
title: "QualiaNet: An Experience-Before-Inference Network"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.14193
priority: medium
status: unread
interest: medium
next_step: skim
---
# QualiaNet: An Experience-Before-Inference Network
> 原文: [https://arxiv.org/abs/2604.14193](https://arxiv.org/abs/2604.14193)

arXiv:2604.14193v1 Announce Type: new
Abstract: Human 3D vision involves two distinct stages: an Experience Module, where stereo depth is extracted relative to fixation, and an Inference Module, where this experience is interpreted to estimate 3D scene properties. Paradoxically, although our experience of stereo vision does not provide us with distance information, it does affect our inferences about visual scale. We propose the Inference Module exploits a natural scene statistic: near scenes produce vivid disparity gradients, while far scenes appear comparatively flat. QualiaNet implements this two-stage architecture computationally: disparity maps simulating human stereo experience are passed to a CNN trained to estimate distance. The network can recover distance from disparity gradients alone, validating this approach.
