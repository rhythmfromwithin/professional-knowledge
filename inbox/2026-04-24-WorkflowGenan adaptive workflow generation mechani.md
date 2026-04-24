---
title: "WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.19756
priority: high
status: unread
interest: medium
next_step: skim
---
# WorkflowGen:an adaptive workflow generation mechanism driven by trajectory experience
> 原文: [https://arxiv.org/abs/2604.19756](https://arxiv.org/abs/2604.19756)

arXiv:2604.19756v1 Announce Type: new
Abstract: Large language model (LLM) agents often suffer from high reasoning overhead, excessive token consumption, unstable execution, and inability to reuse past experiences in complex tasks like business queries, tool use, and workflow orchestration. Traditional methods generate workflows from scratch for every query, leading to high cost, slow response, and poor robustness. We propose WorkflowGen, an adaptive, trajectory experience-driven framework for automatic workflow generation that reduces token usage and improves efficiency and success rate. Early in execution, WorkflowGen captures full trajectories and extracts reusable knowledge at both node and workflow levels, including error fingerprints, optimal tool mappings, parameter schemas, execution paths, and exception-avoidance strategies. It then employs a closed-loop mechanism that performs lightweight generation only on variable nodes via trajectory rewriting, experience updating, and template induction. A three-tier adaptive routing strategy dynamically selects among direct reuse, rewriting-based generation, and full initialization based on semantic similarity to historical queries. Without large annotated datasets, we qualitatively compare WorkflowGen against real-time planning, static single trajectory, and basic in-context learning baselines. Our method reduces token consumption by over 40 percent compared to real-time planning, improves success rate by 20 percent on medium-similarity queries through proactive error avoidance and adaptive fallback, and enhances deployability via modular, traceable experiences and cross-scenario adaptability. WorkflowGen achieves a practical balance of efficiency, robustness, and interpretability, addressing key limitations of existing approaches.
