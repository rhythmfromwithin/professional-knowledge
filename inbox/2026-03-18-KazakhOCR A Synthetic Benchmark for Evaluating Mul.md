---
title: "KazakhOCR: A Synthetic Benchmark for Evaluating Multimodal Models in Low-Resource Kazakh Script OCR"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.13238
priority: medium
status: unread
interest: medium
next_step: skim
---
# KazakhOCR: A Synthetic Benchmark for Evaluating Multimodal Models in Low-Resource Kazakh Script OCR
> 原文: [https://arxiv.org/abs/2603.13238](https://arxiv.org/abs/2603.13238)

arXiv:2603.13238v1 Announce Type: new
Abstract: Kazakh is a Turkic language using the Arabic, Cyrillic, and Latin scripts, making it unique in terms of optical character recognition (OCR). Work on OCR for low-resource Kazakh scripts is very scarce, and no OCR benchmarks or images exist for the Arabic and Latin scripts. We construct a synthetic OCR dataset of 7,219 images for all three scripts with font, color, and noise variations to imitate real OCR tasks. We evaluated three multimodal large language models (MLLMs) on a subset of the benchmark for OCR and language identification: Gemma-3-12B-it, Qwen2.5-VL-7B-Instruct, and Llama-3.2-11B-Vision-Instruct. All models are unsuccessful with Latin and Arabic script OCR, and fail to recognize the Arabic script as Kazakh text, misclassifying it as Arabic, Farsi, and Kurdish. We further compare MLLMs with a classical OCR baseline and find that while traditional OCR has lower character error rates, MLLMs fail to match this performance. These findings show significant gaps in current MLLM capabilities to process low-resource Abjad-based scripts and demonstrate the need for inclusive models and benchmarks supporting low-resource scripts and languages.
