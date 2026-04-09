---
interest: medium
link: https://arxiv.org/abs/2604.03927
next_step: skim
priority: low
slack_ts: '1775703389.626539'
source: cs.DB - Databases
status: unread
title: Version Control System for Data with MatrixOne
---
# Version Control System for Data with MatrixOne
> 原文: [https://arxiv.org/abs/2604.03927](https://arxiv.org/abs/2604.03927)

arXiv:2604.03927v1 Announce Type: new
Abstract: The rapid advancement of artificial intelligence has elevated data to a cornerstone of modern software systems. As data projects become increasingly complex and dynamic, version control for data has become essential rather than merely convenient. Existing version control systems designed for source code are inadequate for large-scale data management, as they often require loading entire datasets into memory for diff and merge operations. Database systems, while providing robust data management capabilities, lack native support for version control operations such as diff and merge between data forks. We present a version control system for data implemented in MatrixOne, a cloud-native relational database system. Our system leverages MatrixOne's immutable storage architecture and multi-version concurrency control (MVCC) to enable git-like operations on database tables at scale. The system supports the complete spectrum of version control operations: clone, tag/branch, diff, merge, and revert, on terabyte-scale datasets with near-instantaneous performance. This version control system enables data engineers to adopt established software engineering workflows: creating branches for isolated experimentation, submitting pull requests for change review, and running CI/CD pipelines efficiently and safely. Changes in the development environment are isolated from production in both data integrity and computing resources. Verified changes can be published to production in atomic transactions, ensuring data consistency and avoiding service disruptions.
