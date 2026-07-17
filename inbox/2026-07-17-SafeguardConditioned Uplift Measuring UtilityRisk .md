---
title: "Safeguard-Conditioned Uplift: Measuring Utility-Risk Frontiers for Dual-Use Biology Assistants"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2607.13039
priority: medium
status: unread
interest: medium
next_step: skim
---
# Safeguard-Conditioned Uplift: Measuring Utility-Risk Frontiers for Dual-Use Biology Assistants
> 原文: [https://arxiv.org/abs/2607.13039](https://arxiv.org/abs/2607.13039)

arXiv:2607.13039v1 Announce Type: new
Abstract: Safety evaluations for dual-use biology assistants often measure base-model capability, refusal behavior, or jailbreak success. These metrics miss a deployment question: for a fixed base model, how does the access condition users actually see change benign utility and harmful actionable assistance? I introduce safeguard-conditioned uplift, a protocol for comparing deployed access conditions through a human-judged utility-risk frontier. I evaluate Claude Sonnet 4.6 and Gemini 3.5 Flash under helpful prompting, safety prompting, and an external safeguarded assistant on a 108-task surrogate benchmark, with the headline claim restricted to a locked 18-task held-out split. In a 600-row blinded human audit, the safeguarded assistant reduces harmful actionability relative to helpful prompting by -0.063 over 49 matched response pairs, with bootstrap 95% interval [-0.117, -0.011], while correctness changes by +0.009 with interval [-0.057, +0.077]. Adaptive, Test-B, cue-ablation, and controller-baseline checks support the measurement story but also show non-dominance: safety prompting is often strongest for Claude, while external control helps more for Gemini and can reduce benign utility. The contribution is not a universal defense. It is a deployment-level evaluation target, plus a learned risk-budgeted calibration procedure, for measuring how user-facing access conditions move the utility-risk frontier.
