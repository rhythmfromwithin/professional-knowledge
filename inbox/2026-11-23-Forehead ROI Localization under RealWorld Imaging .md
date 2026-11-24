---
interest: medium
link: https://arxiv.org/abs/2611.26712
next_step: skim
priority: medium
slack_ts: '1795512704.828869'
source: cs.CV - Computer Vision
status: unread
title: Forehead ROI Localization under Real-World Imaging Degradations via Cross-View
  Pseudo-Labeling
---
# Forehead ROI Localization under Real-World Imaging Degradations via Cross-View Pseudo-Labeling
> 原文: [https://arxiv.org/abs/2611.26712](https://arxiv.org/abs/2611.26712)

arXiv:2611.26712v1 Announce Type: new
Abstract: Forehead region-of-interest (ROI) localization is important for forehead-creases biometrics, particularly when the lower face is occluded. However, localization remains challenging under varying image quality, pose, and illumination. We propose Confidence and Consistency Guided Pseudo-Labeling (CCGP), which adapts Grounding DINO using unlabeled facial images filtered by detection confidence and geometric consistency between original and horizontally flipped views, without modifying the detector architecture or loss. We evaluate CCGP on five external datasets and 350 images spanning seven imaging conditions. CCGP achieves the highest mean intersection over union (mIoU) on four of five external datasets, improving from 0.415 to 0.580 on RMFRD compared with supervised Grounding DINO. On the quality-stratified subset, the largest gains occur under blur (0.487 to 0.719) and low contrast (0.615 to 0.710). CCGP also outperforms conventional self-training on RMFRD (0.580 versus 0.551 mIoU). Despite a slight in-domain performance gap (0.861 vs. 0.866 mIoU) and challenges with off-angle poses, CCGP improves cross-dataset localization under challenging imaging conditions.
