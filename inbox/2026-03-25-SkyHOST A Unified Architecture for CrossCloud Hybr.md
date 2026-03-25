---
title: "SkyHOST: A Unified Architecture for Cross-Cloud Hybrid Object and Stream Transfer"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.20512
priority: medium
status: unread
interest: medium
next_step: skim
---
# SkyHOST: A Unified Architecture for Cross-Cloud Hybrid Object and Stream Transfer
> 原文: [https://arxiv.org/abs/2603.20512](https://arxiv.org/abs/2603.20512)

arXiv:2603.20512v1 Announce Type: new
Abstract: Cloud and big data workloads are increasingly distributing data across multiple cloud providers and regions for rapid decision-making and analytics. Traditional transfer tools are typically specialized for a single paradigm, either stream replication or bulk transfer. This specialization forces users to deploy and manage separate systems with different configurations for each transfer pattern. This paper presents SkyHOST (Hybrid Object and Stream Transfer), a unified data movement architecture built upon the Skyplane framework to bridge the gap between bulk object transfer and streaming workloads through a single control plane and CLI. SkyHOST manages URI-based routing to automatically select the appropriate transfer mechanism, supporting both structured data for record-level ingestion and chunk-based transfer for large binary objects. We demonstrate, through an environmental monitoring use case and empirical evaluation, that SkyHOST provides operational simplicity by consolidating heterogeneous data movement patterns under a single control plane while achieving competitive throughput for cross-region transfers.
