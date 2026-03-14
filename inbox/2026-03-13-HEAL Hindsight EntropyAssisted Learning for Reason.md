---
interest: medium
link: https://arxiv.org/abs/2603.10359
next_step: skim
priority: high
slack_ts: '1773456135.999539'
source: cs.AI - Artificial Intelligence
status: unread
title: 'HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation'
---
# HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation
> 原文: [https://arxiv.org/abs/2603.10359](https://arxiv.org/abs/2603.10359)

arXiv:2603.10359v1 Announce Type: new
Abstract: Distilling reasoning capabilities from Large Reasoning Models (LRMs) into smaller models is typically constrained by the limitation of rejection sampling. Standard methods treat the teacher as a static filter, discarding complex "corner-case" problems where the teacher fails to explore valid solutions independently, thereby creating an artificial "Teacher Ceiling" for the student. In this work, we propose Hindsight Entropy-Assisted Learning (HEAL), an RL-free framework designed to bridge this reasoning gap. Drawing on the educational theory of the Zone of Proximal Development(ZPD), HEAL synergizes three core modules: (1) Guided Entropy-Assisted Repair (GEAR), an active intervention mechanism that detects critical reasoning breakpoints via entropy dynamics and injects targeted hindsight hints to repair broken trajectories; (2) Perplexity-Uncertainty Ratio Estimator (PURE), a rigorous filtering protocol that decouples genuine cognitive breakthroughs from spurious shortcuts; and (3) Progressive Answer-guided Curriculum Evolution (PACE), a three-stage distillation strategy that organizes training from foundational alignment to frontier breakthrough. Extensive experiments on multiple benchmarks demonstrate that HEAL significantly outperforms traditional SFT distillation and other baselines.
