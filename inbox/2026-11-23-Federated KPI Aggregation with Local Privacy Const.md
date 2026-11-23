---
title: "Federated KPI Aggregation with Local Privacy Constraints and Coordinated OLAP Roll-Ups"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2611.26709
priority: low
status: unread
interest: medium
next_step: skim
---
# Federated KPI Aggregation with Local Privacy Constraints and Coordinated OLAP Roll-Ups
> 原文: [https://arxiv.org/abs/2611.26709](https://arxiv.org/abs/2611.26709)

arXiv:2611.26709v1 Announce Type: new
Abstract: Cross-organizational KPI analysis can require aggregated results from independently administered data warehouses without centralizing detailed records. To limit disclosure from small local groups, a site can require a minimum number of contributing records before releasing a KPI value for a group. If each site applies this rule independently, different local contributions may be suppressed and the combined KPI can become incomplete. This paper investigates whether OLAP granularity can be coordinated before local query results are released so that all sites satisfy their local minimum-cohort rules and contribute at the same analytical level. The proposed method selects the least-generalized common roll-up accepted by every site. Site agents coordinate current capabilities and approved local execution across independently administered sites, with privacy checks and aggregate computation remaining deterministic local functions. In a four-site prototype, coordinated roll-up retained all contributions and reproduced the corresponding centralized result, compared with 78.3% retained under independent suppression. A capability-change experiment showed fewer candidate checks and replies and no unsupported requests when current site-agent state was used. The results demonstrate the feasibility of federated KPI aggregation under local privacy constraints through coordinated granularity selection and agent-based coordination.
