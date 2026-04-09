---
interest: medium
link: https://arxiv.org/abs/2604.05862
next_step: skim
priority: medium
slack_ts: '1775703395.838239'
source: cs.DC - Distributed Computing
status: unread
title: Communication Requirements for Linearizable Registers
---
# Communication Requirements for Linearizable Registers
> 原文: [https://arxiv.org/abs/2604.05862](https://arxiv.org/abs/2604.05862)

arXiv:2604.05862v1 Announce Type: new
Abstract: While linearizability is a fundamental correctness condition for distributed systems, ensuring the linearizability of implementations can be quite complex. An essential aspect of linearizable implementations of concurrent objects is the need to preserve the real-time order of operations. In many settings, however, processes cannot determine the precise timing and relative real-time ordering of operations. Indeed, in an asynchronous system, the only ordering information available to them is based on the fact that sending a message precedes its delivery. We show that as a result, message chains must be used extensively to ensure linearizability. This paper studies the communication requirements of linearizable implementations of atomic registers in asynchronous message passing systems. We start by proving two general theorems that relate message chains to the ability to delay and reorder actions and operations in an execution of an asynchronous system, without the changes being noticeable to the processes. These are then used to prove that linearizable register implementations must create extensive message chains among operations of \emph{all} types. In particular, our results imply that linearizable implementations in asynchronous systems are necessarily costly and nontrivial, and provide insight into their structure.
