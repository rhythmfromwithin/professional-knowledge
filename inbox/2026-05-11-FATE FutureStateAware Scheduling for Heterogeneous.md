---
interest: medium
link: https://arxiv.org/abs/2605.07238
next_step: skim
priority: medium
slack_ts: '1778558021.387219'
source: cs.DC - Distributed Computing
status: unread
title: 'FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows'
---
# FATE: Future-State-Aware Scheduling for Heterogeneous LLM Workflows
> 原文: [https://arxiv.org/abs/2605.07238](https://arxiv.org/abs/2605.07238)

arXiv:2605.07238v1 Announce Type: new
Abstract: Large language model (LLM) applications are increasingly executed as heterogeneous multi-stage workflows rather than isolated inference calls. In these workflow directed acyclic graphs (DAGs), scheduling decisions affect not only the currently ready stage, but also the execution state inherited by downstream stages, including model residency, parent-output locality, prefix reuse, and future device reachability. Existing serving and DAG-scheduling policies mainly optimize immediate queue state, placement cost, or reuse signals in isolation, which can fragment useful state and increase end-to-end latency. We present FATE, a future-state-aware scheduler for heterogeneous LLM workflows. FATE combines a CP-SAT-backed frontier planner, horizon-aware candidate scoring, bounded multi-device shard execution, and state-conditional cost estimation. Rather than solving a monolithic full-DAG problem, FATE repeatedly plans over the current ready frontier and scores assignments by both immediate cost and the downstream state they induce. Across real-DAG and controlled prefix-reuse benchmarks, FATE outperforms practical heuristics, classical DAG scheduling, and proxy adaptations of recent workflow-serving policies. On the real-DAG benchmark, it achieves normalized makespan and normalized P95 latency of 0.675 and 0.677, reducing them by 32.5% and 32.3% over RoundRobin and by 8.9% and 8.8% over the strongest non-FATE baseline. Mechanism analysis and ablations show that these gains arise from jointly preserving multiple dimensions of future execution state rather than prefix reuse alone. These results indicate that future-state preservation should be treated as a first-class scheduling objective for heterogeneous LLM workflow serving.
