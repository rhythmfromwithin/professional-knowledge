---
title: "SL(C)AMma: Simultaneous Localisation, (Calibration) and Mapping With a Magnetometer Array"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.19946
priority: medium
status: unread
interest: medium
next_step: skim
---
# SL(C)AMma: Simultaneous Localisation, (Calibration) and Mapping With a Magnetometer Array
> 原文: [https://arxiv.org/abs/2604.19946](https://arxiv.org/abs/2604.19946)

arXiv:2604.19946v1 Announce Type: new
Abstract: Indoor localisation techniques suffer from attenuated Global Navigation Satellite System (GNSS) signals and from the accumulation of unbounded drift by integration of proprioceptive sensors. Magnetic field-based Simultaneous Localisation and Mapping (SLAM) reduces drift through loop closures by revisiting previously seen locations, but extended exploration of unseen areas remains challenging. Recently, magnetometer arrays have demonstrated significant benefits over single magnetometers, as they can directly estimate the odometry. However, inconsistencies between magnetometer measurements negatively affect odometry estimates and complicate loop closure detection. We propose two filtering algorithms: The first focuses on magnetic field-based SLAM using a magnetometer array (SLAMma). The second extends this to jointly estimate the magnetometer calibration parameters (SLCAMma). We demonstrate, using Monte Carlo simulations, that the calibration parameters can be accurately estimated when there is sufficient orientation excitation, and that magnetometers achieve inter-sensor measurement consistency regardless of the type of motion. Experimental validation on ten datasets confirms these results, and we demonstrate that in cases where single magnetometer SLAM fails, SLAMma and SLCAMma provide good trajectory estimates with, more than 80% drift reduction compared to integration of proprioceptive sensors.
