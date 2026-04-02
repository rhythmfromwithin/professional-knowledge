---
title: "Fisheye3R: Adapting Unified 3D Feed-Forward Foundation Models to Fisheye Lenses"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.28896
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fisheye3R: Adapting Unified 3D Feed-Forward Foundation Models to Fisheye Lenses
> 原文: [https://arxiv.org/abs/2603.28896](https://arxiv.org/abs/2603.28896)

arXiv:2603.28896v1 Announce Type: new
Abstract: Feed-forward foundation models for multi-view 3-dimensional (3D) reconstruction have been trained on large-scale datasets of perspective images; when tested on wide field-of-view images, e.g., from a fisheye camera, their performance degrades. Their error arises from changes in spatial positions of pixels due to a non-linear projection model that maps 3D points onto the 2D image plane. While one may surmise that training on fisheye images would resolve this problem, there are far fewer fisheye images with ground truth than perspective images, which limit generalization. To enable inference on imagery exhibiting high radial distortion, we propose Fisheye3R, a novel adaptation framework that extends these multi-view 3D reconstruction foundation models to natively accommodate fisheye inputs without performance regression on perspective images. To address the scarcity of fisheye images and ground truth, we introduce flexible learning schemes that support self-supervised adaptation using only unlabeled perspective images and supervised adaptation without any fisheye training data. Extensive experiments across three foundation models, including VGGT, $\pi^3$, and MapAnything, demonstrate that our approach consistently improves camera pose, depth, point map, and field-of-view estimation on fisheye images.
