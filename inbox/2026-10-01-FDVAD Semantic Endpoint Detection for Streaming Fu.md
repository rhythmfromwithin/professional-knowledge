---
interest: medium
link: https://arxiv.org/abs/2609.35791
next_step: skim
priority: high
slack_ts: '1791003461.285359'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'FD-VAD: Semantic Endpoint Detection for Streaming Full-Duplex Speech'
---
# FD-VAD: Semantic Endpoint Detection for Streaming Full-Duplex Speech
> 原文: [https://arxiv.org/abs/2609.35791](https://arxiv.org/abs/2609.35791)

arXiv:2609.35791v1 Announce Type: new
Abstract: Natural turn-taking in full-duplex voice interaction requires determining from partial speech whether a pause reflects hesitation or a completed conversational intent. Acoustic voice activity detection lacks this semantic information, while cascaded ASR-based endpointing introduces transcription dependence and additional processing stages. We formulate semantic endpoint detection as a causal audio-language reasoning task and introduce FD-VAD, an ASR-free streaming endpointer that maps bounded causal audio windows directly to Continue/Stop decisions. FD-VAD combines a frozen speech encoder with a lightweight modality adapter and a parameter-efficiently adapted language model, using a last-chunk training objective for streaming inference. We further introduce confidence-gated endpoint commitment to control interruption versus delay and boundary-focused hard-negative sampling to improve decisions around ambiguous turn boundaries. Across in-domain and conversational evaluations, FD-VAD outperforms strong streaming and non-streaming semantic turn classifiers, and achieves the highest EOT recall among qualifying systems on TurnBench dev set $0.853$ (at FP<=0.10) in a zero-shot setting. These results show that semantic endpointing can be performed directly from streaming audio without intermediate ASR or dialogue state tracking.
