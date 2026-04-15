---
interest: medium
link: https://arxiv.org/abs/2604.08693
next_step: skim
priority: medium
slack_ts: '1776223654.946169'
source: cs.CY - Computers and Society
status: unread
title: Towards Generalizable Representations of Mathematical Strategies
---
# Towards Generalizable Representations of Mathematical Strategies
> 原文: [https://arxiv.org/abs/2604.08693](https://arxiv.org/abs/2604.08693)

arXiv:2604.08693v1 Announce Type: new
Abstract: Pretrained encoders for mathematical texts have achieved significant improvements on various tasks such as formula classification and information retrieval. Yet they remain limited in representing and capturing student strategies for entire solution pathways. Previously, this has been accomplished either through labor-intensive manual labeling, which does not scale, or by learning representations tied to platform-specific actions, which limits generalizability. In this work, we present a novel approach for learning problem-invariant representations of entire algebraic solution pathways. We first construct transition embeddings by computing vector differences between consecutive algebraic states encoded by high-capacity pretrained models, emphasizing transformations rather than problem-specific features. Sequence-level embeddings are then learned via SimCSE, using contrastive objectives to position semantically similar solution pathways close in embedding space while separating dissimilar strategies. We evaluate these embeddings through multiple tasks, including multi-label action classification, solution efficiency prediction, and sequence reconstruction, and demonstrate their capacity to encode meaningful strategy information. Furthermore, we derive embedding-based measures of strategy uniqueness, diversity, and conformity that correlate with both short-term and distal learning outcomes, providing scalable proxies for mathematical creativity and divergent thinking. This approach facilitates platform-agnostic and cross-problem analyses of student problem-solving behaviors, demonstrating the effectiveness of transition-based sequence embeddings for educational data mining and automated assessment.
