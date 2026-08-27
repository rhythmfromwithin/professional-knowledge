---
title: "Analyzing and Reducing Search Quality Differences in Vector Similarity Search"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.25185
priority: low
status: unread
interest: medium
next_step: skim
---
# Analyzing and Reducing Search Quality Differences in Vector Similarity Search
> 原文: [https://arxiv.org/abs/2608.25185](https://arxiv.org/abs/2608.25185)

arXiv:2608.25185v1 Announce Type: new
Abstract: Modern database services scalably search over large data collections via Approximate Nearest Neighbor Search, which improves search performance at the cost of search quality, measured by recall. In practice, a database operator seeks to achieve a target mean recall while maximizing throughput across search queries. We show that optimizing for mean recall masks significant differences in recall across queries even when target recall is met. As a result, numerous queries face (1) below-target recall, hurting user experience and revenue and (2) above-target recall, wasting computation to deliver unnecessarily high search quality. Thus, it is critical to detect and reduce recall differences across queries. We design RCheck, a light-weight run-time system that identifies low-recall queries and reduces recall differences while achieving high throughput. RCheck's key design principle is to dynamically, efficiently adapt search effort by increasing effort for queries below target recall and decreasing effort for those above it. RCheck tunes available search effort parameters, making it readily deployable. We evaluate RCheck using the widely-used production-style pgvector database. At the same throughput, RCheck improves mean recall by 11-93% and enables 8-47% more queries to meet target recall compared to the state-of-the-art globally-tuned configuration.
