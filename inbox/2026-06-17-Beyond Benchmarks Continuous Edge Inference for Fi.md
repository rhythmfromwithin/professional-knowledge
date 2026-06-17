---
interest: medium
link: https://arxiv.org/abs/2606.17241
next_step: skim
priority: medium
slack_ts: '1781672186.586129'
source: cs.CV - Computer Vision
status: unread
title: 'Beyond Benchmarks: Continuous Edge Inference for Fine-Grained Roadside Perception'
---
# Beyond Benchmarks: Continuous Edge Inference for Fine-Grained Roadside Perception
> 原文: [https://arxiv.org/abs/2606.17241](https://arxiv.org/abs/2606.17241)

arXiv:2606.17241v1 Announce Type: new
Abstract: Continuous AI inference on resource-constrained edge hardware introduces deployment effects that are largely invisible to conventional benchmark evaluation, including temporal instability in streaming video, thermal throttling under sustained load, and workload-dependent performance variability. We present Edge-TSR, a deployment-oriented continuous edge inference system for sustained roadside perception on the NVIDIA Jetson Orin Nano. Edge-TSR integrates detection, tracking, fine-grained classification, and a lightweight track-aware temporal stabilization mechanism that improves streaming inference consistency with negligible computational overhead. Our central finding is that benchmark-centric evaluation systematically overstates deployed edge inference performance. Across three state-of-the-art baselines, we observe consistent 20-30% relative degradation when transitioning from static-image evaluation to real-world streaming deployment. Edge-TSR addresses this gap through temporal inference stabilization, recovering up to 10.16% classification accuracy over per-frame inference baselines while maintaining sustained real-time performance under continuous operation. We evaluate the complete system under diverse real-world deployment conditions, jointly characterizing inference quality, latency, throughput, and thermal behavior during long-duration operation. A 55-minute vehicular deployment over a 26 km route demonstrates sustained operation at 16.18 FPS within safe thermal limits on a single embedded device without cloud offload. Our findings show that deployment-aware evaluation and temporal inference stabilization are necessary components of continuously operating edge AI systems intended for real-world sensing deployments. We release a sample annotated streaming video evaluation dataset and full system implementation to support reproducible deployment-centric evaluation.
