---
interest: medium
link: https://arxiv.org/abs/2609.13170
next_step: skim
priority: medium
slack_ts: '1789446771.405619'
source: cs.DC - Distributed Computing
status: unread
title: A Lifecycle Cost Analysis of Smart-Contract-Coordinated Federated Learning
  Marketplaces
---
# A Lifecycle Cost Analysis of Smart-Contract-Coordinated Federated Learning Marketplaces
> 原文: [https://arxiv.org/abs/2609.13170](https://arxiv.org/abs/2609.13170)

arXiv:2609.13170v1 Announce Type: new
Abstract: Blockchain-enabled Federated Learning (FL) marketplaces enable collaborative model training among mutually distrustful participants through smart contracts. Although numerous architectures exist, their economic evaluation is typically limited to isolated blockchain operations rather than the complete marketplace lifecycle. Consequently, it remains unclear whether operational costs depend on operating at scale. This paper presents an experimental study of the operational cost of a DAO-governed marketplace. Our evaluation decomposes the gas consumption of every blockchain operation throughout the contract lifecycle, performs ablation experiments to isolate the impact of on-chain coordination and IPFS storage on federated training, and derives an analytical model describing the amortization of deployment costs. Results show the lifecycle of a single training task consumes approximately 3.8 million gas units per hired trainer. The average cost per training round reaches its amortization knee - defined as twice the asymptotic recurring cost - after approximately 20 communication rounds. Moreover, integrating smart contracts and IPFS preserves model performance, achieving accuracy comparable to conventional FL deployments. These findings demonstrate that smart-contract-coordinated FL marketplaces exhibit an amortizing cost structure not because on-chain operations are inexpensive, but because recurring costs are one to two orders of magnitude smaller than fixed deployment costs, thereby diluting over the federation's lifetime.
