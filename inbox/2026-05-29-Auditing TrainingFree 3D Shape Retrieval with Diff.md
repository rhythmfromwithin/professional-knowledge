---
interest: medium
link: https://arxiv.org/abs/2605.29004
next_step: skim
priority: medium
slack_ts: '1780113877.075259'
source: cs.CV - Computer Vision
status: unread
title: Auditing Training-Free 3D Shape Retrieval with Diffused Geodesic Moments
---
# Auditing Training-Free 3D Shape Retrieval with Diffused Geodesic Moments
> 原文: [https://arxiv.org/abs/2605.29004](https://arxiv.org/abs/2605.29004)

arXiv:2605.29004v1 Announce Type: new
Abstract: Reported retrieval scores for training-free shape descriptors conflate local signal design, normalization, aggregation, codebook fitting, and metric choices, making isolated component evaluation difficult. This paper reframes descriptor evaluation as a {\em protocol audit}. We introduce Diffused Geodesic Moments (DGM), a seed-conditioned descriptor that computes sparse implicit heat responses, converts them to distance-like fields, and summarizes each vertex by low-order moments across seeds and scales. DGM is used both as a practical non-spectral baseline and as an instrument for isolating protocol effects. On the registered FAUST benchmark split (FAUST-Reg) and the TOSCA shape collection, aggregation-matched experiments show that an independent Geometric Moment Shape Descriptor baseline built on Heat Kernel Signature features (GMSD-HKS) obtains the highest scores in this implementation ($0.621/0.820$ and $0.865/0.963$ mean average precision (mAP)/top-1), Wave Kernel Signature (WKS) remains a strong classical signal, and DGM is useful mainly when sparse solves, non-spectral deployment, or symmetry-informative seed frames are priorities. The broader finding is methodological: the input field and aggregation protocol can dominate the moment formula. The paper contributes a reproducible protocol-cascade analysis, a cross-shape alignment diagnostic for functional-map compatibility, and concrete recommendations for designing and reporting training-free shape descriptors.
