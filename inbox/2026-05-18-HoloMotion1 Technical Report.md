---
interest: medium
link: https://arxiv.org/abs/2605.15336
next_step: skim
priority: medium
slack_ts: '1779164074.742549'
source: cs.RO - Robotics
status: unread
title: HoloMotion-1 Technical Report
---
# HoloMotion-1 Technical Report
> 原文: [https://arxiv.org/abs/2605.15336](https://arxiv.org/abs/2605.15336)

arXiv:2605.15336v1 Announce Type: new
Abstract: In this report, we present HoloMotion-1, a humanoid motion foundation model for zero-shot whole-body motion tracking. A key innovation of HoloMotion-1 is to scale control-policy training with a large-scale hybrid motion corpus, where video-reconstructed motions from in-the-wild videos provide the dominant source of motion diversity, while curated motion-capture and in-house motion data provide higher-fidelity supervision and deployment-oriented coverage. This data regime enables HoloMotion-1 to move beyond conventional MoCap-only training and exposes the policy to substantially broader behaviors, capture conditions, and motion styles.
Learning from such heterogeneous data introduces new challenges, including reconstruction noise, source-domain mismatch, uneven motion quality, and the need for temporal modeling under large behavioral variation. To address these challenges, HoloMotion-1 integrates large-capacity temporal modeling, a sparsely activated Mixture-of-Experts Transformer with KV-cache inference for real-time control, and a sequence-level training strategy that improves learning efficiency on extended motion sequences. Extensive experiments on multiple unseen motion benchmarks show that HoloMotion-1 generalizes robustly across diverse motion types and capture conditions, significantly improves tracking accuracy over prior methods, and transfers directly to a real humanoid robot without task-specific fine-tuning.
