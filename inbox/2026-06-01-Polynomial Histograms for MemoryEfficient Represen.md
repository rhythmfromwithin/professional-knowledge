---
interest: medium
link: https://arxiv.org/abs/2605.30360
next_step: skim
priority: medium
slack_ts: '1780462692.088119'
source: cs.DC - Distributed Computing
status: unread
title: Polynomial Histograms for Memory-Efficient Representation of Long-tailed System
  Distributions
---
# Polynomial Histograms for Memory-Efficient Representation of Long-tailed System Distributions
> 原文: [https://arxiv.org/abs/2605.30360](https://arxiv.org/abs/2605.30360)

arXiv:2605.30360v1 Announce Type: new
Abstract: Distributed systems must frequently keep track of many different types of performance metrics across many different computers. For example, the latency distribution of certain operations may be computed for a large combination of computers, users, and operations. These empirical distributions need to be collected at minimal expense on the individual software components, efficiently aggregated across multiple dimensions, and stored in a compact representation for a variety of downstream data analysis applications.
We describe an information loss metric for binned data that allows us to optimize cost of information loss from different histogram representations. We explore the use of polynomial histograms where each bin of a histogram is annotated with moments of the underlying distribution in that bin. These polynomial histograms are compared to traditional histograms using the same storage cost for additional bins instead of annotations in each bin. We describe an application of these techniques for file system metrics for a large production system, and analytically characterize when polynomial histograms offer more information at lower cost.
