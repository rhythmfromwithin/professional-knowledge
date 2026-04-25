---
interest: medium
link: https://arxiv.org/abs/2604.19958
next_step: skim
priority: medium
slack_ts: '1777087202.613469'
source: cs.DC - Distributed Computing
status: unread
title: 'Equinox: Decentralized Scheduling for Hardware-Aware Orbital Intelligence'
---
# Equinox: Decentralized Scheduling for Hardware-Aware Orbital Intelligence
> 原文: [https://arxiv.org/abs/2604.19958](https://arxiv.org/abs/2604.19958)

arXiv:2604.19958v1 Announce Type: new
Abstract: Earth-observation satellites are emerging as distributed edge platforms for time-critical tasks, yet orbital scheduling remains challenged by intermittent energy harvesting and temporal coupling where eager execution risks future battery depletion. Existing schedulers rely on static priorities and lack mechanisms to adaptively shed work. We present Equinox, a lightweight, decentralized runtime for resource-constrained orbital systems. Equinox enables adaptive scheduling by compressing time-varying constraints, including battery charge, thermal headroom, and queue backlog, into a single state-dependent marginal cost of execution. Derived from a barrier function that rises sharply near safety limits, this cost encodes both instantaneous pressure and future risk. This local signal serves as a constellation-wide coordination primitive. Tasks execute only when their value exceeds the current cost, enabling value-ordered load shedding without explicit policies. If local costs exceed a neighbor's, tasks are dynamically offloaded over inter-satellite links, achieving distributed load balancing without routing protocols or global state. We evaluate Equinox using a multi-day simulation of a 143-satellite constellation grounded in physical Jetson Orin Nano measurements. Equinox improves scientific goodput by 20% and image-processing throughput by 31% over priority-based scheduling while maintaining 2.2x higher mean battery reserves. Under high demand, Equinox achieves 5.2x the execution rate of static scheduling by gracefully shedding work rather than collapsing under contention.
