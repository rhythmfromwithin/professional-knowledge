---
interest: medium
link: https://arxiv.org/abs/2611.03717
next_step: skim
priority: medium
slack_ts: '1793945317.737609'
source: cs.CV - Computer Vision
status: unread
title: Physics-Informed Functional Tucker Method with RKHS Factors for Sparse Spatiotemporal
  Reconstruction
---
# Physics-Informed Functional Tucker Method with RKHS Factors for Sparse Spatiotemporal Reconstruction
> 原文: [https://arxiv.org/abs/2611.03717](https://arxiv.org/abs/2611.03717)

arXiv:2611.03717v1 Announce Type: new
Abstract: Reconstructing physical dynamics from fixed sparse sensors and missing frames is a fundamental challenge in scientific research. Sparsity leaves large regions of the field unconstrained, making the inverse problem ill-posed: a model may fit the observed sensors while producing inaccurate off-sensor structures or unreliable predictions between support frames. To this end, we propose PhysFTM---a physics-informed functional Tucker model that parameterizes the Tucker mode factors in reproducing kernel Hilbert spaces (RKHSs) and incorporates PDE constraints through finite-difference residuals evaluated at off-sensor collocation points. These residuals provide additional physical information in regions without direct observational supervision. PhysFTM first reconstructs continuous spatial fields at support frames via an alternating minimization scheme, optimizing the Tucker core tensor and the RKHS-based factors separately. To enable missing-frame reconstruction, PhysFTM constructs a continuous trajectory in Tucker-core space, which is decoded by the learned spatial RKHS-FTM representation to recover the full spatiotemporal field. Experiments on Allen--Cahn, Navier--Stokes, three-dimensional Heat equations, and a three-dimensional gridded Copernicus ocean reanalysis demonstrate accurate 2D/3D reconstruction under two missing-frame protocols. Code is available at https://github.com/liusirzzz/PhysFTM.
