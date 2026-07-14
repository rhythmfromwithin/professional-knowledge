---
interest: medium
link: https://arxiv.org/abs/2607.09149
next_step: skim
priority: low
slack_ts: '1783998922.167259'
source: cs.DB - Databases
status: unread
title: 'Taxonomy Maintenance In The Wild Over Evolving Scholarly Data: Reliability,
  Efficiency, and Cost-Effectiveness'
---
# Taxonomy Maintenance In The Wild Over Evolving Scholarly Data: Reliability, Efficiency, and Cost-Effectiveness
> 原文: [https://arxiv.org/abs/2607.09149](https://arxiv.org/abs/2607.09149)

arXiv:2607.09149v1 Announce Type: new
Abstract: The rapid growth of scientific publications makes scholarly taxonomies quickly obsolete. We study taxonomy maintenance in the wild, a new problem that moves beyond static construction by continuously adapting taxonomies to evolving scholarly repositories, such as arXiv, for a given research topic. We propose GIST, a robust framework for maintaining evolving taxonomies. Unlike purely LLM-centric approaches, GIST grounds structure induction in expert-curated evidence by extracting partial hierarchies from the "Related Work" sections of papers. It integrates these partial taxonomies into a unified global taxonomy in a geometric box-embedding space, where box containment encodes the inductive bias of is-a relations. To connect semantics with geometric structure, GIST learns a bidirectional mapping between word embeddings and box embeddings. For efficient incremental updates, GIST uses novelty-aware coreset selection to update the model with representative historical signals and new evidence, avoiding costly full retraining. To handle high-velocity paper streams under user-specific token budgets, GIST further combines a hypothesized concept generator with a cost-effective evidence retrieval module. Experiments on real-world arXiv datasets show that GIST outperforms state-of-the-art baselines, improving Node F1 and Edge F1 by 11.0% and 13.1% over the strongest baseline while requiring only 9.6% of its runtime and 12.7% of its monetary cost.
