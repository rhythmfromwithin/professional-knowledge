---
interest: medium
link: https://arxiv.org/abs/2605.04256
next_step: skim
priority: medium
slack_ts: '1778385541.492129'
source: cs.DC - Distributed Computing
status: unread
title: 'phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks'
---
# phys-MCP: A Control Plane for Heterogeneous Physical Neural Networks
> 原文: [https://arxiv.org/abs/2605.04256](https://arxiv.org/abs/2605.04256)

arXiv:2605.04256v1 Announce Type: new
Abstract: Physical neural networks (PNNs) embed computation directly in material dynamics, including molecular, chemical, biological, photonic, memristive, and mechanical substrates. They are attractive for edge computing, especially at the extreme edge, where computation can be placed at the interface to sensing, actuation, or the physical process itself. However, PNNs are difficult to integrate into edge-cloud software stacks because each substrate exposes distinct interfaces, timing behavior, observability limits, and lifecycle requirements. This paper argues that the missing systems component is a common control plane for heterogeneous PNNs. We present phys-MCP, a substrate-aware orchestration architecture that exposes physical neural substrates as discoverable and invocable resources for edge, fog, and cloud workflows, while preserving their possible placement at the extreme edge. phys-MCP defines a capability model, lifecycle semantics, telemetry interfaces, and digital-twin bindings that retain substrate-specific properties such as latency, resetability, plasticity, and I/O modality. We instantiate the architecture through a prototype with three representative backend classes, an HTTP-backed execution path, and an integrated Cortical Labs adapter exposing a wetware-facing API path through the same control model. The evaluation combines controlled experiments on representative backends with end-to-end validation of the Cortical Labs path. Results show descriptor-portable integration across heterogeneous backends, improved runtime-aware matching over simpler baselines, telemetry-aware recovery under representative faults, successful execution against the API-backed wetware path, and small local control-path overhead. Overall, results provide prototype-level evidence that substrate-aware control can span heterogeneous physical AI resources, twin-backed backends, and a wetware-facing API path.
