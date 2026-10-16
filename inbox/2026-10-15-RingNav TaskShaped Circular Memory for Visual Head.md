---
interest: medium
link: https://arxiv.org/abs/2610.19044
next_step: skim
priority: medium
slack_ts: '1792123822.277539'
source: cs.RO - Robotics
status: unread
title: 'RingNav: Task-Shaped Circular Memory for Visual Heading'
---
# RingNav: Task-Shaped Circular Memory for Visual Heading
> 原文: [https://arxiv.org/abs/2610.19044](https://arxiv.org/abs/2610.19044)

arXiv:2610.19044v1 Announce Type: new
Abstract: Tiny robots have limited computation and memory, yet visual navigation systems often maintain more state than a task requires. We ask whether persistent memory can instead be shaped by the task. We present \textbf{RingNav}, a \(10.6\)k--parameter visual heading estimator that constrains its memory to the circular manifold \(S^1\). RingNav learns only the turn between consecutive images, while heading is composed directly on the circle. On the TartanAir Visual SLAM Challenge, RingNav reduces mean absolute turn error by \(27\%\) and accumulated heading error over $4$ sec by \(15\%\) relative to a similarly sized learned-memory model. The structured update also gives exactly zero turn for identical frames and exact cancellation under sequence reversal. Without fine-tuning, RingNav transfers to real-world drone experiments and continues estimating heading under severe visual degradation. RingNav runs at $27.3$Hz on Raspberry Pi Zero 2W and can be deployed on an ultra-low power GAP8 processor at $33.4$Hz.
