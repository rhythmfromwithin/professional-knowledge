---
interest: medium
link: https://arxiv.org/abs/2603.20531
next_step: skim
priority: medium
slack_ts: '1774493857.803389'
source: cs.DC - Distributed Computing
status: unread
title: Epistemic Observability in Language Models
---
# Epistemic Observability in Language Models
> 原文: [https://arxiv.org/abs/2603.20531](https://arxiv.org/abs/2603.20531)

arXiv:2603.20531v1 Announce Type: new
Abstract: We find that models report highest confidence precisely when they are fabricating. Across four model families (OLMo-3, Llama-3.1, Qwen3, Mistral), self-reported confidence inversely correlates with accuracy, with AUC ranging from 0.28 to 0.36 where 0.5 is random guessing.
We prove, under explicit formal assumptions, that this is not a capability gap but an observational one. Under text-only observation, where a supervisor sees only the model's output text, no monitoring system can reliably distinguish honest model outputs from plausible fabrications. We prove two results: first, that any policy conditioning only on the query cannot satisfy epistemic honesty across ambiguous world states; second, that no learning algorithm optimizing reward from a text-only supervisor can converge to honest behavior when the supervisor's observations are identical for both grounded and fabricated responses. Within our formal model, these impossibilities hold regardless of model scale or training procedure, including RLHF and instruction tuning.
We construct a tensor interface that escapes the impossibility by exporting computational byproducts (per-token entropy and log-probability distributions) that are structurally coupled to correctness under standard training. Per-token entropy achieves pooled AUC 0.757, outperforming all text baselines by 2.5--3.9 percentage points at every budget level tested (10\%, 20\%, 30\%). The entropy signal generalizes across architectures (Spearman $\rho = 0.762$).
The core contribution is a cost surface where the empirical mapping from verification budget (fraction of queries receiving expensive checks) to detection accuracy for each judge strategy is a practical lookup for system builders deciding how to allocate verification resources. The contribution is the map. The territory is the system you are building.
