---
interest: medium
link: https://arxiv.org/abs/2608.02653
next_step: skim
priority: medium
slack_ts: '1786154693.443349'
source: cs.RO - Robotics
status: unread
title: 'Light-Loco-Parkour: Versatile Perceptive Whole-Body Locomotion via Multi-Skill
  Distillation'
---
# Light-Loco-Parkour: Versatile Perceptive Whole-Body Locomotion via Multi-Skill Distillation
> 原文: [https://arxiv.org/abs/2608.02653](https://arxiv.org/abs/2608.02653)

arXiv:2608.02653v1 Announce Type: new
Abstract: Existing humanoid whole-body control systems still fall short of the way humans move through cluttered terrain: they either track expressive whole-body references without terrain generalization, or react to terrain online while leaving the arms, torso, and knees largely unused. We present \texttt{Light-Loco-Parkour} (LLP), an end-to-end perceptive whole-body locomotion system that closes this gap with a single deployable policy. Conditioned only on onboard depth and a velocity command, the policy decides when to walk, balance, climb, step down, or vault, with no reference input, skill label, hand-coded gate, or runtime motion graph. Compared with prior humanoid systems, LLP makes three contributions. First, it introduces a whole-body perceptive-control pipeline that extends an RL-trained, velocity-tracking locomotion policy with parkour skills learned from object-interacting motions, so the same policy tracks velocity in open terrain, executes whole-body traversal at obstacles, and resumes locomotion afterward. Second, it acquires terrain-conditioned skills from sparse seeds by expanding a single motion into dynamically feasible, terrain-paired references across obstacle geometry, rather than relying on a large motion corpus. Third, it learns autonomous skill transitions from reward, letting the policy decide when and which whole-body skill to invoke from depth and command alone, with no one-hot skill label, hand-coded state machine, or runtime motion generator. Simulation and real-world experiments show high success across both benchmarked terrains and unseen obstacle variations, and the same policy transfers zero-shot to indoor and outdoor hardware experiments. These results demonstrate autonomous perceptive whole-body locomotion on a humanoid in outdoor settings, using only onboard sensing and a single deployable policy.
