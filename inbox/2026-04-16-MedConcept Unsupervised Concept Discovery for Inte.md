---
title: "MedConcept: Unsupervised Concept Discovery for Interpretability in Medical VLMs"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.11868
priority: medium
status: unread
interest: medium
next_step: skim
---
# MedConcept: Unsupervised Concept Discovery for Interpretability in Medical VLMs
> 原文: [https://arxiv.org/abs/2604.11868](https://arxiv.org/abs/2604.11868)

arXiv:2604.11868v1 Announce Type: new
Abstract: While medical Vision-Language models (VLMs) achieve strong performance on tasks such as tumor or organ segmentation and diagnosis prediction, their opaque latent representations limit clinical trust and the ability to explain predictions. Interpretability of these multimodal representations are therefore essential for the trustworthy clinical deployment of pretrained medical VLMs. However, current interpretability methods, such as gradient- or attention-based visualizations, are often limited to specific tasks such as classification. Moreover, they do not provide concept-level explanations derived from shared pretrained representations that can be reused across downstream tasks. We introduce MedConcept, a framework that uncovers latent medical concepts in a fully unsupervised manner and grounds them in clinically verifiable textual semantics. MedConcept identifies sparse neuron-level concept activations from pretrained VLM representations and translates them into pseudo-report-style summaries, enabling physician-level inspection of internal model reasoning. To address the lack of quantitative evaluation in concept-based interpretability, we introduce a quantitative semantic verification protocol that leverages an independent pretrained medical LLM as a frozen external evaluator to assess concept alignment with radiology reports. We define three concept scores, Aligned, Unaligned, and Uncertain, to quantify semantic support, contradiction, or ambiguity relative to radiology reports and use them exclusively for post hoc evaluation. These scores provide a quantitative baseline for assessing interpretability in medical VLMs. All codes, prompt and data to be released on acceptance. Ke
