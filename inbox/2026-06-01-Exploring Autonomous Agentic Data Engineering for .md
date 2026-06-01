---
title: "Exploring Autonomous Agentic Data Engineering for Model Specialization"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2605.30407
priority: high
status: unread
interest: medium
next_step: skim
---
# Exploring Autonomous Agentic Data Engineering for Model Specialization
> 原文: [https://arxiv.org/abs/2605.30407](https://arxiv.org/abs/2605.30407)

arXiv:2605.30407v1 Announce Type: new
Abstract: Large Language Models (LLMs) have demonstrated strong performance on general tasks, while often struggling to adapt to specialized domains without high-quality domain-specific data. Existing LLM-based data curation methods primarily rely on human-designed workflows, leaving it unexamined whether LLMs can autonomously execute an end-to-end data engineering pipeline for model specialization. We formalize \textbf{Autonomous Agentic Data Engineering}, a novel task designed to evaluate LLMs as autonomous data engineers that drive model specialization through end-to-end data curation. We frame data as an optimizable component and study agents that plan, generate, and iteratively optimize training data across multiple domains, guided by post-training performance improvement. Experiments show that autonomous LLM data engineers yield substantial gains, as GPT-5.2 constructs a training curriculum that improves a student model by \textbf{57.29\%}, entirely through iterative, agent-driven data adaptation. By illuminating both potential and bottlenecks, our study establishes autonomous data engineering as a measurable capability and charts a path toward agent-driven model specialization\footnote{Code will be released at https://github.com/zjunlp/DataAgent.}.
