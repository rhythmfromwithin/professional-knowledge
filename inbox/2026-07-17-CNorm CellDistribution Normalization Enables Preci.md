---
title: "C-Norm: Cell-Distribution Normalization Enables Precision Recognition of Medical-Cell Image"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2607.13116
priority: medium
status: unread
interest: medium
next_step: skim
---
# C-Norm: Cell-Distribution Normalization Enables Precision Recognition of Medical-Cell Image
> 原文: [https://arxiv.org/abs/2607.13116](https://arxiv.org/abs/2607.13116)

arXiv:2607.13116v1 Announce Type: new
Abstract: ThinPrep Cytologic Test (TCT) enables early cervical cancer screening, but manual reading is time-consuming and yields inconsistent diagnostic results among cytopathologists. Existing AI detection models perform poorly under real clinical conditions, primarily restricted by two key constraints: unbalanced spatial distribution of cell populations in TCT slides, and limited high-quality annotated cytology data relying on professional pathologist labeling. To address these limitations, we propose a Cell-Distribution Normalization (C-Norm) method. By decoupling abnormal and normal cells from the original TCT images and re-synthesizing them, this method ensures a uniform distribution of cell populations, thereby mitigating generalization degradation caused by distribution bias. Building upon this, we integrate the YOLOv12 framework with a DINOv3 module. This hybrid architecture leverages the advanced detection capability of YOLO models and the superior feature representations of DINOv3 to capture subtle morphological nuances essential for precise recognition of TCT images. Extensive experiments demonstrate that our proposed method achieves state-of-the-art performance, significantly outperforming mainstream detection algorithms. The complete implementation is available at: https://github.com/ddw2AIGROUP2CQUPT/Cell-Norm
