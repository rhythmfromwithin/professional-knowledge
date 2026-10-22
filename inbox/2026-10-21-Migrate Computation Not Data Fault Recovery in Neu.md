---
interest: medium
link: https://arxiv.org/abs/2610.26985
next_step: skim
priority: low
slack_ts: '1792642779.575059'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Migrate Computation, Not Data: Fault Recovery in Neuromorphic Many-Core Systems'
---
# Migrate Computation, Not Data: Fault Recovery in Neuromorphic Many-Core Systems
> 原文: [https://arxiv.org/abs/2610.26985](https://arxiv.org/abs/2610.26985)

arXiv:2610.26985v1 Announce Type: new
Abstract: As neuromorphic systems scale to thousands of near-memory cores, aging-induced permanent faults in neuron-update datapaths become an important obstacle to long-term deployment. Existing online recovery methods typically retire a faulty core and migrate its neurons, along with their weights and membrane states, to healthy cores. This whole-core treatment incurs high recovery traffic and makes recovery depend on scarce destinations; at high utilization, there may be enough surviving compute capacity but insufficient free storage to copy the affected neuron context. This paper presents SpikeRelay, an online recovery framework for diagnosed compute-unit faults. SpikeRelay exploits the fact that, in many neuromorphic cores, the compute datapath, local SRAM, and router are distinct modules: a compute fault need not destroy stored weights and states or disconnect the core from the NoC. Instead of retiring a faulty core and migrating its neuron data, SpikeRelay converts the faulty core into a storage-and-forwarding node while offloading neuron-update computation to a healthy rescue core. This decoupling of storage and computation eliminates recovery-time data migration and greatly reduces spare-SRAM requirements. Consequently, SpikeRelay sustains 100\% recovery at 92.2\% SRAM utilization and a 50\% fault rate, whereas the best baseline achieves only 22.1\%.
