---
title: "From Craft to Kernel: A Governance-First Execution Architecture and Semantic ISA for Agentic Computers"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.18652
priority: low
status: unread
interest: medium
next_step: skim
---
# From Craft to Kernel: A Governance-First Execution Architecture and Semantic ISA for Agentic Computers
> 原文: [https://arxiv.org/abs/2604.18652](https://arxiv.org/abs/2604.18652)

arXiv:2604.18652v1 Announce Type: new
Abstract: The transition of agentic AI from brittle prototypes to production systems is stalled by a pervasive crisis of craft. We suggest that the prevailing orchestration paradigm-delegating the system control loop to large language models and merely patching with heuristic guardrails-is the root cause of this fragility. Instead, we propose Arbiter-K, a Governance-First execution architecture that reconceptualizes the underlying model as a Probabilistic Processing Unit encapsulated by a deterministic, neuro-symbolic kernel. Arbiter-K implements a Semantic Instruction Set Architecture (ISA) to reify probabilistic messages into discrete instructions. This allows the kernel to maintain a Security Context Registry and construct an Instruction Dependency Graph at runtime, enabling active taint propagation based on the data-flow pedigree of each reasoning node. By leveraging this mechanism, Arbiter-K precisely interdicts unsafe trajectories at deterministic sinks (e.g., high-risk tool calls or unauthorized network egress) and enables autonomous execution correction and architectural rollback when security policies are triggered. Evaluations on OpenClaw and NanoBot demonstrate that Arbiter-K enforces security as a microarchitectural property, achieving 76% to 95% unsafe interception for a 92.79% absolute gain over native policies. The code is publicly available at https://github.com/cure-lab/ArbiterOS.
