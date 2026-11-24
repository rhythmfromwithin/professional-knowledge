---
interest: medium
link: https://arxiv.org/abs/2611.26731
next_step: skim
priority: high
slack_ts: '1795512702.663419'
source: cs.LG - Machine Learning
status: unread
title: Cross-Attack Robust Aggregation for Federated Learning
---
# Cross-Attack Robust Aggregation for Federated Learning
> 原文: [https://arxiv.org/abs/2611.26731](https://arxiv.org/abs/2611.26731)

arXiv:2611.26731v1 Announce Type: new
Abstract: Federated learning (FL) lets resource-constrained IoT and edge devices train a shared model without exchanging raw data, but compromised or faulty devices can poison the global model. Existing robust aggregators each fail in some regime: naive averaging (FedAvg) collapses under high-magnitude attacks, whereas distance- and statistics-based defenses (Krum, median, trimmed mean) sacrifice accuracy on non-IID data and remain vulnerable to stealthy attacks. We present FedTether, which reweights client updates by their deviation from a coordinatewise median through a robust, dead-zoned score applied as a server-side optimizer step. Across three datasets, three attack types, and Byzantine fractions up to 40%, FedTether is the only method top-tier in every regime: it matches FedAvg under stealthy attacks with no robustness tax, exceeds robust baselines by up to 42 accuracy points, and stays accurate where high-magnitude attacks reduce FedAvg to near-random. These properties persist at 50 clients under partial participation, with no shared data or validation set.
