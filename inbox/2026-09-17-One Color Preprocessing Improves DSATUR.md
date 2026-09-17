---
title: "One Color Preprocessing Improves DSATUR"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2609.17633
priority: high
status: unread
interest: medium
next_step: skim
---
# One Color Preprocessing Improves DSATUR
> 原文: [https://arxiv.org/abs/2609.17633](https://arxiv.org/abs/2609.17633)

arXiv:2609.17633v1 Announce Type: new
Abstract: The Graph Coloring Problem (GCP) is NP-hard and DSATUR stands as one of the fastest heuristics for it despite producing colorings that typically use more colors than state-of-the-art coloring algorithms. We propose SSLD (Semidefinite Spectral Learning with DSATUR), which improves DSATUR by preprocessing a first good color class before letting DSATUR complete coloring the rest of the given graph. We obtain this color class from a Semidefinite Programming (SDP), similar to an SDP used to compute the Lov\'asz theta number. To the best of our knowledge, SSLD is the first approach to improve DSATUR by preprocessing through fixed color classes. We evaluate SSLD against DSATUR and against a naive 1-color-class preprocessing algorithm on DIMACS instances, random graphs (Erd\H{o}s--R\'enyi, Watts-Strogatz, Barab\'asi--Albert), Frequency Assignment and Job Shop Scheduling instances. SSLD matches or beats DSATUR in almost every case across over 1600 benchmark instances, and out performs the naive GISD baseline, allows us to confirm the value brought by the SDP-guided choice of the first color class. This quality comes at a runtime cost of roughly 195 times slower that DSATUR, but demonstrating that SDP-guided preprocessing of a first color class is a direction for future improvements.
