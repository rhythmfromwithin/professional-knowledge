---
title: "Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2606.05241
priority: low
status: unread
interest: medium
next_step: skim
---
# Search-Time Contamination in Deep Research Agents: Measuring Performance Inflation in Public Benchmark Evaluation
> 原文: [https://arxiv.org/abs/2606.05241](https://arxiv.org/abs/2606.05241)

arXiv:2606.05241v1 Announce Type: new
Abstract: Public benchmarks enable fair and reproducible evaluation of LLM reasoning, but they become fragile for deep research agents that actively search the web during inference. Such agents may retrieve public benchmark metadata, question context, or even ground-truth answers via web search. This gives rise to Search-Time Contamination (STC), where external retrieval bypasses intended reasoning and inflates measured performance. We systematically study STC in deep research agent evaluation. We define three contamination types with increasing severity, namely Benchmark Metadata Leakage, Question-Context Leakage, and Explicit Answer Leakage, and develop detection algorithms to identify them and quantify their impact on agent performance. Evaluating modern deep research agents on six public benchmarks, we find that STC is widespread and can inflate performance by up to 4%. Our findings show that existing evaluations may overestimate true reasoning ability. We therefore advocate contamination-aware practices, including isolated sandboxes, transparent search trajectories, and controlled benchmark access.
