---
interest: medium
link: https://arxiv.org/abs/2604.00161
next_step: skim
priority: medium
slack_ts: '1775359520.233809'
source: cs.CV - Computer Vision
status: unread
title: 'Q-Mask: Query-driven Causal Masks for Text Anchoring in OCR-Oriented Vision-Language
  Models'
---
# Q-Mask: Query-driven Causal Masks for Text Anchoring in OCR-Oriented Vision-Language Models
> 原文: [https://arxiv.org/abs/2604.00161](https://arxiv.org/abs/2604.00161)

arXiv:2604.00161v1 Announce Type: new
Abstract: Optical Character Recognition (OCR) is increasingly regarded as a foundational capability for modern vision-language models (VLMs), enabling them not only to read text in images but also to support downstream reasoning in real-world visual question answering (VQA). However, practical applications further require reliable text anchors, i.e., accurately grounding queried text to its corresponding spatial region. To systematically evaluate this capability, we introduce TextAnchor-Bench (TABench), a benchmark for fine-grained text-region grounding, which reveals that both general-purpose and OCR-specific VLMs still struggle to establish accurate and stable text anchors. To address this limitation, we propose Q-Mask, a precise OCR framework built upon a causal query-driven mask decoder (CQMD). Inspired by chain-of-thought reasoning, Q-Mask performs causal visual decoding that sequentially generates query-conditioned visual masks before producing the final OCR output. This visual CoT paradigm disentangles where the text is from what the text is, enforcing grounded evidence acquisition prior to recognition and enabling explicit text anchor construction during inference. To train CQMD, we construct TextAnchor-26M, a large-scale dataset of image-text pairs annotated with fine-grained masks corresponding to specific textual elements, encouraging stable text-region correspondences and injecting strong spatial priors into VLM training. Extensive experiments demonstrate that Q-Mask substantially improves text anchoring and understanding across diverse visual scenes.
