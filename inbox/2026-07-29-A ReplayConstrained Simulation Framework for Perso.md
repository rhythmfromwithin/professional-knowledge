---
title: "A Replay-Constrained Simulation Framework for Personalization of Powered Knee--Ankle Prosthesis Controllers"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.22858
priority: medium
status: unread
interest: medium
next_step: skim
---
# A Replay-Constrained Simulation Framework for Personalization of Powered Knee--Ankle Prosthesis Controllers
> 原文: [https://arxiv.org/abs/2607.22858](https://arxiv.org/abs/2607.22858)

arXiv:2607.22858v1 Announce Type: new
Abstract: Personalization of impedance controllers for powered prosthetic legs is critical to accommodating individual gait biomechanics but remains challenging. Existing methods rely on time-intensive human-in-the-loop exploration and/or constrain optimization to low-dimensional, single-joint parameter subspaces. Sim-to-real transfer has enabled high-dimensional locomotion control for legged robots, but in assistive device control the human partner remains un-modelable. We present a replay-constrained simulation framework: a MuJoCo-based simulator reproduces prosthetic knee-ankle dynamics while replaying recorded hip kinematics and feedback-based ground reaction forces from individual walking data, bypassing the need to model complex human neuromuscular control mechanisms. We demonstrate the framework with a deep reinforcement learning policy that personalizes phase-dependent stiffness, damping, and equilibrium angle at both joints simultaneously, maximizing a biomimicry-based reward computed solely from onboard prosthesis measurements. Experiments with three participants with transfemoral amputation during level-ground walking at 0.8~m/s demonstrate strong simulation-to-hardware predictive validity (Pearson $r=0.96$--$0.997$). The best-performing policy on hardware was consistently predicted within the top five simulation policies for all participants. The learned controllers improved overall biomimicry rewards by 42--59\% relative to the unpersonalized baseline. The framework supports scalable high-dimensional personalization of powered prosthetic legs and is amenable to extension to higher-dimensional controller parameterizations such as neural-network controllers.
