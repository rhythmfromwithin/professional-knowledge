---
interest: medium
link: https://arxiv.org/abs/2603.02215
next_step: skim
priority: high
slack_ts: '1773456091.215279'
source: cs.LG - Machine Learning
status: unread
title: RxnNano:Training Compact LLMs for Chemical Reaction and Retrosynthesis Prediction
  via Hierarchical Curriculum Learning
---
# RxnNano:Training Compact LLMs for Chemical Reaction and Retrosynthesis Prediction via Hierarchical Curriculum Learning
> 原文: [https://arxiv.org/abs/2603.02215](https://arxiv.org/abs/2603.02215)

arXiv:2603.02215v1 Announce Type: new
Abstract: Chemical reaction prediction is pivotal for accelerating drug discovery and synthesis planning. Despite advances in data-driven models, current approaches are hindered by an overemphasis on parameter and dataset scaling. Some methods coupled with evaluation techniques that bypass fundamental challenges in reaction representation and fail to capture deep chemical intuition like reaction common sense and {topological atom mapping logic}. We argue that the core challenge lies in instilling these knowledge into the models. To this end, we propose a unified framework that prioritizes chemical understanding over scale through three key innovations: (1) a {Latent Chemical Consistency} objective that models reactions as movements on a continuous chemical manifold, ensuring reversible and physically plausible transformations; (2) a {Hierarchical Cognitive Curriculum} that trains the model through progressive stages, from syntax mastery to semantic reasoning, building robust chemical intuition; (3) {Atom-Map Permutation Invariance (AMPI)}, which force the model to learn invariant relational topology and balance multi-task learning. (4)and structured plan-based reasoning to improve the performance of the LLMs. Our compact {0.5B-parameter model}, \textbf{RxnNano} significantly outperforms fine-tuned LLMs ten times larger (>7B) and all the domain baselines, achieving a 23.5\% Top-1 accuracy improvement on rigorous benchmarks without test-time augmentation. https://github.com/rlisml/RxnNano.
