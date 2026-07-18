---
interest: medium
link: https://arxiv.org/abs/2607.13634
next_step: skim
priority: medium
slack_ts: '1784344408.369169'
source: cs.DC - Distributed Computing
status: unread
title: 'gDMC: A Generic Distributed Model Counting Framework via Work-Stealing'
---
# gDMC: A Generic Distributed Model Counting Framework via Work-Stealing
> 原文: [https://arxiv.org/abs/2607.13634](https://arxiv.org/abs/2607.13634)

arXiv:2607.13634v1 Announce Type: new
Abstract: Propositional Model Counting ($\#\mathsf{SAT}$) is essential for probabilistic reasoning but faces scalability limits on single cores. Existing distributed approaches struggle with high initialization overheads (static decomposition) or rigid architecture. We propose a novel, generic framework for distributed \emph{exact} model counting. Leveraging C++ templates, our architecture decouples parallel orchestration from solving logic, enabling state-of-the-art solvers to be parallelized with minimal modification. We implement an adaptive work-stealing strategy that ensures effective load balancing. Experiments on competition benchmarks show that our approach achieves near-linear scalability and significantly outperforms existing distributed solvers.
