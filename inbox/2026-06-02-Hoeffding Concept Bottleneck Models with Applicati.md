---
title: "Hoeffding Concept Bottleneck Models with Applications to Overhead Images"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2606.00082
priority: high
status: unread
interest: medium
next_step: skim
---
# Hoeffding Concept Bottleneck Models with Applications to Overhead Images
> 原文: [https://arxiv.org/abs/2606.00082](https://arxiv.org/abs/2606.00082)

arXiv:2606.00082v1 Announce Type: new
Abstract: Explainability of deep learning algorithms is critical for computer-vision applications with high-stake decisions. Concept bottleneck models (CBM) have recently shown promising performance to provide explainable and accurate predictions for classification problems, based on a bottleneck of high-level concepts. Existing CBM methods rely on a linear aggregation of the concept scores to compute predictions. However, a large number of concepts is often used in this linear approach, which undermines explainability and favors information leakage. In general, the underlying relation between concepts and output logits is not linear. Therefore, we introduce Hoeffding Concept Bottleneck Models (HCBM), which build on the Hoeffding functional decomposition of gradient-boosted trees to provide non-linear and sparse aggregations of concept scores, and generate compact predictions using prime implicants. HCBM are proved to be robust to interconcept leakage, and outperform standard linear CBM in practice, as shown in extensive experiments. Beyond classification, HCBM can be adapted to object detection, and we focus on a challenging case with overhead images to show the high performance of HCBM in these settings.
