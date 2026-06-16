---
interest: medium
link: https://arxiv.org/abs/2606.14716
next_step: skim
priority: medium
slack_ts: '1781586974.099049'
source: cs.CV - Computer Vision
status: unread
title: 'RAMS: Resource-Adaptive and Detection-Conditioned Model Switching for Embedded
  Edge Perception'
---
# RAMS: Resource-Adaptive and Detection-Conditioned Model Switching for Embedded Edge Perception
> 原文: [https://arxiv.org/abs/2606.14716](https://arxiv.org/abs/2606.14716)

arXiv:2606.14716v1 Announce Type: new
Abstract: Edge object detection on embedded hardware requires balancing inference latency and detection quality under changing resource pressure. We present RAMS, a lightweight runtime controller that monitors device pressure, calibrates switching thresholds from idle behavior, and dynamically selects among three resident YOLOv8 tiers (NANO/SMALL/MEDIUM at 320/416/640 px) without model-reload latency. RAMS defines five switching policies, including two detection-conditioned variants that prevent aggressive downgrades after recent vulnerable-road-user (VRU) detections. We further introduce the VRU-Weighted Accuracy Score (SWAS), a scalar metric for offline policy comparison without ground-truth annotations, together with an oracle-bounded variant that separates detector circularity from genuine tier-retention benefit. Across Raspberry Pi 5, x86 laptops, and Jetson Orin ONNX/TensorRT deployments, the same controller equations operate over a 37x latency range. On Jetson Orin TensorRT under heavy load, the safety2 policy achieves 3.41 ms mean latency, 5.6x faster than fixed-MEDIUM inference, while retaining 74% of its proxy accuracy through near-NANO operation with selective SMALL and MEDIUM locks during VRU-positive windows. Detection-conditioned switching improves SWAS by 25.4% under oracle scoring and 47.3% under detector-derived scoring relative to threshold-only policies under heavy load. Live KITTI evaluation reports per-tier VRU recall of 24.2%, 41.2%, and 59.0%, showing that reactive overrides are fundamentally limited by baseline detector recall.
