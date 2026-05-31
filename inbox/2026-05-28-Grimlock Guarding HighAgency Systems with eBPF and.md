---
interest: medium
link: https://arxiv.org/abs/2605.27488
next_step: skim
priority: low
slack_ts: '1780202378.571569'
source: cs.CR - Cryptography and Security
status: unread
title: 'Grimlock: Guarding High-Agency Systems with eBPF and Attested Channels'
---
# Grimlock: Guarding High-Agency Systems with eBPF and Attested Channels
> 原文: [https://arxiv.org/abs/2605.27488](https://arxiv.org/abs/2605.27488)

arXiv:2605.27488v1 Announce Type: new
Abstract: Agentic systems increasingly run user-authored orchestration code that invokes tools, spawns subtasks, and delegates work across machines and clouds. Although this high agency is productive, it creates a security problem: identity, authorization, provenance, and delegation are often pushed into application code, where they become difficult to enforce consistently and difficult to audit.
We present \emph{Grimlock}, an \emph{Agent Guard} that restores separation of concerns by moving trust enforcement into the sandbox substrate while leaving agent code unchanged. Grimlock uses \emph{eBPF-enforced traffic interception} to ensure that sandbox communication passes through a guard, and combines it with \emph{post-handshake attestation} bound to standard TLS~1.3 channel bindings. After a channel is established, the guard authorizes communication and mints short-lived, channel-bound \emph{scope tokens} that capture least-privilege delegation. At the receiving side, the destination guard re-validates identity, scope, and channel binding, terminates TLS, and releases plaintext to the destination sandbox only after policy checks succeed. kTLS provides an efficient dataplane for protected communication.
As a result, Grimlock offers a path toward transparent, auditable, and scope-bound agent-to-agent communication across heterogeneous multi-cloud environments, using commodity Linux primitives and without requiring changes to user-layer orchestration code.
