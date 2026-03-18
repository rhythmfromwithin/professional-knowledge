---
interest: medium
link: https://arxiv.org/abs/2603.13390
next_step: skim
priority: low
slack_ts: '1773802312.496619'
source: cs.DB - Databases
status: unread
title: 'MCI-SQL: Text-to-SQL with Metadata-Complete Context and Intermediate Correction'
---
# MCI-SQL: Text-to-SQL with Metadata-Complete Context and Intermediate Correction
> 原文: [https://arxiv.org/abs/2603.13390](https://arxiv.org/abs/2603.13390)

arXiv:2603.13390v1 Announce Type: new
Abstract: Text-to-SQL aims to translate natural language queries into SQL statements. Existing methods typically follow a pipeline of pre-processing, schema linking, candidate SQL generation, SQL alignment, and target SQL selection. However, these methods face significant challenges. First, they often struggle with column filtering during schema linking due to difficulties in comprehending raw metadata. Also, the candidate SQL generation process often suffers from reasoning errors, which limits accuracy improvements. To address these limitations, we propose a framework, called MCI-SQL, to efficiently and precisely generate SQL queries. Specifically, we assign metadata-complete contexts to each column, which significantly improves the accuracy of column filtering for schema linking. Also, for candidate SQL generation, we propose an intermediate correction mechanism that validates SQL queries and revises errors in a timely way. Moreover, we also propose effective optimizations in subsequent SQL alignment and selection phases, which further enhance the performance. Experiments on the widely-used BIRD benchmark show that MCI-SQL achieves execution accuracy of 74.45% on the development set and 76.41% on the test set, surpassing current published state-of-the-art results. In addition, we manually identify and correct 412 samples in the BIRD dataset, forming a new version named BIRD-clear, which is released together with our code on GitHub. We also evaluate our methods on BIRD-clear and find that MCI-SQL outperforms baselines by 8.47 percentage points in execution accuracy, further demonstrating the effectiveness and reliability of our framework.
