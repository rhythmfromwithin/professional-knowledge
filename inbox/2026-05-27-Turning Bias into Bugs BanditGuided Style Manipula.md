---
title: "Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.26156
priority: low
status: unread
interest: medium
next_step: skim
---
# Turning Bias into Bugs: Bandit-Guided Style Manipulation Attacks on LLM Judges
> 原文: [https://arxiv.org/abs/2605.26156](https://arxiv.org/abs/2605.26156)

arXiv:2605.26156v1 Announce Type: new
Abstract: The known stylistic biases in LLM judges, such as a preference for verbosity or specific sentence structures, present an underexplored security vulnerability. In this work, we introduce BITE (BIas exploraTion and Exploitation), a black-box adversarial framework that learns semantics-preserving edits to mislead an LLM judge and artificially inflate the scores it assigns. We cast the selection of stylistic edits as a contextual bandit problem and use a LinUCB policy to adaptively choose edits that maximize the judge's score without access to model parameters or gradients. Empirically, we test BITE across a diverse range of LLM judges and tasks, including both pointwise and pairwise comparisons on chatbot leaderboards and AI-reviewer benchmarks. BITE achieves an attack success rate exceeding 65% and raises scores by 1-2 points on a 9-point scale, all while preserving semantic equivalence. We further assess the attack's stealthiness, showing that BITE evades standard style-control methods and several detection baselines. Our findings expose a fundamental weakness in the LLM-as-a-judge paradigm and motivate robust, attack-aware evaluation. Our code is available at https://github.com/xianglinyang/llm-as-a-judge-attack.
