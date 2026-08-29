---
interest: medium
link: https://arxiv.org/abs/2608.26273
next_step: skim
priority: medium
slack_ts: '1787986066.887149'
source: cs.RO - Robotics
status: unread
title: Constraint-Aware Physics-Informed Neural Networks for Static Shape Estimation
  of Co-Manipulative Continuum Robots
---
# Constraint-Aware Physics-Informed Neural Networks for Static Shape Estimation of Co-Manipulative Continuum Robots
> 原文: [https://arxiv.org/abs/2608.26273](https://arxiv.org/abs/2608.26273)

arXiv:2608.26273v1 Announce Type: new
Abstract: Static shape estimation of co-manipulative continuum robots (CCRs) is challenging because the continuum arms and manipulated flexible object form a closed chain that must satisfy both static equilibrium and geometric loop-closure constraints. This paper presents a constraint-aware physics-informed neural network (PINN) for static shape estimation of a tendon-driven CCR modeled using the geometric variable strain formulation. The proposed method incorporates a projected static equilibrium residual and a configuration-level geometric residual to enforce the governing mechanics and closed-chain geometry. In simulation, the PINN is compared with a purely data-driven artificial neural network (ANN) under limited and noisy training data. With 140 samples and 50% label noise, the PINN reduces the relative configuration error, equilibrium residual, and closed-chain residual by 67.88%, 67.35%, and 88.06%, respectively. Using the full dataset, the PINN achieves 0.1597% relative configuration error with an inference time of 0.1773 ms, compared with 17.97 s for an iterative nonlinear solver. Experimental fine-tuning reduces the marker RMSE from 2.657 mm to 0.497 mm and increases R2 from -0.788 to 0.937. These results demonstrate accurate, physically consistent, and computationally efficient static shape estimation of closed-chain CCRs.
