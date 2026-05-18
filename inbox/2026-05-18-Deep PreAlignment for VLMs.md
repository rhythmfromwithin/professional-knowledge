---
interest: medium
link: https://arxiv.org/abs/2605.15300
next_step: skim
priority: medium
slack_ts: '1779077927.279149'
source: cs.CV - Computer Vision
status: unread
title: Deep Pre-Alignment for VLMs
---
# Deep Pre-Alignment for VLMs
> 原文: [https://arxiv.org/abs/2605.15300](https://arxiv.org/abs/2605.15300)

arXiv:2605.15300v1 Announce Type: new
Abstract: Most Vision Language Models (VLMs) directly map outputs from ViT encoders to the LLM via a lightweight projector. While effective, recent analysis suggests this architecture suffers from an alignment challenge: visual features remain distant from the text space in the initial layers of the LLM, forcing the model to waste critical depth~\cite{zhang-etal-2024-investigating,artzy-schwartz-2024-attend} on superficial modality alignment rather than deep understanding and complex reasoning. In this work, we propose Deep Pre-Alignment (DPA), a novel architecture that replaces the standard ViT encoder with a small VLM as perceiver, ensuring visual features are deeply aligned with the text space of the target large language model. Comprehensive experiments demonstrate the effectiveness of DPA. On the 4B parameter scale, DPA outperforms baselines by 1.9 points across 8 multimodal benchmarks, with gains widening to 3.0 points at the 32B scale. Moreover, by offloading alignment to the perceiver, DPA achieves a 32.9\% reduction in language capability forgetting over 3 text benchmarks. We further demonstrate that these gains are consistent across different LLM families including Qwen3 and LLaMA 3.2, highlighting the generality of our approach. Beyond performance, DPA also offers a seamless upgrade path for current VLM development, requiring only a modular replacement for the visual encoder with marginal computation overhead.
