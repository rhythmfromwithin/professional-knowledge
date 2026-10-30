---
interest: medium
link: https://arxiv.org/abs/2610.37256
next_step: skim
priority: low
slack_ts: '1793337887.044769'
source: cs.DB - Databases
status: unread
title: Fast Approximate Line Nearest Neighbor Search
---
# Fast Approximate Line Nearest Neighbor Search
> 原文: [https://arxiv.org/abs/2610.37256](https://arxiv.org/abs/2610.37256)

arXiv:2610.37256v1 Announce Type: new
Abstract: Approximate nearest neighbor (ANN) search, which retrieves vectors close to a given query vector, is a fundamental operation in vector databases. However, emerging applications, such as selecting source images for photo-based animation and video synthesis, may require matching content while allowing a query-specified aspect contrast, such as an illumination change, to vary; a single query point does not directly express this requirement. In this paper, we study approximate line nearest neighbor (LANN) search, where an infinite query line removes the distance contribution along a specified direction while database records remain points. Prior approaches focus on top-$1$ search only for LANN and can incur high construction costs. Converting LANN into ordinary point ANN search through dimension lifting substantially increases index construction and query costs, while direct search on a proximity graph built for ordinary point ANN search can miss distinct regions close to a line. To address these issues, we propose LinePG, which enhances an existing proximity graph with pair edges to facilitate navigation between separated near-line regions. To find these pair edges efficiently, we first generate region pairs with spatial or graph separation, and near a line. We then score edges between the selected region pairs to guide the point endpoint selections. We conduct extensive performance studies and confirm the accuracy and efficiency of LinePG in comparison with the baseline approaches.
