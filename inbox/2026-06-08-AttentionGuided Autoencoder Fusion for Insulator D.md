---
interest: medium
link: https://arxiv.org/abs/2606.06536
next_step: skim
priority: medium
slack_ts: '1780894162.528529'
source: cs.CV - Computer Vision
status: unread
title: Attention-Guided Autoencoder Fusion for Insulator Defect Detection Using UAV
  Transmission-Line Imaging
---
# Attention-Guided Autoencoder Fusion for Insulator Defect Detection Using UAV Transmission-Line Imaging
> 原文: [https://arxiv.org/abs/2606.06536](https://arxiv.org/abs/2606.06536)

arXiv:2606.06536v1 Announce Type: new
Abstract: Automated defect detection in high-voltage transmission-line insulators remains challenging due to severe class imbalance, large scale variation, and the small spatial extent of defect instances in Unmanned Aerial Vehicle (UAV) imagery. To address these challenges, this paper proposes AE-YOLO, an Attention-Guided AutoEncoder-Enhanced YOLO framework for robust insulator defect detection. The architecture integrates lightweight bottleneck autoencoders within a Feature Pyramid Network-Path Aggregation Network (FPN-PAN) neck. This preserves anomaly-sensitive information during multi-scale feature fusion. Convolutional Block Attention Modules (CBAM) are used throughout the backbone, enhancing feature discrimination and suppressing background interference. The framework also introduces a variance-maximizing autoencoder regularization strategy, which encourages diverse, defect-discriminative latent representations. The network trains using a unified objective that combines focal loss, Complete IoU (CIoU) loss, and autoencoder regularization to address foreground-background imbalance and improve localization accuracy. During inference, Weighted Boxes Fusion (WBF) combines predictions from YOLOv8, YOLOv10, and YOLO11. An autoencoder-guided confidence boosting mechanism improves sensitivity to rare defect categories. Experiments on the Insulator-Defect Detection dataset show that AE-YOLO with an EfficientNetV2 backbone achieves 95.10 percent mAP at 0.5, 96.40 percent precision, and 93.80 percent recall. This performance surpasses the strongest YOLO-family baseline by 5.0 points in mAP at 0.5 and 6.7 points in recall. These results confirm the effectiveness and adaptability of the framework. The model is a practical and scalable solution for UAV-based transmission-line inspection and defect monitoring.
