---
interest: medium
link: https://arxiv.org/abs/2603.06620
next_step: skim
priority: low
slack_ts: '1773631327.120579'
source: cs.SE - Software Engineering
status: unread
title: 'GraphSkill: Documentation-Guided Hierarchical Retrieval-Augmented Coding for
  Complex Graph Reasoning'
---
# GraphSkill: Documentation-Guided Hierarchical Retrieval-Augmented Coding for Complex Graph Reasoning
> 原文: [https://arxiv.org/abs/2603.06620](https://arxiv.org/abs/2603.06620)

arXiv:2603.06620v1 Announce Type: new
Abstract: The growing demand for automated graph algorithm reasoning has attracted increasing attention in the large language model (LLM) community. Recent LLM-based graph reasoning methods typically decouple task descriptions from graph data, generate executable code augmented by retrieval from technical documentation, and refine the code through debugging. However, we identify two key limitations in existing approaches: (i) they treat technical documentation as flat text collections and ignore its hierarchical structure, leading to noisy retrieval that degrades code generation quality; and (ii) their debugging mechanisms focus primarily on runtime errors, yet ignore more critical logical errors. To address them, we propose {\method}, an \textit{agentic hierarchical retrieval-augmented coding framework} that exploits the document hierarchy through top-down traversal and early pruning, together with a \textit{self-debugging coding agent} that iteratively refines code using automatically generated small-scale test cases. To enable comprehensive evaluation of complex graph reasoning, we introduce a new dataset, {\dataset}, covering small-scale, large-scale, and composite graph reasoning tasks. Extensive experiments demonstrate that our method achieves higher task accuracy and lower inference cost compared to baselines\footnote{The code is available at \href{https://github.com/FairyFali/GraphSkill}{\textcolor{blue}{https://github.com/FairyFali/GraphSkill}}.}.
