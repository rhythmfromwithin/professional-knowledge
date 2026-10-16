---
title: "Navigation by Skylight Polarization via Rayleigh Model Optimization on a Road Vehicle"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.20797
priority: medium
status: unread
interest: medium
next_step: skim
---
# Navigation by Skylight Polarization via Rayleigh Model Optimization on a Road Vehicle
> 原文: [https://arxiv.org/abs/2610.20797](https://arxiv.org/abs/2610.20797)

arXiv:2610.20797v1 Announce Type: new
Abstract: Reliable absolute heading estimation is critical for road-vehicle navigation, particularly when magnetic, inertial, or GNSS-based references are degraded. This paper presents a skylight polarization navigation method that estimates vehicle heading by globally optimizing a Rayleigh sky model against measurements from a division-of-focal-plane polarimetric camera. The proposed framework combines a pinhole camera model, a single-scattering Rayleigh polarization model, and a solar position algorithm to synthesize the expected full image angle of polarization distribution for candidate vehicle states. A degree of polarization weighted root mean square error objective function compares measured and simulated polarization patterns, allowing the estimator to use all available sky information while attenuating low confidence pixels caused by clouds, buildings, foliage, and other depolarizing occlusions. Experimental evaluation is performed using three urban road vehicle trajectories collected with a roof mounted polarimetric camera and a high precision dual-antenna GNSS/INS reference system. Results show sub-degree RMS yaw error across all trajectories, ranging from $0.718^{\circ}$ to $0.889^{\circ}$. Compared with representative feature-based and model-based polarization navigation methods, the proposed approach reduces RMS heading error by up to 87% and demonstrates improved robustness to partial sky occlusion.
