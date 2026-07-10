---
title: "CoFINN: Conservation Flux Informed Neural Networks for Physics Problems Governed by Conservation Laws"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.06587
priority: medium
status: unread
interest: medium
next_step: skim
---
# CoFINN: Conservation Flux Informed Neural Networks for Physics Problems Governed by Conservation Laws
> 原文: [https://arxiv.org/abs/2607.06587](https://arxiv.org/abs/2607.06587)

arXiv:2607.06587v1 Announce Type: new
Abstract: We present CoFINN (Conservation Flux Informed Neural Networks), a physics-informed deep learning framework for predicting compressible flow fields governed by conservation laws. Unlike conventional data-driven convolutional neural networks (CNNs), which optimize only pixel-wise similarity metrics, CoFINN embeds finite-volume conservation physics directly into the training process. Unlike classical physics-informed methods which enforce differential-equation residuals at collocation points through automatic differentiation, CoFINN adopts a finite-volume perspective consistent with modern CFD methodology. CoFINN interprets CNN output fields as structured computational grids, where each pixel represents a finite-volume cell, and enforces conservation consistency through sophisticated numerical flux calculations. The framework is evaluated on transonic flow prediction around airfoils at (M=0.7, Re=6 \* 10^6), including challenging conditions involving shock waves and high angles of attack. Results show that CoFINN improves aerodynamic force prediction accuracy, reducing drag prediction error by up to 34% at extreme angles of attack and by approximately 15% on average across the test set. Improvements are particularly significant in limited-data regimes, demonstrating that the conservation-based loss acts as an effective physical regularizer. The proposed approach maintains the computational efficiency advantages of CNN surrogates while significantly improving physical consistency and conservation behavior. The framework is architecture-agnostic and extensible to broader classes of conservation-law-governed physical systems.
