---
title: "Pricing Cross-Bank Context in Federated Anti-Money Laundering"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2610.35996
priority: low
status: unread
interest: medium
next_step: skim
---
# Pricing Cross-Bank Context in Federated Anti-Money Laundering
> 原文: [https://arxiv.org/abs/2610.35996](https://arxiv.org/abs/2610.35996)

arXiv:2610.35996v1 Announce Type: new
Abstract: Most graph-based Anti-Money Laundering (AML) methods assume access to a pooled transaction graph containing all accounts and payments, which in reality does not exist. Federated learning offers the necessary privacy guarantees but it remains unclear how money laundering patterns spanning separate graphs can effectively be detected. We exploit transactions already recorded by both endpoint banks to approximate remote account states locally, enabling multi-layer Graph Neural Network (GNN) computation without additional account-specific exchange. Starting from this baseline, we test whether the remaining context is worth sharing, using a disclosure ladder that adds two transaction counts per remote account or the counterparty's own GNN states. On AMLworld HI-Small, across six GNN backbones and up to 32 silos, the observable baseline yields the largest gain and keeps it as fragmentation shrinks the visible slice; counts add a robust correction, while exact remote states help only in specific regimes. In controlled privacy--utility studies, the noise needed to protect shared states erases their detection value before it buys meaningful privacy, whereas counts stay useful even under strong privacy protection. These findings support a practical rule for banks: use what they already record, and formally protect the little that must move.
