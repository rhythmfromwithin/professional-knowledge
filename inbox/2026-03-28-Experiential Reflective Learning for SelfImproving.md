---
title: "Experiential Reflective Learning for Self-Improving LLM Agents"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.24639
priority: high
status: unread
interest: medium
next_step: skim
---
# Experiential Reflective Learning for Self-Improving LLM Agents
> 原文: [https://arxiv.org/abs/2603.24639](https://arxiv.org/abs/2603.24639)

arXiv:2603.24639v1 Announce Type: new
Abstract: Recent advances in large language models (LLMs) have enabled the development of autonomous agents capable of complex reasoning and multi-step problem solving. However, these agents struggle to adapt to specialized environments and do not leverage past interactions, approaching each new task from scratch regardless of their accumulated experience. We introduce Experiential Reflective Learning (ERL), a simple self-improvement framework that enables rapid environment adaptation through experiential learning. ERL reflects on task trajectories and outcomes to generate heuristics, capturing actionable lessons that transfer across tasks. At test time, relevant heuristics are retrieved based on the current task and injected into the agent's context to guide execution. On the Gaia2 benchmark, ERL improves success rate by 7.8% over a ReAct baseline, with large gains in task completion reliability, and outperforms prior experiential learning methods. Through systematic ablations, we find that selective retrieval is essential and that heuristics provide more transferable abstractions than few-shot trajectory prompting. These results demonstrate that reflecting on single-attempt experiences to extract transferable heuristics enables effective agent self-improvement.
