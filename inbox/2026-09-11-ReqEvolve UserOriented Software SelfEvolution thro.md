---
title: "ReqEvolve: User-Oriented Software Self-Evolution through Automatic Requirement Interpretation"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2609.10590
priority: low
status: unread
interest: medium
next_step: skim
---
# ReqEvolve: User-Oriented Software Self-Evolution through Automatic Requirement Interpretation
> 原文: [https://arxiv.org/abs/2609.10590](https://arxiv.org/abs/2609.10590)

arXiv:2609.10590v1 Announce Type: new
Abstract: The paradigm of software self-evolution enables systems to autonomously extend and reconfigure their own capabilities during execution in response to technical specifications. Yet requests for new functionality often originate from end users and are rarely expressed in technical terms. As a result, developers must translate user needs into technical specifications before the system can evolve, delaying early validation of the requested functionality by preventing users from immediately observing the resulting behaviour. To address this gap, we present ReqEvolve, a runtime code generation system that enables user-driven self-evolution by accepting high-level user requests. The system integrates automatic requirements engineering (RE) and test-driven development (TDD) to transform these requests into executable functionality through clarification, specification decomposition, test generation, and runtime integration. We evaluate ReqEvolve on 72 software evolution cases across 18 projects against two baselines: SpecFix, an RE-focused code generation approach, and an ablation variant of our system. ReqEvolve achieves 89.2% Pass@1, outperforming SpecFix by 18.8% (p < 0.01, r = 0.79, large effect) and the ablation baseline by 32.6% (p < 0.001, r = 0.88, large effect). These results provide initial evidence that user-driven self-evolution is a viable paradigm for autonomously extending software capabilities from user requests, thereby accelerating requirements validation prior to developer verification.
