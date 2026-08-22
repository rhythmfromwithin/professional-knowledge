---
interest: medium
link: https://arxiv.org/abs/2608.17027
next_step: skim
priority: medium
slack_ts: '1787362727.457299'
source: cs.RO - Robotics
status: unread
title: 'FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated
  Experiences'
---
# FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences
> 原文: [https://arxiv.org/abs/2608.17027](https://arxiv.org/abs/2608.17027)

arXiv:2608.17027v1 Announce Type: new
Abstract: Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior to the real world, as is commonly done in locomotion, sidesteps this struggle, so we replicate that recipe for loco-manipulation. In doing so, we find that cloning synthetic demonstrations results in a low performance ceiling no matter the amount of training data. Reinforcement learning breaks through it, and refining the cloned policy with Flow-GRPO on a single sparse reward yields performance that synthetic behavior cloning cannot match. Together, these stages form our end-to-end sim-to-real pipeline spanning more than 150,000 scenes, which we use to train FetchMan. We evaluate it on FetchMan-Bench, a simulation benchmark we release, and deploy it zero-shot on a real Unitree G1, where our single-object reach-and-pick policy walks to and grasps a target across unseen scenes at 73.3% success. Finally, we extend this recipe to multi-object training, a first step toward loco-manipulation generalist policies at this data scale.
