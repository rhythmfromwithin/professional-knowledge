---
interest: medium
link: https://arxiv.org/abs/2609.25325
next_step: skim
priority: low
slack_ts: '1790137560.443869'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Online Automated Algorithm Design with Large Language Models
---
# Online Automated Algorithm Design with Large Language Models
> 原文: [https://arxiv.org/abs/2609.25325](https://arxiv.org/abs/2609.25325)

arXiv:2609.25325v1 Announce Type: new
Abstract: Large language models (LLMs) enable automated algorithm design (AAD) through reasoning and code synthesis. However, most existing LLM-based AAD methods separate algorithm design from target optimization, deploying a fixed design even as the optimization state evolves. Conventional adaptive optimizers can respond to such changes, but their adjustments remain confined to predefined parameters, operators, or strategies. To address these limitations, we introduce online LLM-based AAD, a novel optimization paradigm that treats the algorithm itself as a state-dependent decision variable. At each stage, LLM agents synthesize an algorithm with new behavior logic from the current optimization state. Executing the generated algorithm advances the search and provides feedback for subsequent designs, coupling algorithm design with target optimization without requiring a separate offline algorithm pretraining stage. To implement this paradigm, we propose OnDesign, a multi-agent framework that reconciles competing design perspectives to synthesize executable algorithms and uses execution feedback to refine how runtime evidence is interpreted for subsequent designs. We evaluate OnDesign across two mainstream black-box optimization paradigms on three scenarios: Bayesian optimization, evolutionary continuous optimization, and evolutionary mixed-variable optimization. Extensive experiments on six benchmark suites and one engineering problem across multiple problem dimensions demonstrate superior overall performance over conventional optimizers and offline LLM-based AAD methods.
