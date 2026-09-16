---
title: "Docker Containers vs. Virtual Machines: A Comparative Study of Architecture, Performance, Configuration, and Security"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2609.16148
priority: low
status: unread
interest: medium
next_step: skim
---
# Docker Containers vs. Virtual Machines: A Comparative Study of Architecture, Performance, Configuration, and Security
> 原文: [https://arxiv.org/abs/2609.16148](https://arxiv.org/abs/2609.16148)

arXiv:2609.16148v1 Announce Type: new
Abstract: Modern application platforms must isolate workloads while preserving deployment speed, portability, resource efficiency, and security. Virtual machines (VMs) and Docker containers address this requirement at different abstraction layers: VMs virtualize hardware and run independent guest operating systems, whereas containers isolate processes while sharing the host kernel. This paper presents a comparative, literature-based analysis of the two approaches across architecture, configuration and lifecycle management, performance, scalability, and security. Published studies generally associate containers with shorter startup times, smaller images, higher workload density, and near-native execution for many workloads. These benefits depend on workload characteristics, storage and network drivers, resource controls, and experimental design. VMs introduce greater overhead but offer independent kernels, heterogeneous guest operating systems, and a stronger isolation boundary. The comparison therefore treats efficiency and isolation as a design trade-off rather than declaring one technology universally superior. A hybrid architecture, in which containers run inside hardened VMs, often provides a practical balance for cloud and multi-tenant systems.
