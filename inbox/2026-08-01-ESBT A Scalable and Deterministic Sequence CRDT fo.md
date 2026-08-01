---
title: "ESBT: A Scalable and Deterministic Sequence CRDT for Distributed Collaborative Editing"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.28101
priority: medium
status: unread
interest: medium
next_step: skim
---
# ESBT: A Scalable and Deterministic Sequence CRDT for Distributed Collaborative Editing
> 原文: [https://arxiv.org/abs/2607.28101](https://arxiv.org/abs/2607.28101)

arXiv:2607.28101v1 Announce Type: new
Abstract: Modern collaborative editing systems require efficient mechanisms for managing concurrent updates across distributed replicas. Sequence Conflict-free Replicated Data Types (CRDTs) have become the de facto standard for supporting decentralized collaboration; they enable decentralized replicas to apply operations in arbitrary order while converging to a common state. Although existing sequence CRDTs guarantee Strong Eventual Consistency (SEC), they often suffer from uncontrolled identifier growth and increasing memory consumption during long-running, highly concurrent editing sessions, which severely limits their scalability and performance. This paper presents the Extended Stern-Brocot Tree (ESBT), a mathematically grounded identifier allocation scheme for distributed collaborative text editing, providing a dense, deterministic, and compact identifier space. The proposed allocation strategy bounds identifier growth while preserving deterministic ordering and Strong Eventual Consistency. Experimental evaluation using workloads of up to 100,000 concurrent operations generated across 50 collaborating sites shows that ESBT improves responsiveness by 28 to 88% under pure insertions and 59 to 74% under mixed insertion/deletion workloads, while reducing identifier memory consumption by 50 to 75% in beginning and random insertion patterns compared with the best-performing baseline sequence CRDTs (Logoot and LSEQ). Under the adversarial middle-insertion workload (10,000 operations), ESBT further improves responsiveness by 86.53% and reduces identifier size by 92.81%. These results demonstrate that ESBT effectively addresses the principal scalability limitations of existing sequence CRDTs and provides an efficient and scalable foundation for large-scale collaborative editing systems.
