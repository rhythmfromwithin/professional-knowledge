---
interest: medium
link: https://arxiv.org/abs/2605.27375
next_step: skim
priority: high
slack_ts: '1780028404.346459'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world
  Tasks'
---
# LCO: LLM-based Constraint Optimization for Safer Agentic LLMs in Real-world Tasks
> 原文: [https://arxiv.org/abs/2605.27375](https://arxiv.org/abs/2605.27375)

arXiv:2605.27375v1 Announce Type: new
Abstract: Large Language Models (LLMs) are increasingly acting as autonomous agents, but their continuous interaction with the environment can lead to in-context reward hacking (ICRH), a phenomenon where LLMs iteratively optimize their behavior to maximize proxy objectives, inadvertently producing harmful side effects. Existing defense methods are insufficient to address this risk, as ICRH arises not from adversarial inputs but from the model's own over-optimization. To mitigate this issue, we propose \textbf{LLM-based Constraint Optimization (LCO)}, a framework that effectively reduces ICRH without model fine-tuning. LCO consists of two modules: \textit{self-thought module}, which guides the LLM to proactively deliberate and integrate potential safety constraints before execution; and \textit{evolutionary sampling module}, which employs LLM-based crossover and mutation to constrain the model's actions within a safe solution space while maintaining task performance. Experimental results demonstrate that LCO substantially alleviates ICRH in both output-refine and policy-refine scenarios. In particular, on the tweet engagement optimization task, LCO achieves a 39% reduction in the Toxicity Growth Rate (TGR) on GPT-4, while on the policy optimization benchmark, it reduces the ICRH Occurrence Rate by 15.23%, demonstrating safety improvement without sacrificing task performance.
