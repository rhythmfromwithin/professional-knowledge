---
interest: medium
link: https://arxiv.org/abs/2610.00045
next_step: skim
priority: high
slack_ts: '1791091836.856039'
source: cs.CL - Computation and Language (NLP)
status: unread
title: SCM-based Fairness and Faithful Explainability for Legal Document Classification
---
# SCM-based Fairness and Faithful Explainability for Legal Document Classification
> 原文: [https://arxiv.org/abs/2610.00045](https://arxiv.org/abs/2610.00045)

arXiv:2610.00045v1 Announce Type: new
Abstract: Transformer models such as LegalBERT are increasingly used in legal decision support, raising concerns about both fairness and the transparency of model explanations. These properties are usually evaluated separately, leaving open whether a debiasing intervention that changes fairness also changes how faithfully explanations reflect model reasoning. This study investigates that relationship on the ECtHR alleged-violations corpus from LexGLUE. It compares a LegalBERT baseline with a fairness-regularized variant that penalizes stereotypical warmth and competence representations during fine-tuning. The evaluation covers predictive performance, demographic fairness, and SHAP explanation faithfulness across five random seeds. At the performance-optimal regularization strength, the intervention does not reduce demographic disparity. This null result holds across two fairness definitions and a conventional word-pair control on the gender axis. Classification performance is largely unchanged. However, the intervention consistently degrades explanation sufficiency across all five seeds and three thresholds. A shuffled-pair control reproduces this degradation while leaving performance and fairness unchanged, indicating that the effect arises from contrastive representational regularization rather than specifically from the warmth and competence structure. The results demonstrate a dissociation between fairness and explanation faithfulness: changes in explanation behavior do not necessarily indicate changes in fairness, and fairness must therefore be evaluated directly.
