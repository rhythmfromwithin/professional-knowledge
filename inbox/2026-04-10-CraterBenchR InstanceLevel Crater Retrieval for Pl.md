---
title: "CraterBench-R: Instance-Level Crater Retrieval for Planetary Scale"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.06245
priority: medium
status: unread
interest: medium
next_step: skim
---
# CraterBench-R: Instance-Level Crater Retrieval for Planetary Scale
> 原文: [https://arxiv.org/abs/2604.06245](https://arxiv.org/abs/2604.06245)

arXiv:2604.06245v1 Announce Type: new
Abstract: Impact craters are a cornerstone of planetary surface analysis. However, while most deep learning pipelines treat craters solely as a detection problem, critical scientific workflows such as catalog deduplication, cross-observation matching, and morphological analog discovery are inherently retrieval tasks. To address this, we formulate crater analysis as an instance-level image retrieval problem and introduce CraterBench-R, a curated benchmark featuring about 25,000 crater identities with multi-scale gallery views and manually verified queries spanning diverse scales and contexts. Our baseline evaluations across various architectures reveal that self-supervised Vision Transformers (ViTs), particularly those with in-domain pretraining, dominate the task, outperforming generic models with significantly more parameters. Furthermore, we demonstrate that retaining multiple ViT patch tokens for late-interaction matching dramatically improves accuracy over standard single-vector pooling. However, storing all tokens per image is operationally inefficient at a planetary scale. To close this efficiency gap, we propose instance-token aggregation, a scalable, training-free method that selects K seed tokens, assigns the remaining tokens to these seeds via cosine similarity, and aggregates each cluster into a single representative token. This approach yields substantial gains: at K=16, aggregation improves mAP by 17.9 points over raw token selection, and at K=64, it matches the accuracy of using all 196 tokens with significantly less storage. Finally, we demonstrate that a practical two-stage pipeline, with single-vector shortlisting followed by instance-token reranking, recovers 89-94% of the full late-interaction accuracy while searching only a small candidate set. The benchmark is publicly available at hf.co/datasets/jfang/CraterBench-R.
