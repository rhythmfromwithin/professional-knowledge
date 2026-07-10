---
title: "Seekable OCI: Lazy-Loading Container Images via Range-Request Indexing"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.06868
priority: medium
status: unread
interest: medium
next_step: skim
---
# Seekable OCI: Lazy-Loading Container Images via Range-Request Indexing
> 原文: [https://arxiv.org/abs/2607.06868](https://arxiv.org/abs/2607.06868)

arXiv:2607.06868v1 Announce Type: new
Abstract: Container image pulling accounts for the majority of pod startup time in Kubernetes environments. Standard pull downloads the entire image before the container can start, even when the application accesses only a fraction of the image content at startup. We present SOCI (Seekable OCI), a lazy-loading architecture that enables containers to start without downloading the full image. SOCI builds an external index over standard OCI images, mapping files to byte ranges within compressed layers. At runtime, a FUSE filesystem intercepts file accesses and serves them via HTTP range requests. Unlike prior approaches that require image format conversion, SOCI works with unmodified images and standard registries. The index is stored as an OCI referrer artifact, requiring no changes to images, registries, or deployment tooling. On a 1.3 GB Python web service image, SOCI reduces cold-start pull time from 20 seconds to approximately 2.8 seconds (7.4x speedup), with pull time independent of image size. Larger images see larger speedups (9.3x on a 2.5 GB image) because SOCI pull time is constant while standard pull scales linearly. We measure a crossover at 80% access density: below this, lazy loading wins; above, parallel full pull is faster. SOCI lazy loading is deployed in production on Amazon EKS and Amazon ECS Fargate (which launched 18.4 million tasks per day during Prime Day 2025), and has been serving lazy-load requests since 2023. EKS Auto Mode uses SOCI's parallel pull mode for GPU instances.
