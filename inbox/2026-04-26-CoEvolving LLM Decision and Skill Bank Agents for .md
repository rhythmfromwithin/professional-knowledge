---
interest: medium
link: https://arxiv.org/abs/2604.20987
next_step: skim
priority: high
slack_ts: '1777261685.349969'
source: cs.AI - Artificial Intelligence
status: unread
title: Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks
---
# Co-Evolving LLM Decision and Skill Bank Agents for Long-Horizon Tasks
> 原文: [https://arxiv.org/abs/2604.20987](https://arxiv.org/abs/2604.20987)

arXiv:2604.20987v1 Announce Type: new
Abstract: Long horizon interactive environments are a testbed for evaluating agents skill usage abilities. These environments demand multi step reasoning, the chaining of multiple skills over many timesteps, and robust decision making under delayed rewards and partial observability. Games are a good testbed for evaluating agent skill usage in environments. Large Language Models (LLMs) offer a promising alternative as game playing agents, but they often struggle with consistent long horizon decision making because they lack a mechanism to discover, retain, and reuse structured skills across episodes. We present COSPLAY, a co evolution framework in which an LLM decision agent retrieves skills from a learnable skill bank to guide action taking, while an agent managed skill pipeline discovers reusable skills from the agents unlabeled rollouts to form a skill bank. Our framework improves both the decision agent to learn better skill retrieval and action generation, while the skill bank agent continually extracts, refines, and updates skills together with their contracts. Experiments across six game environments show that COSPLAY with an 8B base model achieves over 25.1 percent average reward improvement against four frontier LLM baselines on single player game benchmarks while remaining competitive on multi player social reasoning games.
