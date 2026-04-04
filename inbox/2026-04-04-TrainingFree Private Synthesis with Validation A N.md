---
interest: medium
link: https://arxiv.org/abs/2604.01821
next_step: skim
priority: medium
slack_ts: '1775270938.325969'
source: cs.CY - Computers and Society
status: unread
title: 'Training-Free Private Synthesis with Validation: A New Frontier for Practical
  Educational Data Sharing'
---
# Training-Free Private Synthesis with Validation: A New Frontier for Practical Educational Data Sharing
> 原文: [https://arxiv.org/abs/2604.01821](https://arxiv.org/abs/2604.01821)

arXiv:2604.01821v1 Announce Type: new
Abstract: While secondary use of real-world data (RWD) in education offers substantial research opportunities, data sharing is often limited by privacy constraints. Differentially private synthetic data generation (DP-SDG) has emerged as a possible solution. However, educational RWD is fragmented across platforms and institutions and stored in different formats, so DP-SDG must be tailored to each dataset, requiring substantial engineering effort. In addition, such data are often small-sample and high-dimensional, making deep learning (DL)-based methods common but difficult to implement without specialist expertise. In this setting, it is also hard to achieve practically useful downstream utility. As a result, despite its theoretical promise, DP-SDG remains far from a practical solution in education. To address this issue, we propose a more practical two-stage method: (1) training-free, LLM-based DP-SDG is performed for sharing synthetic data and (2) on-demand real-data validation, where researchers submit code for remote validation of results. This simple method is designed for individual data custodians without extensive DP-SDG expertise. It can also be adapted to multi-shot synthesis, where data from different learner cohorts are synthesised regularly. We evaluate this method experimentally in both the one-shot and multi-shot synthesis settings using RWD collected over three years and conduct a case study with real researchers. Results show that LLM-based DP-SDG performs comparably to a DL-based baseline while greatly reducing engineering costs, and that non-DP validation causes measurable but moderate privacy leakage. Nonetheless, in the case study researchers reported that on average only 36% of synthetic findings are validated on real data. Overall, the paper provides a practical method for sharing educational RWD, while highlighting challenges in risk mitigation and epistemic precision.
