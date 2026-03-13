---
interest: medium
link: https://arxiv.org/abs/2603.09978
next_step: skim
priority: low
slack_ts: '1773369886.504859'
source: cs.SE - Software Engineering
status: unread
title: 'One Model, Many Skills: Parameter-Efficient Fine-Tuning for Multitask Code
  Analysis'
---
# One Model, Many Skills: Parameter-Efficient Fine-Tuning for Multitask Code Analysis
> 原文: [https://arxiv.org/abs/2603.09978](https://arxiv.org/abs/2603.09978)

arXiv:2603.09978v1 Announce Type: new
Abstract: Large language models have recently surpassed specialized systems on code generation, yet their effectiveness on other code-analysis tasks remains less clear. At the same time, multi-task learning offers a way to unify diverse objectives within a single model, but fully fine-tuning LLMs across tasks is computationally prohibitive. Parameter-efficient fine-tuning mitigates this cost by updating only a small fraction of weights. Although PEFT has proven effective in single-task settings, its potential for multi-task learning has not yet been systematically explored. We present the first comprehensive evaluation of multi-task PEFT for code analysis, comparing several methods across diverse tasks and model architectures. Our experiments show that a single PEFT module shared across tasks can match, and in some cases surpass, full multi-task fine-tuning, confirming that the benefits of PEFT extend beyond isolated tasks. When comparing single-task and multi-task setups, we find that multi-task PEFT achieves a favorable performance-efficiency trade-off: it delivers accuracy close to single-task fine-tuning while reducing storage requirements, cutting the number of trainable parameters by a factor of the task count, and lowering computation costs by as much as 85%. At the same time, multi-task gains remain sensitive to task grouping. Through task-pairing experiments, we identify key factors shaping outcomes: task stability, model architecture, task complementarity, asymmetry, and dataset quality determine the success of co-fine-tuning. Finally, we benchmark efficient multi-task PEFT against direct prompting of open-source general-purpose LLMs, including DeepSeek, Qwen, Mistral, CodeLlama, and StarCoder. Despite their strong performance in code generation, these models underperform on analysis tasks, where even a 1B-parameter model with multi-task PEFT achieves significantly better results.
