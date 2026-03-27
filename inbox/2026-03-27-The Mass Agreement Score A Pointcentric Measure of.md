---
title: "The Mass Agreement Score: A Point-centric Measure of Cluster Size Consistency"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2603.23581
priority: medium
status: unread
interest: medium
next_step: skim
---
# The Mass Agreement Score: A Point-centric Measure of Cluster Size Consistency
> 原文: [https://arxiv.org/abs/2603.23581](https://arxiv.org/abs/2603.23581)

arXiv:2603.23581v1 Announce Type: new
Abstract: In clustering, strong dominance in the size of a particular cluster is often undesirable, motivating a measure of cluster size uniformity that can be used to filter such partitions. A basic requirement of such a measure is stability: partitions that differ only slightly in their point assignments should receive similar uniformity scores. A difficulty arises because cluster labels are not fixed objects; algorithms may produce different numbers of labels even when the underlying point distribution changes very little. Measures defined directly over labels can therefore become unstable under label-count perturbations. I introduce the Mass Agreement Score (MAS), a point-centric metric bounded in [0, 1] that evaluates the consistency of expected cluster size as measured from the perspective of points in each cluster. Its construction yields fragment robustness by design, assigning similar scores to partitions with similar bulk structure while remaining sensitive to genuine redistribution of cluster mass.
