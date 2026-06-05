---
title: "Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2606.05233
priority: low
status: unread
interest: medium
next_step: skim
---
# Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming
> 原文: [https://arxiv.org/abs/2606.05233](https://arxiv.org/abs/2606.05233)

arXiv:2606.05233v1 Announce Type: new
Abstract: Recent computer-using-agent (CUA) red-teaming papers report prompt-injection attack success rates (ASR) of 42-98%, but these headline numbers cluster on retired models and on the most-vulnerable model in each paper's panel. We ask whether those techniques, reproduced as hand-crafted templates, still work against current frontier CUAs. We release CUA-HandCrafted, a public benchmark of 793 episodes spanning 24 multi-step web tasks, 56 attack templates, 8 attack families, and 4 system-prompt configurations. Against Claude Sonnet 4.6 and GPT-5.4 we measure 0/140 multi-step attack success (Clopper-Pearson 95% upper bound 2.60%); a prompt ablation shows this resistance lives in the model weights. Yet it does not generalize: on a sister coding-agent benchmark (SkillBench), the same weights fall to hand-crafted skill-injection at up to 100%. We argue that the literature's high ASR is largely attributable to RL-optimized injection text rather than the attack categories, and that frontier safety hardening is domain-conditioned, specific to the heavily-targeted browser surface. Reporting techniques without releasing the optimized strings, or extrapolating browser-domain safety to other CUA modalities, makes published ASR numbers unreproducible.
