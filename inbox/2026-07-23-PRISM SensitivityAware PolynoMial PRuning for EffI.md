---
title: "PRISM: Sensitivity-Aware PolynoMial PRuning for EffIcient Neural Network Encryption"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.18342
priority: low
status: unread
interest: medium
next_step: skim
---
# PRISM: Sensitivity-Aware PolynoMial PRuning for EffIcient Neural Network Encryption
> 原文: [https://arxiv.org/abs/2607.18342](https://arxiv.org/abs/2607.18342)

arXiv:2607.18342v1 Announce Type: new
Abstract: Structured pruning is essential for making neural network inference feasible under homomorphic encryption (HE), yet its impact on model reliability has remained unexplored. This paper presents a systematic reliability characterization of pruned CKKS-encrypted neural networks and introduces Polynomial-Sensitivity-Aware Pruning (PSAP), a structured pruning method that is inherently reliability-aware. PSAP scores filters jointly by weight magnitude, polynomial activation sensitivity, and rotation cost, which concentrates pruning in fault-tolerant regions. Across two architectures, two datasets, two numerical representations, and five bit-error rates (40 full-model and 108 per-layer experiments), PSAP-pruned models limit catastrophic (>10 pp accuracy drop) layers to at most two versus 5--14 for magnitude-pruned baselines, reducing worst-case vulnerability by up to 29 times under int32 bit-flip injection. Direct CKKS encrypted fault injection indicates a safe operating boundary near BER~ 10^{-5}, supporting int32 injection as a conservative reliability proxy. The fault-critical structural layers account for only 1.1% of parameters, enabling selective hardening at minimal overhead. These reliability gains are obtained alongside competitive efficiency: PSAP reduces Halevi--Shoup rotations by up to 45.2\% on ResNet-32, and an adaptive mixed-degree allocation scheme lowers multiplicative depth from 66 to 56 levels, enabling leveled inference without bootstrapping.
