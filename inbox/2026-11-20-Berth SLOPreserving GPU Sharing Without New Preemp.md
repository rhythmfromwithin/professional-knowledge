---
interest: medium
link: https://arxiv.org/abs/2611.25091
next_step: skim
priority: medium
slack_ts: '1795243598.140079'
source: cs.DC - Distributed Computing
status: unread
title: 'Berth: SLO-Preserving GPU Sharing Without New Preemption'
---
# Berth: SLO-Preserving GPU Sharing Without New Preemption
> 原文: [https://arxiv.org/abs/2611.25091](https://arxiv.org/abs/2611.25091)

arXiv:2611.25091v1 Announce Type: new
Abstract: Inference services keep GPUs reserved for their worst-case load, and most of that capacity sits idle. Filling it with best-effort work such as training is the obvious remedy, and latency is why it rarely happens: on a shared GPU, a request that must finish within milliseconds finds the best-effort job's kernels running or queued ahead of it. Spatial sharing cannot evict them, temporal sharing gives the request only its turn, and hardware partitioning protects it by idling what it does not use. Systems that keep both the SLO and the utilization have reached inside the stack (rewriting kernels, patching the driver, instrumenting the framework), which the operator of a closed GPU stack cannot do. This paper argues that reaching inside is unnecessary. The time-slicer built into commodity GPUs already preempts a running kernel within a fraction of a millisecond and switches the moment a context runs out of work; what it lacks is priority, and priority can be created from outside by controlling what the best-effort context has to run. Berth is a user-space system built on this observation: a preloaded shim feeds the best-effort job to the GPU only when no request needs it (feed control), a declared deadline reference extends the rule to continuous-batching LLM engines, and a shortened best-effort time slice, set without privileges, bounds what a long kernel can cost. Berth changes no application, framework, kernel or driver. Across 31 scenario points with MLPerf SLOs and 13 baselines, Berth meets SLOs within a few percentage points of running alone, above every baseline, with 2.7-3.5x the best-effort throughput of the strongest ones; beside LLM serving, it meets per-token targets for nearly every request while training keeps running. Sharing a closed GPU under SLOs needs no new preemption mechanism, only control over what the existing one sees.
