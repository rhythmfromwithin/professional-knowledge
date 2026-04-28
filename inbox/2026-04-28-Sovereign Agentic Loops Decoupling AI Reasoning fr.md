---
title: "Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2604.22136
priority: low
status: unread
interest: medium
next_step: skim
---
# Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems
> 原文: [https://arxiv.org/abs/2604.22136](https://arxiv.org/abs/2604.22136)

arXiv:2604.22136v1 Announce Type: new
Abstract: Large language model (LLM) agents increasingly issue API calls that mutate real systems, yet many current architectures pass stochastic model outputs directly to execution layers. We argue that this coupling creates a safety risk because model correctness, context awareness, and alignment cannot be assumed at execution time. We introduce Sovereign Agentic Loops (SAL), a control-plane architecture in which models emit structured intents with justifications, and the control plane validates those intents against true system state and policy before execution. SAL combines an obfuscation membrane, which limits model access to identity-sensitive state, with a cryptographically linked Evidence Chain for auditability and replay. We formalize SAL and show that, under the stated assumptions, it provides policy-bounded execution, identity isolation, and deterministic replay. In an OpenKedge prototype for cloud infrastructure, SAL blocks 93% of unsafe intents at the policy layer, rejects the remaining 7% via consistency checks, prevents unsafe executions in our benchmark, and adds 12.4 ms median latency.
