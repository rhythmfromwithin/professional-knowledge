---
interest: medium
link: https://arxiv.org/abs/2607.27698
next_step: skim
priority: low
slack_ts: '1786328462.775839'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge
  for Dynamic Multi-Mode Project Scheduling
---
# Guiding Large Language Models with Genetic Programming-Evolved Heuristic Knowledge for Dynamic Multi-Mode Project Scheduling
> 原文: [https://arxiv.org/abs/2607.27698](https://arxiv.org/abs/2607.27698)

arXiv:2607.27698v1 Announce Type: cross
Abstract: In dynamic multi-mode project scheduling, activities have alternative execution modes and uncertain durations, while precedence relations and limited resources constrain their execution. Heuristic priority rules support fast online decisions, but their design requires substantial domain expertise. Genetic programming (GP) hyper-heuristics can automatically evolve such rules. Large language models (LLMs), meanwhile, provide a flexible interface for interpreting scheduling information and explaining decisions. However, zero-shot LLM decisions may lack domain knowledge, consume many tokens, and vary across repeated queries. GP-evolved rules therefore provide a potential source of scheduling knowledge for guiding LLM decisions. Unlike existing LLM--GP hybrids that use LLMs to support heuristic evolution, we transfer knowledge in the reverse direction, using knowledge extracted from high-quality GP rules to guide an online LLM decision maker. We extract knowledge from high-quality GP rules and inject it through Feature Selection, Feature Hint, Rule Reference, and Rule Follow. These mechanisms are evaluated in terms of scheduling performance, token consumption, decision stability, and the feature focus expressed in generated rationales. GP-derived guidance generally improves the unguided LLM, but its representation matters. Simplifying the decision context or supplying explicit decision logic is more effective than highlighting important features. Feature Selection offers the best token efficiency, whereas Rule Follow achieves strong performance at greater token cost. Guidance also improves decision stability and changes the features expressed in generated rationales.
