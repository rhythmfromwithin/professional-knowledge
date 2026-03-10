---
title: "Impact of Localization Errors on Label Quality for Online HD Map Construction"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.03452
priority: medium
status: unread
interest: medium
next_step: skim
---
# Impact of Localization Errors on Label Quality for Online HD Map Construction
> 原文: [https://arxiv.org/abs/2603.03452](https://arxiv.org/abs/2603.03452)

arXiv:2603.03452v1 Announce Type: new
Abstract: High-definition (HD) maps are crucial for autonomous vehicles, but their creation and maintenance is very costly. This motivates the idea of online HD map construction. To provide a continuous large-scale stream of training data, existing HD maps can be used as labels for onboard sensor data from consumer vehicle fleets. However, compared to current, well curated HD map perception datasets, this fleet data suffers from localization errors, resulting in distorted map labels. We introduce three kinds of localization errors, Ramp, Gaussian, and Perlin noise, to examine their influence on generated map labels. We train a variant of MapTRv2, a state-of-the-art online HD map construction model, on the Argoverse 2 dataset with various levels of localization errors and assess the degradation of model performance. Since localization errors affect distant labels more severely, but are also less significant to driving performance, we introduce a distance-based map construction metric. Our experiments reveal that localization noise affects the model performance significantly. We demonstrate that errors in heading angle exert a more substantial influence than position errors, as angle errors result in a greater distortion of labels as distance to the vehicle increases. Furthermore, we can demonstrate that the model benefits from non-distorted ground truth (GT) data and that the performance decreases more than linearly with the increase in noisy data. Our study additionally provides a qualitative evaluation of the extent to which localization errors influence the construction of HD maps.
