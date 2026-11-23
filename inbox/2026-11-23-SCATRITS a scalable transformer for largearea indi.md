---
interest: medium
link: https://arxiv.org/abs/2611.26715
next_step: skim
priority: medium
slack_ts: '1795417670.641389'
source: cs.CV - Computer Vision
status: unread
title: 'SCATR-ITS: a scalable transformer for large-area individual tree segmentation
  from LiDAR point clouds'
---
# SCATR-ITS: a scalable transformer for large-area individual tree segmentation from LiDAR point clouds
> 原文: [https://arxiv.org/abs/2611.26715](https://arxiv.org/abs/2611.26715)

arXiv:2611.26715v1 Announce Type: new
Abstract: Individual tree segmentation (ITS) from LiDAR point clouds is one of the most widely studied segmentation tasks in forestry. Although deep learning methods define the state of the art on the majority of ITS benchmarks, their high computational complexity and long runtime currently prevent their adoption in large-scale operational workflows. In this work, we present SCATR-ITS, a scalable transformer model specifically designed for efficient ITS over large geographical areas. Based on the ForestFormer3D framework, SCATR-ITS transitions to superpoint-level processing to accelerate inference, with the superpoints constructed from learned embeddings. The architecture incorporates size-aware superpoint-level postprocessing, a dynamic query count module to handle high variation in forest structure, and a maximal input stride designed to minimize prediction redundancy. SCATR-ITS achieves accuracy on par with the state of the art on the FGI-EMIT and FOR-InstanceV2 datasets with an up to 8.5$\times$ higher inference speed. In addition, SCATR-ITS has a significantly lower GPU VRAM footprint during both training and inference, and exhibits excellent zero-shot generalization across multiple datasets. To demonstrate large-area ITS capabilities, SCATR-ITS is applied to a 142 km$^2$ region of Finnish national laser scanning data where it achieves an average throughput of 13.8 min/km$^2$, $\sim$18.6$\times$ faster than ForestFormer3D and approaching the speed of the unsupervised watershed algorithm, which it vastly outperforms in accuracy and segment quality. Overall, SCATR-ITS delivers state-of-the-art accuracy at speeds where operational-scale adoption becomes viable, paving the way toward countrywide deployment. The source code for SCATR-ITS and pretrained weights are available at https://github.com/ruoppa/scatr\_its.
