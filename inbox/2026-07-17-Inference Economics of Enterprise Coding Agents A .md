---
interest: medium
link: https://arxiv.org/abs/2607.13080
next_step: skim
priority: low
slack_ts: '1784344402.872039'
source: cs.SE - Software Engineering
status: unread
title: 'Inference Economics of Enterprise Coding Agents: A Case Study of Cloud vs.
  On-Premise LLMs'
---
# Inference Economics of Enterprise Coding Agents: A Case Study of Cloud vs. On-Premise LLMs
> 原文: [https://arxiv.org/abs/2607.13080](https://arxiv.org/abs/2607.13080)

arXiv:2607.13080v1 Announce Type: new
Abstract: Autonomous coding agents force engineering organizations to choose between API-based frontier models -- strong reasoning at high token cost -- and on-premise quantized open-weights models, which promise low-marginal-cost scaling and data sovereignty at some loss of reasoning fidelity. We study this trade-off through a single-developer, non-randomized longitudinal case study over two contiguous 28-day periods on a production monorepo: an API-based Claude Opus 4.7/4.8 configuration using Claude Code versus an on-premise GLM-5.1/5.2 configuration using Opencode, quantized to NVFP4, on NVIDIA Blackwell hardware. Analyzing LLM telemetry and Git history, we find that prompt caching (99.3% hit rate) cuts realized API cost by 88.6% to an effective \$0.57 per million tokens -- below even the \$2.83 amortized unit cost of the shared on-premise slice (a utilization-dependent inversion; total realized spend and total cost of ownership (TCO) are the robust quantities). At comparable gross code churn, the local configuration was associated with a far higher defect-repair burden: a Fix Commit Ratio (FCR) of 74.9% versus 45.9%, with the odds of a commit being a repair 2.6 to 4.9 times higher within every difficulty tier (Mantel-Haenszel OR = 3.61). Under Taiwan-market parameters and a symmetric labor model, on-premise deployment nonetheless saves 40.1% of true TCO under shared GPU allocation, whereas dedicated reservation costs 43.8% more than the cached API. Under shared allocation, the genuine penalty is not monetary but a measurable developer-experience burden -- timestamp indicators show more work trapped in debugging spirals and a slower commit cadence -- and an offline replay shows hybrid routing gateways trade defect rate for infrastructure savings along a cost-quality frontier rather than dominate the pure-API baseline.
