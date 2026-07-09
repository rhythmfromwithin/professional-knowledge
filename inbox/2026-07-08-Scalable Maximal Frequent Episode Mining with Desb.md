---
interest: medium
link: https://arxiv.org/abs/2607.03188
next_step: skim
priority: low
slack_ts: '1783569518.348609'
source: cs.DB - Databases
status: unread
title: Scalable Maximal Frequent Episode Mining with Desbordante
---
# Scalable Maximal Frequent Episode Mining with Desbordante
> 原文: [https://arxiv.org/abs/2607.03188](https://arxiv.org/abs/2607.03188)

arXiv:2607.03188v1 Announce Type: new
Abstract: Episode mining aims to extract subsequences of events that possess certain distinctive properties and constitute facts valuable to the user. Maximal frequent episode mining concentrates on discovery of frequently-appearing subsequences, which are not included into any other larger frequent subsequence. The state-of-the-art for this problem is the MaxFEM algorithm which enumerates possible subsequences, while applying various pruning techniques to accelerate the search. However, this is a computationally-intensive problem: reducing the minimum number of required subsequence occurrences or increasing the length of the subsequence both substantially raise running time, which limits practical use of MaxFEM. In this paper we describe our efforts in designing a high-performing algorithm for this problem. For this we: 1) develop an efficient C++ implementation of MaxFEM, and 2) devise an efficient technique to parallelizing it. As the result, we propose an improved parallel MaxFEM variant, which we call ParMaxFEM. Additionally, we integrate the improved algorithm into Desbordante - a high-performance, open-source data profiler with deep Python integration that treats patterns as first-class entities and allows users to develop their custom programs that can include discovery and validation of patterns. To evaluate our approach we compare both C++ implementations with the original SPMF implementation. Experiments demonstrated that our reimplemented version provides up to $8\times$ speedup over the SPMF baseline, while our parallelization technique provides up to $35\times$ improvement overall (on 8 cores).
