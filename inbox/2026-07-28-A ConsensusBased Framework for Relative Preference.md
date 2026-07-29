---
interest: medium
link: https://arxiv.org/abs/2607.21632
next_step: skim
priority: high
slack_ts: '1785295219.722669'
source: cs.CL - Computation and Language (NLP)
status: unread
title: A Consensus-Based Framework for Relative Preference Evaluation of Large Language
  Models
---
# A Consensus-Based Framework for Relative Preference Evaluation of Large Language Models
> 原文: [https://arxiv.org/abs/2607.21632](https://arxiv.org/abs/2607.21632)

arXiv:2607.21632v1 Announce Type: new
Abstract: Traditional benchmarks for LLMs primarily rely on static datasets and objective scoring metrics, which often fail to capture differences in response quality when multiple answers are acceptable. In such settings, correctness alone is insufficient to distinguish between responses that vary in clarity, completeness, and usefulness.
This paper introduces a consensus-based evaluation framework that measures relative preference among model-generated responses rather than absolute correctness. Instead of evaluating outputs against a fixed ground truth, we assess how a panel of diverse LLMs ranks anonymized candidate responses to the same prompt. This approach treats aggregate inter-model agreement as a proxy for perceived response quality under blind conditions.
We conduct a controlled study using five state-of-the-art LLMs across multiple domains, including programming, general knowledge, safety, logical reasoning, and mathematics. Each model generates responses and independently ranks peer outputs through a structured voting process. Scores are aggregated into a Relative Intelligence Index (RII), representing how frequently a model's responses are preferred by other models.
Our findings reveal consistent preference patterns across domains, with certain models more frequently ranked highly by their peers. However, we emphasize that these results reflect inter-model preference alignment rather than objective correctness or human judgment. This framework provides a scalable, model-driven method for comparative evaluation, offering an alternative perspective on response quality in scenarios where multiple valid answers exist. While not directly aligned with human evaluation, prior work suggests that aggregated model preferences can partially correlate with human judgments, motivating this as a proxy signal.
