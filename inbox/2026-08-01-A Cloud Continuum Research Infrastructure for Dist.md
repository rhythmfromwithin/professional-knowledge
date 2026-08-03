---
interest: medium
link: https://arxiv.org/abs/2607.28193
next_step: skim
priority: medium
slack_ts: '1785728288.019309'
source: cs.DC - Distributed Computing
status: unread
title: A Cloud Continuum Research Infrastructure for Distributed CPS Experimentation
---
# A Cloud Continuum Research Infrastructure for Distributed CPS Experimentation
> 原文: [https://arxiv.org/abs/2607.28193](https://arxiv.org/abs/2607.28193)

arXiv:2607.28193v1 Announce Type: new
Abstract: Cloud Continuum applications require experimental environments capable of combining heterogeneous Edge, Fog, Cloud, and high-performance computing resources while preserving reproducibility, observability, and control over distributed deployments. This paper presents a two-level reference architecture for Cloud Continuum experimentation built on top of the SLICES Cloud Continuum Blueprint. The proposed approach separates the research-infrastructure layer, which exposes and manages distributed resources, from the application layer, where Cyber-Physical workflows are organized according to an Edge-Fog-Cloud pattern in which placement, timing, and data provenance are treated as first-class experimental concerns.
The architecture is designed to support multiple continuum applications rather than a single domain-specific prototype. At the Edge, applications interact with physical devices and perform low-latency sensing or safety actions; at the Fog, they execute near-source coordination, mediation, and stream-processing logic; at the Cloud, they consolidate global knowledge through analytics, optimization, and visualization. This partitioning enables researchers to deploy, customize, and compare alternative control and monitoring strategies over the same programmable infrastructure substrate.
The approach is validated through two representative use cases: Renewable Energy Community management, where distributed Digital Twin coordination and time-window-based energy control are requested, and AirWatch, a monitoring pipeline focused on anomaly detection, low-latency alerting, and cloud-side aggregation. Both workloads are evaluated through a systematic campaign of 40 runs comparing virtualized and physical edge deployments over a geographically distributed infrastructure.
