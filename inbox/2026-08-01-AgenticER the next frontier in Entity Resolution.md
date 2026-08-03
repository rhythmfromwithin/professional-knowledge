---
interest: medium
link: https://arxiv.org/abs/2607.27435
next_step: skim
priority: low
slack_ts: '1785728288.433579'
source: cs.DB - Databases
status: unread
title: 'AgenticER: the next frontier in Entity Resolution'
---
# AgenticER: the next frontier in Entity Resolution
> 原文: [https://arxiv.org/abs/2607.27435](https://arxiv.org/abs/2607.27435)

arXiv:2607.27435v1 Announce Type: new
Abstract: Entity Resolution (ER) is a fundamental problem in data management, playing a critical role in tasks like data cleaning and knowledge graph construction. The existing ER approaches range from traditional rule-based to deep learning techniques and LLM-based methods, but typically operate under a ``passive paradigm'', as duplicates are detected through static, one-shot similarity computations. Such approaches fail to capture the inherently uncertain and context-dependent nature of real-world ER tasks, especially in data lakes with streaming content in heterogeneous formats such as CSV files, JSON files, RDF dumps, and free text. In such settings, resolving ambiguity often requires iterative evidence gathering, reasoning across multiple sources, even selective human involvement. To cover this gap, we advocate a paradigm shift from passive to Agentic ER, which frames ER as a sequential decision-making process that is performed by autonomous agents. These agents actively plan ER strategies, acquire external evidence, decide when to query additional sources or humans, and optimize trade-offs between accuracy, cost, and latency. We formalize Agentic ER as a decision-theoretic problem, we propose a reference architecture, we identify core research challenges, and outline new evaluation dimensions tailored to agentic behavior. By introducing Agentic ER, we aim to establish a new research direction at the intersection of data management and intelligent agents.
