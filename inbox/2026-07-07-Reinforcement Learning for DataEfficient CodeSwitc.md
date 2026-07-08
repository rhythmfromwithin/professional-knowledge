---
interest: medium
link: https://arxiv.org/abs/2607.02757
next_step: skim
priority: high
slack_ts: '1783481421.618439'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Reinforcement Learning for Data-Efficient Code-Switched ASR
---
# Reinforcement Learning for Data-Efficient Code-Switched ASR
> 原文: [https://arxiv.org/abs/2607.02757](https://arxiv.org/abs/2607.02757)

arXiv:2607.02757v1 Announce Type: new
Abstract: Audio-language models can be prompted for code-switched speech, but their decoding is not optimized for code-switching and often fails at language boundaries. We propose a practical reinforcement learning with verifiable rewards recipe for data-efficient adaptation of audio-language models to code-switched ASR using group relative policy optimization, combining an error rate reward with a script fidelity reward that penalizes wrong writing systems and a two-pass draft-and-refinement procedure. Using Qwen2-Audio as a reproducible testbed across 10 language pairs, training on only TTS code-switched speech, we show that RLVR with 10% of the data matches LoRA supervised fine-tuning trained on the full dataset, with the largest gains on typologically distant pairs. The error rate reward eliminates translation errors while the script fidelity reward separately reduces script contamination without degradation. These gains transfer zero-shot to a human-recorded code-switching corpus.
