---
interest: medium
link: https://arxiv.org/abs/2609.14418
next_step: skim
priority: low
slack_ts: '1789532923.171739'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Surrogate-Assisted Genetic Programming with Phenotypic Characterisation in
  Dynamic Multi-Mode Project Scheduling
---
# Surrogate-Assisted Genetic Programming with Phenotypic Characterisation in Dynamic Multi-Mode Project Scheduling
> 原文: [https://arxiv.org/abs/2609.14418](https://arxiv.org/abs/2609.14418)

arXiv:2609.14418v1 Announce Type: new
Abstract: Dynamic multi-mode resource-constrained project scheduling requires decisions to be made under precedence constraints, limited resources, multiple execution modes, and uncertain activity durations. Genetic programming (GP) can automatically evolve heuristic rules for such problems, but its simulation-based fitness evaluation is computationally expensive. This study investigates phenotypic characterisation (PC) in surrogate-assisted GP to evolve higher-quality scheduling heuristics under a fixed budget of full simulation-based fitness evaluations. A key question is how GP individuals should be encoded into phenotypic characterisations to support effective fitness estimation. To answer this question, three PC encoding schemes with different levels of information richness are designed: priority-value encoding, which preserves raw rule outputs; rank encoding, which captures candidate ordering; and binary encoding, which represents final scheduling decisions. These encodings are combined with different distance metrics to measure behavioural similarity between GP individuals. The experimental results show that binary encoding with Euclidean distance provides the most effective and robust surrogate guidance. Further analyses show that surrogate estimation accuracy alone does not fully explain the performance differences. The PC representation also determines how effectively phenotypically redundant offspring are removed and how much behavioural diversity is retained after preselection. Ablation experiments further demonstrate that duplicate removal and surrogate preselection provide complementary benefits, with their combination producing the largest improvement. These findings highlight that effective surrogate-assisted GP depends not only on identifying promising offspring, but also on controlling redundancy and preserving useful diversity during evolutionary search.
