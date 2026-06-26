---
interest: medium
link: https://arxiv.org/abs/2606.26175
next_step: skim
priority: medium
slack_ts: '1782447552.699449'
source: cs.RO - Robotics
status: unread
title: 'RMTL: Reinforced Micro-task Learning for Long-Horizon Manipulation with VLM
  Rewards'
---
# RMTL: Reinforced Micro-task Learning for Long-Horizon Manipulation with VLM Rewards
> 原文: [https://arxiv.org/abs/2606.26175](https://arxiv.org/abs/2606.26175)

arXiv:2606.26175v1 Announce Type: new
Abstract: Reinforcement learning (RL) for robotic manipulation often requires manually designing a dense reward function, which is difficult to tune and often fragile, or learning a reward from human demonstrations or preferences, which can be expensive. A recent line of work uses pretrained vision-language models (VLMs) as zero-shot reward models, replacing these costs with a single text prompt. However, we argue that a single global prompt is too coarse for long-horizon manipulation tasks with randomized initial conditions. The single-prompt VLM reward is near-flat for much of the trajectory, making early progress hard for the agent to detect. We propose Reinforced Micro-Task Learning (RMTL), an approach that decomposes a manipulation task into a small set of language-described micro-tasks and trains the agent to switch between them. At each step, the agent receives a multi-view VLM reward computed using the prompt of the currently active micro-task and averaged across multiple camera views to reduce the effect of view-specific occlusions. A reverse curriculum gradually exposes the agent to harder initial conditions, while a PPO worker is first trained with a fixed distance-based rule that selects the active micro-task. We then replace this rule with a learned hierarchical manager, turning rule-based phase selection into a fully learned hierarchical policy. We instantiate RMTL on the Fetch manipulation environment using three short stage-specific prompts and without additional prompt tuning. Experiments show that RMTL provides more informative reward signals than single-prompt VLM rewards, enabling faster learning. These results suggest that decomposing VLM rewards into micro-task-specific language prompts can substantially improve the scalability of language-guided reinforcement learning for robotic manipulation.
