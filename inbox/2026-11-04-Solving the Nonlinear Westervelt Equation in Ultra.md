---
title: "Solving the Nonlinear Westervelt Equation in Ultrasound Propagation Using Physics-Informed Neural Networks"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2611.05130
priority: low
status: unread
interest: medium
next_step: skim
---
# Solving the Nonlinear Westervelt Equation in Ultrasound Propagation Using Physics-Informed Neural Networks
> 原文: [https://arxiv.org/abs/2611.05130](https://arxiv.org/abs/2611.05130)

arXiv:2611.05130v1 Announce Type: cross
Abstract: Modeling the nonlinear acoustic wave propagation in biological tissues needs accuracy, especially in ultrasound imaging and therapeutic applications. The 1D Westervelt equation, \( p\_{xx} - p\_{tt} + \gamma\, p\_{ttt} + \eta\,(p^{2})\_{tt}=0, \) could be used to describe a finite-amplitude ultrasound propagation in these tissues. This equation accounts for nonlinearity, \(\eta\), and attenuation, \(\gamma\). To solve this equation, we observe that traditional solvers may struggle to do so correctly. This is due to the difficulties arising from the nonlinear nature of the equation. We solve the equation by defining three synthetic cases - linear (\(\eta=0.001\), \(\gamma=10^{-6}\)), shock-dominated (\(\eta=0.02\), \(\gamma=10^{-6}\)), and dissipation-dominated (\(\eta=0.01\), \(\gamma=5\times10^{-4}\)) - and using Physics-Informed Neural Networks (PINNs) to showcase the solution. A sinusoidal activation function is used to capture the oscillatory behavior of the problem. The results of our study, with PDE residual converging to at least \(10^{-6}\), boundary condition loss to \(10^{-5}\), and the PINN loss converging to \(10^{-5}\) for each case at \(30,000\) epochs, show that \(\gamma\) scales the rate of amplitude decay, while \(\eta\) governs frequency-dependent phase speeds.
