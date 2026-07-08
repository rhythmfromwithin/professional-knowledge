---
title: "RES-DARE: Failure-Aware Expert Adaptation and Rollback-Safe Self-Repair for Intrusion Detection"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.02687
priority: low
status: unread
interest: medium
next_step: skim
---
# RES-DARE: Failure-Aware Expert Adaptation and Rollback-Safe Self-Repair for Intrusion Detection
> 原文: [https://arxiv.org/abs/2607.02687](https://arxiv.org/abs/2607.02687)

arXiv:2607.02687v1 Announce Type: new
Abstract: Intrusion detection systems are often trained under static benchmark conditions, although deployed network environments are affected by traffic drift, sensor noise, changing workloads, and evolving attack behaviour. Under such distribution shifts, static detectors may produce confident but incorrect predictions, leading to silent and unsafe failure modes. In this paper, RES-DARE (Recursive Evolving Specialists-Digital Adaptive Reasoning Engine) is proposed as a failure-aware continual intrusion detection framework with rollback-safe self-repair. Difficult, uncertain, and misclassified samples are treated as failure signals for expert specialisation rather than being discarded as noise. A supervised contrastive encoder, two-pass expert router, failure-buffer mechanism, HDBSCAN-based failure-region discovery, and trust-risk monitor are integrated to support adaptive IDS behaviour. AEHM-v2 is introduced as a rollback-safe repair mechanism, where candidate adaptations are provisionally activated and committed only when macro-F1 is preserved or improved while trust risk remains stable. Otherwise, the system is rolled back to its last validated state. RES-DARE is evaluated on CICIDS2017, UNSW-NB15, and TON\\_IoT, achieving macro-F1 scores of 0.9850, 0.9736, and 0.9691, respectively. Under Gaussian feature corruption at strength 0.10, RES-DARE retains an Attack-F1 of 0.7920 on CICIDS2017 and achieves near-zero catastrophic forgetting with F = 0.0015. The results show that RES-DARE improves robustness, warning capability, and deployment safety under degraded conditions.
