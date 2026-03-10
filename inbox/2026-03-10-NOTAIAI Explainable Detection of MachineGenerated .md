---
title: "NOTAI.AI: Explainable Detection of Machine-Generated Text via Curvature and Feature Attribution"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2603.05617
priority: high
status: unread
interest: medium
next_step: skim
---
# NOTAI.AI: Explainable Detection of Machine-Generated Text via Curvature and Feature Attribution
> 原文: [https://arxiv.org/abs/2603.05617](https://arxiv.org/abs/2603.05617)

arXiv:2603.05617v1 Announce Type: new
Abstract: We present NOTAI.AI, an explainable framework for machine-generated text detection that extends Fast-DetectGPT by integrating curvature-based signals with neural and stylometric features in a supervised setting. The system combines 17 interpretable features, including Conditional Probability Curvature, ModernBERT detector score, readability metrics, and stylometric cues, within a gradient-boosted tree (XGBoost) meta-classifier to determine whether a text is human- or AI-generated. Furthermore, NOTAI.AI applies Shapley Additive Explanations (SHAP) to provide both local and global feature-level attribution. These attributions are further translated into structured natural-language rationales through an LLM-based explanation layer, which enables user-facing interpretability. The system is deployed as an interactive web application that supports real-time analysis, visual feature inspection, and structured evidence presentation. A web interface allows users to input text and inspect how neural and statistical signals influence the final decision. The source code and demo video are publicly available to support reproducibility.
