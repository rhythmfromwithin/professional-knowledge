---
interest: medium
link: https://arxiv.org/abs/2607.06611
next_step: skim
priority: high
slack_ts: '1783740337.905109'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated
  Multilingual Transcripts
---
# Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts
> 原文: [https://arxiv.org/abs/2607.06611](https://arxiv.org/abs/2607.06611)

arXiv:2607.06611v1 Announce Type: new
Abstract: Automatically recognizing the sentiment, positive or negative, from speech is a challenging task, requiring both the analysis of vocal inflections and the interpretation of uttered words. Recent solutions rely on audio foundation models to solve the task, but it remains unclear if such models can take all aspects into account. To this end, we propose a multimodal solution that integrates audio and text information via cross-modal transformers, where text transcripts are automatically generated via an automatic speech recognition (ASR) tool. Moreover, we create multiple text modalities by automatically translating the transcripts into multiple languages via machine translation tools. Audio and multilingual text features are combined via a cascaded architecture comprising cross-modal transformer blocks that integrate modalities one by one. We further distill knowledge from the multimodal model, called teacher, into a unimodal (audio only) model, called student. We conduct experiments on a large-scale dataset, demonstrating that the automatically generated textual information can bring significant performance boosts in multimodal sentiment polarity classification. Our ablation study confirms that both automatic transcripts and automatic translations are helpful. Moreover, we show that the audio-only model can be enhanced via distillation, boosting performance without any computational overhead during inference. To reproduce the reported results, we publicly release our code at https://github.com/andreidurdun/cross-modal-audio-sentiment.
