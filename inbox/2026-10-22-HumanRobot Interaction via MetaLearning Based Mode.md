---
title: "Human-Robot Interaction via Meta-Learning Based Mode Recognition and Adaptive Control"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2610.28761
priority: medium
status: unread
interest: medium
next_step: skim
---
# Human-Robot Interaction via Meta-Learning Based Mode Recognition and Adaptive Control
> 原文: [https://arxiv.org/abs/2610.28761](https://arxiv.org/abs/2610.28761)

arXiv:2610.28761v1 Announce Type: new
Abstract: In human-robot interaction (HRI) tasks, humans may interact with the robot in either an active guiding or passive following state, resulting in distinct control objectives for each interaction mode. Most existing approaches rely on predefined switching thresholds to distinguish interaction modes, but their performance can be sensitive to measurement noise. To address this limitation, we propose a novel framework with the following key contributions. First, a neural network (NN) trained via meta-learning is developed to recognize human intention without manually defined thresholds. By successfully incorporating force-dependent parameters from the controller, the recognition rates are improved from 90.1\% to 99.1\% for the passive mode and from 79.8\% to 97.1\% for the active mode. Second, an adaptive meta-learning controller is introduced to compensate for human disturbances and enable online adaptation to varying interaction forces. Third, a multiple-trajectory meta-learning algorithm is designed to jointly learn an environment-basis representation and force-dependent parameters, allowing the controller to deal with unmodeled dynamics efficiently. Experimental results demonstrate that the proposed framework achieves robust and accurate control performance, while providing reliable mode recognition for safe and adaptive physical HRI.
