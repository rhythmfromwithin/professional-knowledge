---
title: "TransGP: Task-Conditioned Transformer-Guided Genetic Programming for Multitask Dynamic Flexible Job Shop Scheduling"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2604.03705
priority: low
status: unread
interest: medium
next_step: skim
---
# TransGP: Task-Conditioned Transformer-Guided Genetic Programming for Multitask Dynamic Flexible Job Shop Scheduling
> 原文: [https://arxiv.org/abs/2604.03705](https://arxiv.org/abs/2604.03705)

arXiv:2604.03705v1 Announce Type: new
Abstract: Hyper-heuristics have become a popular approach for solving dynamic flexible job shop scheduling (DFJSS) problems. They use gradient-free optimization techniques like Genetic Programming (GP) to evolve non-differentiable heuristics. However, conventional GP methods tend to converge slowly because they rely solely on evolutionary search to find good heuristics. Existing multitask GP methods can solve multiple tasks simultaneously and speed up the search by transferring knowledge across similar tasks. But they mostly exchange heuristic building blocks without truly generating heuristics conditioned on task information. In this paper, we aim to accelerate convergence and enable task-specific heuristic generation by incorporating a task-conditioned Transformer model. The Transformer works in two ways. First, it learns the distribution of elite heuristics, biasing the search toward promising regions of the heuristic space. Second, through conditional generation, it produces heuristics tailored to specific tasks, allowing the model to handle multiple scheduling tasks at once and improving overall optimization efficiency. Based on these ideas, we propose TransGP, a Task-Conditioned Transformer-Guided GP framework. This evolutionary paradigm integrates generative modeling with GP, enabling efficient multitask heuristic learning and knowledge transfer. We evaluate TransGP on a range of DFJSS scenarios. Experimental results show that TransGP consistently outperforms multitask GP baselines, widely used handcrafted heuristics, and the pure Transformer model, achieving faster convergence, superior solution quality, and enhanced robustness.
