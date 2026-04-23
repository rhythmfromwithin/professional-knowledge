---
interest: medium
link: https://arxiv.org/abs/2604.18614
next_step: skim
priority: medium
slack_ts: '1776915205.027309'
source: cs.DC - Distributed Computing
status: unread
title: 'HadAgent: Harness-Aware Decentralized Agentic AI Serving with Proof-of-Inference
  Blockchain Consensus'
---
# HadAgent: Harness-Aware Decentralized Agentic AI Serving with Proof-of-Inference Blockchain Consensus
> 原文: [https://arxiv.org/abs/2604.18614](https://arxiv.org/abs/2604.18614)

arXiv:2604.18614v1 Announce Type: new
Abstract: Proof-of-Work (PoW) blockchain consensus consumes vast computational resources without producing useful output, while the rapid growth of large language model (LLM) agents has created unprecedented demand for GPU computation. We present HadAgent, a decentralized agentic AI serving system that replaces hash-based mining with Proof-of-Inference (PoI), a consensus mechanism in which nodes earn block-creation rights by executing deterministic LLM inference tasks. Because verification requires only re-executing a single forward pass under identical conditions, cross-node verification operates at consensus speed. HadAgent organizes validated records into a three-lane block body with dedicated DATA, MODEL, and PROOF channels, each protected by an independent Merkle root for fine-grained tamper detection. A two-tier node architecture classifies secondary nodes as trusted or non-trusted based on historical behavior: trusted nodes serve inference results in real time through optimistic execution, while non-trusted nodes must undergo full consensus verification. A harness layer monitors node behavior through heartbeat probes, anomaly detection via deterministic recomputation, and automated trust management, creating a self-correcting feedback loop that isolates malicious or unreliable participants. Experiments on a prototype implementation demonstrate 100% detection rate and 0% false positive rate for tampered records, sub-millisecond validation latency for record and hub operations, and effective harness convergence that excludes adversarial nodes within two rounds while promoting honest nodes to trusted status within five rounds.
