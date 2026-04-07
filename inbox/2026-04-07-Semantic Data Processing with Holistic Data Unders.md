---
interest: medium
link: https://arxiv.org/abs/2604.02655
next_step: skim
priority: low
slack_ts: '1775531935.156999'
source: cs.DB - Databases
status: unread
title: Semantic Data Processing with Holistic Data Understanding
---
# Semantic Data Processing with Holistic Data Understanding
> 原文: [https://arxiv.org/abs/2604.02655](https://arxiv.org/abs/2604.02655)

arXiv:2604.02655v1 Announce Type: new
Abstract: Semantic operators have increasingly become integrated within data systems to enable processing data using Large Language Models (LLMs). Despite significant recent effort in improving these operators, their accuracy is limited due to a critical flaw in their implementation: lack of holistic data understanding. In existing systems, semantic operators often process each data record independently using an LLM, without considering data context, only leveraging LLM's dataset-agnostic interpretation of the user-provided task. However, natural language is imprecise, so a task can only be accurately performed if it is correctly interpreted in the context of the dataset. For example, for classification and scoring tasks, which are typical semantic map tasks, the standard method of processing each record row by row yields inaccurate results in a wide range of datasets. We propose HoldUp, a new method for semantic data processing with holistic data understanding. HoldUp processes records jointly, leveraging cross-record relationships to correctly interpret the task within the data context. Enabling holistic data understanding, however, is challenging due to what we call LLM data understanding paradox: while large representative data subsets are necessary to provide context, feeding long inputs to LLMs causes quality degradation due to well-known long-context issues. To resolve this paradox, we develop a novel clustering algorithm to identify the latent structure within the dataset through judicious use of LLMs, inspired by bagging. Using this approach as a primitive, we develop novel clustering-based classification and scoring methods to perform these two tasks with high accuracy. Experiments across 15 real-world datasets show that HoldUp consistently outperforms existing solutions, providing up to 33% higher accuracy for classification and 30% higher accuracy for scoring and clustering tasks.
