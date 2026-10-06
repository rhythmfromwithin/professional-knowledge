---
title: "MOSAIC-SV: Real-Time Adaptive Identification of Vessel Dynamics for the Control and Deployment of Aquatic Robots"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.03898
priority: medium
status: unread
interest: medium
next_step: skim
---
# MOSAIC-SV: Real-Time Adaptive Identification of Vessel Dynamics for the Control and Deployment of Aquatic Robots
> 原文: [https://arxiv.org/abs/2610.03898](https://arxiv.org/abs/2610.03898)

arXiv:2610.03898v1 Announce Type: new
Abstract: Model-based control of an aquatic robotic platform depends on a hydrodynamic model that is costly to identify and specific to the hull, payload, and conditions it was measured in. Here, we present MOSAIC-SV, a deployable real-time adaptive dynamics identification and control system that identifies a control-sufficient dynamics model from a spec-sheet engineering prior, without dedicated identification trials, and re-estimates it at every control step of a closed-loop mission while the controller plans on it. A physically admissible unscented Kalman filter re-estimates hydrodynamic, disturbance, and actuator parameters at every control step of the closed-loop mission; while a command-dependent consider projection withholds corrections the current command cannot attribute between actuator effectiveness and external force; and a model predictive path integral controller plans on the current estimate. In simulation on a CyberShip II plant, MOSAIC-SV recovers the transit performance of the calibrated model under static mismatch and transient changes, and stays within 20% of its own transit time at the unscaled prior when its inertia or damping prior is wrong by an order of magnitude. In on-water field trials on the Blue Robotics BlueBoat, a twin-thruster catamaran, MOSAIC-SV transits at least 25% faster and predicts its own motion with at least 56% less error than its frozen engineering prior, including under an unmodeled payload. The same MOSAIC-SV system concept was also feasibly deployed on a 6.3-tonne dual outboard monohull.
