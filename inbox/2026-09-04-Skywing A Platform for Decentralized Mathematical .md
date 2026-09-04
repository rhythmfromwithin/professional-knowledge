---
title: "Skywing: A Platform for Decentralized Mathematical Computing in Unreliable Environments"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.03145
priority: medium
status: unread
interest: medium
next_step: skim
---
# Skywing: A Platform for Decentralized Mathematical Computing in Unreliable Environments
> 原文: [https://arxiv.org/abs/2609.03145](https://arxiv.org/abs/2609.03145)

arXiv:2609.03145v1 Announce Type: new
Abstract: Emerging edge, autonomous, and cyber-physical systems increasingly require mathematical computation across heterogeneous devices connected by unreliable communication networks. Traditional high-performance computing and distributed data-processing frameworks provide powerful abstractions for managed environments but are less suited to decentralized settings where centralized coordination, reliable communication, and global synchronization cannot be assumed. This paper presents Skywing, an open-source platform for decentralized mathematical computing in unreliable environments. Its programming model consists of three abstractions: agents represent participants in a decentralized computation, processors encapsulate algorithm-specific update rules, and iterations manage distributed execution. Skywing supports asynchronous operation, publish-subscribe communication, managed message handling, and the composition of independent algorithms into complex decentralized workflows. We demonstrate Skywing using representative algorithms from consensus, optimization, and numerical linear algebra. Experiments on the native Skywing runtime include Push Sum and Max Consensus, a composed monitoring and control workflow, resilient Push Sum under delayed communication, and resilient asynchronous Jacobi under malevolent data corruption. These demonstrations show that Skywing supports diverse decentralized algorithms while separating mathematical logic from communication and execution infrastructure. Skywing serves as both a deployment framework for decentralized applications and a research platform for developing resilient mathematical algorithms.
