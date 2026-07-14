---
interest: medium
link: https://arxiv.org/abs/2607.08801
next_step: skim
priority: low
slack_ts: '1783998903.308989'
source: cs.CR - Cryptography and Security
status: unread
title: A Seed for Privacy -- semi-automatic privacy-revealing data reminder in databases
  and data streams
---
# A Seed for Privacy -- semi-automatic privacy-revealing data reminder in databases and data streams
> 原文: [https://arxiv.org/abs/2607.08801](https://arxiv.org/abs/2607.08801)

arXiv:2607.08801v1 Announce Type: new
Abstract: Sharing databases and data streams imposes the danger of revealing private information in the form of complex events which can comprise individual data elements and their combinations. Identifying these privacy-revealing complex events is crucial for preserving privacy while maintaining data utility. However, data producers often lack the expertise to comprehensively identify these events, which undermines many state-of-the-art privacy-preserving mechanisms that rely on accurate event labeling. To address this challenge, we developed pArborist - a tool that can semi-automatically create a set of queries to identify and label privacy-revealing complex events in both static datasets and dynamic data streams, guided by the privacy requirements of the data producer. pArborist uses the schema of the database or data stream combined with initial input from the data producer, i.e., seed queries. From each seed query, pArborist grows a tree containing all possible syntactically correct queries, constrained by an upper limit on computational resources. Following this growing phase, the tree is refined by eliminating queries that lack correlation to the seed or are conditionally independent of the seed. Our evaluation indicates that pArborist achieves overall recall of 90% and precision of 93% in finding privacy-revealing queries, and this significantly surpasses the state-of-the-art approach FQID. In data stream processing experiments, pArborist introduces a delay of approximately 1.3 ms following an average warm-up period of 920 ms. The experiments also show that pArborist can automatically detect privacy-revealing complex events according to GDPR.
