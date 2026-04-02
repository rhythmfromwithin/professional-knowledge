---
interest: medium
link: https://arxiv.org/abs/2603.26765
next_step: skim
priority: high
slack_ts: '1775098521.174719'
source: cs.AI - Artificial Intelligence
status: unread
title: Bitboard version of Tetris AI
---
# Bitboard version of Tetris AI
> 原文: [https://arxiv.org/abs/2603.26765](https://arxiv.org/abs/2603.26765)

arXiv:2603.26765v1 Announce Type: new
Abstract: The efficiency of game engines and policy optimization algorithms is crucial for training reinforcement learning (RL) agents in complex sequential decision-making tasks, such as Tetris. Existing Tetris implementations suffer from low simulation speeds, suboptimal state evaluation, and inefficient training paradigms, limiting their utility for large-scale RL research. To address these limitations, this paper proposes a high-performance Tetris AI framework based on bitboard optimization and improved RL algorithms. First, we redesign the Tetris game board and tetrominoes using bitboard representations, leveraging bitwise operations to accelerate core processes (e.g., collision detection, line clearing, and Dellacherie-Thiery Features extraction) and achieve a 53-fold speedup compared to OpenAI Gym-Tetris. Second, we introduce an afterstate-evaluating actor network that simplifies state value estimation by leveraging Tetris afterstate property, outperforming traditional action-value networks with fewer parameters. Third, we propose a buffer-optimized Proximal Policy Optimization (PPO) algorithm that balances sampling and update efficiency, achieving an average score of 3,829 on 10x10 grids within 3 minutes. Additionally, we develop a Python-Java interface compliant with the OpenAI Gym standard, enabling seamless integration with modern RL frameworks. Experimental results demonstrate that our framework enhances Tetris's utility as an RL benchmark by bridging low-level bitboard optimizations with high-level AI strategies, providing a sample-efficient and computationally lightweight solution for scalable sequential decision-making research.
