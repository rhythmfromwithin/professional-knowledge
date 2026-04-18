---
interest: medium
link: https://arxiv.org/abs/2604.13097
next_step: skim
priority: low
slack_ts: '1776482303.574499'
source: cs.SE - Software Engineering
status: unread
title: 'ECM Contracts: Contract-Aware, Versioned, and Governable Capability Interfaces
  for Embodied Agents'
---
# ECM Contracts: Contract-Aware, Versioned, and Governable Capability Interfaces for Embodied Agents
> 原文: [https://arxiv.org/abs/2604.13097](https://arxiv.org/abs/2604.13097)

arXiv:2604.13097v1 Announce Type: new
Abstract: Embodied agents increasingly rely on modular capabilities that can be installed, upgraded, composed, and governed at runtime. Prior work has introduced embodied capability modules (ECMs) as reusable units of embodied functionality, and recent research has explored their runtime governance and controlled evolution. However, a key systems question remains unresolved: how can ECMs be composed and released as a stable software ecosystem rather than as ad hoc skill bundles?
We present ECM Contracts, a contract-based interface model for embodied capability modules. Unlike conventional software interfaces that specify only input and output types, ECM Contracts encode six dimensions essential for embodied execution: functional signature, behavioral assumptions, resource requirements, permission boundaries, recovery semantics, and version compatibility. Based on this model, we introduce a compatibility framework for ECM installation, composition, and upgrade, enabling static and pre-deployment checks for type mismatches, dependency conflicts, policy violations, resource contention, and recovery incompatibilities.
We further propose a release discipline for embodied capabilities, including version-aware compatibility classes, deprecation rules, migration constraints, and policy-sensitive upgrade checks. We implement a prototype ECM registry, resolver, and contract checker, and evaluate the approach on modular embodied tasks in a robotics runtime setting. Results show that contract-aware composition substantially reduces unsafe or invalid module combinations, and that contract-guided release checks improve upgrade safety and rollback readiness compared with schema-only or ad hoc baselines.
Our findings suggest that stable embodied software ecosystems require more than modular packaging: they require explicit contracts that connect capability composition, governance, and evolution.
