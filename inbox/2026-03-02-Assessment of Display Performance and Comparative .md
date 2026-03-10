---
title: "Assessment of Display Performance and Comparative Evaluation of Web Map Libraries for Extensive 3D Geospatial Data"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2602.23660
priority: medium
status: unread
interest: medium
next_step: skim
---
# Assessment of Display Performance and Comparative Evaluation of Web Map Libraries for Extensive 3D Geospatial Data
> 原文: [https://arxiv.org/abs/2602.23660](https://arxiv.org/abs/2602.23660)

arXiv:2602.23660v1 Announce Type: new
Abstract: Large-scale 3D geospatial data visualization has become increasingly critical for the development of the digital society infrastructure in Japan. This study conducted a comprehensive performance evaluation of two major WebGL-based web mapping libraries, CesiumJS and MapLibre GL JS, using large-scale 3D point-cloud data from the VIRTUAL SHIZUOKA and PLATEAU building models. The research employs standardized 3D Tiles 1.1, and Mapbox Vector Tiles (MVT) formats, comparing performance across different data scales (2nd and 3rd grid levels) using Core Web Vitals metrics, including First Contentful Paint (FCP), Largest Contentful Paint (LCP), Speed Index, Total Blocking Time (TBT), and Cumulative Layout Shift (CLS).
The results demonstrate that MVT-based building visualization with MapLibre GL JS achieves optimal performance (FCP 0.8s, TBT 0ms), whereas MapLibre GL JS combined with deck.gl shows superior performance for large-scale point cloud processing (TBT: 3ms, CesiumJS: 21,357ms). This study provides data-driven selection guidelines for appropriate technology choices according to use cases, establishing reproducible performance evaluation frameworks for 3D web mapping technologies during the WebGPU and OGC 3D Tiles 1.1 standardization era.
