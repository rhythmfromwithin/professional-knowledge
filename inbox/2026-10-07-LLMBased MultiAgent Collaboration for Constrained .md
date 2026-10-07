---
interest: medium
link: https://arxiv.org/abs/2610.07030
next_step: skim
priority: medium
slack_ts: '1791351200.199449'
source: cs.DC - Distributed Computing
status: unread
title: LLM-Based Multi-Agent Collaboration for Constrained Multi-Objective Container
  Placement
---
# LLM-Based Multi-Agent Collaboration for Constrained Multi-Objective Container Placement
> 原文: [https://arxiv.org/abs/2610.07030](https://arxiv.org/abs/2610.07030)

arXiv:2610.07030v1 Announce Type: new
Abstract: Container placement in data centers must simultaneously minimize power consumption and maximize affinity preferences, while satisfying multi-resource capacity and anti-affinity constraints. Traditional approaches typically rely on fixed rules, which lack adaptability to dynamic cluster states and are difficult to extend for adaptive decision-making. On the other hand, meta-heuristic methods, although more flexible, are often computationally expensive, slower and prone to getting trapped in local optima. In this work, we propose an adaptive and efficient approach based on an LLM-driven multi-agent collaboration framework, where four specialized agents operate in a closed-loop ReAct cycle at each placement step. A Power Consumption Agent and an Affinity Agent debate over competing objectives, while a Placement Agent resolves conflicts using Tolerance-Gated Arbitration (TGA). A Rearrangement Agent further refines decisions through the Monotone Improvement Rule (MIR) in a post-placement refinement phase. All the agents reason over deterministic, feasibility-filtered candidate tables provided by the environment, ensuring that every proposed action inherently satisfies hard constraints. Based on experimental evaluation using the Google Cluster Trace with a configuration of 100 applications and 25 machines, the proposed framework consumes 8.36% less power and achieves 39.30% higher affinity than the power-greedy baseline. Ablation studies confirm that each architectural component, the multi-round debate mechanism, the TGA in the Placement Agent, and the MIR in the Rearrangement Agent, contributes meaningfully to the overall performance, with removal of any single component degrading both power consumption and affinity satisfaction.
