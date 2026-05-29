---
interest: medium
link: https://arxiv.org/abs/2605.23912
next_step: skim
priority: high
slack_ts: '1780028370.332679'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Raon-Speech Technical Report
---
# Raon-Speech Technical Report
> 原文: [https://arxiv.org/abs/2605.23912](https://arxiv.org/abs/2605.23912)

arXiv:2605.23912v1 Announce Type: new
Abstract: We present Raon-Speech, a top-performing 9B-parameter speech language model (SpeechLM) for English and Korean speech understanding, answering, and generation, and Raon-SpeechChat, a high-performing full-duplex extension for natural real-time conversation. Raon-Speech successfully transforms a pre-trained LLM into a SpeechLM that both understands and generates speech while preserving strong text capabilities. It trains on 1.38M hours of highly curated English and Korean speech and text datasets with the following training stages: (1) speech modules alignment, (2) end-to-end SpeechLM pre-training with knowledge distillation, and (3) multi-task preference optimization-based post-training. Across 42 English and Korean speech and text benchmarks, Raon-Speech establishes the strongest overall profile on speech-centric tasks in our comparison against eight similarly sized recent audio foundation models, including Qwen2.5-Omni and Fun-Audio-Chat, while preserving strong text question answering performance. Building upon it, Raon-SpeechChat enables natural full-duplex conversation by continual training on 119K hours of time-aligned real and synthetic dialogue data. It proceeds through three complementary training stages: (1) causal encoder adaptation, (2) full-duplex pre-training, (3) full-duplex fine-tuning for voice and role-control. On multiple full-duplex benchmarks, Raon-SpeechChat shows its clearest strengths on the turn-taking and interruption-sensitive behaviors covered by FDB v1.0, and remains competitive across the broader full-duplex evaluation suite. We open-source all model checkpoints, the training and inference pipeline, and an interactive demo.
