---
title: "Dimensional Balance Improves Large Scale Spatiotemporal Prediction Performance"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.18793
priority: high
status: unread
interest: medium
next_step: skim
---
# Dimensional Balance Improves Large Scale Spatiotemporal Prediction Performance
> 原文: [https://arxiv.org/abs/2605.18793](https://arxiv.org/abs/2605.18793)

arXiv:2605.18793v1 Announce Type: new
Abstract: Accurate spatiotemporal pattern analysis is critical in fields such as urban traffic, meteorology, and public health monitoring. However, existing methods face performance bottlenecks, typically yielding only incremental gains and often exhibiting limited cross-domain transferability. We analyze this bottleneck through spatial and temporal entropy measures, which are used as diagnostic indicators of spatiotemporal complexity mismatch rather than as guarantees that entropy alignment alone yields better forecasting. Empirically, larger mismatch is often accompanied by higher prediction uncertainty, especially under a fixed model-capacity budget. Guided by this diagnostic, we propose a scalable, adaptive framework that harmonizes spatial and temporal feature representations. Spatial dimensionality is compressed via low-rank matrix embedding to preserve essential structure, while an extended temporal horizon captures long-range dependencies and mitigates cumulative errors arising from temporal heterogeneity. Extensive experiments on urban traffic, meteorological, and epidemic datasets demonstrate substantial accuracy gains and broad applicability across the evaluated domains, suggesting that the framework is promising for a wide range of spatiotemporal tasks beyond the current study. The code is available on GitHub at https://github.com/ST-Balance/ST-Balance.
