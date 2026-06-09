---
interest: medium
link: https://arxiv.org/abs/2606.07558
next_step: skim
priority: medium
slack_ts: '1780978312.257729'
source: cs.CV - Computer Vision
status: unread
title: Page image classifier fine-tuned on century-spanning archives of scanned documents
  for further content-specific processing
---
# Page image classifier fine-tuned on century-spanning archives of scanned documents for further content-specific processing
> 原文: [https://arxiv.org/abs/2606.07558](https://arxiv.org/abs/2606.07558)

arXiv:2606.07558v1 Announce Type: new
Abstract: Purpose: Digitization projects in the humanities produce vast, heterogeneous archives of historical documents, making manual sorting impractical at scale. This work addresses the need for an automated system to classify scanned page images based on visual content type - text, tables, and graphics - enabling content-specific downstream processing such as Optical Character Recognition (OCR) or structured data extraction. Methods: An image classification system was developed and evaluated on a dataset of over 48,000 annotated historical page images from century-old Czech archaeological archives, refined through four successive annotation stages with domain-expert review. A Random Forest Classifier baseline was established using hand-crafted image features. Subsequently, deep learning architectures were fine-tuned and compared: Convolutional Neural Networks (EfficientNetV2, RegNetY), Vision and Document Image Transformers (ViT, DiT), and multimodal CLIP models. An 11-category label scheme was designed collaboratively with domain experts and evaluated via five-fold cross-validation. Results: The feature-based baseline achieved approximately 75% accuracy. Fine-tuned CNNs and Transformers substantially outperformed it, with RegNetY-16GF achieving 99.16% and ViT-large 99.12% Top-1 accuracy on the held-out test set. CLIP ViT-B/16 reached 99.14% with optimized text descriptions. Conclusion: Image-only models, particularly RegNetY-16GF, deliver near-perfect classification accuracy and produce consistent labels across 649,508 unlabeled archival pages with over 90% inter-model agreement. Fine-tuned CLIP, despite competitive test-set accuracy, showed under 65% agreement with image-only models on unlabeled data, making it less suitable for deployment. The final models, annotated dataset, and software are publicly available under open-source licenses.
