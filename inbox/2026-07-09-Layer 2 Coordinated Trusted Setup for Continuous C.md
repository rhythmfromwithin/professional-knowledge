---
title: "Layer 2 Coordinated Trusted Setup for Continuous CRS Generation"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.05776
priority: medium
status: unread
interest: medium
next_step: skim
---
# Layer 2 Coordinated Trusted Setup for Continuous CRS Generation
> 原文: [https://arxiv.org/abs/2607.05776](https://arxiv.org/abs/2607.05776)

arXiv:2607.05776v1 Announce Type: new
Abstract: Zero-knowledge proof systems rely on a trusted setup phase to generate a Common Reference String (CRS), yet existing approaches are typically static, one-time ceremonies that are inflexible and vulnerable to long-term compromise. Offloading continuous, recurring trusted setups to a decentralized Layer 2 (L2) network introduces a fundamental coordination challenge arising from the mismatch between high-throughput transaction processing and the multi-round requirements of trusted setup ceremonies. This paper presents an L2-coordinated framework that safely decouples transaction pipelines from ceremony execution to achieve automated, continuous CRS generation without centralized coordination. We design and implement two protocol variants over a decentralized, PBFT-coordinated ZK-rollup architecture: an on-chain smart contract approach and an asynchronous peer-to-peer consensus variant. Both designs utilize non-interactive zero-knowledge proofs of knowledge alongside commit-reveal structures to eliminate adaptive manipulation vectors and isolate ceremony latency. Experimental evaluations under simulated wide-area network constraints and adversarial conditions demonstrate that our architecture successfully isolates ceremony liveness. Continuous setups complete reliably within practical time bounds despite node dropouts or malicious contributions, while preserving stable L2 transaction throughput.
