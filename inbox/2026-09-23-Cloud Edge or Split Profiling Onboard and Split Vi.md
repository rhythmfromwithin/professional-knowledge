---
interest: medium
link: https://arxiv.org/abs/2609.25415
next_step: skim
priority: medium
slack_ts: '1790223761.765309'
source: cs.DC - Distributed Computing
status: unread
title: Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment
  for Drone AI
---
# Cloud, Edge, or Split? Profiling Onboard and Split Vision-Language Model Deployment for Drone AI
> 原文: [https://arxiv.org/abs/2609.25415](https://arxiv.org/abs/2609.25415)

arXiv:2609.25415v1 Announce Type: new
Abstract: Vision-Language Models (VLMs) enable edge devices like unmanned aerial vehicles (UAVs) to interpret visual observations and reason about complex environments using natural-language instructions. However, their practical deployment remains challenging as onboard inference is constrained by limited computational, memory, and energy resources, whereas cloud-based inference introduces communication latency, bandwidth overhead, and dependence on network connectivity. To address these limitations, split computing offers a promising alternative by partitioning VLM inference between the resource-constrained UAVs and more capable remote servers. However, the performance trade-offs among fully onboard, cloud-based, and split-computing architectures for lightweight VLMs have not yet been systematically profiled. This paper benchmarks these three deployment paradigms using SmolVLM-256M as a representative lightweight VLM. We quantify their inference latency, computational resource utilization, communication overhead, and energy consumption across varying image resolutions and network conditions. Our results show that no deployment strategy is universally optimal; instead, the preferred strategy depends on the interaction between network conditions and input image resolution.
