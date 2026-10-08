---
title: "Trust-Region Optimization for Smooth Potential-Interaction Energies in Wasserstein Space"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.08883
priority: medium
status: unread
interest: medium
next_step: skim
---
# Trust-Region Optimization for Smooth Potential-Interaction Energies in Wasserstein Space
> 原文: [https://arxiv.org/abs/2610.08883](https://arxiv.org/abs/2610.08883)

arXiv:2610.08883v1 Announce Type: new
Abstract: Finding low-energy configurations of interacting particles and approximating probability distributions lead to the minimization of potential-interaction energies in Wasserstein space. These energies can be nonconvex, making it important to exploit second-order information while controlling the reliability of local approximations. We study trust-region optimization of smooth potential-interaction energies on the Wasserstein space of probability measures with finite second moment. The method uses a quadratic model along pushforward curves, an $L^2(\rho)$ step radius, and a Steihaug-Toint subsolver with an explicit self-adjoint second-variation operator. A ratio test determines acceptance and guides the radius update. Under a lower energy bound and globally bounded Hessians of the potential and interaction kernel, we prove that the objective is nonincreasing, the Wasserstein-gradient norms converge to zero, and an $\varepsilon$-stationary iterate is reached within $O(\varepsilon^{-2})$ total outer trials, including rejected trials. If the potential is quadratically coercive, every weak accumulation point is stationary. The analysis applies to arbitrary initial measures with finite second moment. For empirical measures, the iteration is a finite-dimensional trust-region method in the $L^2(\rho\_N)$ inner product, with complexity constants independent of particle number and dimension when the initial objective gaps are uniformly bounded. Numerical experiments include a smooth soft-particle energy, maximum-mean-discrepancy minimization for non-Gaussian targets, component ablations, and scaling studies in particle number and dimension.
