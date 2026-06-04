---
interest: medium
link: https://arxiv.org/abs/2606.00774
next_step: skim
priority: low
slack_ts: '1780548658.154929'
source: cs.DB - Databases
status: unread
title: 'SCOPE: Cost-Efficient Model Selection for Compound AI Systems under Quality
  Constraints'
---
# SCOPE: Cost-Efficient Model Selection for Compound AI Systems under Quality Constraints
> 原文: [https://arxiv.org/abs/2606.00774](https://arxiv.org/abs/2606.00774)

arXiv:2606.00774v1 Announce Type: new
Abstract: A compound AI system consists of multiple LLM modules, together handling complex and multi-step tasks that exceed the capabilities of a single model. Existing systems often use a single expensive LLM across all modules to improve the result quality of the whole system. However, this configuration incurs prohibitive costs, particularly for data management and analytics tasks at scale, such as data manipulation. To this end, we formalize the problem of constrained LLM selection for compound AI systems, leveraging the diverse pricing and capabilities of different LLMs to achieve competitive quality at lower cost. Given a query dataset and a user-specified quality threshold, we aim to select an LLM for each module to minimize the system's average cost while ensuring that overall quality meets the required threshold. To solve this problem, we propose SCOPE, a cost-efficient optimization algorithm. Unlike existing approaches that rely on expensive dataset-level evaluations, SCOPE exploits per-query results to rapidly estimate the system's cost and quality, and constructs confidence bounds to guide the search for promising LLM combinations. Furthermore, SCOPE provides theoretical guarantees for meeting the quality threshold and achieving near-optimal average cost. We evaluate SCOPE against 7 baselines on three data processing tasks, demonstrating that it outperforms all baselines. Under the same search budget and quality constraint, it finds solutions with up to $20\times$ lower cost than the best competitor during the search and achieves up to $6\times$ lower final cost in the returned solution.
