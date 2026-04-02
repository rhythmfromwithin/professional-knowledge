---
interest: medium
link: https://arxiv.org/abs/2603.26498
next_step: skim
priority: medium
slack_ts: '1775098514.904149'
source: cs.DC - Distributed Computing
status: unread
title: 'Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language
  Model Inference'
---
# Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference
> 原文: [https://arxiv.org/abs/2603.26498](https://arxiv.org/abs/2603.26498)

arXiv:2603.26498v1 Announce Type: new
Abstract: Multimodal Large Language Models (MLLMs) power platforms like ChatGPT, Gemini, and Copilot, enabling richer interactions with text, images, and videos. These heterogeneous workloads introduce additional inference stages, such as vision preprocessing and encoding, that inflate latency and memory demand. Existing LLM serving systems, optimized for text-only workloads, fail under multimodality: large requests (e.g., videos) monopolize resources, causing severe head-of-line blocking and performance degradation. Our key insight is that multimodal requests differ by orders of magnitude in resource demands, which we capture through a simple abstraction: videos behave like rocks, images like pebbles, and text like sand. We design RPS-Serve, a modality-aware scheduler that lets sand flow quickly through pebbles and rocks, ensuring interactive responsiveness while avoiding starvation. RPS-Serve classifies requests, prioritizes them dynamically, and applies aging to avoid starvation. Evaluation across state-of-the-art MLLMs shows that RPS-Serve reduces, on average, time-to-first-token (TTFT) by 54% overall, and by 78.5% for latency-critical requests, compared to current systems. RPS-Serve delivers LLM-like responsiveness for MLLMs, with modality-aware scheduling and by making the most efficient use of the available resources.
