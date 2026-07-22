---
title: "Multi-level context Modeling for consistent expert selection in Mixture-of-Experts"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2607.16427
priority: high
status: unread
interest: medium
next_step: skim
---
# Multi-level context Modeling for consistent expert selection in Mixture-of-Experts
> 原文: [https://arxiv.org/abs/2607.16427](https://arxiv.org/abs/2607.16427)

arXiv:2607.16427v1 Announce Type: new
Abstract: Mixture-of-Experts (MoE) enables efficient scaling of Transformer models by routing tokens to a small subset of experts. However, existing routers typically condition expert selection on shallow or isolated token representations, which often produce unstable and semantically inconsistent routing decisions across layers. In this work, we revisit expert selection from a representation perspective and identify context incompleteness as a key bottleneck limiting effective expert specialization. To address this issue, we propose Multi-level Context Fusion MOE (MCF-MOE), a framework that constructs context-aware representations by integrating complementary signals from cross-layer semantic aggregation and local token-level interactions, enabling more informative and consistent expert selection. Experiments on language modeling and understanding benchmarks demonstrate that MCF-MOE consistently improves routing consistency and downstream performance over strong MoE baselines, highlighting the importance of contextual completeness in expert routing. The code is available at https://anonymous.4open.science/r/MCFMOE.
