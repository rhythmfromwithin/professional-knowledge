---
interest: medium
link: https://arxiv.org/abs/2604.00317
next_step: skim
priority: medium
slack_ts: '1775270905.422809'
source: cs.DC - Distributed Computing
status: unread
title: 'From Skew to Symmetry: Node-Interconnect Multi-Path Balancing with Execution-time
  Planning for Modern GPU Clusters'
---
# From Skew to Symmetry: Node-Interconnect Multi-Path Balancing with Execution-time Planning for Modern GPU Clusters
> 原文: [https://arxiv.org/abs/2604.00317](https://arxiv.org/abs/2604.00317)

arXiv:2604.00317v1 Announce Type: new
Abstract: Modern GPU-based high-performance computing clusters offer unprecedented communication bandwidth through heterogeneous intra-node interconnects and inter-node networks. However, despite this high aggregate bandwidth, many real-world communication patterns fail to fully utilize the available hardware. Traffic skew often leads to situations where a small subset of links becomes oversaturated while others remain underutilized, resulting in congestion, latency spikes, and poor scalability. Existing communication frameworks such as NCCL and MPI with UCX typically rely on static fastest-path routing or hashing-based multi-rail striping, which leaves significant bandwidth unused when runtime traffic deviates from expected distributions. To address these limitations, we propose NIMBLE (Node-Interconnect Multi-path Balancing with Execution-time orchestration), a runtime communication orchestration system that dynamically redistributes traffic to balance link utilization across all available intra-node and inter-node paths. NIMBLE formulates this as a capacity-normalized minimum-congestion optimization problem and solves it efficiently using a multiplicative-weights algorithm. It further employs CUDA-aware GPU kernel-based RDMA pipelining to route traffic through intermediate GPUs and rail-matched NICs. The system is endpoint-driven, integrates transparently with existing communication libraries without requiring application changes, and preserves ordering, determinism, and low overhead. On H100-SXM4 nodes with fully connected NVLink and four NDR400 rails, NIMBLE achieves up to 2.3x higher intra-node bandwidth and 3.8x higher inter-node throughput compared to single-path baselines. It outperforms NCCL and MPI by up to 5.2x on skewed All-to-Allv workloads and 1.35x on end-to-end LLM MoE workloads, while matching baseline performance under balanced traffic.
