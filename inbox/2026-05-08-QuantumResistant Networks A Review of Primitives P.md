---
title: "Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.04129
priority: low
status: unread
interest: medium
next_step: skim
---
# Quantum-Resistant Networks: A Review of Primitives, Protocols and Best Practices
> 原文: [https://arxiv.org/abs/2605.04129](https://arxiv.org/abs/2605.04129)

arXiv:2605.04129v1 Announce Type: new
Abstract: Large-scale quantum computers threaten the public-key cryptographic foundations underpinning today's network security infrastructures. While significant progress has been made in standardizing post-quantum cryptographic (PQC) primitives and adapting individual protocols such as TLS and SSH, far less attention has been paid to the broader architectural consequences of the post-quantum transition for networked systems. In particular, many real-world deployments such as mobile networks, industrial control systems, IoT environments, and regulated infrastructures cannot assume the universal availability, deployability, or desirability of PQ public-key infrastructures. This paper presents the first comprehensive systematization of PQ-resistant network architectures, focusing on key distribution and management as a system-level design problem rather than a protocol-local substitution. We introduce a unified taxonomy spanning cryptographic foundations (symmetric-only, PQ-PKI, hybrid, and information-theoretic multi-path), key-distribution architectures (centralized, hierarchical, replicated, threshold, MPC-backed, and serverless), trust and threat models, key-management lifecycle, and deployment environments. Using this framework, we analyze the security, scalability, and operational trade-offs of a wide range of architectures under realistic PQ adversary assumptions, including harvest-now, decrypt-later attacks and partial infrastructure compromise. Our study highlights fundamental gaps in existing approaches, clarifies when PQ-PKI is necessary or avoidable, and identifies promising research directions for building cryptographically agile, quantum-resilient network infrastructures.
