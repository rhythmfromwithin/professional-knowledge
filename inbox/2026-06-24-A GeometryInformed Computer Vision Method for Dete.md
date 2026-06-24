---
interest: medium
link: https://arxiv.org/abs/2606.23699
next_step: skim
priority: medium
slack_ts: '1782274334.341359'
source: cs.CV - Computer Vision
status: unread
title: A Geometry-Informed Computer Vision Method for Detecting and Examining Overtaking
  Vehicles From A Bicycle
---
# A Geometry-Informed Computer Vision Method for Detecting and Examining Overtaking Vehicles From A Bicycle
> 原文: [https://arxiv.org/abs/2606.23699](https://arxiv.org/abs/2606.23699)

arXiv:2606.23699v1 Announce Type: new
Abstract: Instrumented bicycle studies have produced direct field evidence on vehicle passing behavior, but extracting overtaking events from continuous rear-facing video has remained dependent on manual, frame-by-frame annotation. This bottleneck constrains sample sizes and limits naturalistic cycling safety research. We present a geometry-informed computer vision pipeline that automates overtaking event detection from a single bicycle-mounted camera without multi-sensor configurations or explicit camera calibration. The system combines RT-DETR object detection with ByteTrack multi-object tracking through a three-stage geometric validation module enforcing bearing angle trend, apparent size growth, and spatial confirmation criteria derived from perspective projection principles. Validated on 315 manually annotated real-world overtaking events from urban roads in Ann Arbor, Michigan, the pipeline achieved 97.8% recall with zero false positives. The system identified overtaking intentions a mean of 2.44 seconds before vehicle passage, with 84.1% of events exceeding the 1.5-second human reaction time threshold, demonstrating feasibility for active cyclist warning. Lateral passing distance measurements from 96 events revealed 33.3% of passes below the 5-foot (152.4 cm) threshold, consistent with non-compliance rates in prior field and self-reported studies. A preliminary calibration-free lateral distance estimation approach using bounding box geometric features achieved mean absolute errors of 13-14 cm under leave-one-out cross-validation, sufficient to distinguish close passes from standard passes for safety categorization. By automating event isolation from consumer-grade footage, the system removes the primary annotation bottleneck of instrumented bicycle research and provides a scalable foundation for vehicle-bicycle interaction analysis across larger datasets and diverse urban environments.
