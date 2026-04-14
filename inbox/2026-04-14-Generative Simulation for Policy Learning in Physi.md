---
title: "Generative Simulation for Policy Learning in Physical Human-Robot Interaction"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.08664
priority: medium
status: unread
interest: medium
next_step: skim
---
# Generative Simulation for Policy Learning in Physical Human-Robot Interaction
> 原文: [https://arxiv.org/abs/2604.08664](https://arxiv.org/abs/2604.08664)

arXiv:2604.08664v1 Announce Type: new
Abstract: Developing autonomous physical human-robot interaction (pHRI) systems is limited by the scarcity of large-scale training data to learn robust robot behaviors for real-world applications. In this paper, we introduce a zero-shot "text2sim2real" generative simulation framework that automatically synthesizes diverse pHRI scenarios from high-level natural-language prompts. Leveraging Large Language Models (LLMs) and Vision-Language Models (VLMs), our pipeline procedurally generates soft-body human models, scene layouts, and robot motion trajectories for assistive tasks. We utilize this framework to autonomously collect large-scale synthetic demonstration datasets and then train vision-based imitation learning policies operating on segmented point clouds. We evaluate our approach through a user study on two physically assistive tasks: scratching and bathing. Our learned policies successfully achieve zero-shot sim-to-real transfer, attaining success rates exceeding 80% and demonstrating resilience to unscripted human motion. Overall, we introduce the first generative simulation pipeline for pHRI applications, automating simulation environment synthesis, data collection, and policy learning. Additional information may be found on our project website: https://rchi-lab.github.io/gen\_phri/
