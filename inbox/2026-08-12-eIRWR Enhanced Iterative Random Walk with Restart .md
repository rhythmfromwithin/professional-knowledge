---
title: "eIRWR: Enhanced Iterative Random Walk with Restart for Scalable Root Cause Analysis in Microservices"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.08073
priority: medium
status: unread
interest: medium
next_step: skim
---
# eIRWR: Enhanced Iterative Random Walk with Restart for Scalable Root Cause Analysis in Microservices
> 原文: [https://arxiv.org/abs/2608.08073](https://arxiv.org/abs/2608.08073)

arXiv:2608.08073v1 Announce Type: new
Abstract: Root cause analysis (RCA) in microservice architectures needs to pinpoint the originating faulty service responsible for the cascading symptoms seen across hundreds or thousands of interdependent services. Graph-based random walk methods propagate anomaly evidence over the service dependency graph. However, existing anomaly-restart walks leave much of the localization signal unused: they restart from the raw anomaly vector, which is dominated by loud downstream victims rather than the quieter source. Through a controlled ablation, we first show that the "resilience damping" often applied to the transition matrix is mathematically equivalent to raising the restart probability; we therefore benchmark against a restart-tuned Personalized PageRank (PPR) rather than its default configuration. We then present Enhanced Iterative Random Walk with Restart (eIRWR), which (a) concentrates restart mass on the most suspicious nodes through power-law teleportation sharpening, (b) augments the transition matrix with self-loops and backward edges so that probability accumulates at cascade sources, and (c) refines its belief across an outer loop. On three large-scale topologies (12K-25K nodes) from the Alibaba Microservice Trace Dataset, eIRWR attains a Mean Reciprocal Rank (MRR) of 0.75 at moderate root-cause visibility, a 2.8 times improvement over the best aggregate-metric baseline and well above a restart-tuned PPR. At high visibility, it reaches MRR= 0.94, while running in under 25ms on graphs with 17,000 nodes, making it suitable for online deployment.
