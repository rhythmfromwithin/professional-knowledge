---
title: "Wiggle and Go! System Identification for Zero-Shot Dynamic Rope Manipulation"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2604.22102
priority: medium
status: unread
interest: medium
next_step: skim
---
# Wiggle and Go! System Identification for Zero-Shot Dynamic Rope Manipulation
> 原文: [https://arxiv.org/abs/2604.22102](https://arxiv.org/abs/2604.22102)

arXiv:2604.22102v1 Announce Type: new
Abstract: Many robotic tasks are unforgiving; a single mistake in a dynamic throw can lead to unacceptable delays or unrecoverable failure. To mitigate this, we present a novel approach that leverages learned simulation priors to inform goal-conditioned dynamic manipulation of ropes for efficient and accurate task execution. Related methods for dynamic rope manipulation either require large real-world datasets to estimate rope behavior or the use of iterative improvements on attempts at the task for goal completion. We introduce Wiggle and Go!, a system-identification, two-stage framework that enables zero-shot task rope manipulation. The framework consists of a system identification module that observes rope movement to predict descriptive physical parameters, which then informs an optimization method for goal-conditioned action prediction for the robot to execute zero-shot in the real. Our method achieves strong performance across multiple dynamic manipulation tasks enabled by the same task-agnostic system identification module which offers seamless switching between different manipulation tasks, allowing a single model to support a diverse array of manipulation policies. We achieve a 3.55 cm average accuracy on 3D target striking in real using rope system parameters in comparison to 15.34 cm accuracy when our task model is not system-parameter-informed. We achieve a Pearson correlation coefficient of 0.95 between Fourier frequencies of the predicted and real ropes on an unseen trajectory. Project website please see https://wiggleandgo.github.io/
