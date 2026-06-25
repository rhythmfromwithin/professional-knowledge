---
interest: medium
link: https://arxiv.org/abs/2606.25082
next_step: skim
priority: medium
slack_ts: '1782360759.496089'
source: cs.DC - Distributed Computing
status: unread
title: Energy Efficient Scheduling of AI/ML Workloads on Multi Instance GPUs with
  Dynamic Repartitioning
---
# Energy Efficient Scheduling of AI/ML Workloads on Multi Instance GPUs with Dynamic Repartitioning
> 原文: [https://arxiv.org/abs/2606.25082](https://arxiv.org/abs/2606.25082)

arXiv:2606.25082v1 Announce Type: new
Abstract: Increasing demand from AI/ML workloads is exacerbating the rising energy consumption of data centers. Recent advances in hardware such as NVIDIA's Multi Instance GPUs (MIGs) offer improvements in flexibility and computational power and the opportunity for data centers to manage incoming jobs in energy-efficient ways, while maintaining acceptable performance. The challenge in achieving this multi-objective in a MIG environment through job scheduling is multi-faceted. Firstly, for a given MIG configuration, one seeks an easy-to-implement scheduling algorithm which selects a job from the queue as well as decides on which slice in the configuration the job runs. Secondly, for the identified scheduling algorithm, a particular MIG configuration may not always be suitable (as the workload fluctuates) and may need to be repartitioned. We tackle both problems using simulations and reinforcement learning (RL). We present a dynamic repartitioning scheduling framework for a single MIG as a solution to a multi-objective heterogeneous machine scheduling problem with preemption. In particular, we compare four scheduling algorithms and identify a promising one. Then, we employ reinforcement learning to perform dynamic repartitioning over a day. Furthermore, using a diurnal workload pattern based on real-world data center traces, we demonstrate the superiority of our dynamic repartitioning algorithm over twice-daily repartitioning ($26\%$), static partitioning ($31\%$) and no partitioning at all ($68\%$) according to a multi-objective function of energy consumption and tardiness. Our results indicate specific preferred configurations at different times of the day under different queue conditions, suggesting a policy for predictive and automatic reconfiguration.
