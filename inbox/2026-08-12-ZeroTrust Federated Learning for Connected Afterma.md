---
title: "Zero-Trust Federated Learning for Connected Aftermarket Devices"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.07591
priority: low
status: unread
interest: medium
next_step: skim
---
# Zero-Trust Federated Learning for Connected Aftermarket Devices
> 原文: [https://arxiv.org/abs/2608.07591](https://arxiv.org/abs/2608.07591)

arXiv:2608.07591v1 Announce Type: new
Abstract: Connected aftermarket devices extend vehicle diagnostics, repair workflows, and over-the-air software maintenance beyond original equipment manufacturer boundaries, yet their heterogeneous ownership and long service life complicate conventional perimeter security. This paper develops Zero Trust Federated Learning for Connected Aftermarket Devices (ZT FL CADE), an edge-learning architecture that combines device-level access control, privacy-preserving federated learning, and adversarial validation for over-the-air update and predictive maintenance decisions. The evaluation uses a single synthetic dataset of 144,000 telemetry windows from 240 devices, 12 vendor domains, and 180 days of operation. Features include bus entropy, update latency, attestation age, signature retries, environmental signals, fault-code rates, packet loss, drift, mileage, and trust score, with targets for maintenance risk, update intrusion, and access action. ZT FL CADE trains local temporal models, aggregates privacy-bounded updates, scores each device against behavioral and update integrity evidence, and routes update requests to allow, challenge, or quarantine actions. Synthetic experiments improve maintenance risk F1 from 0.837 for Fed Avg to 0.883, improve intrusion F1 from 0.856 to 0.897, and preserve 0.842 intrusion recall when 20 percent of selected clients are adversarial. Mean access-decision latency remains 44 MS, below the 100 MS operational budget used in the simulation. The results do not establish field validation, but they indicate that zero-trust policy enforcement and federated learning can be evaluated jointly rather than as separate aftermarket security controls. Index Terms Zero trust architecture, federated learning, connected aftermarket devices, over-the-air updates, adversarial machine learning, edge artificial intelligence, predictive maintenance, automotive cybersecurity
