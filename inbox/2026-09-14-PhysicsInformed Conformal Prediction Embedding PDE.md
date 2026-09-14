---
interest: medium
link: https://arxiv.org/abs/2609.11935
next_step: skim
priority: high
slack_ts: '1789360379.244869'
source: cs.LG - Machine Learning
status: unread
title: 'Physics-Informed Conformal Prediction: Embedding PDE Consistency into Distribution-Free
  Uncertainty Quantification for Neural Operators'
---
# Physics-Informed Conformal Prediction: Embedding PDE Consistency into Distribution-Free Uncertainty Quantification for Neural Operators
> 原文: [https://arxiv.org/abs/2609.11935](https://arxiv.org/abs/2609.11935)

arXiv:2609.11935v1 Announce Type: new
Abstract: Neural operators such as the Fourier Neural Operator (FNO) achieve remarkable accuracy in approximating solutions to partial differential equations (PDEs). However, providing rigorous uncertainty estimates remains an open challenge. We propose Physics-Informed Conformal Prediction (PI-CP), a framework that embeds PDE residuals into the nonconformity score of split conformal prediction, producing prediction intervals that are (i) distribution-free with provable coverage guarantees, and (ii) spatially adaptive when the PDE residual correlates with prediction error -- tighter where physics is well-satisfied, wider where it is violated. Additionally, we prove that FNO's translation equivariance creates a fundamental approximation barrier for PDEs with Dirichlet boundary conditions, and show that coordinate channels resolve this with up to 63x error reduction. We validate PI-CP across six physics scenarios -- heat conduction (2D/3D), structural mechanics (2D/3D), Darcy flow, and Navier-Stokes -- demonstrating consistent 89-91% coverage for all four Conformal methods, while MC Dropout and Deep Ensembles are unstable (82-100%). FNO outperforms CNN and DeepONet by 10-12x.
