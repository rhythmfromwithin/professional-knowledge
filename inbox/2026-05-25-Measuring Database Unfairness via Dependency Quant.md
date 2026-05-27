---
interest: medium
link: https://arxiv.org/abs/2605.22952
next_step: skim
priority: low
slack_ts: '1779856023.895549'
source: cs.DB - Databases
status: unread
title: Measuring Database Unfairness via Dependency Quantification Under Differential
  Privacy
---
# Measuring Database Unfairness via Dependency Quantification Under Differential Privacy
> 原文: [https://arxiv.org/abs/2605.22952](https://arxiv.org/abs/2605.22952)

arXiv:2605.22952v1 Announce Type: new
Abstract: Differential privacy (DP) has become the de facto standard for protecting sensitive data, providing strong guarantees that published statistics or models reveal limited information about any individual. However, privacy noise and restricted data access make it increasingly difficult to assess the fairness and reliability of private datasets. In this paper, we propose a formal framework for quantifying data unfairness under DP. We identify three core desiderata for unfairness measures based on previous work: positivity, monotonicity, and DP computability. We further instantiate them through three complementary measures: (1) a mutual information-based measure with a total variation distance proxy suitable for DP, (2) a data repair-based measure approximated via a reduction to weighted MaxSAT, and (3) a top-$k$ tuple contribution measure that isolates the most influential records in fairness violations. We design privacy-preserving algorithms and analyze their sensitivity, accuracy, and efficiency. Extensive experiments on multiple real-world datasets demonstrate that our proposed measures faithfully approximate their non-private counterparts, effectively quantify bias under privacy constraints, and provide insights for data management.
