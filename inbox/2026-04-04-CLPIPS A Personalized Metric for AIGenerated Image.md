---
interest: medium
link: https://arxiv.org/abs/2604.01234
next_step: skim
priority: medium
slack_ts: '1775270921.503209'
source: cs.CV - Computer Vision
status: unread
title: 'CLPIPS: A Personalized Metric for AI-Generated Image Similarity'
---
# CLPIPS: A Personalized Metric for AI-Generated Image Similarity
> 原文: [https://arxiv.org/abs/2604.01234](https://arxiv.org/abs/2604.01234)

arXiv:2604.01234v1 Announce Type: new
Abstract: Iterative prompt refinement is central to reproducing target images with text to image generative models. Previous studies have incorporated image similarity metrics (ISMs) as additional feedback to human users. Existing ISMs such as LPIPS and CLIP provide objective measures of image likeness but often fail to align with human judgments, particularly in context specific or user driven tasks. In this paper, we introduce Customized Learned Perceptual Image Patch Similarity (CLPIPS), a customized extension of LPIPS that adapts a metric's notion of similarity directly to human judgments. We aim to explore whether lightweight, human augmented fine tuning can meaningfully improve perceptual alignment, positioning similarity metrics as adaptive components for human in the loop workflows with text to image tools. We evaluate CLPIPS on a human subject dataset in which participants iteratively regenerate target images and rank generated outputs by perceived similarity. Using margin ranking loss on human ranked image pairs, we fine tune only the LPIPS layer combination weights and assess alignment via Spearman rank correlation and Intraclass Correlation Coefficient. Our results show that CLPIPS achieves stronger correlation and agreement with human judgments than baseline LPIPS. Rather than optimizing absolute metric performance, our work emphasizes improving alignment consistency between metric predictions and human ranks, demonstrating that even limited human specific fine tuning can meaningfully enhance perceptual alignment in human in the loop text to image workflows.
