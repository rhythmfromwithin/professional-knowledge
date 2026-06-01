---
interest: medium
link: https://arxiv.org/abs/2605.28876
next_step: skim
priority: low
slack_ts: '1780290087.011289'
source: cs.SE - Software Engineering
status: unread
title: 'LogDx-CI: Benchmarking Log Reduction Tools for LLM Root-Cause Diagnosis'
---
# LogDx-CI: Benchmarking Log Reduction Tools for LLM Root-Cause Diagnosis
> 原文: [https://arxiv.org/abs/2605.28876](https://arxiv.org/abs/2605.28876)

arXiv:2605.28876v1 Announce Type: new
Abstract: CI failure logs are large (median 5k lines, max 200k in this corpus) and noisy. Coding agents that try to debug them depend on an upstream tool to reduce the log to a manageable context, but the field has had no public empirical comparison of which reductions preserve enough evidence for downstream LLM diagnosis. We introduce LogDx-CI, a benchmark that compares 11 context-reduction tools (raw, tail, grep, three RTK modes, two real LLM map-reduce summarizers, three hybrid routers) on 35 real GitHub Actions failure cases, scored by 3 LLM debugger families (Claude Haiku 4.5, Claude Sonnet 4.6, OpenAI gpt-5-mini) plus a Sonnet 4.6 tool-using agent. We report three load-bearing findings. (1)~Hybrid grep+tail routers dominate the cost-quality Pareto frontier; the top two methods score 0.670 / 0.666 at $\sim$ \$0.03 per case, same-ballpark quality as standalone grep at $4.5\times$ fewer tokens. (2)~In the agent-loop regime, the quality range across reduction tools collapses $7\times$ (single-shot spread 0.42 $\to$ agent-loop spread 0.059); the agent rescues weak contexts via follow-up tool calls. However, cost differences persist: weak contexts force the agent to issue 2--4$\times$ more tool calls to recover. (3)~A cross-family LLM-summary pair (gpt-5-mini summarizer feeding a Claude Haiku debugger) beats the same-family pair by $+0.071$ averaged across four diagnoser variants, falsifying the self-call-bias hypothesis on this task. The gpt-5-mini summarizer is also the agent-loop \#1 method (score 0.749) at $0.37$ tool-calls per case and $10\times$ lower reducer cost than the Haiku summarizer (\$0.18 vs \$1.75 per case). All data, code, per-case bundles, and reproducibility infrastructure are public.
