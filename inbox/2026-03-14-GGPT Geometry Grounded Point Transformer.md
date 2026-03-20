---
interest: medium
link: https://arxiv.org/abs/2603.11174
next_step: skim
priority: medium
slack_ts: '1773974643.814549'
source: cs.CV - Computer Vision
status: unread
title: 'GGPT: Geometry Grounded Point Transformer'
---
# GGPT: Geometry Grounded Point Transformer
> 原文: [https://arxiv.org/abs/2603.11174](https://arxiv.org/abs/2603.11174)

arXiv:2603.11174v1 Announce Type: new
Abstract: Recent feed-forward networks have achieved remarkable progress in sparse-view 3D reconstruction by predicting dense point maps directly from RGB images. However, they often suffer from geometric inconsistencies and limited fine-grained accuracy due to the absence of explicit multi-view constraints. We introduce the Geometry-Grounded Point Transformer (GGPT), a framework that augments feed-forward reconstruction with reliable sparse geometric guidance. We first propose an improved Structure-from-Motion pipeline based on dense feature matching and lightweight geometric optimisation to efficiently estimate accurate camera poses and partial 3D point clouds from sparse input views. Building on this foundation, we propose a geometry-guided 3D point transformer that refines dense point maps under explicit partial-geometry supervision using an optimised guidance encoding. Extensive experiments demonstrate that our method provides a principled mechanism for integrating geometric priors with dense feed-forward predictions, producing reconstructions that are both geometrically consistent and spatially complete, recovering fine structures and filling gaps in textureless areas. Trained solely on ScanNet++ with VGGT predictions, GGPT generalises across architectures and datasets, substantially outperforming state-of-the-art feed-forward 3D reconstruction models in both in-domain and out-of-domain settings.
