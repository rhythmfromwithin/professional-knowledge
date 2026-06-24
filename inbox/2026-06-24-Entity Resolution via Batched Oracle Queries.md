---
interest: medium
link: https://arxiv.org/abs/2606.24407
next_step: skim
priority: low
slack_ts: '1782274336.718849'
source: cs.DB - Databases
status: unread
title: Entity Resolution via Batched Oracle Queries
---
# Entity Resolution via Batched Oracle Queries
> 原文: [https://arxiv.org/abs/2606.24407](https://arxiv.org/abs/2606.24407)

arXiv:2606.24407v1 Announce Type: new
Abstract: We consider an oracle that processes a limited batch of records at a time and clusters those that refer to the same real-world entity. We study how to interrogate such an oracle to resolve entities in a dataset whose size is far larger than a single batch, and where no batch is guaranteed to contain all records of any given entity. We aim at a pay-as-you-go approach, to have full control over the costs (the number of oracle consults), while achieving the highest possible recall at every step. We formally cast this problem as batched entity resolution, prove that selecting optimal batches is NP-hard, and provide an optimal solution under a natural condition on entity sizes. Finally, we evaluate our approach on six datasets and show its superiority over state-of-the-art baselines.
