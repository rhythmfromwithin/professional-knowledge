---
interest: medium
link: https://arxiv.org/abs/2605.27652
next_step: skim
priority: medium
slack_ts: '1779941832.288929'
source: cs.DC - Distributed Computing
status: unread
title: Carbon-Aware Mapping and Scheduling for Deadline-Constrained Workflows
---
# Carbon-Aware Mapping and Scheduling for Deadline-Constrained Workflows
> 原文: [https://arxiv.org/abs/2605.27652](https://arxiv.org/abs/2605.27652)

arXiv:2605.27652v1 Announce Type: new
Abstract: As datacenters continue to grow in scale, their energy consumption and resulting carbon footprint have become pressing concerns. With the increasing share of renewable energy in a datacenter's mixed energy supply, shifting task execution to periods of high green-power availability is a promising strategy to reduce carbon emissions. However, in heterogeneous computing environments, the power consumption of compute nodes in a datacenter can also vary. In practice, workloads submitted to datacenters are often not isolated tasks, but entire workflows consisting of interdependent tasks with precedence constraints. A further challenge arises from the fact that carbon emission reductions must typically be achieved under strict workflow deadlines. In this work, we show that the problem posed by these challenges for the scheduler is NP-hard and admits no constant-factor approximation even for the uni-processor case. Motivated by this hardness, we present a novel algorithm CWM that combines carbon-aware mapping and scheduling to construct feasible solutions. Our approach integrates dynamic programming with efficient heuristics to exploit renewable energy availability and infrastructure heterogeneity. To assess the quality of the new algorithm, we evaluate it against the state-of-the-art approach CaWoSched and show that CWM achieves significant reductions in terms of carbon emissions in experiments. In particular, we are able to achieve a median carbon cost reduction of 42% over the best version of CaWoSched when the deadline is two times the makespan of a carbon-agnostic baseline. Note that CaWoSched itself already reduces the carbon-agnostic baseline by 36%.
