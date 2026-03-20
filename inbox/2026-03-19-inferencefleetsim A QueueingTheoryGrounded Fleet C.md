---
interest: medium
link: https://arxiv.org/abs/2603.16054
next_step: skim
priority: medium
slack_ts: '1773974692.666549'
source: cs.DC - Distributed Computing
status: unread
title: 'inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for
  LLM Inference'
---
# inference-fleet-sim: A Queueing-Theory-Grounded Fleet Capacity Planner for LLM Inference
> 原文: [https://arxiv.org/abs/2603.16054](https://arxiv.org/abs/2603.16054)

arXiv:2603.16054v1 Announce Type: new
Abstract: Sizing a GPU fleet for LLM inference is harder than it looks. The obvious questions -- how many GPUs, which type, where to split a two-pool fleet -- have no closed-form answers. They depend on the full token-length distribution, the routing policy, and queueing dynamics that turn ugly under heavy-tailed workloads. Existing tools optimize per-engine configuration for a fixed GPU count; none of them address the upstream question of how many GPUs to buy and how to arrange them.
inference-fleet-sim fills that gap. It combines analytical M/G/c queueing with discrete-event simulation (DES) to find the minimum-cost fleet configuration that empirically meets a P99 TTFT SLO. It includes a physics-informed GPU performance model covering A10G, A100, and H100 across monolithic, two-pool-routed, and disaggregated topologies, all without requiring access to real hardware. We run the tool on seven fleet-planning scenarios drawn from two public workload traces (LMSYS, Azure) and one synthetic agent-heavy trace. Each one surfaces a result that simple analysis gets wrong -- the right split threshold, the cheapest GPU type, whether an apparently idle fleet is actually broken -- and shows why joint simulation of queueing, routing, and hardware is necessary to find it.
