---
title: "Nitsum: Serving Tiered LLM Requests with Adaptive Tensor Parallelism"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2605.05467
priority: medium
status: unread
interest: medium
next_step: skim
---
# Nitsum: Serving Tiered LLM Requests with Adaptive Tensor Parallelism
> 原文: [https://arxiv.org/abs/2605.05467](https://arxiv.org/abs/2605.05467)

arXiv:2605.05467v1 Announce Type: new
Abstract: LLM serving is increasingly multi-tenant: the same deployment must handle latency-critical interactive requests and more relaxed background workloads under a fixed GPU budget. This creates a tiered-SLO setting where maximizing overall goodput (requests that satisfy both TTFT and TPOT targets) is challenging because workload mix, request lengths, and load intensity vary over time. Existing systems mainly optimize request-level controls (e.g., queuing and batching) while keeping execution configuration largely static, which limits adaptation under multi-tier contention.
We present Nitsum, a distributed LLM serving system that treats tensor parallelism (TP) as a first-class runtime control surface rather than a static deployment choice. Nitsum jointly optimizes TP level, prefill/decode GPU split, and request scheduling. To make frequent TP adaptation practical, Nitsum introduces TP-aware weight reuse and fast KV migration. Experiments on real traces and targeted microbenchmarks show that Nitsum improves SLO-compliant goodput over SoTA by up to 5.3 times.
