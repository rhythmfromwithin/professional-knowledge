---
interest: medium
link: https://arxiv.org/abs/2606.04415
next_step: skim
priority: medium
slack_ts: '1780633553.336919'
source: cs.DC - Distributed Computing
status: unread
title: 'FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location'
---
# FlexNPU: Transparent NPU Virtualization for Dynamic LLM Prefill-Decode Co-location
> 原文: [https://arxiv.org/abs/2606.04415](https://arxiv.org/abs/2606.04415)

arXiv:2606.04415v1 Announce Type: new
Abstract: Modern AI serving increasingly relies on NPUs for conventional inference and large language model serving. However, current NPU deployments commonly expose physical devices directly to applications, which limits runtime control over scheduling and makes it difficult to adapt execution to phase-level workload behavior. This limitation is particularly evident in LLM serving, where the prefill phase is compute-intensive while the decode phase is often constrained by memory bandwidth and KV-cache accesses. Static prefill-decode (PD) disaggregation reduces phase interference, but can introduce resource imbalance and unnecessary data movement. We present FlexNPU, a transparent user-space virtualization layer for Ascend NPUs. FlexNPU interposes on AscendCL APIs and routes NPU operations through per-device daemons, decoupling unmodified from physical NPU devices without modifying model code, AI frameworks, or NPU drivers. This runtime boundary allows FlexNPU to virtualize NPU objects, control operator dispatch, and support phase-aware scheduling for LLM serving. In particular, FlexNPU enables dynamic PD co-location, which adapts scheduling between prefill and decode according to their complementary resource characteristics. We implement FlexNPU on Huawei Ascend NPUs and evaluate it with typical LLM workloads. Compared with direct NPU passthrough, FlexNPU introduces no measurable inference overhead and slightly improves throughput in some scenarios. On a 384-card Ascend 910C deployment of DeepSeek-R1, FlexNPU improves throughput over static PD disaggregation by 5.15% and 26.33%. On Qwen2.5-7B, compared with static PD co-location, FlexNPU maintains comparable throughput while reducing TTFT by over 92% across tested workloads with nearly unchanged TPOT. These results show that transparent NPU virtualization is a practical substrate for efficient and responsive LLM serving.
