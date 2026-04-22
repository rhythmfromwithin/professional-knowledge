---
interest: medium
link: https://arxiv.org/abs/2604.16409
next_step: skim
priority: medium
slack_ts: '1776828614.038779'
source: cs.DC - Distributed Computing
status: unread
title: Scene-Aware Latency Estimation for Microservices via Multi-Scale Graph Fusion
---
# Scene-Aware Latency Estimation for Microservices via Multi-Scale Graph Fusion
> 原文: [https://arxiv.org/abs/2604.16409](https://arxiv.org/abs/2604.16409)

arXiv:2604.16409v1 Announce Type: new
Abstract: Cloud-Native microservice architectures have become prevalent owing to their inherent flexibility and scalability properties. To satisfy service quality guarantees, cloud providers must implement efficient proactive autoscaling algorithms. However, effective proactive scaling critically depends on accurately estimating end-to-end latency under given resource quotas, which remains highly challenging. Existing methods struggle with the multi-hierarchical nature and dynamic operational contexts of microservice systems. They primarily employ single-scale modeling that fails to capture inherent organizational structures and lacks adaptability to varying workload types. To address these limitations, we propose MSGAF, a Multi-Scale Graph Adaptive Fusion framework with Scene-Aware Learning for microservice latency estimation. Our approach constructs hierarchical graph representations through learnable aggregation-based coarsening, capturing system behaviors across microscopic, mesoscopic, and macroscopic levels. The framework comprises three components: a system state encoding module transforming heterogeneous monitoring data into unified representations, a multi-scale graph adaptive fusion module leveraging graph attention networks for hierarchical feature extraction, and a scene-aware learning module employing specialized expert networks with dynamic weight allocation for context-specific estimation. Additionally, we design and implement a comprehensive non-intrusive monitoring system for real-time data collection. Extensive experiments on benchmark microservice applications demonstrate that MSGAF significantly outperforms state-of-the-art methods across diverse operational scenarios, providing substantial improvements for cloud-native performance optimization.
