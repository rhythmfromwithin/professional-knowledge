---
title: "COLE$^+$: Towards Practical Column-based Learned Storage for Blockchain Systems"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2603.00509
priority: low
status: unread
interest: medium
next_step: skim
---
# COLE$^+$: Towards Practical Column-based Learned Storage for Blockchain Systems
> 原文: [https://arxiv.org/abs/2603.00509](https://arxiv.org/abs/2603.00509)

arXiv:2603.00509v1 Announce Type: new
Abstract: Blockchain provides a decentralized and tamper-resistant ledger for securely recording transactions across a network of untrusted nodes. While its transparency and integrity are beneficial, the substantial storage requirements for maintaining a complete transaction history present significant challenges. For example, Ethereum nodes require around 23TB of storage, with an annual growth rate of 4TB. Prior studies have employed various strategies to mitigate the storage challenges. Notably, COLE significantly reduces storage size and improves throughput by adopting a column-based design that incorporates a learned index, effectively eliminating data duplication in the storage layer. However, this approach has limitations in supporting chain reorganization during blockchain forks and state pruning to minimize storage overhead. In this paper, we propose COLE$^+$, an enhanced storage solution designed to address these limitations. COLE$^+$ incorporates a novel rewind-supported in-memory tree structure for handling chain reorganization, leveraging content-defined chunking (CDC) to maintain a consistent hash digest for each block. For on-disk storage, a new two-level Merkle Hash Tree (MHT) structure, called prunable version tree, is developed to facilitate efficient state pruning. Both theoretical and empirical analyses show the effectiveness of COLE$^+$ and its potential for practical application in real-world blockchain systems.
