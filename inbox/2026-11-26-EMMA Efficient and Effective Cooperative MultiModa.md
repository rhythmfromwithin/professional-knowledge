---
title: "EMMA: Efficient and Effective Cooperative Multi-Modal Analytics over Embodied AI Data"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2611.33765
priority: low
status: unread
interest: medium
next_step: skim
---
# EMMA: Efficient and Effective Cooperative Multi-Modal Analytics over Embodied AI Data
> 原文: [https://arxiv.org/abs/2611.33765](https://arxiv.org/abs/2611.33765)

arXiv:2611.33765v1 Announce Type: new
Abstract: Embodied AI has seen growing real-world deployment, particularly in autonomous vehicles and robots. These vehicles and robots continuously capture large collections of multi-modal data, such as video, LiDAR point clouds, and GPS trajectories. Historical collections of these data support model improvement and safety assessment through scene retrieval, object trajectory extraction, and corresponding analysis. Processing such analytical queries is challenging because answering them may require combining information from different modalities and observations captured by different moving vehicles or robots, while extracting that information with deep models at every scene incurs prohibitive cost. We present EMMA, an operator-oriented query-processing framework for embodied AI data. EMMA compiles analytical queries into composable operators and executes them on demand. To support accurate query evaluation, EMMA performs modality-aware staged predicate evaluation and selectively combines overlapping observations. To reduce query cost, EMMA uses a temporal co-location index to identify joint-analysis candidates, adaptive scene skipping to reduce model calls, and a shared world store to reuse extracted information across operators and queries. EMMA trains execution policies offline and deploys them as plug-ins. Based on lightweight observations, these policies determine whether the current scene is analyzed independently or jointly and how many subsequent scenes can be safely skipped, balancing analytical accuracy and execution cost. Experiments show that EMMA substantially reduces query execution cost while preserving query accuracy.
