---
title: "Spot-and-Scoot: Peeking Into Spot Instance Availability"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.16457
priority: medium
status: unread
interest: medium
next_step: skim
---
# Spot-and-Scoot: Peeking Into Spot Instance Availability
> 原文: [https://arxiv.org/abs/2604.16457](https://arxiv.org/abs/2604.16457)

arXiv:2604.16457v1 Announce Type: new
Abstract: Spot instances offer significant cost savings of up to 90% over on-demand prices, making them an attractive resource for large-scale computing workloads. However, understanding their availability dynamics is essential for building systems that tolerate interruptions, and observing this availability directly requires keeping instances running, which incurs costs that scale with the number of monitored instance types and their per-instance price. We propose Spot-and-Scoot (SnS), a cost-efficient method that collects spot instance availability signals by leveraging the cloud provider's provisioning lifecycle. Since the outcome of a spot request is determined before the instance enters the running state, SnS submits requests and cancels them upon provisioning acceptance, collecting binary availability signals at near-zero instance cost. Submitting multiple concurrent requests per measurement point further yields a quantitative estimate of available capacity. We validate SnS through simultaneous collection of probing signals and actual running instance traces across 68 instance types and 15 regions on both AWS and Azure, totaling 336,033 spot requests. Analysis of 2,635 real-world interruption events reveals that co-interruptions within the same instance type and availability zone occur within three minutes in over 92% of cases, motivating a binary availability formulation. Based on this formulation, we derive three complementary features from SnS signals and demonstrate that their combination achieves an F1-macro score of up to 0.90 for current availability modeling and maintains 0.85 at a 60-minute prediction horizon. A trace-driven simulation using TPC-DS workloads further demonstrates the potential of SnS-based prediction to reduce lost computation compared to an unguided baseline.
