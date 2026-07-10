---
title: "When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2607.06595
priority: low
status: unread
interest: medium
next_step: skim
---
# When Agents Remember Too Much: Memory Poisoning Attacks on Large Language Model Agents
> 原文: [https://arxiv.org/abs/2607.06595](https://arxiv.org/abs/2607.06595)

arXiv:2607.06595v1 Announce Type: new
Abstract: Personal AI agents powered by large language models can reason and act using available tools to access emails, manage calendars, and push code to remote repositories, all with minimal oversight. When augmented with long-term memory, an agent can recall specific details relevant to the current task, reducing the need for large context windows. Currently, long-term memory agents tend to fall into two distinct domains: conversational and action-planning agents. Personal assistant agents sit at the convergence of these two domains and handle sensitive information while interacting with untrusted information sources, creating previously unaccounted security vulnerabilities. In this work, we introduce the novel attack vector, GhostWriter, which exploits current memory subsystems in tool-using personal agents to poison their memory store. GhostWriter operates in two phases: injection, where an adversary sends a hidden attack payload to the target agent; and activation, in which the poisoned memory is retrieved. We show that GhostWriter achieves near-universal injection rates of approximately 98% and a high average activation rate of approximately 60% against state-of-the-art agents. This attack is possible due to the lack of security-focused memory governance. In response, we propose Agentic Memory Sentry (AM-Sentry), which leverages two mitigation techniques: a memory-saving policy and a memory-retrieval screen. Our experiments show that AM-Sentry dramatically reduces GhostWriter's success rate while preserving agent utility.
