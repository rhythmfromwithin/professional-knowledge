---
interest: medium
link: https://arxiv.org/abs/2606.27566
next_step: skim
priority: medium
slack_ts: '1782708433.321649'
source: cs.RO - Robotics
status: unread
title: Spacecraft Fiducial Marker for Autonomous Rendezvous, Proximity Operations,
  and Docking
---
# Spacecraft Fiducial Marker for Autonomous Rendezvous, Proximity Operations, and Docking
> 原文: [https://arxiv.org/abs/2606.27566](https://arxiv.org/abs/2606.27566)

arXiv:2606.27566v1 Announce Type: new
Abstract: Robotic operations in space are challenging due to the harsh environment and the high cost of failure. Fiducial markers provide visual references that aid autonomous rendezvous, proximity operations, and docking for space robots. However, existing fiducial markers are mostly single-scale and largely designed for terrestrial robotics. Such markers leave the camera's field of view at close range, precisely during the proximity and docking phases where reliable tracking is most critical. This paper presents AstraTag, a fiducial marker designed for autonomous on-orbit robotic operations. The marker template is based on a square Spidron pattern whose recursive, self-similar structure enables detection across multiple spatial scales. Marker identification uses a 48-bit signature derived from triangular sub-regions of the template and encoded with a Generalised Reed-Solomon (GRS) code. The detection pipeline performs contour-based quadrilateral localisation, perspective normalisation, and signature matching against a pre-computed dictionary. To handle markers affixed to curved spacecraft surfaces, it incorporates a Thin-Plate Spline (TPS) re-warp fallback that exploits the marker's internal rectangular borders as additional geometric correspondences. We benchmark AstraTag against three-layer Fractal ArUco and AprilTag on spacecraft mockups with flat and curved surfaces. On curved surfaces, AstraTag achieves a higher detection rate than both baselines, offering a robust recursive-marker option for space robotics.
