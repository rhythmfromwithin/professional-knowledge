---
interest: medium
link: https://arxiv.org/abs/2603.22502
next_step: skim
priority: medium
slack_ts: '1774754582.576559'
source: cs.RO - Robotics
status: unread
title: 'MapForest: A Modular Field Robotics System for Forest Mapping and Invasive
  Species Localization'
---
# MapForest: A Modular Field Robotics System for Forest Mapping and Invasive Species Localization
> 原文: [https://arxiv.org/abs/2603.22502](https://arxiv.org/abs/2603.22502)

arXiv:2603.22502v1 Announce Type: new
Abstract: Monitoring and controlling invasive tree species across large forests, parks, and trail networks is challenging due to limited accessibility, reliance on manual scouting, and degraded under-canopy GNSS. We present MapForest, a modular field robotics system that transforms multi-modal sensor data into GIS-ready invasive-species maps. Our system features: (i) a compact, platform-agnostic sensing payload that can be rapidly mounted on UAV, bicycle, or backpack platforms, and (ii) a software pipeline comprising LiDAR-inertial mapping, image-based invasive-species detection, and georeferenced map generation. To ensure reliable operation in GNSS-intermittent environments, we enhance a LiDAR-inertial mapping backbone with covariance-aware GNSS factors and robust loss kernels. We train an object detector to detect the Tree-of-Heaven (Ailanthus altissima) from onboard RGB imagery and fuse detections with the reconstructed map to produce geospatial outputs suitable for downstream decision making. We collected a dataset spanning six sites across urban environments, parks, trails, and forests to evaluate individual system modules, and report end-to-end results on two sites containing Tree-of-Heaven. The enhanced mapping module achieved a trajectory deviation error of 1.95 m over a 1.2 km forest traversal, and the Tree-of-Heaven detector achieved an F1 score of 0.653. The datasets and associated tooling are released to support reproducible research in forest mapping and invasive-species monitoring.
