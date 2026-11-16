---
interest: medium
link: https://arxiv.org/abs/2611.17505
next_step: skim
priority: medium
slack_ts: '1794808695.316799'
source: cs.CV - Computer Vision
status: unread
title: 'Adversarial Tracking: Attacks on Image Sensors for Object Tracking in Autonomous
  Vehicles'
---
# Adversarial Tracking: Attacks on Image Sensors for Object Tracking in Autonomous Vehicles
> 原文: [https://arxiv.org/abs/2611.17505](https://arxiv.org/abs/2611.17505)

arXiv:2611.17505v1 Announce Type: new
Abstract: Object tracking systems estimate the motion of surrounding vehicles by linking detected objects across video frames. In particular, Tracking-By-Detection (TBD) systems combine object detectors with motion prediction and data association to maintain object identities over time. However, neural network-based detectors are vulnerable to adversarial attacks that perturb input images, and their impact on downstream trajectory estimation is not fully characterized by detection accuracy alone. Therefore, this paper evaluates image-specific and image-agnostic attacks on YOLOv3 and YOLOv4 detectors paired with SORT, Deep SORT, Strong SORT, and OC-SORT tracking systems. The evaluation uses CARLA simulator and measures tracking quality through Multiple Object Tracking Accuracy (MOTA), Higher Order Tracking Accuracy (HOTA), and Identification F1 (IDF1). Under image-specific attacks, HOTA for YOLOv3-based trackers declines from 53.45-56.19% to 14.85-17.03%, while MOTA reaches -772.60% in the worst case. YOLOv4-based trackers exhibit greater robustness, while HOTA still declines to 25.06-26.86%. In addition, image-agnostic attacks can reduce the tracking accuracy using a single Universal Adversarial Perturbation (UAP), without generating a separate perturbation for individual frames.
