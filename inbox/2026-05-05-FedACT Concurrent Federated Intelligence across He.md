---
title: "FedACT: Concurrent Federated Intelligence across Heterogeneous Data Sources"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.00011
priority: high
status: unread
interest: medium
next_step: skim
---
# FedACT: Concurrent Federated Intelligence across Heterogeneous Data Sources
> 原文: [https://arxiv.org/abs/2605.00011](https://arxiv.org/abs/2605.00011)

arXiv:2605.00011v1 Announce Type: new
Abstract: Federated Learning (FL) enables collaborative intelligence across decentralized data source devices in a privacy-preserving way. While substantial research attention has been drawn to optimizing the learning process for an individual task, real-world applications increasingly require multiple machine learning tasks simultaneously training their models across a shared pool of devices. Naively applying single-FL optimization techniques in multi-FL systems results in suboptimal system performance, particularly due to device heterogeneity and resource inefficiency. To address such a critical open challenge, we introduce {\em FedACT}, a novel resource heterogeneity-aware device scheduling approach designed to efficiently schedule heterogeneous devices across multiple concurrent FL jobs, with the goal of minimizing their average job completion time (JCT). {\em FedACT} dynamically assigns devices to FL jobs based on an alignment scoring mechanism that evaluates the compatibility between available resources of devices and resource demands of jobs. Additionally, it incorporates participation fairness to ensure balanced contributions from devices across jobs, further enhancing the accuracy levels of learned global models. An optimal scheduling plan is formulated in {\em FedACT} by prioritizing devices with higher alignment scores, while ensuring fair participation across jobs. To evaluate the effectiveness of the proposed scheduling algorithm, we carried out comprehensive experiments using diverse FL jobs and benchmark datasets. Experimental results demonstrate that {\em FedACT} reduces the average JCT by up to 8.3\(\times\) and improves model accuracy by up to 44.5\%, compared to the state-of-the-art baselines.
