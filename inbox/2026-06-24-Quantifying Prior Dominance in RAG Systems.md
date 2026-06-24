---
interest: medium
link: https://arxiv.org/abs/2606.23695
next_step: skim
priority: high
slack_ts: '1782274339.037929'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Quantifying Prior Dominance in RAG Systems
---
# Quantifying Prior Dominance in RAG Systems
> 原文: [https://arxiv.org/abs/2606.23695](https://arxiv.org/abs/2606.23695)

arXiv:2606.23695v1 Announce Type: new
Abstract: Retrieval-Augmented Generation (RAG) grounds Large Language Models in external knowledge, yet current evaluations rely on discrete heuristics that suffer from ''epistemic blindness'' - failing to distinguish genuine contextual information extraction from parametric memory recall. To address this, we introduce the Normalized Context Utilization (NCU) metric, leveraging continuous token log-probabilities across zero-shot, oracle, and adversarial conditions to strictly quantify contextual information gain. Evaluating architectures ranging from 1.5B to 72B parameters alongside a proprietary commercial API reveals that for strict factual extraction (without Chain-of-Thought reasoning), traditional scaling laws exhibit extreme diminishing returns: highly efficient Small Language Models (SLMs) match or outperform high-capacity architectures. Furthermore, we demonstrate that ``Prior Dominance'' correlates with model scale and proprietary alignments. The evaluated commercial API not only overrode explicit external evidence in nearly half of adversarial conflicts, but also frequently suffered from systemic confidence collapse (Negative Transfer) when its parametric priors were contradicted. Our findings highlight the structural epistemic advantage and superior contextual adherence of SLMs in strict extraction workflows.
