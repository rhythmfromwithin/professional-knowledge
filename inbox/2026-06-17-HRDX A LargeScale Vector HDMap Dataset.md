---
interest: medium
link: https://arxiv.org/abs/2606.17080
next_step: skim
priority: medium
slack_ts: '1781672192.244079'
source: cs.RO - Robotics
status: unread
title: 'HRDX: A Large-Scale Vector HD-Map Dataset'
---
# HRDX: A Large-Scale Vector HD-Map Dataset
> 原文: [https://arxiv.org/abs/2606.17080](https://arxiv.org/abs/2606.17080)

arXiv:2606.17080v1 Announce Type: new
Abstract: Reliable autonomous driving requires vectorized HD maps that are geometrically accurate, semantically rich, and scalable to long-horizon driving. However, existing public HD map datasets are limited in scale, provide sparse semantic attributes, and lack modalities such as aerial imagery that could enable new research directions. We present HRDX, a large-scale dataset for vector HD-map construction, spanning about 40 hours (1,400 km) of minimally overlapping drives, which is several times larger than prior public HD map datasets. Data is captured using six synchronized surround cameras, a 128-beam LiDAR, and centimeter-level RTK GNSS/IMU, and is further complemented by precisely aligned aerial orthoimagery. Annotations cover 10 vector map classes, complemented with over 20 semantic and topological attributes. To evaluate this richer ontology, we introduce the Composite Score (CS) to jointly assess geometric fidelity and attribute correctness. Benchmark experiments show that HRDX's scale improves online vector-map construction, and that aligned aerial imagery provides a useful structural prior: using aerial imagery at training and/or inference improves geometric map quality, while aerial-augmented teachers can transfer part of this benefit to camera-only students without increasing inference-time sensor requirements. HRDX is intended to support reproducible research on large-scale HD-map learning, multimodal BEV fusion, and training-time privileged information. HRDX dataset and benchmarks are available at https://github.com/honda-research-institute/HRDX
