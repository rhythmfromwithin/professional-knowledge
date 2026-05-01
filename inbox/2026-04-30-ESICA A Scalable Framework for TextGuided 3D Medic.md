---
interest: medium
link: https://arxiv.org/abs/2604.24876
next_step: skim
priority: medium
slack_ts: '1777608124.495469'
source: cs.CV - Computer Vision
status: unread
title: 'ESICA: A Scalable Framework for Text-Guided 3D Medical Image Segmentation'
---
# ESICA: A Scalable Framework for Text-Guided 3D Medical Image Segmentation
> 原文: [https://arxiv.org/abs/2604.24876](https://arxiv.org/abs/2604.24876)

arXiv:2604.24876v1 Announce Type: new
Abstract: Text guided 3D medical image segmentation offers a flexible alternative to class based and spatial prompt based models by allowing users to specify regions of interest directly in natural language. This paradigm avoids reliance on predefined label sets, reduces ambiguous outputs, and aligns more naturally with clinical workflows. However, existing text guided frameworks are often computationally expensive, exhibit weak text volume feature alignment, and fail to capture fine anatomical details. We propose ESICA, a lightweight and scalable framework that addresses these challenges through three innovations: (1) a similarity matrix based mask prediction formulation that enhances semantic alignment, (2) an efficient decomposed decoder with adapter modules for accurate volumetric decoding, and (3) a two pass refinement strategy that sharpens boundaries and resolves uncertain regions. To improve training stability and generalization, ESICA adopts a two stage scheme consisting of positive only pretraining followed by balanced fine tuning. On the CVPR BiomedSegFM benchmark spanning five imaging modalities (CT, MRI, PET, ultrasound, and microscopy), ESICA achieves state of the art segmentation accuracy, while the compact ESICA4 Lite variant attains similar segmentation performance with substantially fewer parameters, yielding a superior efficiency accuracy trade off. Our framework advances text guided segmentation toward efficient, scalable, and clinically deployable systems. Code will be made publicly available at https://github.com/mirthAI/ESICA.
