---
interest: medium
link: https://arxiv.org/abs/2609.00036
next_step: skim
priority: medium
slack_ts: '1788321940.861139'
source: cs.CV - Computer Vision
status: unread
title: A Cone-Constrained Bilinear Decomposition for Total Scaled-Gradient Variation
  Models
---
# A Cone-Constrained Bilinear Decomposition for Total Scaled-Gradient Variation Models
> 原文: [https://arxiv.org/abs/2609.00036](https://arxiv.org/abs/2609.00036)

arXiv:2609.00036v1 Announce Type: new
Abstract: The total scaled-gradient variation (TSGV) regularizer, derived from sparse modeling of piecewise-linear structures, has been shown to preserve edges and corners in image restoration. However, its highly nonconvex and nonlinear nature poses severe computational challenges, as existing methods often suffer from parameter sensitivity or lack convergence guarantees. To overcome this, we propose a tailored bilinear decomposition that decouples the nonlinear weighted gradient in the TSGV regularizer. This approach yields an equivalent optimization problem governed by cone or sphere constraints, depending on the chosen scaling function. In particular, the cone constraint plays a central role in characterizing edge- and corner-preserving behavior. We solve this reformulation using the alternating minimization method (AMM) equipped with a majorization--minimization strategy, ensuring a monotonic decrease in energy without step-size tuning. Furthermore, we provide a geometric interpretation of the edge-preserving properties of these constraints by analyzing their asymptotic behavior near image singularities. We establish the global convergence of the proposed method to a critical point within the Kurdyka--{\L}ojasiewicz framework. Extensive numerical experiments on Gaussian denoising and non-line-of-sight (NLOS) imaging show that the proposed method achieves PSNR and SSIM competitive with or superior to representative variational methods, especially at high noise levels, and improves the structural reconstruction under dense and sparse scanning.
