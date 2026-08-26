---
interest: medium
link: https://arxiv.org/abs/2608.20346
next_step: skim
priority: high
slack_ts: '1787708780.114349'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Building and Evaluating a Synthetic Bengali Speech Resource for Telecom Customer
  Care
---
# Building and Evaluating a Synthetic Bengali Speech Resource for Telecom Customer Care
> 原文: [https://arxiv.org/abs/2608.20346](https://arxiv.org/abs/2608.20346)

arXiv:2608.20346v1 Announce Type: new
Abstract: Speech systems used in customer-facing applications often require domain-specific language coverage. We present a synthetic Bengali speech dataset for telecom customer-care scenarios. The dataset contains 10,000 audio-text pairs, approximately 26.82 hours of 24 kHz speech, and predefined train, validation, and test splits of 9,000, 500, and 500 examples. It is publicly released on Hugging Face under the CC-BY-4.0 license. The speech was generated with OmniVoice in voice-cloning mode using a real female reference recording and transcript, with bfloat16 precision, 16 diffusion sampling steps, and a speaking-rate control value of 1.0. Along with the original Bengali text, the dataset provides a normalized transcript field designed for ASR/STT training and evaluation. We report an automatic intelligibility check over all 10,000 samples using a domain-adapted Whisper ASR model fine-tuned from bengaliAI/tugstugi\_bengaliai-regional-asr\_whisper-medium, along with a manual listening check on selected samples. The evaluation gives an average WER of 2.54%, an average CER of 0.59%, and median WER and CER values of 0.00%. These results suggest strong text-audio consistency under the selected automatic evaluation pipeline, while the paper also discusses the limitations of synthetic speech and STT-based evaluation.
