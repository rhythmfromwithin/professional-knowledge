---
title: "Joint SLA Admission and Risk Allocation for Cloud Resource Provisioning"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.26924
priority: medium
status: unread
interest: medium
next_step: skim
---
# Joint SLA Admission and Risk Allocation for Cloud Resource Provisioning
> 原文: [https://arxiv.org/abs/2611.26924](https://arxiv.org/abs/2611.26924)

arXiv:2611.26924v1 Announce Type: new
Abstract: Cloud controllers must reserve enough CPU and memory to meet demand without leaving too much capacity idle. Under a shared service-level agreement (SLA), a shortage of CPU or memory (considered as resource) counts toward the same limit. Dividing the allowed shortage risk between them changes how much extra capacity each need. We study this choice when forecast-error histories are short or correlated over time. Our controller compares different approaches to split the allowed shortage risk between resources. For each split, the controller uses historical forecast errors to determine how much extra capacity to reserve. It checks whether the history is enough to support that split and its consistency across different parts of the history. Among the splits that pass, it chooses the one with the lowest combined cost of shortages and idle capacity. Otherwise, the controller continues serving the workload with a calibrated fallback. In our simulation, we set a joint SLA target of sufficient CPU and memory in at least 95% of time slots and used 192 hours of historical forecast errors to structure the controller. Compared with always using fallback, the controller reduced the time slots allocation with either of the resource shortage by 1.04 percentage points on average. This reduction came with a 0.0091 increase in normalized cost from shortages and idle capacity. In the Bitbrains trace, five nonoverlapping test windows did not provide clear evidence of whether shortages increased or decreased. We also examine how execution delays and adjustment limits affect this trade off.
