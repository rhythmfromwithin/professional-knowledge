---
interest: medium
link: https://arxiv.org/abs/2606.10663
next_step: skim
priority: low
slack_ts: '1781065411.817739'
source: cs.DB - Databases
status: unread
title: Reconstructing OPC UA Address Spaces from Time-Series Databases
---
# Reconstructing OPC UA Address Spaces from Time-Series Databases
> 原文: [https://arxiv.org/abs/2606.10663](https://arxiv.org/abs/2606.10663)

arXiv:2606.10663v1 Announce Type: new
Abstract: OPC UA has become the dominant open protocol in operational technology. Time-series databases routinely archive OPC UA telemetry but discard the semantic metadata (node hierarchy, engineering units, and type definitions) which gives sensor values their meaning. Recovering this information from a time-series database is non-trivial: namespace indices recorded at the source are session-local and unstable across restarts, and naive merging across multiple source servers results in identifier collisions. We present opcua-ts, an implemented architecture that persists this semantic information alongside its telemetry in a general-purpose time-series database under a lifecycle-stable join key, and that reconstructs the source address space as a live OPC UA endpoint. We characterize the conditions under which the reconstruction is sound across multi-source deployments and validate the approach with a NodeSet2 XML round-trip against the source server. Initial results from a boiler-simulator round-trip indicate that the approach is feasible.
