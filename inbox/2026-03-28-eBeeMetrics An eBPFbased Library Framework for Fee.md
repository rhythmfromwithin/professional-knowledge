---
title: "eBeeMetrics: An eBPF-based Library Framework for Feedback-free Observability of QoS Metrics"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.25067
priority: medium
status: unread
interest: medium
next_step: skim
---
# eBeeMetrics: An eBPF-based Library Framework for Feedback-free Observability of QoS Metrics
> 原文: [https://arxiv.org/abs/2603.25067](https://arxiv.org/abs/2603.25067)

arXiv:2603.25067v1 Announce Type: new
Abstract: Many system management runtimes (SMRs), such as resource management and power management techniques, rely on quality-of-service (QoS) metrics, such as tail latency or throughput, as feedback. These QoS metrics are generally neither observable with hardware performance counters nor directly observable within the OS kernel. This introduces complexity and overhead in instrumenting the application and integrating QoS performance metric feedback with many management runtimes. To bridge this gap, we introduced eBeeMetrics, an eBPF-based library framework to accurately observe application-level metrics derived from only eBPF-observable events, such as system calls. eBeeMetrics can be used as a drop-in replacement to decouple system management runtimes from QoS metric feedback reporting, or can supplement existing QoS metrics to better identify server-side dynamics. eBeeMetrics achieves a strong correlation with real-world measured throughput and latency metrics across various latency-sensitive workloads. The eBeeMetrics tool is open-source; the source code is available at: https://github.com/Ibnathism/eBeeMetrics.
