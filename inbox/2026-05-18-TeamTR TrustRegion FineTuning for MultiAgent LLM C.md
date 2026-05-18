---
title: "TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.15207
priority: high
status: unread
interest: medium
next_step: skim
---
# TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination
> 原文: [https://arxiv.org/abs/2605.15207](https://arxiv.org/abs/2605.15207)

arXiv:2605.15207v1 Announce Type: new
Abstract: Multi-agent LLM systems have shown promise for complex reasoning, yet recent evaluations reveal they often underperform single-model baselines. We identify a structural failure mode in sequential fine-tuning of shared-context teams: updating one agent shifts the team's context distribution, and when subsequent updates are evaluated on cached rollouts, this mismatch compounds. We formalize this as the compounding occupancy shift and prove that stale-occupancy evaluation incurs a penalty that scales quadratically with the number of agents. In contrast, intermediate-occupancy evaluation reduces this to linear scaling. We propose TeamTR, a trust-region framework that resamples trajectories after each component update and enforces per-agent divergence control, yielding rigorous per-update and per-stage improvement lower bounds. Experiments show that TeamTR outperforms single-agent and sequential baselines with 7.1% on average, mitigates coordination regressions, and supports plug-and-play component replacement. Code is available at https://github.com/Yydc/TeamTR.
