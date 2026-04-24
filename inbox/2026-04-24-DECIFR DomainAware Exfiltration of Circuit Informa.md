---
title: "DECIFR: Domain-Aware Exfiltration of Circuit Information from Federated Gradient Reconstruction"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.19915
priority: low
status: unread
interest: medium
next_step: skim
---
# DECIFR: Domain-Aware Exfiltration of Circuit Information from Federated Gradient Reconstruction
> 原文: [https://arxiv.org/abs/2604.19915](https://arxiv.org/abs/2604.19915)

arXiv:2604.19915v1 Announce Type: new
Abstract: Federated Learning (FL) is a promising approach for multiparty collaboration as a privacy-preserving technique in hardware assurance, but its security against adversaries with domain-specific knowledge is underexplored. This paper demonstrates a critical vulnerability where available standard cell library layouts (SCLL) can be exploited to compromise the privacy of sensitive integrated circuit (IC) training data. We introduce DECIFR, a novel two-stage Membership Inference Attack (MIA) that requires no auxiliary dataset. The attack employs a guided Gradient Inversion Attack (GIA) to reconstruct a client's training images from intercepted model updates. Our findings reveal that the fidelity of these reconstructions directly correlates with membership status, allowing an adversary to reliably distinguish members from non-members based on image quality. This work exposes a practical threat that overcomes the limitations of conventional attacks and underscores that standard FL protocols are insufficient for securing domains with extensive knowledge. We conclude that robust defenses are essential for the secure application of FL in hardware assurance.
