---
interest: medium
link: https://arxiv.org/abs/2606.06830
next_step: skim
priority: medium
slack_ts: '1780894167.828239'
source: cs.CY - Computers and Society
status: unread
title: Learning Fair Demand Models
---
# Learning Fair Demand Models
> 原文: [https://arxiv.org/abs/2606.06830](https://arxiv.org/abs/2606.06830)

arXiv:2606.06830v1 Announce Type: new
Abstract: Data-driven pricing is increasingly prevalent in sectors such as airlines, lending, insurance, and retail. By learning demand models from customer features and setting prices accordingly, these systems may generate discriminatory outcomes that raise fairness concerns. This leads to fundamental questions - how and where should systems incorporate fairness considerations in the pricing pipeline, and how does it ultimately affect societal outcomes? To answer these, we study a stylized model where a seller has a two-stage decision pipeline comprising linear demand model estimation followed by price optimization. The seller considers fairness notions in training loss, price, and demand, under both parity-wise and Rawlsian perspectives.
We show that equalizing training loss across consumer groups leads to multiple solutions, which in turn can result in undesirable outcomes despite being a standard approach in fair machine learning. Focusing instead on fairness applied directly to prices or demand, we compare two strategies that enforce fairness in either the demand estimation stage or the price optimization stage. For parity-wise fairness, we characterize when each strategy yields higher social welfare under small fairness levels. We show that when market sizes and prices in the dataset are similar, imposing price fairness in the estimation stage is more beneficial to consumers, whereas imposing demand fairness in the optimization stage yields better consumer outcomes. For Rawlsian fairness, the two strategies coincide exactly. Lastly, we extend our model to alternate demand functions and conduct a case study using real-world vaccine pricing data.
