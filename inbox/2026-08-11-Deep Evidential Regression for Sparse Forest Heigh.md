---
title: "Deep Evidential Regression for Sparse Forest Height Estimation from Multimodal Satellite Imagery"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2608.06406
priority: medium
status: unread
interest: medium
next_step: skim
---
# Deep Evidential Regression for Sparse Forest Height Estimation from Multimodal Satellite Imagery
> 原文: [https://arxiv.org/abs/2608.06406](https://arxiv.org/abs/2608.06406)

arXiv:2608.06406v1 Announce Type: new
Abstract: Accurate estimation of forest height from satellite imagery is essential for applications such as carbon accounting, biodiversity monitoring, and ecosystem management. While recent deep learning approaches provide accurate predictions, they typically do not quantify predictive uncertainty. This limitation is particularly relevant in geospatial settings characterized by sparse supervision and geographic distribution shift. In this work, we investigate Deep Evidential Regression (DER) for forest height estimation on the TreeUQ benchmark, a large-scale dataset designed for the joint estimation of tree count and average tree height at 10 m resolution, based on Sentinel-1/-2 data as well as tree inventory data over the federal state of Bavaria. To account for the extreme label sparsity of the tree inventory data, we introduce a masked evidential loss for dense geospatial prediction. Using a U-Net architecture with multimodal Sentinel-1 and Sentinel-2 inputs, the proposed approach jointly predicts tree height and associated uncertainty estimates in a single forward pass. Experimental results show that DER achieves predictive performance comparable to a deterministic U-Net while additionally providing well-calibrated uncertainty estimates. These findings demonstrate the potential of evidential learning as an efficient framework for uncertainty-aware forest structure estimation from Earth observation data.
