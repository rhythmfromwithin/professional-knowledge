---
interest: medium
link: https://arxiv.org/abs/2610.40828
next_step: skim
priority: medium
slack_ts: '1793686638.377689'
source: cs.RO - Robotics
status: unread
title: 'From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills
  and Offline Proxies for Dexterous Manipulation'
---
# From Teleoperation to Long-Horizon Dexterity: Evaluating Visuomotor Skills and Offline Proxies for Dexterous Manipulation
> 原文: [https://arxiv.org/abs/2610.40828](https://arxiv.org/abs/2610.40828)

arXiv:2610.40828v1 Announce Type: new
Abstract: Imitation learning policies are intended to make robotic manipulation robust to variations in object pose, appearance, and environment that challenge pre-programmed motion. However, real-world performance remains difficult to predict, as conventional optimization signals such as validation loss show no consistent relationship with robot success. To identify the design choices that govern real-world performance, 281 imitation-learning policies spanning seven policy families were evaluated in approximately 1,700 real-robot trials of RJ45 connector grasping and insertion using a five-fingered robotic hand. Controlled ablations showed that observation and action representations dominated conventional optimizer and sampling choices. For point-cloud policies, region-of-interest cropping, representation in the robot-base frame, and normalization within the point encoder each improved success by 70-100 percentage points. For the vision-language-action policy, absolute rather than relative action prediction improved insertion success by up to 70 percentage points. Skill decomposition, multi-view perception, and recovery demonstrations were associated with the strongest-performing systems, although their effects were not independently isolated. Of 67 offline metrics evaluated, only five measures of predicted-motion smoothness and directness reliably correlated with insertion success (r = -0.70 to -0.80), and only within a single policy family. These results identify representation choices as key determinants of real-world imitation-learning performance and show that offline metrics can shortlist policies, but cannot replace real-robot evaluation.
