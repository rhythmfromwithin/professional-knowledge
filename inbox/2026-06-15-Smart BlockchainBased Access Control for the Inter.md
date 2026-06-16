---
interest: medium
link: https://arxiv.org/abs/2606.13798
next_step: skim
priority: low
slack_ts: '1781586961.605489'
source: cs.CR - Cryptography and Security
status: unread
title: Smart Blockchain-Based Access Control for the Internet of Things
---
# Smart Blockchain-Based Access Control for the Internet of Things
> 原文: [https://arxiv.org/abs/2606.13798](https://arxiv.org/abs/2606.13798)

arXiv:2606.13798v1 Announce Type: new
Abstract: Securing access control in large-scale Internet of Things (IoT) deployments requires mechanisms that adapt to risk while preserving low latency for benign traffic. Permissioned blockchains such as Hyperledger Fabric offer auditability through smart contracts, but static endorsement policies impose the same validation depth on all requests, regardless of security posture. We propose a risk-adaptive enforcement layer for Hyperledger Fabric that couples an off-chain LSTM-based risk oracle with deterministic on-chain checks. The oracle assigns each request to a tier (Low, Moderate, High) and issues a signed attestation bound to the client identity and target key/version. Endorsing peers verify the attestation in chaincode and enforce tier-conditioned SBE policies without modifying the ordering service or consensus. Experiments on a Fabric testbed show that tier-conditioned endorsement strengthens validation for higher-risk requests while retaining low confirmation latency for benign workloads.
