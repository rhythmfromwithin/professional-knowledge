---
interest: medium
link: https://arxiv.org/abs/2604.09643
next_step: skim
priority: medium
slack_ts: '1776310484.528459'
source: cs.CV - Computer Vision
status: unread
title: 'PA-SFM: Tracker-free differentiable acoustic radiation for freehand 3D photoacoustic
  imaging'
---
# PA-SFM: Tracker-free differentiable acoustic radiation for freehand 3D photoacoustic imaging
> 原文: [https://arxiv.org/abs/2604.09643](https://arxiv.org/abs/2604.09643)

arXiv:2604.09643v1 Announce Type: new
Abstract: Three-dimensional (3D) handheld photoacoustic tomography typically relies on bulky and expensive external positioning sensors to correct motion artifacts, which severely limits its clinical flexibility and accessibility. To address this challenge, we present PA-SFM, a tracker-free framework that leverages exclusively single-modality photoacoustic data for both sensor pose recovery and high-fidelity 3D reconstruction via differentiable acoustic radiation modeling. Unlike traditional structure-from-motion (SFM) methods based on visual features, PA-SFM integrates the acoustic wave equation into a differentiable programming pipeline. By leveraging a high-performance, GPU-accelerated acoustic radiation kernel, the framework simultaneously optimizes the 3D photoacoustic source distribution and the sensor array pose via gradient descent. To ensure robust convergence in freehand scenarios, we introduce a coarse-to-fine optimization strategy that incorporates geometric consistency checks and rigid-body constraints to eliminate motion outliers. We validated the proposed method through both numerical simulations and in-vivo rat experiments. The results demonstrate that PA-SFM achieves sub-millimeter positioning accuracy and restores high-resolution 3D vascular structures comparable to ground-truth benchmarks, offering a low-cost, software-defined solution for clinical freehand photoacoustic imaging. The source code is publicly available at \href{https://github.com/JaegerCQ/PA-SFM}{https://github.com/JaegerCQ/PA-SFM}.
