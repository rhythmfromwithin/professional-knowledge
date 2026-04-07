---
title: "Reinforcement Learning from Human Feedback: A Statistical Perspective"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2604.02507
priority: medium
status: unread
interest: medium
next_step: skim
---
# Reinforcement Learning from Human Feedback: A Statistical Perspective
> 原文: [https://arxiv.org/abs/2604.02507](https://arxiv.org/abs/2604.02507)

arXiv:2604.02507v1 Announce Type: new
Abstract: Reinforcement learning from human feedback (RLHF) has emerged as a central framework for aligning large language models (LLMs) with human preferences. Despite its practical success, RLHF raises fundamental statistical questions because it relies on noisy, subjective, and often heterogeneous feedback to learn reward models and optimize policies. This survey provides a statistical perspective on RLHF, focusing primarily on the LLM alignment setting. We introduce the main components of RLHF, including supervised fine-tuning, reward modeling, and policy optimization, and relate them to familiar statistical ideas such as Bradley-Terry-Luce (BTL) model, latent utility estimation, active learning, experimental design, and uncertainty quantification. We review methods for learning reward functions from pairwise preference data and for optimizing policies through both two-stage RLHF pipelines and emerging one-stage approaches such as direct preference optimization. We further discuss recent extensions including reinforcement learning from AI feedback, inference-time algorithms, and reinforcement learning from verifiable rewards, as well as benchmark datasets, evaluation protocols, and open-source frameworks that support RLHF research. We conclude by highlighting open challenges in RLHF. An accompanying GitHub demo https://github.com/Pangpang-Liu/RLHF\_demo illustrates key components of the RLHF pipeline.
