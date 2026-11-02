---
title: "Resource Locks and Fast Unlock for Shared Balances in Certificate-Based Payment Systems"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.41207
priority: medium
status: unread
interest: medium
next_step: skim
---
# Resource Locks and Fast Unlock for Shared Balances in Certificate-Based Payment Systems
> 原文: [https://arxiv.org/abs/2610.41207](https://arxiv.org/abs/2610.41207)

arXiv:2610.41207v1 Announce Type: new
Abstract: Certificate-based payment systems such as FastPay settle a payment with one round of signatures from a quorum of validators and avoid global ordering. The client collects the signatures, and validators never talk to each other. We observe that this client-driven design is complete only as long as no lock is ever undone. Each account has a single writer, a conflict can only come from that writer's own misbehavior, and the account stays locked as the penalty. Stablecoin payments routinely need balances that several accounts debit: treasuries, merchant pools, allowances and subscriptions. There, honest accounts race, locks must be undone, and a quorum certificate held privately by a client can be silently overridden. We prove that no unlock rule is safe in this setting unless certificate formation is visible to validators.
We present a hybrid protocol. Personal accounts keep the client-driven FastPay path unchanged. A shared resource is a balance with its own version number and a set of authorized accounts. Transactions on shared resources are submitted to any validator and certified by a two-phase broadcast, ECHO then READY. The admission check requires both the sender's nonce and the resource's nonce to be free. Without contention, this path needs no consensus. When concurrent debits split the votes in any proportion, validators detect the split themselves, freeze the affected resource version, and resolve it with one agreement instance scoped to that version. Losing transactions return their sender nonce. We prove consistency, no overdraft, validity, finality and liveness. The protocol composes with the PDCC reconfiguration protocol.
