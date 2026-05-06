---
interest: medium
link: https://arxiv.org/abs/2605.00974
next_step: skim
priority: low
slack_ts: '1778039500.956179'
source: cs.CR - Cryptography and Security
status: unread
title: 'SRTJ: Self-Evolving Rule-Driven Training-Free LLM Jailbreaking'
---
# SRTJ: Self-Evolving Rule-Driven Training-Free LLM Jailbreaking
> 原文: [https://arxiv.org/abs/2605.00974](https://arxiv.org/abs/2605.00974)

arXiv:2605.00974v1 Announce Type: new
Abstract: LLMs are increasingly equipped with safety alignment mechanisms, yet recent studies demonstrate that they remain vulnerable to jailbreaking attacks that elicit harmful behaviors without explicit policy violations. While a growing body of work has explored automated jailbreak strategies, existing methods face several fundamental challenges, including the lack of systematic utilization of both successful and failed attack experiences, as well as the absence of principled mechanisms for composing and selecting reusable attack rules under diverse constraints. As a result, existing methods struggle to accumulate transferable knowledge over time and to reliably adapt attack strategies across different targets and evolving safety mechanisms. To address these issues, we propose a Self-Evolving Rule-Driven Training-Free Jailbreak (SRTJ) framework that systematically discovers, composes, and refines attack strategies through interaction and feedback, without updating model parameters. Specifically, SRTJ couples experience-driven attack generation with answer set programming (ASP)-based rule selection and constraint-aware composition, where iterative verifier feedback is leveraged to jointly refine successful strategies and analyze failure patterns. The resulting rule memory evolves in a hierarchical multi-level manner, explicitly organizing distilled attack knowledge into long-term, middle-term, and short-term rules, thereby capturing both stable transferable strategies and transient adaptive behaviors to effectively balance exploration and exploitation across attack attempts. Extensive experiments on mainstream jailbreak benchmark (HarmBench) demonstrate that SRTJ achieves strong and stable attack performance across different target LLMs, while exhibiting improved robustness and generalization compared to existing jailbreak methods. The code is available at https://github.com/TheSolkatt/SRTJ.
