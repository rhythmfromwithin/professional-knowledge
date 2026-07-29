---
title: "Pose-Aware Modeling to Mitigate Pose-Related Artifacts in Tactile Gloves"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2607.22964
priority: medium
status: unread
interest: medium
next_step: skim
---
# Pose-Aware Modeling to Mitigate Pose-Related Artifacts in Tactile Gloves
> 原文: [https://arxiv.org/abs/2607.22964](https://arxiv.org/abs/2607.22964)

arXiv:2607.22964v1 Announce Type: new
Abstract: Tactile gloves digitize contact and force during hand-object interactions, enabling robotics applications in dexterous manipulation, teleoperation, and learning from demonstration. To preserve hand dexterity and capture the nuances of natural interactions, these gloves and the integrated tactile sensors are designed to be soft, flexible, and comfortable. However, such flexible sensors are sensitive not only to contact forces but also unavoidably to hand pose changes, resulting in pose-related artifacts (PRAs). PRAs are especially problematic in the low-force range, resulting in misdetections or late-onset detections of contact, which raises the minimum detectable force (MDF) of the glove. In this work, we characterize the PRAs in relation to pose and force. Building on these insights, we introduce a glove-agnostic algorithmic framework that leverages hand pose information, which is increasingly available, to mitigate PRAs without glove modifications. Our pose-aware force estimation model augments tactile-to-force pipelines with a residual prediction branch that explicitly accounts for pose-induced sensor deformations. We validate our approach across 3 glove designs and 15 users, reducing MDF by 10.4%, 12.2%, and 18.3%, with consistent improvements across all evaluated metrics. This method provides a practical path to improving the usability of tactile gloves in data collection and diverse robotic applications.
