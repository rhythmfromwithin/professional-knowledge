---
interest: medium
link: https://arxiv.org/abs/2604.06189
next_step: skim
priority: high
slack_ts: '1775964763.624689'
source: cs.AI - Artificial Intelligence
status: unread
title: High-Precision Estimation of the State-Space Complexity of Shogi via the Monte
  Carlo Method
---
# High-Precision Estimation of the State-Space Complexity of Shogi via the Monte Carlo Method
> 原文: [https://arxiv.org/abs/2604.06189](https://arxiv.org/abs/2604.06189)

arXiv:2604.06189v1 Announce Type: new
Abstract: Determining the state-space complexity of the game of Shogi (Japanese Chess) has been a challenging problem, with previous combinatorial estimates leaving a gap of five orders of magnitude ($10^{64}$ to $10^{69}$). This large gap arises from the difficulty of distinguishing Shogi positions legally reachable from the initial position among the vast number of valid board configurations. In this paper, we present a high-precision statistical estimation of the number of reachable positions in Shogi. Our method combines Monte Carlo sampling with a novel reachability test that utilizes a reverse search toward a set of "King-King only" (KK) positions, rather than a single-target backward search to the single initial position. This approach significantly reduces the search effort for determining unreachability. Based on a sample of 5 billion positions, we estimated the number of legal positions in Shogi to be $6.55 \times 10^{68}$ (to three significant digits) with a $3\sigma$ confidence level, substantially improving upon previously known bounds. We also applied this method to Mini Shogi, determining its complexity to be approximately $2.38 \times 10^{18}$.
