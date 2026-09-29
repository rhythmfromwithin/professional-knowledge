---
interest: medium
link: https://arxiv.org/abs/2609.31784
next_step: skim
priority: high
slack_ts: '1790659468.813429'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Witeness Overlap: Directional Provenance Inside Open-Weight Model Families'
---
# Witeness Overlap: Directional Provenance Inside Open-Weight Model Families
> 原文: [https://arxiv.org/abs/2609.31784](https://arxiv.org/abs/2609.31784)

arXiv:2609.31784v1 Announce Type: new
Abstract: Open-weight models are often released, fine-tuned, aligned, merged, and re-released, making provenance audits ask not only whether checkpoints are related, but also which checkpoint came first. Many existing model-provenance methods are designed for a base-known audit setting: given a victim or source model, they test whether a suspect model is related to it. Although these audits are framed as source-to-suspect tests, their underlying evidence is often symmetric, relying on representation similarity, weight similarity, behavioral fingerprints, or correlation statistics. Symmetric pairwise comparisons can detect relatedness, but they cannot by themselves orient relationship between checkpoints A and B. We therefore introduce a local geometric comparison: instead of comparing two checkpoints directly, we add a third same-family checkpoint as a witness and compare the geometry around each candidate endpoint. Direction is inferred by asking which candidate behaves more like a branching parent. Motivated by this idea, and by the empirically observed asymmetry between parent-anchored and child-anchored witness-overlap distributions, we propose Witness Overlap, a prompt-free, training-free white-box test for directional provenance. On 176 LLM checkpoints from 16 families, our one-witness test orients 95.3\% of parent-child decisions using Frobenius cosine. We further evaluate root identification, sibling discrimination, generalizations to VLM and diffusion families, and chain-structured ordering. The signal is robust to weight noise and sparse pruning, with a proposed SVD weight reduction variant showing greater robustness than Frobenius cosine.
