---
interest: medium
link: https://arxiv.org/abs/2605.11151
next_step: skim
priority: high
slack_ts: '1778731264.291669'
source: cs.AI - Artificial Intelligence
status: unread
title: 'RankQ: Offline-to-Online Reinforcement Learning via Self-Supervised Action
  Ranking'
---
# RankQ: Offline-to-Online Reinforcement Learning via Self-Supervised Action Ranking
> 原文: [https://arxiv.org/abs/2605.11151](https://arxiv.org/abs/2605.11151)

arXiv:2605.11151v1 Announce Type: new
Abstract: Offline-to-online reinforcement learning (RL) improves sample efficiency by leveraging pre-collected datasets prior to online interaction. A key challenge, however, is learning an accurate critic in large state--action spaces with limited dataset coverage. To mitigate harmful updates from value overestimation, prior methods impose pessimism by down-weighting out-of-distribution (OOD) actions relative to dataset actions. While effective, this essentially acts as a behavior cloning anchor and can hinder downstream online policy improvement when dataset actions are suboptimal. We propose RankQ, an offline-to-online Q-learning objective that augments temporal-difference learning with a self-supervised multi-term ranking loss to enforce structured action ordering. By learning relative action preferences rather than uniformly penalizing unseen actions, RankQ shapes the Q-function such that action gradients are directed toward higher-quality behaviors. Across sparse reward D4RL benchmarks, RankQ achieves performance competitive with or superior to seven prior methods. In vision-based robot learning, RankQ enables effective offline-to-online fine-tuning of a pretrained vision-language-action (VLA) model in a low-data regime, achieving on average a 42.7% higher simulation success rate than the next best method. In a high-data setting, RankQ improves simulation performance by 13.7% over the next best method and achieves strong sim-to-real transfer, increasing real-world cube stacking success from 43.1% to 84.7% relative to the VLA's initial performance.
