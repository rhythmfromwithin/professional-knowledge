---
title: "Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.21688
priority: medium
status: unread
interest: medium
next_step: skim
---
# Closed-Loop Sim-to-Real Reinforcement Learning for Deformable Microfiber Shape Control
> 原文: [https://arxiv.org/abs/2605.21688](https://arxiv.org/abs/2605.21688)

arXiv:2605.21688v1 Announce Type: new
Abstract: Autonomous contact-based micromanipulation is challenging because surface and interfacial interactions at the microscale are difficult to model accurately, limiting the use of conventional model-based control and sim-to-real learning. We present a closed-loop sim-to-real reinforcement learning (RL) approach for microfiber shape control on a surface. The central idea is to train geometric shape regulation in a simplified frictionless simulator and rely on real-time visual feedback during deployment to iteratively correct the observed effects of unmodeled surface interactions. An RL policy trained entirely in simulation is transferred directly to a physical dual-gripper micromanipulation system operating at 40 Hz, without retraining or domain adaptation. Using silk microfibers as a testbed, the policy achieves a mean point-wise shape error of 270 $\pm$ 80 $\mu$m across twenty-four diverse initial configurations. Across nine specimens covering all combinations of three fiber diameters (50, 80, and 120 $\mu$m) and three manipulated lengths (10 mm, 15mm, and 20 mm), the same policy achieves sub-millimeter final shape error without any retraining or retuning. These results show that a policy learned in a simplified simulator can achieve repeatable real-world microfiber shape regulation under surface contact, provided that the task-relevant effects of the sim-to-real mismatch remain observable and correctable within the closed feedback loop.
