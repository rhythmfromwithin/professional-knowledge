---
title: "Token Management in Multi-Tenant AI Inference Platforms"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.00356
priority: medium
status: unread
---
# Token Management in Multi-Tenant AI Inference Platforms
> 原文: [https://arxiv.org/abs/2603.00356](https://arxiv.org/abs/2603.00356)

arXiv:2603.00356v1 Announce Type: new
Abstract: Multi-tenant AI inference platforms must balance resource utilization against service-level guarantees under variable demand. Conventional approaches fail to achieve this balance: dedicated endpoints strand capacity on idle models, while rate limits ignore the heterogeneous cost of inference requests. We introduce \emph{token pools}, a control-plane abstraction that represents inference capacity as explicit entitlements expressed in inference-native units (token throughput, KV cache, concurrency). Unlike rate limits, which govern request admission without regard to execution cost, token pools authorize both admission and autoscaling from the same capacity model, ensuring consistency between what is promised and what is provisioned. The abstraction captures burst modes across multiple dimensions invisible to conventional throttling. Dynamic per-entitlement limits on each burst dimension enable fine-grained control over resource consumption while permitting work-conserving backfill by low-priority traffic. The design supports priority-aware allocation, service tiers with differentiated guarantees, and debt-based fairness mechanisms, all without modifying the underlying inference runtime or cluster scheduler. In experiments on a Kubernetes cluster with vLLM backends, token pools maintain a bounded P99 latency for guaranteed workloads during overload by selectively throttling spot traffic, while a baseline without admission control experiences unbounded latency degradation across all workloads. A second experiment demonstrates debt-based fair-share convergence among elastic workloads with heterogeneous SLO requirements during capacity scarcity.
