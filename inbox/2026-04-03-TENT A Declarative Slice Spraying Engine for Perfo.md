---
title: "TENT: A Declarative Slice Spraying Engine for Performant and Resilient Data Movement in Disaggregated LLM Serving"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.00368
priority: medium
status: unread
interest: medium
next_step: skim
---
# TENT: A Declarative Slice Spraying Engine for Performant and Resilient Data Movement in Disaggregated LLM Serving
> 原文: [https://arxiv.org/abs/2604.00368](https://arxiv.org/abs/2604.00368)

arXiv:2604.00368v1 Announce Type: new
Abstract: Modern GPU clusters are built upon a complex hierarchy of heterogeneous interconnects, ranging from multi-rail RDMA to proprietary fabrics such as Multi-Node NVLink and Ascend UB. Orchestrating these diverse links effectively remains a critical challenge in disaggregated LLM serving. Operating Mooncake TE on thousands of GPUs exposed a critical limitation shared by existing frameworks: imperative, statically bound path selection. This rigidity forces engines to rely on state-blind striping that ignores congestion signals, creating communication silos, wasting multi-rail bandwidth due to head-of-line blocking, and leading to operational fragility where routine faults require manual intervention. We present TENT, a data-movement engine that decouples transfer intent from physical execution. Instead of locking workloads to fixed backends, TENT unifies heterogeneous interconnects into a single dynamic resource pool. Applications simply declare transfer intents, while TENT dynamically decomposes elephant flows into fine-grained slices and "sprays" them across links based on instantaneous link quality. This telemetry-driven orchestration eliminates head-of-line blocking and enables transparent, sub-50 ms self-healing by rerouting slices around failures without application logic. TENT serves as the production data plane for LLM inference and RL pipelines at multiple industrial sites. Our evaluation on H800 HGX clusters shows that TENT outperforms state-of-the-art baselines, including Mooncake TE, NIXL, and UCCL. In LLM inference with SGLang HiCache, TENT achieves up to 1.36x higher throughput and 26% lower P90 TTFT than Mooncake TE. In RL pipelines, TENT accelerates parameter updates in Moonshot Checkpoint Engine by 20-26%.
