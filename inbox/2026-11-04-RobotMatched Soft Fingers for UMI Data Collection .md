---
interest: medium
link: https://arxiv.org/abs/2611.03779
next_step: skim
priority: medium
slack_ts: '1793859290.964849'
source: cs.RO - Robotics
status: unread
title: 'Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours
  of Pick and Place'
---
# Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place
> 原文: [https://arxiv.org/abs/2611.03779](https://arxiv.org/abs/2611.03779)

arXiv:2611.03779v1 Announce Type: new
Abstract: Training robot policies for multi-task pick and place requires demonstrations on many objects, which handheld Universal Manipulation Interfaces (UMIs) can collect quickly and cheaply. However, existing UMIs depend on external base stations, use rigid fingers that give no signal about contact forces, or use parallel-jaw fingers that limit grip strength. We present a battery-powered handheld interface, built on YUBI, whose soft, angled fingers wrap around objects, deform visibly under load as a visual proxy for force, and match the grippers of the robot. With it, we collect a 99.7-hour dataset over 53 objects, train $\pi\_{0.5}$ policies on 49 of them, and hold out the other 4 as unseen objects. We find that a top camera raises success by 13 points even when only about half of the data includes it, and that mid-training on our multi-task data raises success after fine-tuning on unseen objects from 35% to 57%. Finger design, dataset, and data processing code: https://lute-corp.github.io/soft-yubi-site/
