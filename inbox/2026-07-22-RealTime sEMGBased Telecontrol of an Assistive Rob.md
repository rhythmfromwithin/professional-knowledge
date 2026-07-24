---
interest: medium
link: https://arxiv.org/abs/2607.16310
next_step: skim
priority: medium
slack_ts: '1784863623.186309'
source: cs.RO - Robotics
status: unread
title: Real-Time sEMG-Based Telecontrol of an Assistive Robotic Arm Using a 1D Convolutional
  Neural Network
---
# Real-Time sEMG-Based Telecontrol of an Assistive Robotic Arm Using a 1D Convolutional Neural Network
> 原文: [https://arxiv.org/abs/2607.16310](https://arxiv.org/abs/2607.16310)

arXiv:2607.16310v1 Announce Type: new
Abstract: Motor impairments affecting the upper limb significantly reduce autonomy in daily activities, particularly for tasks involving object manipulation. Assistive robotic arms offer a promising solution, provided they can be controlled in an intuitive, reliable, and responsive manner. Among human--machine interface approaches, surface electromyography (sEMG) enables non-invasive access to muscle activity and thus to the user's motor intentions. This work proposes a real-time sEMG-based interface for the teleoperation of an assistive robotic arm. The system relies on four-channel sEMG acquisition, signal preprocessing, segmentation into sliding windows, and classification using a one-dimensional convolutional neural network (CNN). Several real-time strategies are investigated, including threshold-based onset detection, a two-stage classification approach (rest vs movement followed by gesture recognition), and a single classifier handling both rest and five gestures. The complete pipeline is implemented and evaluated both in simulation and on a real robotic platform. The CNN-based approach achieves high classification performance, with a test accuracy above 90\% and strong generalization on experimentally acquired signals. The system exhibits stable real-time behavior, with an average latency of approximately 0.32 s consistent with the chosen windowing strategy, and the robot can be controlled reliably using discrete gestures, producing coherent and smooth movements in both simulated and real environments. These findings demonstrate the feasibility of sEMG-based telecontrol for assistive robotics and highlight the importance of integrating signal processing, deep learning, and control strategies within a unified real-time framework. Future work may explore hybrid control approaches combining sEMG with additional sensing modalities to further improve robustness and usability.
