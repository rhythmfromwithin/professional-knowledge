---
interest: medium
link: https://arxiv.org/abs/2607.08938
next_step: skim
priority: low
slack_ts: '1783998907.301359'
source: cs.SE - Software Engineering
status: unread
title: 'Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated
  Harness Adaptation'
---
# Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation
> 原文: [https://arxiv.org/abs/2607.08938](https://arxiv.org/abs/2607.08938)

arXiv:2607.08938v1 Announce Type: new
Abstract: Frontier LLM agents are automating many business tasks, but their high inference cost makes large-scale deployment unsustainable. Small language models (SLMs) offer a cheaper alternative, yet they typically fall short when swapped into a harness designed for a frontier LLM. We show that for many routine business tasks, SLM agents can match LLM performance at 90% lower cost, when paired with an adapted harness that can be automatically discovered by a meta agent. The key insight is that much of the task difficulty is shared across instances and can be lifted from the model into the harness via tailored instructions, tools, and orchestration loops. To study this systematically, we create a framework that maps agent failure modes to harness adaptation strategies, and build a harness optimizer that automatically discovers effective adaptations from failure trajectories. Across seven business-oriented agentic tasks and three SLM families, we found optimized harnesses significantly improve performance on 16 of 21 task-SLM pairs, with seven pairs closing the SLM-LLM performance gap and the best SLM agent recovering 89.7% of LLM performance at 4% of the cost. Our analysis further shows that adaptation works best for tasks with more repetitive workflows and for SLMs with sufficient base capabilities. Together, these results suggest that harness adaptation can expand the practical deployment range of SLM agents in routine business tasks.
