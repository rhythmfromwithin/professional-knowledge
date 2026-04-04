---
title: "Safety, Security, and Cognitive Risks in World Models"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.01346
priority: low
status: unread
interest: medium
next_step: skim
---
# Safety, Security, and Cognitive Risks in World Models
> 原文: [https://arxiv.org/abs/2604.01346](https://arxiv.org/abs/2604.01346)

arXiv:2604.01346v1 Announce Type: new
Abstract: World models -- learned internal simulators of environment dynamics -- are rapidly becoming foundational to autonomous decision-making in robotics, autonomous vehicles, and agentic AI. Yet this predictive power introduces a distinctive set of safety, security, and cognitive risks. Adversaries can corrupt training data, poison latent representations, and exploit compounding rollout errors to cause catastrophic failures in safety-critical deployments. World model-equipped agents are more capable of goal misgeneralisation, deceptive alignment, and reward hacking precisely because they can simulate the consequences of their own actions. Authoritative world model predictions further foster automation bias and miscalibrated human trust that operators lack the tools to audit.
This paper surveys the world model landscape; introduces formal definitions of trajectory persistence and representational risk; presents a five-profile attacker capability taxonomy; and develops a unified threat model extending MITRE ATLAS and the OWASP LLM Top 10 to the world model stack. We provide an empirical proof-of-concept on trajectory-persistent adversarial attacks (GRU-RSSM: A\_1 = 2.26x amplification, -59.5% reduction under adversarial fine-tuning; stochastic RSSM proxy: A\_1 = 0.65x; DreamerV3 checkpoint: non-zero action drift confirmed). We illustrate risks through four deployment scenarios and propose interdisciplinary mitigations spanning adversarial hardening, alignment engineering, NIST AI RMF and EU AI Act governance, and human-factors design. We argue that world models must be treated as safety-critical infrastructure requiring the same rigour as flight-control software or medical devices.
