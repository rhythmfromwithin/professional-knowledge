---
title: "GitFarm: Git as a Service for Large-Scale Monorepos"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2604.11977
priority: low
status: unread
interest: medium
next_step: skim
---
# GitFarm: Git as a Service for Large-Scale Monorepos
> 原文: [https://arxiv.org/abs/2604.11977](https://arxiv.org/abs/2604.11977)

arXiv:2604.11977v1 Announce Type: new
Abstract: At the scale of Uber's monorepos, traditional Git workflows become a fundamental bottleneck. Cloning multi-gigabyte repositories, maintaining local checkouts, periodically syncing from upstream, and executing repetitive fetch or push operations consume substantial compute and I/O across hundreds of automation systems. Although CI (Continuous Integration) systems such as Jenkins and Buildkite provide caching mechanisms to reduce clone times, in practice, these approaches incur significant infrastructure overhead, manual maintenance, inconsistent cache hit rates, and cold start latencies of several minutes for large monorepos. Moreover, thousands of independent clone and fetch operations add heavy load on upstream Git servers, making them slow and difficult to scale. To address these limitations, we present GitFarm, a platform that provides Git as a stateful, identity-scoped, repository-centric execution service through a gRPC API. GitFarm decouples repository management from clients by executing Git operations remotely within secure, ephemeral sandboxes backed by pre-warmed repositories. The system enforces identity-scoped authorization, supports multi-command workflows, and leverages specialized backend clusters for workload isolation. For clients, this design eliminates local clones, provides a ready-to-use checkout in less than a second, and significantly lowers client-side compute and I/O overhead by offloading operations to GitFarm. Also, client services no longer experience cold starts (up to 15 minutes) due to initial clones of the monorepos on each host. The results demonstrate that Git as a service provides substantial performance and cost benefits, while preserving the flexibility of native Git semantics.
