---
interest: medium
link: https://arxiv.org/abs/2606.19382
next_step: skim
priority: low
slack_ts: '1781847258.961299'
source: cs.SE - Software Engineering
status: unread
title: DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling
---
# DynAMO:Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling
> 原文: [https://arxiv.org/abs/2606.19382](https://arxiv.org/abs/2606.19382)

arXiv:2606.19382v1 Announce Type: new
Abstract: While LLM-powered agents offer end-to-end automation for industrial asset lifecycles, real-world Industry 4.0 deployment is hindered by latency, concurrency instability, and safety risks. We present DynAMO (Dynamic Asset Management Orchestration), a deployment-ready engine using a Plan-then-Execute architecture to generate verifiable workflow graphs. DynAMO supports both SequentialWorkflow (topological execution) and ParallelWorkflow (dependency-aware concurrency). By dynamically identifying independent tasks, DynAMO preserves structural correctness and safety while significantly improving efficiency through controlled reasoning overlap.
Across six controlled experiments on the AssetOpsBench industrial benchmark, DynAMO demonstrates substantial performance and robustness gains. Parallel execution reduces end-to-end latency by a median of 1.6x over sequential orchestration, rising to 1.8x on highly parallelizable workflows. After instrumenting external tool calls with realistic latencies, a latency decomposition shows that LLM reasoning and orchestration still account for more than 90% of execution time, identifying model inference as the primary system bottleneck. Structured context pruning reduces inference latency by approximately 30%, and DynAMO maintains correct functional behaviour (task completion, agent sequencing, and output quality) while exhibiting graceful degradation under controlled fault injection. Reproducibility analysis further confirms stable execution under repeated runs, with parallel scheduling reducing latency variance. These findings establish DynAMO as a practical blueprint for scalable, safe, and latency-aware agent deployment in Industry 4.0 automation pipelines. Code is available at: https://github.com/kushwaha001/DynAMO
