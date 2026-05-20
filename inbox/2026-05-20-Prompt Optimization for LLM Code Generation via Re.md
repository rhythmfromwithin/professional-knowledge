---
title: "Prompt Optimization for LLM Code Generation via Reinforcement Learning"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2605.19102
priority: low
status: unread
interest: medium
next_step: skim
---
# Prompt Optimization for LLM Code Generation via Reinforcement Learning
> 原文: [https://arxiv.org/abs/2605.19102](https://arxiv.org/abs/2605.19102)

arXiv:2605.19102v1 Announce Type: new
Abstract: Large Language Models (LLMs) can generate code from natural language, but their performance is highly sensitive to prompt formulation. We propose a reinforcement-learning-based framework that models prompt refinement as a sequential decision-making problem. A Proximal Policy Optimization (PPO) agent iteratively improves prompts using a hybrid action space that combines direct generation, genetic lexical mutation and semantic rewriting, guided by shaped rewards derived from unit-test feedback. We evaluate the framework on MBPP+, HumanEval+, and APPS using CodeT5+, CodeLLaMA, and DeepSeek-Coder as frozen code generators. On the 500-task MBPP+ test set, the PPO agent achieves strict Pass@1 scores of 57.58%, 64.80%, and 85.50%, respectively, outperforming EPiC, Reflexion, and Random-Hybrid. Soft-Pass@1 reaches 67.90%, 73.10%, and 88.20%, respectively. Similar improvements are observed on HumanEval+ and APPS across all backbone models. The results demonstrate that reinforcement learning with shaped test-driven rewards improves functional correctness in LLM-based code generation.
