---
title: "Efficient Cost-Based Rewrite in a Bottom-Up Optimizer"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.05044
priority: low
status: unread
interest: medium
next_step: skim
---
# Efficient Cost-Based Rewrite in a Bottom-Up Optimizer
> 原文: [https://arxiv.org/abs/2605.05044](https://arxiv.org/abs/2605.05044)

arXiv:2605.05044v1 Announce Type: new
Abstract: The query optimizer in a Database Management Systems (DBMS), translates declarative queries into efficient execution plans. Conventional bottom-up optimization consists of two main stages: Query Rewrite (QRW) and Cost-Based Optimization (CBO). However, applying a rewrite rule during QRW may not always be beneficial; the best choice may depend on the (estimated) execution cost of the original and rewritten expressions. Fully exploiting such cost-dependent rules necessitates interleaving QRW with frequent CBO invocations, thereby incurring substantial overhead and often impractical optimization times. To mitigate this inefficiency, we introduce a novel cost-based rewrite framework for bottom-up optimizers. The core of our approach is a multi-level caching mechanism for intermediate CBO results aimed at eliminating redundant computation. Furthermore, we establish and exploit upper cost bounds to intelligently prune the search space during optimization. We also contribute methodological solutions for caching and reusing intermediate plan results within a bottom-up optimizer architecture. The framework has been implemented in the GaussDB optimizer. Experiments show that it significantly reduces overall optimization time, demonstrating the effectiveness of our approach.
