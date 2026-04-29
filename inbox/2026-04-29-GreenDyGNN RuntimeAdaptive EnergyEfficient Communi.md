---
interest: medium
link: https://arxiv.org/abs/2604.23139
next_step: skim
priority: medium
slack_ts: '1777434596.205089'
source: cs.DC - Distributed Computing
status: unread
title: 'GreenDyGNN: Runtime-Adaptive Energy-Efficient Communication for Distributed
  GNN Training'
---
# GreenDyGNN: Runtime-Adaptive Energy-Efficient Communication for Distributed GNN Training
> 原文: [https://arxiv.org/abs/2604.23139](https://arxiv.org/abs/2604.23139)

arXiv:2604.23139v1 Announce Type: new
Abstract: Distributed GNN training is dominated by remote feature fetching, which can be very costly. Multi-hop neighborhood sampling crosses partition boundaries and triggers fine-grained RPCs whose fixed initiation cost and GPU-stall latency waste energy. Prior systems try to reduce this overhead with presampling and static caching, but cache policies cannot react to runtime network variation. We show that under time-varying congestion, static caching can increase energy by up to 45% because a fixed rebuild schedule is insufficient. We present GreenDyGNN, which formulates cache window management as a sequential decision problem. GreenDyGNN performs intra-epoch cache rebuilds and uses a Double-DQN agent, trained in a calibrated simulator with domain-randomized congestion, to adapt rebuild window size and per-owner cache allocation at each boundary. An asynchronous double-buffered pipeline makes adaptation effectively free. Under congestion, GreenDyGNN cuts total energy by up to 43% over Default DGL and 4-24% over the best static policy, while closely matching the optimum under clean conditions.
