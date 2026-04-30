---
title: "Versioned Late Materialization for Ultra-Long Sequence Training in Recommendation Systems at Scale"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.24806
priority: low
status: unread
interest: medium
next_step: skim
---
# Versioned Late Materialization for Ultra-Long Sequence Training in Recommendation Systems at Scale
> 原文: [https://arxiv.org/abs/2604.24806](https://arxiv.org/abs/2604.24806)

arXiv:2604.24806v1 Announce Type: cross
Abstract: Modern Deep Learning Recommendation Models (DLRMs) follow scaling laws with sequence length, driving the frontier toward ultra-long User Interaction History (UIH). However, the industry-standard "Fat Row" paradigm, which pre-materializes these sequences into every training example, creates a storage and I/O wall where data infrastructure usage exceeds GPU training capacity due to data redundancy that is amplified in multi-tenant environments where models with vastly different sequence length requirements share a union dataset. We present a \emph{versioned late materialization} paradigm that eliminates this redundancy by storing UIH once in a normalized, immutable tier and reconstructing sequences just-in-time during training via lightweight versioned pointers. The system ensures Online-to-Offline (O2O) consistency through a bifurcated protocol that prevents future leakage across both streaming and batch training, while a read-optimized immutable storage layer provides multi-dimensional projection pushdown for heterogeneous model tenants. Disaggregated data preprocessing with pipelined I/O prefetching and data-affinity optimizations masks the latency of training-time sequence reconstruction, keeping training throughput compute-bound by GPUs. Deployed on production DLRMs, the system reduces training data infrastructure resource usage while enabling aggressive sequence length scaling that delivers significant model quality gains, serving as the foundational data infrastructure for modern recommendation model architectures, including HSTU and ULTRA-HSTU.
