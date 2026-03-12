---
title: "On the Formal Limits of Alignment Verification"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.08761
priority: medium
status: unread
interest: medium
next_step: skim
---
# On the Formal Limits of Alignment Verification
> 原文: [https://arxiv.org/abs/2603.08761](https://arxiv.org/abs/2603.08761)

arXiv:2603.08761v1 Announce Type: new
Abstract: The goal of AI alignment is to ensure that an AI system reliably pursues intended objectives. A foundational question for AI safety is whether alignment can be formally certified: whether there exists a procedure that can guarantee that a given system satisfies an alignment specification. This paper studies the nature of alignment verification. We prove that no verification procedure can simultaneously satisfy three properties: soundness (no misaligned system is certified), generality (verification holds over the full input domain), and tractability (verification runs in polynomial time). Each pair of properties is achievable, but all three cannot hold simultaneously. Relaxing any one property restores the corresponding possibility, indicating that practical bounded or probabilistic assurance remains viable. The result follows from three independent barriers: the computational complexity of full-domain neural network verification, the non-identifiability of internal goal structure from behavioral observation, and the limits of finite evidence for properties defined over infinite domains. The trilemma establishes the limits of alignment certification and characterizes the regimes in which meaningful guarantees remain possible.
