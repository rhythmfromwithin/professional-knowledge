---
interest: medium
link: https://arxiv.org/abs/2606.26211
next_step: skim
priority: low
slack_ts: '1782447546.451059'
source: cs.CR - Cryptography and Security
status: unread
title: 'Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini
  Multi-Agent Ecosystem'
---
# Data Facts: A Metadata Schema for Structured Data Exchange in the NANDini Multi-Agent Ecosystem
> 原文: [https://arxiv.org/abs/2606.26211](https://arxiv.org/abs/2606.26211)

arXiv:2606.26211v1 Announce Type: new
Abstract: NANDini (Networked Agents Natural Distillation of Interconnected Nodal Intelligence) envisions an automated ecosystem where intelligent agents independently create, process, and exchange data to drive decisions at scale. Realizing this vision requires infrastructure beyond agent discovery and communication: agents must be able to advertise, evaluate, and verify the datasets they hold.
Current protocols, including NANDA for federated registry and A2A and MCP for inter-agent messaging, address identity and communication but provide no mechanism for structured data exchange. Existing enterprise data-sharing frameworks, such as IDS-RAM, Gaia-X, and Ocean Protocol, assume human-in-the-loop governance that is incompatible with autonomous, real-time agent interactions.
We introduce Data Facts, a core NANDini concept: a lightweight JSON metadata schema that bridges agent discovery and data access through a single pointer, `data\_facts\_url`, added to an existing Agent Facts registry record. The linked document encodes dataset identity, access tier, whether public, semi-private, or private, endpoint, a time-to-live for freshness validation, and a SHA-256 integrity checksum.
For private and semi-private data, we implement a three-layer security pipeline: JWT authentication, capability-scoped gateway authorization, and an A2A credential delegation protocol. Across 840 decision-making evaluations, data-informed agents achieve 100% accuracy versus 35.2% without data access (p < 0.001); TTL enforcement reduces stale-data errors from 37.6% to 8.8%; checksum verification achieves 100% corruption detection at all injection rates; and the security pipeline blocks all 46 forgery attempts with zero data leakage.
