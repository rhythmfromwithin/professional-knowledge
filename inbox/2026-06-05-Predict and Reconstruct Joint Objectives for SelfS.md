---
title: "Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2606.05173
priority: high
status: unread
interest: medium
next_step: skim
---
# Predict and Reconstruct: Joint Objectives for Self-Supervised Language Representation Learning
> 原文: [https://arxiv.org/abs/2606.05173](https://arxiv.org/abs/2606.05173)

arXiv:2606.05173v1 Announce Type: new
Abstract: Masked language modelling (MLM) has been the dominant pre-training objective for text encoders since BERT, yet it encourages representations that are strongly anchored to surface-form token identity rather than deeper semantic structure. Inspired by the success of Joint Embedding Predictive Architectures (JEPA) (LeCun, 2022) in vision and audio, we propose a hybrid pre-training objective that combines a JEPA-style latent-space prediction loss with a standard MLM objective over a single shared encoder. A learnable scalar parameter continuously balances the two objectives during training. We pre-train both a hybrid model and a pure-MLM baseline on English Wikipedia using identical architectures and compute budgets (NVIDIA H100). Extensive representation analysis across five GLUE benchmarks (SST-2, MRPC, MNLI, CoLA, STS-B) using four pooling strategies reveals that the hybrid encoder produces significantly more uniform embeddings (uniformity less than -0.16 vs -0.05 for MLM), exhibits richer spectral geometry under max pooling, encodes less surface-level lexical information, and achieves a better semantic-to-lexical balance. Despite similar linear-probe downstream accuracy, the geometric differences are consistent and significant, suggesting that the JEPA predictive objective reshapes the latent space in ways that standard accuracy metrics alone cannot capture.
