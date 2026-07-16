---
title: "Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.12105
priority: medium
status: unread
interest: medium
next_step: skim
---
# Robust In-Hand Manipulation via Priors in Reinforcement Learning and Mechanical Design
> 原文: [https://arxiv.org/abs/2607.12105](https://arxiv.org/abs/2607.12105)

arXiv:2607.12105v1 Announce Type: new
Abstract: In-hand manipulation without external sensing is challenging due to uncertainties from finger-object contacts and disturbances by gravity. While reinforcement learning has shown promise in learning complex finger gaiting, existing approaches do not prioritize maintaining well-conditioned grasps for sustained manipulation. We introduce two complementary physics priors for robust in-hand rolling: a global grasp-quality prior derived from classical grasp analysis and a local contact-geometry prior based on fingertip curvature. The grasp-quality prior is used as a dense reward-shaping term that encourages well-distributed contacts with improved worst-case wrench resistance. The contact-geometry prior is expressed in the fingertip geometry that mechanically shapes the contact interface toward task-aligned rolling while reducing off-axis drift. We evaluate the effect of these priors on learning in-hand rolling manipulation for a multifingered robotic hand manipulating three different objects at four palm orientations. Results show significant improvement in rotation efficiency, grasp stability, and disturbance rejection, suggesting that physics priors embedded in both learning and fingertip morphology improve task robustness and sim-to-real transfer. An overview video can be found at https://youtu.be/pdd1wHxQnJM?si=dM-U5kiiPTYsk3Pk.
