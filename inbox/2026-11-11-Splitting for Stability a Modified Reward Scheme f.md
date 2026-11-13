---
interest: medium
link: https://arxiv.org/abs/2611.13252
next_step: skim
priority: low
slack_ts: '1794550327.390189'
source: cs.CR - Cryptography and Security
status: unread
title: 'Splitting for Stability: a Modified Reward Scheme for Transaction-Fee-Only
  Regimes'
---
# Splitting for Stability: a Modified Reward Scheme for Transaction-Fee-Only Regimes
> 原文: [https://arxiv.org/abs/2611.13252](https://arxiv.org/abs/2611.13252)

arXiv:2611.13252v1 Announce Type: new
Abstract: As Bitcoin's block subsidy declines over time, miner revenue will come to depend increasingly on transaction fees. In fee-dominated regimes, winner-take-all reward structures can create incentives for undercutting and fork-based mining strategies, leading to instability and reduced transaction throughput.
To prevent this instability, we propose a reward-splitting mechanism in which the winning block producer receives an $\alpha$-portion of the block reward, while the rest is distributed among other miners; this incentivizes mining on previous blocks with higher rewards, while preserving the incentive to produce blocks with high rewards.
We evaluate the proposed reward structure through analysis and simulation. Our analysis derives a local profitability condition for one-step Function-Fork deviations, showing how the winner-side reward, loser-side subsidy, and honest hash power jointly determine whether undercutting is profitable. Simulations show parameter regions in which honest behavior dominates fork-based deviations. In the cases where forking becomes dominant, the learned strategy is the least aggressive variant studied. The analysis and simulations suggest that suitable reward-splitting parameters can reduce the honest participation needed to suppress aggressive forking strategies relative to the winner-take-all structure studied in prior work. Finally, we show that the modified reward scheme does not appear to worsen selfish mining incentives.
Together, these results suggest that reward redistribution can mitigate fee-driven fork incentives without introducing stronger selfish mining incentives, providing a possible direction for incentive design in fee-era proof-of-work systems.
