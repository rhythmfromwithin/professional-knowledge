---
title: "TacHair: Tactile Contact-Distribution Guided Online Correction for Robotic Hair Stroking and Perception"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.10637
priority: medium
status: unread
interest: medium
next_step: skim
---
# TacHair: Tactile Contact-Distribution Guided Online Correction for Robotic Hair Stroking and Perception
> 原文: [https://arxiv.org/abs/2610.10637](https://arxiv.org/abs/2610.10637)

arXiv:2610.10637v1 Announce Type: new
Abstract: Hair stroking is common in daily grooming and personal care, and is also widely used in hair-product evaluation, motivating robots with similar physical interaction capabilities. Existing robotic hair-care and surface-following methods mainly rely on trajectory planning, compliance, force regulation, or tactile-conditioned policies, but deformable hair can remain in contact while gradually drifting across the end-effector, making local interaction difficult to regulate. We propose TacHair, a tactile contact-distribution guided online correction framework that represents high-resolution tactile observations as a spatial hair-contact distribution. A visuotactile imitation policy generates the nominal stroking motion, while a separately trained residual module corrects local contact deviations, separating task progression from contact recovery. We evaluate TacHair in 525 real-robot trials across five head geometries and three hair conditions. A successful stroke requires both sufficient task progression and contact maintenance; our method improves success from 42.9% to 62.3% and contact maintenance from 59.4% to 88.0% over the same visuotactile policy without correction. These results demonstrate spatial tactile contact distributions as an effective feedback representation for contact-preserving interaction with deformable and visually occluded surfaces. Demos, code, and datasets are available at https://tachair.github.io.
