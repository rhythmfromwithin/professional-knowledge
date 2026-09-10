---
interest: medium
link: https://arxiv.org/abs/2609.09164
next_step: skim
priority: medium
slack_ts: '1789013735.687129'
source: cs.DC - Distributed Computing
status: unread
title: 'HELIOS: Guardrailed LLM-Driven Evolution of Autonomous Resource Orchestration
  Policies for Multi-Cloud Distributed Systems'
---
# HELIOS: Guardrailed LLM-Driven Evolution of Autonomous Resource Orchestration Policies for Multi-Cloud Distributed Systems
> 原文: [https://arxiv.org/abs/2609.09164](https://arxiv.org/abs/2609.09164)

arXiv:2609.09164v1 Announce Type: new
Abstract: Operating latency-sensitive services across multiple public clouds creates an optimization surface no single provider autoscaler can see: on-demand vCPU prices differ by provider, spot discounts and interruption risks vary by provider and instance type, egress fees penalize state movement, and provider-level failures can take down single-cloud deployments. Large language models (LLMs) are appealing orchestrators because they can synthesize non-trivial decision logic from a natural-language environment description. However, placing an LLM on the critical path of every scheduling decision is impractical: for a 200-service fleet, per-decision inference would cost more than the cloud capacity it manages and add multi-second latency to a millisecond-scale control loop. HELIOS moves the LLM off the critical path. The LLM evolves executable orchestration policies, small Python programs over a fixed feature interface, against a trace-driven multi-cloud simulator. Only the champion program runs in production, wrapped in guardrails that enforce capacity feasibility, SLO-class placement rules, and churn budgets regardless of evolved code's proposal. On real workload traces (PlanetLab, Bitbrains, Azure) combined with 2026 price and interruption-frequency data from AWS, Azure, and GCP, the evolved policy reduces penalized operating cost by 45% versus a single-cloud best-fit baseline and by 9-19% versus calibrated multi-cloud heuristics. It matches an oracle-informed MILP planner's premium-SLO performance at 40% lower cost and outperforms a DQN meta-controller trained with 2.6x more environment interactions. Guardrails are essential: without them, the same policy family degrades to 97-98% premium-tier downtime under a 10x spot-hazard stress test, versus 0.17% when guarded. We release the simulator, policies, LLM prompt/response archive, and per-generation fitness logs for full reproducibility.
