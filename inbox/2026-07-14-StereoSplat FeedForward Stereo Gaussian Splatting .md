---
interest: medium
link: https://arxiv.org/abs/2607.08808
next_step: skim
priority: medium
slack_ts: '1784085267.545679'
source: cs.CV - Computer Vision
status: unread
title: 'StereoSplat+: Feed-Forward Stereo Gaussian Splatting with Diffusion-Assisted
  Progressive Inference'
---
# StereoSplat+: Feed-Forward Stereo Gaussian Splatting with Diffusion-Assisted Progressive Inference
> 原文: [https://arxiv.org/abs/2607.08808](https://arxiv.org/abs/2607.08808)

arXiv:2607.08808v1 Announce Type: new
Abstract: Recent advances in 3D Gaussian Splatting (3DGS) have enabled high-quality, render-ready scene representations for novel-view synthesis. However, most existing 3DGS pipelines rely on multi-view observations (or non-causal access to future frames) to achieve sufficient coverage, which is often unavailable in on-device robotics and AR settings where sensing is restricted to a single stereo rig. Recovering a high-quality 3DGS scene from one stereo observation, therefore, remains challenging due to occlusions, limited field of view, and missing geometry. We present StereoSplat+, a diffusion-enhanced feed-forward framework that enables causal reconstruction from a single stereo pair. Our method builds on two key components. First, we propose StereoSplat, an input-invariant feed-forward 3D Gaussian estimator that takes a variable number of posed stereo pairs as input and predicts high-quality 3D Gaussians. StereoSplat fuses complementary geometry cues via a cost-volume branch and a triplane-based 3D volume branch and leverages continuous pose encoding to generalize across view counts and camera configurations. Second, since multiple posed stereo pairs are typically unavailable at inference time, we introduce a diffusion-enhanced one-shot progressive inference scheme called StereoSplat+: starting from one stereo pair, we render novel stereo views from the predicted 3DGS, refine them with a one-step diffusion enhancer, and feed them back as additional inputs to update the 3DGS. Experiments on the KITTI-360 dataset show that StereoSplat+ improves novel-view rendering quality and geometry accuracy, especially in occluded regions and under strong view extrapolation, outperforming recent feed-forward 3DGS baselines.
