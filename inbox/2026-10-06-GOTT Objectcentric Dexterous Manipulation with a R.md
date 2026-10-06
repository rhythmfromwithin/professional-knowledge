---
title: "GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.03861
priority: medium
status: unread
interest: medium
next_step: skim
---
# GOTT: Object-centric Dexterous Manipulation with a Reusable Cross-Embodiment Primitive
> 原文: [https://arxiv.org/abs/2610.03861](https://arxiv.org/abs/2610.03861)

arXiv:2610.03861v1 Announce Type: new
Abstract: Foundation models and large-scale human data provide rich sources of manipulation intent, but translating this intent into multi-fingered robot behavior remains difficult. Dexterous hands still lack a reusable low-level primitive that reliably establishes contact across tasks and embodiments. We propose GOTT, a reach-acquire-move framework built around a single cross-embodiment contact-acquisition primitive. Given a robot-agnostic object trajectory and a reach specification, GOTT first brings the hand near a task-relevant contact region. The shared closed-loop primitive then establishes stable contact from this approximate initialization, and a pose-conditioned controller tracks the desired object motion. Reach specifications may come from future-aware planning, external models, or human demonstrations, while the primitive and tracking backend remain unchanged. Simulation and real-world experiments show that GOTT is able to establish robust contact across diverse objects, arm-hand platforms, and seen and unseen hand morphologies. It also consistently improves end-to-end task success over open-loop grasp execution.
