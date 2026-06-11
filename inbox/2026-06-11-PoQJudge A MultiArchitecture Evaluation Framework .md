---
interest: medium
link: https://arxiv.org/abs/2606.11196
next_step: skim
priority: high
slack_ts: '1781153120.892409'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality
  in Decentralized LLM Inference'
---
# PoQ-Judge: A Multi-Architecture Evaluation Framework for Cost-Aware Proof-of-Quality in Decentralized LLM Inference
> 原文: [https://arxiv.org/abs/2606.11196](https://arxiv.org/abs/2606.11196)

arXiv:2606.11196v1 Announce Type: new
Abstract: Decentralized LLM inference networks need lightweight, reference-free quality evaluation for Proof of Quality (PoQ). We present PoQ-Judge, a framework that trains dedicated judge models to score query-output pairs without ground-truth references. We study three architectures across the quality-cost tradeoff: a TextCNN judge, a MiniLM cross-encoder, and a DeBERTa judge. Using two-stage training on UltraFeedback plus GPT-labeled in-domain data, the best model reaches 0.747 Pearson correlation with the ground-truth proxy on a held-out test set, outperforming reference-based evaluators from prior work. As a reference-free component in composite scoring, it achieves 0.645 Pearson correlation, matching the best single reference-based evaluator while removing the need for reference answers. We also show that online calibration identifies semantic quality as the dominant dimension and that cascade evaluation reduces cost by 72.7 percent with only modest quality loss. Results are much stronger on QA than summarization, pointing to proxy quality as the main remaining limitation.
