---
title: "SWARM-LLM: Collaborative Inference for Edge-based Small Language Models"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2606.14711
priority: medium
status: unread
interest: medium
next_step: skim
---
# SWARM-LLM: Collaborative Inference for Edge-based Small Language Models
> 原文: [https://arxiv.org/abs/2606.14711](https://arxiv.org/abs/2606.14711)

arXiv:2606.14711v1 Announce Type: new
Abstract: Large language models (LLMs) provide strong performance across a wide range of tasks but are typically hosted on centralised cloud infrastructure, incurring significant bandwidth, latency, and privacy costs. In contrast, small language models (SLMs) can run on edge devices but have limited capability and robustness. This paper introduces SWARM-LLM, a routing and collaboration layer that coordinates a small swarm of edge-hosted SLMs with an optional cloud foundation model (FM). SWARM-LLM decides, for each query, whether to answer locally, collaborate with peer SLMs, or "summon" a cloud FM, using lightweight uncertainty estimates and safety signals. We implement a working prototype on commodity hardware with three heterogeneous SLMs and a 70B-parameter cloud FM accessed via API, and evaluate it on a controlled study workload of easy, hard, and safety-oriented queries. Our results show that SWARM-LLM substantially improves performance on hard questions compared to an edge-only deployment, while limiting cloud usage to roughly one quarter of queries, illustrating a practical trade-off between accuracy, latency, and cost for privacy-conscious edge deployments. The implementation code is available at the GitHub repository https://github.com/mdahshan/swarm\_llm.
