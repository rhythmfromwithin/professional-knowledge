---
interest: medium
link: https://arxiv.org/abs/2606.26151
next_step: skim
priority: medium
slack_ts: '1782447556.269019'
source: cs.RO - Robotics
status: unread
title: 'Unsupervised Memory-Enhanced Video Transformers: Obstacle Detection for Autonomous
  Agricultural Rover'
---
# Unsupervised Memory-Enhanced Video Transformers: Obstacle Detection for Autonomous Agricultural Rover
> 原文: [https://arxiv.org/abs/2606.26151](https://arxiv.org/abs/2606.26151)

arXiv:2606.26151v1 Announce Type: new
Abstract: While autonomous rovers have become indispensable to precision farming, achieving consistent operational safety remains a critical challenge. Conventional safety sensors, such as LiDAR, fail to detect obstacles positioned below the plant canopy, posing a significant risk. While camera-based supervised learning methods can detect common objects, they perform poorly when faced with obstacles that were not present in their training data. Actual unsupervised anomaly detection offers a solution by learning the normal visual patterns of an environment, but often fails for the dynamic scenes captured by a moving rover.\\ This paper introduces Video Memory Transformers for Anomaly Detection (VMTAD), a fully unsupervised method designed for real-time obstacle detection in dynamic agricultural scenes. VMTAD utilizes a transformer-driven architecture augmented with a dedicated memory module. This memory module leverages temporal context by processing encoded representations of preceding frames. This approach enables the system to effectively address the dynamic context caused by the robot's movement. The model is trained using only images that represent normal operation, requiring no data labels.\\ VMTAD was rigorously evaluated on the 'Grillion' agricultural rover. On a challenging rapeseed dataset, VMTAD achieved state-of-the-art performance, reaching a 0.973 detection and 0.997 segmentation Area Under the Receiver Operating Characteristic curve. A lightweight variant provides an optimal balance of high accuracy and real-time inference (14 ms), which is critical for safety, as confirmed by our analysis of the rover's total stopping distance.
