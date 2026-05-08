---
title: "Autonomous Laparoscope Control through Unified Mechanics-Based Representation of Multimodal Intraoperative Information"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.04408
priority: medium
status: unread
interest: medium
next_step: skim
---
# Autonomous Laparoscope Control through Unified Mechanics-Based Representation of Multimodal Intraoperative Information
> 原文: [https://arxiv.org/abs/2605.04408](https://arxiv.org/abs/2605.04408)

arXiv:2605.04408v1 Announce Type: new
Abstract: Laparoscope-holding robots can provide surgeons with a stable laparoscopic field of view (FOV) and reduce the burden on human assistants. To maintain an ideal intraoperative FOV, the robot must continuously adjust the laparoscope pose according to intraoperative information. However, intraoperative multimodal signals, such as position, force/torque, and images, differ markedly in physical meaning and units, making it difficult to build a unified representation and to generate control commands that can be used directly for laparoscope control. To address this issue, we propose a laparoscope-holding robot control method based on unified mechanics modeling of multimodal information. First, we design mapping strategies for multiple intraoperative sources, including position, force/torque, and images, and unify them into an equivalent-wrench representation in the operational space. Then, using a task-priority scheme, we inject the wrenches into the task space and the null space, respectively, and synthesize laparoscope control commands via task-priority projection, thereby achieving consistent representation and coordinated fusion of multimodal information within a single framework. Finally, taking the intraoperative remote center of motion (RCM) position, force/torque sensor readings, and laparoscopic images as examples, we construct an RCM-constraint wrench to enforce the RCM geometric constraint and reduce the contact force at the trocar site, a laparoscope-manipulation wrench to enable compliant dragging, and an instrument-tracking wrench to achieve autonomous visual tracking of the instruments. Experiments on a surgical phantom and in vivo porcine trials demonstrate that the proposed method supports multi-task operation, including compliant laparoscope manipulation and autonomous instrument tracking, while maintaining the RCM constraint and reducing sustained trocar-site loading.
