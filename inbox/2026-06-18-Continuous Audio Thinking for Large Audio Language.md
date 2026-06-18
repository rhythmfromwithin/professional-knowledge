---
interest: medium
link: https://arxiv.org/abs/2606.18273
next_step: skim
priority: high
slack_ts: '1781759640.707229'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Continuous Audio Thinking for Large Audio Language Models
---
# Continuous Audio Thinking for Large Audio Language Models
> 原文: [https://arxiv.org/abs/2606.18273](https://arxiv.org/abs/2606.18273)

arXiv:2606.18273v1 Announce Type: new
Abstract: Large audio language models (LALMs) have shown impressive capabilities on diverse audio understanding tasks, ranging from speech transcription to music analysis. However, because LALMs are typically trained to produce text-aligned responses, their hidden states are progressively shaped for text generation rather than for preserving acoustic information. As a result, the diverse acoustic content that audio carries, such as phonetic detail, prosody, sound events, affect, and pitch, is lost along the way and difficult to leverage in the response. We introduce Continuous Audio Thinking (CoAT), a framework that equips audio language models with a continuous latent workspace for organizing acoustic information prior to response generation, grounded by distillation from audio experts. Within the thinking space, the model can utilize the rich acoustic information provided by expert distillation when generating its response. Furthermore, the proposed continuous thinking block can be processed in a single prefill, so CoAT does not require additional autoregressive decoding cost over the baseline. Across three LALMs, Qwen2-Audio, Qwen2.5-Omni-7B, and Audio Flamingo~3, performance gains on a broad benchmark suite spanning audio reasoning, audio understanding, music classification, speech emotion, and speech transcription demonstrate the effectiveness of CoAT. Further analysis confirms that the auxiliary supervision propagates from the thinking positions to the model's textual responses.
