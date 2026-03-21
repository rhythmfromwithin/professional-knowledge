---
title: "Act While Thinking: Accelerating LLM Agents via Pattern-Aware Speculative Tool Execution"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.18897
priority: medium
status: unread
interest: medium
next_step: skim
---
# Act While Thinking: Accelerating LLM Agents via Pattern-Aware Speculative Tool Execution
> 原文: [https://arxiv.org/abs/2603.18897](https://arxiv.org/abs/2603.18897)

arXiv:2603.18897v1 Announce Type: new
Abstract: LLM-powered agents are emerging as a dominant paradigm for autonomous task solving. Unlike standard inference workloads, agents operate in a strictly serial "LLM-tool" loop, where the LLM must wait for external tool execution at every step. This execution model introduces severe latency bottlenecks. To address this problem, we propose PASTE, a Pattern-Aware Speculative Tool Execution method designed to hide tool latency through speculation. PASTE is based on the insight that although agent requests are semantically diverse, they exhibit stable application level control flows (recurring tool-call sequences) and predictable data dependencies (parameter passing between tools). By exploiting these properties, PASTE improves agent serving performance through speculative tool execution. Experimental results against state of the art baselines show that PASTE reduces average task completion time by 48.5% and improves tool execution throughput by 1.8x.
