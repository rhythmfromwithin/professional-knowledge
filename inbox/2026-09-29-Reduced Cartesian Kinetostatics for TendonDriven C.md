---
interest: medium
link: https://arxiv.org/abs/2609.31771
next_step: skim
priority: medium
slack_ts: '1790832418.373269'
source: cs.RO - Robotics
status: unread
title: 'Reduced Cartesian Kinetostatics for Tendon-Driven Continuum Robots: Residual-Stabilized
  Full-Shape Propagation'
---
# Reduced Cartesian Kinetostatics for Tendon-Driven Continuum Robots: Residual-Stabilized Full-Shape Propagation
> 原文: [https://arxiv.org/abs/2609.31771](https://arxiv.org/abs/2609.31771)

arXiv:2609.31771v1 Announce Type: new
Abstract: Many planning and control tasks for tendon-driven continuum robots (TDCRs) require the complete Cartesian backbone geometry. We present a reduced Cartesian framework for planar, axially compressible TDCRs that propagates equilibrium configurations along prescribed tendon-force and tendon-displacement trajectories. The backbone is represented by two global position fields. Following exact variation, a Taylor-Galerkin reduction condenses prescribed spatial properties and distributed loads into offline moment vectors, yielding analytic reduced residuals and Jacobians without online spatial quadrature or numerical differentiation. Analytical differentiation and residual correction yield first-order rate systems requiring one fixed-dimensional linear solve per rate evaluation after initial equilibrium alignment on a regular branch. Across four simulated cases covering variable tendon routing, nonuniform geometry, axial compression, and their combined effects, the propagated Cartesian shapes and distributed strains closely match pointwise geometrically variable-strain (GVS) equilibrium solutions. Residual correction suppresses propagation drift across the tested step sizes while adding only about 0.98% to the mean update time of uncorrected Euler. The proposed method requires 0.508 ms per update on average, approximately 11 times faster than pointwise GVS solves. Displacement-driven experiments yield a maximum normalized mean backbone position error of 1.02% and a maximum end-effector position error of 0.28%. These results support efficient and accurate Cartesian full-shape prediction along prescribed actuation paths.
