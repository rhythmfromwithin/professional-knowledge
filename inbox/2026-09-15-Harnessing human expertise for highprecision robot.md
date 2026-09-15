---
interest: medium
link: https://arxiv.org/abs/2609.13234
next_step: skim
priority: medium
slack_ts: '1789446773.728149'
source: cs.RO - Robotics
status: unread
title: 'Harnessing human expertise for high-precision robotic assembly in industrialized
  construction: A sample-efficient installer-in-the-loop interactive reinforcement
  learning framework'
---
# Harnessing human expertise for high-precision robotic assembly in industrialized construction: A sample-efficient installer-in-the-loop interactive reinforcement learning framework
> 原文: [https://arxiv.org/abs/2609.13234](https://arxiv.org/abs/2609.13234)

arXiv:2609.13234v1 Announce Type: new
Abstract: Industrialized construction imposes stringent precision requirements on robotic assembly of modular components such as prefabricated window units. In tolerance-critical operations, the central bottleneck is not only mechanical clearance but also converting tacit installer expertise into data-efficient autonomy under sparse acceptance feedback, contact variability, and millimeter-scale constraints. We present an installer-in-the-loop interactive reinforcement learning framework that acquires expertise through offline teleoperated demonstrations, sparse event-driven binary takeovers at contact-failure boundaries, and acceptance-aligned terminal rewards, logged under a unified schema for traceable offline-to-online adaptation. A temporally abstract action-sequence policy built on Q-chunking with Flow Q-Learning captures multimodal recovery maneuvers under sparse terminal rewards, while a non-updating warm-start phase stabilizes the offline-to-online transition. The framework is evaluated in MuJoCo across the workflow from suction acquisition through clearance-limited seating, under structured staging and end-to-end randomized placement. Within a defined stress-test regime with 2 mm per-side clearance, bounded pose perturbations, and friction randomization, the pipeline attains 100\% autonomous seating with 12--15 min of cumulative installer supervision over 3.0 h of online training, and reaches the 95\% success milestone in approximately 0.5 h and 1.5 h in the two experiments. We also report wall-clock adaptation time, cumulative takeover minutes, intervention-rate decay, and stage-wise failure attribution to inform supervision budgeting. Ablations isolate the complementary contributions of temporal abstraction, installer intervention, and warm-start value calibration.
