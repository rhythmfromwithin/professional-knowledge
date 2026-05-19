---
title: "Reducing Hallucination in Vision-Language Models via Stage-wise Preference Optimization under Distribution Shift"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.16411
priority: low
status: unread
interest: medium
next_step: skim
---
# Reducing Hallucination in Vision-Language Models via Stage-wise Preference Optimization under Distribution Shift
> 原文: [https://arxiv.org/abs/2605.16411](https://arxiv.org/abs/2605.16411)

arXiv:2605.16411v1 Announce Type: cross
Abstract: Hallucination remains a fundamental challenge in vision-language models (VLMs), where autoregressive generation may produce linguistically plausible yet physically inconsistent or visually ungrounded responses due to likelihood maximization under joint probabilistic modeling.
We propose a stage-wise preference optimization framework for hallucination reduction through targeted multimodal data construction. Rather than directly optimizing on generic instruction-following data, our approach progressively constructs hallucination-focused preference pairs near known failure boundaries. The framework emphasizes ambiguous spatial orientation, object relationships, OCR uncertainty, and adversarial false-premise training. Hallucinated negatives are generated through minimally perturbed yet visually inconsistent alternatives, enabling Direct Preference Optimization (DPO) to better separate grounded reasoning from plausible hallucination.
Experiments on open-source benchmarks and real-world multimodal evaluation scenarios demonstrate improved grounding consistency, reduced hallucination, and more informative grounded responses. Cross-model qualitative evaluation further shows that the proposed multimodal LLM DPO framework produces more visually grounded responses than several frontier proprietary VLMs, such as in ambiguous spatial reasoning and adversarial false-premise settings. The results suggest that hallucination may arise not only from limited model capacity, but also from inherent tendencies of autoregressive probabilistic generation to favor linguistically plausible continuations under weak visual grounding. Future work may explore physical consistency modeling, uncertainty-aware multimodal reasoning, and architectural alternatives beyond standard autoregressive decoding.
