---
title: "Bridging the Missing-Modality Gap: Improving Text-Only Calibration of Vision Language Models"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.12517
priority: high
status: unread
interest: medium
next_step: skim
---
# Bridging the Missing-Modality Gap: Improving Text-Only Calibration of Vision Language Models
> 原文: [https://arxiv.org/abs/2605.12517](https://arxiv.org/abs/2605.12517)

arXiv:2605.12517v1 Announce Type: new
Abstract: Vision-language models (VLMs) are often deployed on text-only inputs, although they are trained with images. We find that removing the vision modality causes large drops in accuracy and severe miscalibration, and the model does not behave like its original language backbone under text-only prompting. This failure is not explained only by missing semantic information. Even when text descriptions preserve key content, confidence becomes unreliable, while adding a visual signal through generated images partially restores accuracy and calibration. We propose the Latent Imagination Module (LIM), a lightweight cross-attention module that predicts imagined latent embeddings from textual input and feeds them into a frozen VLM backbone without pixel-level image synthesis. Across text-only benchmarks, unseen tasks, and missing-image scenarios, LIM improves accuracy and reduces calibration error. These results suggest that latent modality completion is a practical approach for reliable VLM inference under missing-modality.
