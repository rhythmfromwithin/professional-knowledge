---
interest: medium
link: https://arxiv.org/abs/2604.26997
next_step: skim
priority: low
slack_ts: '1777692903.701099'
source: cs.CR - Cryptography and Security
status: unread
title: 'Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent
  Discovery, Identity, and Governance in Kubernetes'
---
# Agent Name Service (ANS): A Proof-of-Concept Trust Layer for Secure AI Agent Discovery, Identity, and Governance in Kubernetes
> 原文: [https://arxiv.org/abs/2604.26997](https://arxiv.org/abs/2604.26997)

arXiv:2604.26997v1 Announce Type: new
Abstract: Autonomous AI agent ecosystems require stronger mechanisms for secure discovery, identity verification, capability attestation, and policy governance. Current deployments frequently lack (1) uniform agent discovery, (2) cryptographic agent authentication, (3) capability proofs that protect secrets, and (4) enforceable policy controls. This paper presents an implementation-oriented proof of concept for the Agent Name Service (ANS), a DNS-inspired trust layer for AI agent discovery and interoperability in Kubernetes, grounded in the ANS protocol specification~\cite{huang2025ans}. The implementation uses Decentralized Identifiers (DIDs), Verifiable Credentials (VCs), policy-as-code enforcement with Open Policy Agent (OPA), and Kubernetes-native integration patterns (CRDs, admission controls, service mesh integration). In a demo research environment (3-node cluster, 50-agent workflow simulation), we observe sub-10ms response in demonstrated service paths and full success for scripted demo deployment scenarios. We explicitly scope these findings as proof-of-concept evidence rather than production certification. We further provide a threat model, assumptions, and limitations to separate implemented evidence from protocol-defined and roadmap capabilities. The result is an evidence-grounded pathway from ANS protocol concepts to reproducible engineering practice for secure multi-agent systems.
