---
interest: medium
link: https://arxiv.org/abs/2608.07539
next_step: skim
priority: low
slack_ts: '1786501796.622219'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'AutoPSO: A Metaframework for Automated Particle Swarm Optimization'
---
# AutoPSO: A Metaframework for Automated Particle Swarm Optimization
> 原文: [https://arxiv.org/abs/2608.07539](https://arxiv.org/abs/2608.07539)

arXiv:2608.07539v2 Announce Type: new
Abstract: Particle swarm optimization (PSO) is a widely used metaheuristic, prized for its simplicity and small parameter set. Although decades of research have produced numerous PSO variants that improve performance by modifying key components (e.g., parameter schedules, swarm topologies, or updating rules), two fundamental challenges persist. First, most existing approaches are problem-specific and hand-crafted, leading to poor cross-task generalization and forcing practitioners to navigate an impractically large design space, which also hinders systematic reuse of prior effective mechanisms. Second, mainstream implementations remain CPU-bound, constraining scalability and substantially increasing computational cost in real-world applications. To address these challenges, we propose {AutoPSO}, a highly automated metaframework for constructing customized PSO algorithms. AutoPSO formulates PSO-based optimization as a bi-level process: an outer search explores the joint space of effective PSO components, while an inner loop instantiates candidate variants to solve the target task and provide feedback. The outer search operates over a curated, open-design component pool, supporting flexible replacement of the component set and the outer optimizer. Crucially, by leveraging EvoX for population tensorization and batched evaluations, AutoPSO can efficiently assess thousands of particles within practical time budgets. Comprehensive experiments on numerical benchmarks and neuroevolution robotic control tasks demonstrate that AutoPSO consistently discovers novel PSO variants that significantly outperform strong baselines. Ablation and scalability studies further highlight the contribution of individual algorithmic components and confirm that AutoPSO achieves increasing performance gains with larger swarm sizes. Code is available at {https://github.com/EMI-Group/autopso}.
