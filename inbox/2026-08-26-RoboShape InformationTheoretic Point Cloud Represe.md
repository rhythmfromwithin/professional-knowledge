---
interest: medium
link: https://arxiv.org/abs/2608.21380
next_step: skim
priority: medium
slack_ts: '1787820609.937289'
source: cs.RO - Robotics
status: unread
title: 'RoboShape: Information-Theoretic Point Cloud Representations for Privacy-Aware
  Robot Perception'
---
# RoboShape: Information-Theoretic Point Cloud Representations for Privacy-Aware Robot Perception
> 原文: [https://arxiv.org/abs/2608.21380](https://arxiv.org/abs/2608.21380)

arXiv:2608.21380v1 Announce Type: new
Abstract: With the increased adoption of robotic agents operating in human environments by scanning and sharing 3D representations (e.g., for fleet learning, cloud-based planning, or collaborative mapping), collected point clouds reveal not just the objects in a scene but also sensitive spatial context, such as room function or information that occupants never consented to disclose. Traditional point cloud encoders offer no principled control over this: either all is preserved, or none. Hence, we introduce RoboShape, an information theory guided compression head following the frozen {\tt Sonata} encoder. We project voxel-level embeddings using the Donsker-Varadhan formulation of mutual information (MI). Specifically, we maximize the MI between embeddings and object-level understanding while minimizing it for private attributes. RoboShape leads to 87.5\% smaller embeddings that retain 98.7\% of object classification utility while collapsing sensitive attribute predictions by 39.3\% across the three real-world indoor LiDAR datasets. Its privacy-preserving embeddings are cheaper to transmit over the network or to train a model for any downstream tasks. We release the RoboShape codebase to give the robotics community a practical, encoder-agnostic tool for building perception pipelines that are compact, privacy-aware, and deployment-ready.
