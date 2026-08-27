---
interest: medium
link: https://arxiv.org/abs/2608.21424
next_step: skim
priority: medium
slack_ts: '1787820599.310299'
source: cs.CV - Computer Vision
status: unread
title: 'EditStream: A Unified Autoregressive Framework for Interactive Video Generation
  and Editing'
---
# EditStream: A Unified Autoregressive Framework for Interactive Video Generation and Editing
> 原文: [https://arxiv.org/abs/2608.21424](https://arxiv.org/abs/2608.21424)

arXiv:2608.21424v1 Announce Type: new
Abstract: Interactive video generation and editing are becoming increasingly important for creative design. In this report, we introduce EditStream: a unified framework for interactive video generation and editing. EditStream unifies multiple video creation and manipulation tasks within a single DiT-based model through flexible task-specific conditioning, and further transforms it into a fast, few-step autoregressive model for efficient streaming. It supports Text-to-Video, Image-to-Video, Video-to-Video, Editing Propagation, Reference-guided Video Editing, and Camera Pose Change, enabling flexible control over video generation, transformation, and editing within one system. To make the unified model practical for interactive use, we develop a two-stage distillation approach that combines Velocity Moment Matching (VMM) with autoregressive unrolling. VMM matches conditional velocity moments at student-reached intermediate states to preserve generation quality and motion, while unrolling exposes the student to its own autoregressive predictions to improve temporal stability. Together, they alleviate common challenges in few-step autoregressive video generation, including over-saturation, degraded motion, temporal instability, and complex training. EditStream provides a practical and scalable solution that bridges high-quality diffusion-based video models with interactive creative workflows.
