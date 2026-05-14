---
title: "Scale-Gest: Scalable Model-Space Synthesis and Runtime Selection for On-Device Gesture Detection"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2605.12506
priority: medium
status: unread
interest: medium
next_step: skim
---
# Scale-Gest: Scalable Model-Space Synthesis and Runtime Selection for On-Device Gesture Detection
> 原文: [https://arxiv.org/abs/2605.12506](https://arxiv.org/abs/2605.12506)

arXiv:2605.12506v1 Announce Type: new
Abstract: Realizing on-device ML-based gesture detection under tight real-time performance, energy and memory constraints is challenging, especially when considering mobile devices with varying battery-power levels. Existing EdgeAI deployments typically rely on a single fixed detector, limiting optimization opportunities. We present Scale-Gest, a novel run-time adaptive gesture detection framework that expands the detector space into a dense family of tiny-YOLO architectures. We introduce multiple novel device-calibrated ACE (Accuracy-Complexity-Energy) profiles by analyzing different model-resolution-stride operating points. A lightweight run-time controller selects an appropriate ACE mode under user-defined and battery constraints, while a motion-aware hand-gesture-tracking ROI gate crops the input for reduced complexity detection. To evaluate performance of our system in real-world car driving scenarios, we introduce a temporally-annotated Driver Simulated Gesture (DSG-18) dataset. Scale-Gest maintains event-level F1 while significantly reducing energy and latency compared to single-detector approaches. On a battery-powered laptop running gesture streams, our ACE controller reduces per-frame energy by 4x (from 6.9 mJ to 1.6 mJ) while maintaining high gesture-detection performance (event-level F1 = 0.8-0.9) and low mean latency (6 ms).
