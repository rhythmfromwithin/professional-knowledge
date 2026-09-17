---
title: "State Without a Landlord: An Architecture Proposal for Peer-to-Peer Replication of Durable Workflow State"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.17645
priority: low
status: unread
interest: medium
next_step: skim
---
# State Without a Landlord: An Architecture Proposal for Peer-to-Peer Replication of Durable Workflow State
> 原文: [https://arxiv.org/abs/2609.17645](https://arxiv.org/abs/2609.17645)

arXiv:2609.17645v1 Announce Type: new
Abstract: Durable-execution frameworks commonly journal execution steps of a long-running function and reconstruct state by deterministic replay; the journal is therefore the workflow's authoritative state, and in current deployments it typically resides with whichever provider hosts the run. This paper examines what changes if the journal is instead an authenticated, append-only log replicated among the parties to the workflow. We propose an architecture in which runs are chains of single-writer epoch cores; executor succession is governed by quorum-finalized closure certificates; durability, timeout, and checkpoint decisions are carried by explicit certificates rather than implicit trust; and large payloads travel a separate content-addressed distribution plane. A threat model separates what signatures establish (authorship and order) from what they do not (truth of recorded effects). We state the design as a set of typed artifacts and invariants, identify which claims are established by existing systems and which are proposals requiring validation, and define the prototype experiments, including specific adversarial cases, that would validate or falsify the proposal's central mechanisms.
