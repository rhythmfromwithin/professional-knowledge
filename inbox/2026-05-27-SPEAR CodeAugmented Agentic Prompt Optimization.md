---
interest: medium
link: https://arxiv.org/abs/2605.26275
next_step: skim
priority: high
slack_ts: '1780028382.219649'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'SPEAR: Code-Augmented Agentic Prompt Optimization'
---
# SPEAR: Code-Augmented Agentic Prompt Optimization
> 原文: [https://arxiv.org/abs/2605.26275](https://arxiv.org/abs/2605.26275)

arXiv:2605.26275v1 Announce Type: new
Abstract: Automatic prompt engineering (APE) rewrites prompts to improve downstream task performance, but existing APE loops treat the optimizer itself as a fixed pipeline. We port the code-as-action paradigm of CodeAct (Wang et al., 2024a) to APE and propose SPEAR (Sandboxed Prompt Engineer with Active Roll-back), a free-form agentic optimizer with four tools -- evaluate, python, set\_prompt, finish -- that decides autonomously how and when to use them. The distinctive tool is the Python sandbox: the optimizer writes and executes arbitrary Python on the current evaluation DataFrame, performing structural error analysis (confusion matrices, error clustering, per group metrics) the agent itself authors. Two guardrails turn the long-horizon agent into a monotone-improving optimizer: auto-rollback on metric regression, and an optional guard metric floor. We evaluate on three industrial LLM-as-judge suites (13 judge tasks across recruiter-intake, conversational-memory, and query-refinement systems) plus seven BBH tasks and GSM8K. SPEAR wins every industrial task on the primary metric ($\kappa$ 0.857 vs 0.359 on tool-selection; F1-macro 0.815 vs 0.763 on filter-relevance; $\kappa$ 0.254 vs 0.218 on the hardest extraction dimension). On BBH-7 SPEAR averages 0.938 accuracy vs GEPA 0.628 and TextGrad 0.484. Ablations show the Python tool is the largest single lever on complex judge tasks ($\Delta \approx +0.79\kappa$ on the 5-class tool-selection judge, $\Delta \approx +0.35\kappa$ on the hardest extraction dimension when removed); its irreplaceable contribution is class-pair confusion aggregation that a long-context LLM cannot extract reliably from the raw eval DataFrame.
