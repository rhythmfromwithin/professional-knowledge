---
title: "EgoSteer: A Full-Stack System Towards Steerable Dexterous Manipulation from Egocentric Videos"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.09701
priority: medium
status: unread
interest: medium
next_step: skim
---
# EgoSteer: A Full-Stack System Towards Steerable Dexterous Manipulation from Egocentric Videos
> 原文: [https://arxiv.org/abs/2607.09701](https://arxiv.org/abs/2607.09701)

arXiv:2607.09701v1 Announce Type: new
Abstract: Steerability is a defining capability of generalist robot policies, yet remains largely absent in dexterous-hand systems for lack of large-scale, language-aligned, and action-accurate demonstration data. To address this bottleneck, we present a full-stack system that scales dexterous VLA pre-training from egocentric human videos and enables data-efficient real-robot post-training. It integrates EgoSmith, a data pipeline that curates in-the-wild egocentric videos into 9.6K hours of high-quality pre-training data with 9x higher throughput and better accuracy than prior SOTA; a unified robot stack for teleoperation and human-in-the-loop correction; and EgoSteer, a world-model-enhanced VLA trained on optimized infrastructure. Human-data pre-training equips EgoSteer with language-guided manipulation priors, which are grounded through robot post-training and improved by DAgger refinement. Empirically, EgoSteer robustly executes free-form instructions across 40+ diverse tasks, demonstrating failure recovery, dexterity, and generalization. The pre-trained model also few-shot adapts to complex long-horizon tasks, including box folding, on two embodiments with 75+% success. We open-source the system, data, and model at https://egosteer.github.io/.
