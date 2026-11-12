---
interest: medium
link: https://arxiv.org/abs/2611.13342
next_step: skim
priority: low
slack_ts: '1794466368.798889'
source: cs.CR - Cryptography and Security
status: unread
title: Early Rug Pull Detection on Solana
---
# Early Rug Pull Detection on Solana
> 原文: [https://arxiv.org/abs/2611.13342](https://arxiv.org/abs/2611.13342)

arXiv:2611.13342v1 Announce Type: new
Abstract: Web3 platforms that help users discover and trade newly launched crypto tokens, including launchpads, decentralized-exchange (DEX) interfaces, wallets, and token-analytics sites, must assess tokens before their legitimacy is clear. On Solana, where token creation is inexpensive and tokens use standard programs rather than custom per-token smart contracts, rug pulls can unfold within minutes. Effective warnings must therefore rely on limited histories. Although graph neural networks (GNNs) have improved rug-pull detection on EVM chains, it remains unclear whether transfer structure adds predictive value over non-graph models at minute-scale decision points, and how that value changes as history accumulates. We study 2,700 tokens sampled from SolRPDS, collecting one-minute market histories from Birdeye and token transfers from Solana RPC. We define a rug pull operationally by requiring a liquidity drain, price collapse, and persistent liquidity depletion over a nominal 24-hour period after token creation. All features use only information available at or before each prediction cutoff. We evaluate observation windows of 12.5, 35.5, and 93 minutes, selected in advance from the published lifespan distribution of Solana rug pulls, and represent each token as a temporal transfer graph. Within the first 12.5 minutes, rug-pull and non-rug graphs already differ in size, density, reciprocity, and receiver-side centralization. We compare GNNs against matched non-graph models using the same token-level and graph-summary features on identical samples. A fixed panel of tokens observed in all three windows further isolates the effect of longer observation from changes in token population. Our findings inform the design of early-warning mechanisms for newly launched Solana tokens in Web3 interfaces.
