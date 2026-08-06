---
title: "NeuroMosaic: Anatomically Grounded Multimodal Large Language Modeling for Molecularly Aware Glioma Reasoning from 3D MRI and Clinical Narratives"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2608.03187
priority: low
status: unread
interest: medium
next_step: skim
---
# NeuroMosaic: Anatomically Grounded Multimodal Large Language Modeling for Molecularly Aware Glioma Reasoning from 3D MRI and Clinical Narratives
> 原文: [https://arxiv.org/abs/2608.03187](https://arxiv.org/abs/2608.03187)

arXiv:2608.03187v1 Announce Type: new
Abstract: Multimodal medical large language models remain structurally weak for neuro-oncology because volumetric evidence is compressed into generic visual tokens and diagnostic conclusions often lack an auditable link to MRI regions. We present NeuroMosaic, a 3D multimodal language model that converts multi-sequence brain MRI into anatomy-indexed regional tokens, aligns them with clinical narrative and molecular concepts, and generates evidence-linked outputs. The architecture combines a multi-resolution volumetric tokenizer, a neuroanatomical graph router, a molecular concept memory, and selective risk control. Across four glioma cohorts, NeuroMosaic achieved an internal subtype macro-F1 of 0.827 and external macro-F1 values of 0.784, 0.761, and 0.742. On UPenn-GBM, it improved over the strongest matched-input baseline by 3.6 percentage points (95% CI: 1.8 to 5.4, adjusted p = 0.0018), with IDH, 1p/19q, and MGMT AUROCs of 0.918, 0.861, and 0.781. Evidence pointing accuracy reached 0.703, and targeted evidence deletion reduced correct-answer probability by 0.187, compared with 0.046 for random deletion. These results establish anatomy-indexed routing as a measurable mechanism for accurate, grounded, and calibrated volumetric medical-language reasoning.
