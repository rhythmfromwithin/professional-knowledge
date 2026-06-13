---
interest: medium
link: https://arxiv.org/abs/2606.12473
next_step: skim
priority: medium
slack_ts: '1781324788.304679'
source: cs.CV - Computer Vision
status: unread
title: Stereo Vision-Based Fall Prediction and Detection using Human Pose Estimation
  on the AMD Kria K26 SOM
---
# Stereo Vision-Based Fall Prediction and Detection using Human Pose Estimation on the AMD Kria K26 SOM
> 原文: [https://arxiv.org/abs/2606.12473](https://arxiv.org/abs/2606.12473)

arXiv:2606.12473v1 Announce Type: new
Abstract: Background and Objective: Falls among elderly people can cause serious injury and reduce quality of life. Timely prediction and detection are essential to prevent harm and support well-being. We propose a portable, low-power, battery-operated, vision-based fall prediction and detection system using HPE on an AMD Kria K26 System-on-Module (SOM). The objective is a non-intrusive, privacy-preserving system for real-time fall detection.
Methods: The system uses an Intel RealSense D455 range-sensing camera connected to the K26 SOM by USB. It captures synchronized RGB and depth frames, 640 x 480 x 3 and 640 x 480 pixels, at 60 FPS. The SOM runs a three-stage pipeline with quantized YOLOX, Anchor-to-Joint (A2J), and fall-detection models. YOLOX identifies human bounding boxes from RGB frames, then discards the RGB frames to preserve privacy. A2J uses depth frames to estimate 15 joint keypoints per person. A CNN uses selected joint coordinates (x, y, z) to classify fall activity. YOLOX was trained on CrowdHuman; A2J on ITOP, MP-3DHP, UR Fall Detection, and a custom SDSU PSG dataset; and the CNN on UR Fall Detection and SDSU PSG. The design used a single-core DPU with a serial pipeline and a dual-core DPU running YOLOX and A2J with multiple threads.
Results: Quantized accuracy was evaluated using IoU >= 50% for YOLOX, mAP with a 10-cm rule for A2J, and classification accuracy, (TP + TN)/(TP + TN + FP + FN), for the CNN. Accuracies were 74%, 84.13%, and 75.85%. Throughput improved from 2.5 FPS for the single-threaded pipeline to 4.5 FPS for the multi-threaded version.
Conclusion: Results demonstrate the feasibility of privacy-preserving fall detection on an AMD Kria K26 edge device. On-device HPE and fall classification runs without cloud dependency, supporting elderly monitoring and assistive healthcare. Future work will improve model accuracy and speed.
