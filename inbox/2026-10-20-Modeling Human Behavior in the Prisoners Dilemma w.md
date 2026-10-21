---
interest: medium
link: https://arxiv.org/abs/2610.23860
next_step: skim
priority: high
slack_ts: '1792556404.547179'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Modeling Human Behavior in the Prisoner's Dilemma with Large Language Models
---
# Modeling Human Behavior in the Prisoner's Dilemma with Large Language Models
> 原文: [https://arxiv.org/abs/2610.23860](https://arxiv.org/abs/2610.23860)

arXiv:2610.23860v1 Announce Type: new
Abstract: The Prisoner's Dilemma has long served as a foundational framework for studying human decision-making and cooperative outcomes across social scenarios, yet human behavior consistently deviates from predictions of fully rational economic theory. Previous works have studied human and LLM outcomes in the Prisoner's Dilemma; however, these studies have lacked at least one key feature: a memory component for LLM agents, accessible open-source models, or comparison against empirical human data. This project investigates whether open-source LLMs, TII Falcon 7B Instruct, Google Gemma 7B, Meta Llama 3.1 8B Instruct, Microsoft Phi Mini MoE Instruct, and Qwen 2.5 7B Instruct, can model human cooperation patterns in repeated Prisoner's Dilemma games, while examining how an LLM's knowledge that its opponent will be shuffled affects its decisions. Using a standardized prompting framework, we simulated interactions in two trial types: a fixed-partner setting where both agents retain memory, and a shuffled-partner setting where a memory-enabled agent, informed that its opponent changes across rounds, interacts with a memoryless agent. For each trial, we measured cooperation rates over 100 rounds and 10-round increments and compared them to human data from Montero-Porras et al. (2022). Under both frameworks, all LLMs differed from the human cooperation rate. Open-source LLMs generally over-cooperated relative to humans, particularly in the shuffled framework, where human cooperation averaged 28.5% while several models exceeded 80%. Qwen-2.5-7B-Instruct showed deterministic tendencies, while Phi-mini-MoE-Instruct displayed greater variability and briefly approximated human rates. These findings suggest that LLMs have potential as behavioral simulation agents and provide a benchmark across two interaction environments, although open-source models are not yet reliable substitutes for human participants.
