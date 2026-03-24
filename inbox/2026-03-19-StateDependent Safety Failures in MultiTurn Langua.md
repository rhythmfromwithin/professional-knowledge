---
interest: medium
link: https://arxiv.org/abs/2603.15684
next_step: skim
priority: low
slack_ts: '1774320340.577309'
source: cs.CR - Cryptography and Security
status: unread
title: State-Dependent Safety Failures in Multi-Turn Language Model Interaction
---
# State-Dependent Safety Failures in Multi-Turn Language Model Interaction
> 原文: [https://arxiv.org/abs/2603.15684](https://arxiv.org/abs/2603.15684)

arXiv:2603.15684v1 Announce Type: new
Abstract: Safety alignment in large language models is typically evaluated under isolated queries, yet real-world use is inherently multi-turn. Although multi-turn jailbreaks are empirically effective, the structure of conversational safety failure remains insufficiently understood. In this work, we study safety failures from a state-space perspective and show that many multi-turn failures arise from structured contextual state evolution rather than isolated prompt vulnerabilities. We introduce STAR, a state-oriented diagnostic framework that treats dialogue history as a state transition operator and enables controlled analysis of safety behavior along interaction trajectories. Rather than optimizing attack strength, STAR provides a principled probe of how aligned models traverse the safety boundary under autoregressive conditioning. Across multiple frontier language models, we find that systems that appear robust under static evaluation can undergo rapid and reproducible safety collapse under structured multi-turn interaction. Mechanistic analysis reveals monotonic drift away from refusal-related representations and abrupt phase transitions induced by role-conditioned context. Together, these findings motivate viewing language model safety as a dynamic, state-dependent process defined over conversational trajectories.
