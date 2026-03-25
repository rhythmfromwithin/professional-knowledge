---
title: "Fusing Driver Perceived and Physical Risk for Safety Critical Scenario Screening in Autonomous Driving"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.20232
priority: medium
status: unread
interest: medium
next_step: skim
---
# Fusing Driver Perceived and Physical Risk for Safety Critical Scenario Screening in Autonomous Driving
> 原文: [https://arxiv.org/abs/2603.20232](https://arxiv.org/abs/2603.20232)

arXiv:2603.20232v1 Announce Type: new
Abstract: Autonomous driving testing increasingly relies on mining safety critical scenarios from large scale naturalistic driving data, yet existing screening pipelines still depend on manual risk annotation and expensive frame by frame risk evaluation, resulting in low efficiency and weakly grounded risk quantification. To address this issue, we propose a driver risk fusion based hazardous scenario screening method for autonomous driving. During training, the method combines an improved Driver Risk Field with a dynamic cost model to generate high quality risk supervision signals, while during inference it directly predicts scenario level risk scores through fast forward passes, avoiding per frame risk computation and enabling efficient large scale ranking and retrieval. The improved Driver Risk Field introduces a new risk height function and a speed adaptive look ahead mechanism, and the dynamic cost model integrates kinetic energy, oriented bounding box constraints, and Gaussian kernel diffusion smoothing for more accurate interaction modeling. We further design a risk trajectory cross attention decoder to jointly decode risk and trajectories. Experiments on the INTERACTION and FLUID datasets show that the proposed method produces smoother and more discriminative risk estimates. On FLUID, it achieves an AUC of 0.792 and an AP of 0.825, outperforming PODAR by 9.1 percent and 5.1 percent, respectively, demonstrating its effectiveness for scalable risk labeling and hazardous scenario screening.
