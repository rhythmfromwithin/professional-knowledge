---
interest: medium
link: https://arxiv.org/abs/2604.02434
next_step: skim
priority: high
slack_ts: '1775531922.292369'
source: cs.AI - Artificial Intelligence
status: unread
title: Compositional Neuro-Symbolic Reasoning
---
# Compositional Neuro-Symbolic Reasoning
> 原文: [https://arxiv.org/abs/2604.02434](https://arxiv.org/abs/2604.02434)

arXiv:2604.02434v1 Announce Type: new
Abstract: We study structured abstraction-based reasoning for the Abstraction and Reasoning Corpus (ARC) and compare its generalization to test-time approaches. Purely neural architectures lack reliable combinatorial generalization, while strictly symbolic systems struggle with perceptual grounding. We therefore propose a neuro-symbolic architecture that extracts object-level structure from grids, uses neural priors to propose candidate transformations from a fixed domain-specific language (DSL) of atomic patterns, and filters hypotheses using cross-example consistency. Instantiated as a compositional reasoning framework based on unit patterns inspired by human visual abstraction, the system augments large language models (LLMs) with object representations and transformation proposals. On ARC-AGI-2, it improves base LLM performance from 16% to 24.4% on the public evaluation set, and to 30.8% when combined with ARC Lang Solver via a meta-classifier. These results demonstrate that separating perception, neural-guided transformation proposal, and symbolic consistency filtering improves generalization without task-specific finetuning or reinforcement learning, while reducing reliance on brute-force search and sampling-based test-time scaling. We open-source the ARC-AGI-2 Reasoner code (https://github.com/CoreThink-AI/arc-agi-2-reasoner).
