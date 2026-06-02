---
title: "AEyeDE: An Attention-Based Attribution Framework for AI-Generated Text Detection"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2606.00016
priority: high
status: unread
interest: medium
next_step: skim
---
# AEyeDE: An Attention-Based Attribution Framework for AI-Generated Text Detection
> 原文: [https://arxiv.org/abs/2606.00016](https://arxiv.org/abs/2606.00016)

arXiv:2606.00016v1 Announce Type: new
Abstract: Detecting AI-generated text is becoming increasingly challenging as modern language models approach human-level fluency and can evade detectors that rely on surface statistics or likelihood-based signals. We propose \textsc{AEyeDE}, an attribution-driven approach to human-AI authorship detection that leverages model attention as a discriminative signal. Specifically, we extract attention-based attribution matrices for both human- and AI-generated text using a \emph{proxy} Transformer model with white-box access and train a lightweight Convolutional Neural Network to learn representations from these attribution maps. Across encoder-decoder translation settings, our method consistently outperforms a text-only baseline. In decoder-only settings, it performs strongly in generator-specific detection, remains competitive on standard benchmarks, and shows robustness under cross-dataset transfer and alternative-spelling perturbations. We further show that attention maps exhibit recurring local structures whose relative frequencies differ consistently between human- and AI-generated text across datasets and proxy models. These findings suggest that attention-based attribution maps provide a complementary and interpretable signal for AI-generated text detection. We will make the code publicly available to support future research.
