---
interest: medium
link: https://arxiv.org/abs/2605.00832
next_step: skim
priority: medium
slack_ts: '1778125807.162589'
source: cs.CV - Computer Vision
status: unread
title: Synthetic Designed Experiments for Diagnosing Vision Model Failure
---
# Synthetic Designed Experiments for Diagnosing Vision Model Failure
> 原文: [https://arxiv.org/abs/2605.00832](https://arxiv.org/abs/2605.00832)

arXiv:2605.00832v1 Announce Type: new
Abstract: Current synthetic data pipelines for computer vision generate images without diagnosing what the downstream model actually needs. This open-loop paradigm treats synthetic data as cheap real data, randomly sampling the generator's output space and hoping to cover the model's failure modes. We argue this fundamentally misuses synthetic data's unique property: the controllable, independent variation of scene factors.Drawing on the statistical theory of Design of Experiments (DoE), we propose Synthetic Designed Experiments for Representational Sufficiency (SDRS). SDRS treats the downstream model as a black-box system and the synthetic generator as an experimental apparatus. Using fractional factorial designs, SDRS efficiently audits a model's factor-sensitivity profile via ANOVA decomposition. It classifies failures into two actionable types: Type I gaps (coverage failures on underrepresented factor levels) and Type II gaps (reliance on spurious nuisance dependencies). The audit then prescribes targeted synthetic data to address each gap type. We validate SDRS on three experiments: (1) a controlled diagnostic on dSprites with planted biases, where the audit correctly identifies both gap types and targeted data improves accuracy from 49.9% to 79.0%; (2) a dense segmentation task on procedural scenes, where detecting background-complexity shortcuts and applying targeted data improves mIoU from 0.948 to 0.998; and (3) an entanglement detection experiment showing that the ANOVA audit identifies cross-factor contamination in imperfect generators. Finally, we show that per-factor invariance penalties can transfer sensitivity between factors, identifying an open problem for representation-level correction.
