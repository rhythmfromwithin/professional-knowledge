---
title: "Why Constrained Updates Still Forget: A Functional-Path Analysis of Continual SFT"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2610.30191
priority: medium
status: unread
interest: medium
next_step: skim
---
# Why Constrained Updates Still Forget: A Functional-Path Analysis of Continual SFT
> 原文: [https://arxiv.org/abs/2610.30191](https://arxiv.org/abs/2610.30191)

arXiv:2610.30191v1 Announce Type: new
Abstract: Supervised fine-tuning adapts language models to specialized tasks but can disrupt previously acquired behavior. Existing approaches constrain parameters, gradients, or replay objectives, yet the connection between the protected object, the intervening trajectory, and retained outputs remains unclear. We develop a functional-path account that decomposes old-loss changes along realized updates into the controlled direction, gradient staleness, probe mismatch, and finite-step effects. The account yields a conditional refresh budget and identifies the restoring direction supplied by informative replay. Matched QLoRA interventions separate constraint granularity from placement before or after Adam: placement strongly affects retention across the studied code-label audits, whereas the granularity interaction depends on the endpoint. Checkpointed generation separates endpoint recovery from higher sampled-path accuracy, and matched replay schedules reveal loss exposure concealed by final scores. A sequential-task comparison extends this distinction to backward transfer: subspace regularization and projection improve average retention while trading off different old tasks; supervised replay protects both more consistently in this setting. Additional response interfaces distinguish content gains from exact-response retention. These findings connect update-level protection to task-wise behavior and motivate mitigation through explicit functional anchors, trajectory evaluation, and joint old/new auditing.
