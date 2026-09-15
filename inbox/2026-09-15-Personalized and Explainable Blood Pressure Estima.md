---
title: "Personalized and Explainable Blood Pressure Estimation from PPG via Hybrid CNN--Morphological Features"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.13190
priority: medium
status: unread
interest: medium
next_step: skim
---
# Personalized and Explainable Blood Pressure Estimation from PPG via Hybrid CNN--Morphological Features
> 原文: [https://arxiv.org/abs/2609.13190](https://arxiv.org/abs/2609.13190)

arXiv:2609.13190v1 Announce Type: new
Abstract: Continuous cuffless blood pressure (BP) monitoring using photoplethysmography (PPG) offers a promising solution for personalized healthcare. However, existing methods have two major limitations. Handcrafted feature-based approaches rely on precise fiducial point detection and are limited to short-term analysis, while deep learning models, despite their accuracy, often operate as black boxes with limited physiological interpretability. To address these challenges, we propose a physiology-guided hybrid framework for personalized BP estimation that couples a convolutional neural network (CNN) branch capturing global and local waveform dynamics with a morphology-prior branch that explicitly encodes person-specific vascular characteristics. By embedding a morphology-based feature set that explicitly encodes individual vascular characteristics, the proposed framework enhances personalization and reduces dependence on large-scale training datasets. Evaluated on a subset of the MIMIC-III database under a subject-specific (personalized) testing protocol, the proposed personalized physiology-guided hybrid approach achieved mean absolute errors (MAEs) of 3.77 mmHg for systolic BP and 2.36 mmHg for diastolic BP, corresponding to relative improvements of 43.7% and 32.4% over a subject-specific (personalized) CNN-only baseline. SHAP-based analysis confirmed that the introduced morphology-prior features align with individual vascular characteristics, reinforcing per-subject interpretability. These findings highlight the potential of personalized, physiology-guided hybrid learning with novel morphological descriptors for accurate and explainable BP monitoring in real-world settings.
