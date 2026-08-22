---
title: "Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2608.19375
priority: medium
status: unread
interest: medium
next_step: skim
---
# Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control
> 原文: [https://arxiv.org/abs/2608.19375](https://arxiv.org/abs/2608.19375)

arXiv:2608.19375v1 Announce Type: new
Abstract: High-fidelity embodied AI simulators provide realistic evaluation of complex robotic systems, but their computational cost limits their direct use for large-scale reinforcement learning campaigns. We advocate the use of less accurate but more expeditious simulations, which might draw on data-driven, e.g., neural dynamics, models. This contribution argues that the practical value of a neural dynamics model for complex robot control lies in learning the \emph{right abstraction}: a reduced state that preserves the control-relevant physics of the high-fidelity system while enabling high-throughput policy learning. We develop a neural reduced dynamics (NRD) framework that separates the state the model propagates from what can be supplied as an input or recovered analytically, trains policies entirely inside the frozen learned model, and validates them back in the high-fidelity simulator. Two case studies instantiate it across three control tasks: terrain-aware HMMWV trajectory tracking on rigid, bumpy and deformable Continuum Representation Model (CRM) terrain; and goal reaching for a stock tracked vehicle and its front-mounted articulated arm. Every policy transfers back to the high-fidelity simulator. A single policy trained inside the terrain-conditioned dynamics model, and given no terrain input of its own, attains lower median and mean tracking error than both single-terrain specialists on all three terrains, including zero-shot bumpy terrain. Quantitatively, the tracked vehicle reaches 100 of 100 goals and the arm 97 of 100, with zero contacts or joint-limit violations. The NRD models advance roughly four orders of magnitude faster in simulated time than the high-fidelity simulator scenes they replace, making iterative on-policy learning practical and supporting neural reduced dynamics as a bridge between accurate but expensive physics simulation and scalable robot learning.
