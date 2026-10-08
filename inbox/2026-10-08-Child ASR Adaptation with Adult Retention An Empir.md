---
title: "Child ASR Adaptation with Adult Retention: An Empirical Study"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2610.08827
priority: high
status: unread
interest: medium
next_step: skim
---
# Child ASR Adaptation with Adult Retention: An Empirical Study
> 原文: [https://arxiv.org/abs/2610.08827](https://arxiv.org/abs/2610.08827)

arXiv:2610.08827v1 Announce Type: new
Abstract: Automatic Speech Recognition (ASR) systems often underperform for children and non-native speakers, while adapting adult ASR models to child speech can cause adult-speech forgetting. We study child ASR adaptation with adult retention across Arabic and English. We compare full fine-tuning, LoRA, and post-hoc weight-space merging across encoder--decoder, encoder--CTC, and AudioLLM-based ASR systems. Experiments use Arabic native and non-native child speech, English MyST child speech, and adult benchmarks from MGB-2 and LibriSpeech test-clean. We evaluate recognition quality with WER and quantify the adaptation--retention trade-off using Retention Index, Child Adaptation Gain, and Adaptation Recovery. Results show that child adaptation is necessary, especially for non-native Arabic and English child speech, but direct adaptation often reduces adult ASR performance. Bilingual adaptation is more stable than language-specific adaptation. Weight-space merging often improves the trade-off, especially for encoder--CTC, Whisper, and AudioLLM-based ASR, with LERP favoring adult retention and TIES recovering stronger child gains. For the encoder--decoder model, direct bilingual fine-tuning remains strongest in raw WER.\footnote{Code, and models are available at https://github.com/qcri/Child-ASR-Adaptation.
