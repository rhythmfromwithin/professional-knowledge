---
interest: medium
link: https://arxiv.org/abs/2606.07577
next_step: skim
priority: high
slack_ts: '1780978312.108719'
source: cs.AI - Artificial Intelligence
status: unread
title: 'OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual
  LLMs'
---
# OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs
> 原文: [https://arxiv.org/abs/2606.07577](https://arxiv.org/abs/2606.07577)

arXiv:2606.07577v1 Announce Type: new
Abstract: Audio-visual large language models (LLMs) hold strong promise for long-form video understanding, yet their long-video inference is fundamentally limited by the linear growth of video tokens and key-value (KV) caches. We present OmniMem, a memory-efficient streaming framework designed specifically for audio-visual LLMs. Unlike existing compression methods that treat all tokens uniformly, OmniMem introduces a modality-aware memory allocation strategy that separately manages visual and audio contexts, addressing the severe token imbalance between the two modalities. OmniMem further preserves informative and non-redundant KV states through perturbation-aware memory selection, enabling compact memory without sacrificing long-range understanding. To strengthen compression under realistic deployment constraints, we also explore budget-aware fine-tuning, which encourages the model to consolidate useful information into retained memory. Experiments on VideoMME Long, LVBench, and LVOmniBench with video-SALMONN 2+ and Qwen-2.5-Omni show that OmniMem consistently improves over strong training-free compression baselines by 2-4% absolute accuracy under the same memory budgets, with an additional 1-2% gain after fine-tuning.
