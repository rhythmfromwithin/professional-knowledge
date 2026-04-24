---
interest: medium
link: https://arxiv.org/abs/2604.19891
next_step: skim
priority: low
slack_ts: '1777001713.779099'
source: cs.CR - Cryptography and Security
status: unread
title: A Data-Free Membership Inference Attack on Federated Learning in Hardware Assurance
---
# A Data-Free Membership Inference Attack on Federated Learning in Hardware Assurance
> 原文: [https://arxiv.org/abs/2604.19891](https://arxiv.org/abs/2604.19891)

arXiv:2604.19891v1 Announce Type: new
Abstract: Federated Learning (FL) is an emerging solution to the data scarcity problem for training deep learning models in hardware assurance. While FL is designed to enhance privacy by not sharing raw data, it remains vulnerable to Membership Inference Attacks (MIAs) that can leak sensitive intellectual property (IP). Traditional MIAs are often impractical in this domain because they require access to auxiliary datasets that can match the unique statistical properties of private data. This paper introduces a novel, data-free MIA targeting image segmentation models in FL for hardware assurance. Our methodology leverages Standard Cell Library Layouts (SCLLs) as priors to guide a gradient inversion attack, allowing an adversary to reconstruct images from a client's intercepted model update without needing any private data. We demonstrate that, by analyzing the reconstruction fidelity, an adversary can infer sensitive hardware characteristics, successfully distinguishing between circuit layers (e.g., metal vs. diffusion) and technology nodes (e.g., 32nm vs. 90nm). Our findings reveal that a novel loss term can conditionally amplify the attack's effectiveness by overcoming evaluation bottlenecks for structurally complex data. This work underscores a significant IP risk, challenging the assumption that FL provides inherent privacy guarantees and proving that severe information leakage can occur even without access to domain-specific datasets.
