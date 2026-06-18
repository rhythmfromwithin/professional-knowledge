---
interest: medium
link: https://arxiv.org/abs/2606.18377
next_step: skim
priority: low
slack_ts: '1781759641.442889'
source: cs.SE - Software Engineering
status: unread
title: Exploring Statistical Change Point Detection Techniques for Performance Anomaly
  Detection at Mozilla
---
# Exploring Statistical Change Point Detection Techniques for Performance Anomaly Detection at Mozilla
> 原文: [https://arxiv.org/abs/2606.18377](https://arxiv.org/abs/2606.18377)

arXiv:2606.18377v1 Announce Type: new
Abstract: Software performance regressions can have significant business consequences, making automated detection a critical component of modern continuous integration pipelines. At Mozilla, performance anomaly detection is handled by Perfherder, Mozilla's performance engineering management system that relies on a Student's T-test-based approach to flag regressions across hundreds of daily code changes. However, our preliminary analysis of one year of Mozilla performance data reveals that 12.5% of generated alert groups are false positives, while approximately 6.8% of them contain regressions missed by the automated system.
This paper presents an empirical study evaluating 25 change-point detection (CPD) methods and 15 ensemble approaches as alternatives to Mozilla's current method. We construct a ground-truth dataset of 174 performance time series manually annotated by eleven Mozilla performance engineers, representing one of the first practitioner-annotated CPD benchmarks for performance engineering. Our results show that while offline and hybrid CPD methods improve recall over Mozilla's method, they do so at a high cost to precision. Ensemble voting strategies alleviate this trade-off and offer more consistent performance, resulting in 11% improvement in the F1-score. We validate the experimental results through a practitioner survey and report on lessons learned from integrating the best methods into Mozilla's performance engineering system.
