---
interest: medium
link: https://arxiv.org/abs/2609.12075
next_step: skim
priority: medium
slack_ts: '1789360368.737219'
source: cs.DC - Distributed Computing
status: unread
title: Efficient Vision-Language-Action Management and Serving for Robot Factories
---
# Efficient Vision-Language-Action Management and Serving for Robot Factories
> 原文: [https://arxiv.org/abs/2609.12075](https://arxiv.org/abs/2609.12075)

arXiv:2609.12075v1 Announce Type: new
Abstract: Vision-Language-Action (VLA) models show high robotic manipulation capabilities via a two-stage design: a Vision-Language Model (VLM) stage followed by an Action Diffusion Transformer (ADiT) stage. Since robots must meet strict Service-Level Objectives (SLOs) for safety, VLA inference is inherently latency-critical. Meeting these SLOs requires high-end GPUs, yet weight, cost, and power constraints preclude integrating such GPUs on-robot. Prior works offload VLA inference to edge servers that serve many robots on VLA models. However, current VLA systems lack support for multi-request, multi-model execution on a multi-GPU server under SLOs, while existing serving systems for multi-stage models are optimized for throughput and stage disaggregation across separate GPUs, which are ill-suited for the millisecond-scale stages of VLA models. We design Robion, the first VLA serving and management system for multi-robot, multi-model requests on multi-GPU edge servers that meets SLOs. Our serving engine disaggregates the VLM and ADiT stages within a GPU via two streams, dynamically restricting the SMs on VLM stream so ADiT always finds SMs to run alongside it, and co-locates multiple models by sharing these streams across them, prioritizing requests by least remaining SLO time. Our management engine enables flexible model placements on multi-GPU servers, and integrates an intelligent traffic controller that maximizes per-model batching under the chosen placement while bounding each GPU's load to meet SLOs. For individual models, Robion serves on average 6.7$\times$ and 1.5$\times$ higher robot load within 98% SLO attainment over vLLM-Omni, the most widely used multi-stage serving system, and Monolithic, which runs VLM and ADiT as a single pipeline, respectively. In a large-scale experiment of serving 8 different models on a 4-GPU server, Robion can serve up to 64 robots within 98% SLO attainment.
