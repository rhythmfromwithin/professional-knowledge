---
title: "Autoregressive View Model"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2611.23417
priority: medium
status: unread
interest: medium
next_step: skim
---
# Autoregressive View Model
> 原文: [https://arxiv.org/abs/2611.23417](https://arxiv.org/abs/2611.23417)

arXiv:2611.23417v1 Announce Type: new
Abstract: We present the Autoregressive View Model (AVM), which generates a scene as a stream of views without constructing an explicit 3D representation. Through a unified in-context interface, AVM conditions on images or videos to generate short clips along a requested camera path. Visual context grounds reconstruction and interpolation, while a learned prior enables extrapolation into unseen regions. AVM retrieves relevant views from inputs and generated history to form a bounded active context. We fine-tune a pretrained bidirectional video diffusion transformer with flow matching in an N-in-1-out formulation. We then tune a causal model on its own rollouts to improve photorealism, reduce denoising steps, and limit long-horizon drift. We scale training to approximately 8M scenes and video clips. We evaluate generation capacity and scene persistence across benchmarks for camera control, text control, visual quality, dynamics, sparse and 4D reconstruction, and long-horizon consistency. The results demonstrate that AVM adapts to diverse input and output settings through one in-context interface.
