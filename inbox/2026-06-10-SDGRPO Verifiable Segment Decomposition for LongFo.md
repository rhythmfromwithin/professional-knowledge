---
interest: medium
link: https://arxiv.org/abs/2606.09871
next_step: skim
priority: medium
slack_ts: '1781065412.786879'
source: cs.CV - Computer Vision
status: unread
title: 'SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation'
---
# SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation
> 原文: [https://arxiv.org/abs/2606.09871](https://arxiv.org/abs/2606.09871)

arXiv:2606.09871v1 Announce Type: new
Abstract: Group Relative Policy Optimization (GRPO) and its variants, originally developed for Large Language Models (LLMs), have recently been applied to Multimodal LLMs and produced strong results. However, their coarse-grained holistic credit assignment from a single scalar advantage underfits vision-language (VL) tasks, where outputs are often long-form responses grounded in semantically rich images. To address this limitation, we exploit a structured signal that single-scalar formulations discard: the natural segmentation of long-form VL outputs. Concretely, we propose Segment-Decomposed GRPO (SD-GRPO), which z-normalizes verifiable per-segment rewards across the rollout group, yielding a vector of per-segment advantages in place of a single scalar. We evaluate SD-GRPO across three settings spanning controlled and real-world long-form VL generation, organized by increasing semantic entanglement across segments. On a controlled multi-panel dense-captioning task constructed from DOCCI, where segments are semantically independent, SD-GRPO consistently outperforms the GRPO baseline, with larger gains at higher segment counts. Extending to a controlled multi-chart long-form VQA task constructed from MultiChartQA, we show both theoretically and empirically that rollout-level rewards suffer from cross-segment credit misattribution that scales with output length. On a real-world scientific figure captioning task on the MMSci dataset, where subfigure captions share context across the figure, blending holistic and per-segment rewards further improves on both, suggesting per-segment normalization alone is insufficient when segments are semantically entangled. Finally, by integrating SD-GRPO into Dr. GRPO, we confirm that it can be applied to any GRPO framework with minimal implementation overhead to enhance long-form VL generation.
