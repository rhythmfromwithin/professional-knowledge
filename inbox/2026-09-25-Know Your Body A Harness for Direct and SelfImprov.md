---
title: "Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2609.28530
priority: medium
status: unread
interest: medium
next_step: skim
---
# Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs
> 原文: [https://arxiv.org/abs/2609.28530](https://arxiv.org/abs/2609.28530)

arXiv:2609.28530v1 Announce Type: new
Abstract: A general-purpose vision-language model can understand a task goal without knowing how a particular robot's motion and functional parts produce the intended effect. We introduce KnowBody, a harness that makes these action-relevant body relations explicit, queryable, and revisable while keeping the model weights frozen. Initialized from one off-task trajectory, a partial body model guides action selection and the interpretation of past interactions. New evidence refines the model, and knowledge dependent on revised body estimates is rechecked before reuse. Across 32 fixed-budget trials on four real-robot tasks, initialized KnowBody achieves 75% completion versus 25% for the native harness and requires fewer planner rounds on successful trials in tasks completed by both. With persistent updates enabled, planner rounds decrease by 29-53% from the first to the fifth recorded success.
