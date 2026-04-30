---
interest: medium
link: https://arxiv.org/abs/2604.23266
next_step: skim
priority: medium
slack_ts: '1777521054.115849'
source: cs.DC - Distributed Computing
status: unread
title: 'The Blockchain Execution Dilemma: Optimizing Revenue XOR Fair Ordering'
---
# The Blockchain Execution Dilemma: Optimizing Revenue XOR Fair Ordering
> 原文: [https://arxiv.org/abs/2604.23266](https://arxiv.org/abs/2604.23266)

arXiv:2604.23266v1 Announce Type: new
Abstract: The successive generations of consensus algorithms have progressively shifted the performance bottleneck of blockchains to the execution layer. While recent works address this by parallelizing transaction execution, they often overlook the critical role of transaction sequencing. Historically, transaction ordering was left to validator discretion, a practice prone to Maximal Extractable Value (MEV) attacks, or rigid fair-ordering protocols that limit validator revenue. In this work, we address the tension between validator revenue and order fairness using a dynamic optimization framework. We introduce a blockchain-independent model for transaction sequencing in a continuous setting where block executions can overlap. Within this framework, we propose an anytime genetic algorithm that utilizes gas prices, object sets, and predicted execution times to optimize schedules. We evaluate our approach with real-world datasets from Sui and Ethereum, and demonstrate that our algorithm increases validator profit by approximately 15% and accelerates congestion relief by up to 58%. Furthermore, we quantify the impact of fair-ordering constraints, showing they can reduce validator revenue by 50% to 60% during periods of high congestion. We provide the first evidence that enforcing strict fair ordering effectively nullifies the advantages of advanced sequencing.
