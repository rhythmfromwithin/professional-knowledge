---
interest: medium
link: https://arxiv.org/abs/2608.02608
next_step: skim
priority: medium
slack_ts: '1786154698.275769'
source: cs.DC - Distributed Computing
status: unread
title: 'Separating Intelligence from Inference: A Standard for Edge-Native AI Computing'
---
# Separating Intelligence from Inference: A Standard for Edge-Native AI Computing
> 原文: [https://arxiv.org/abs/2608.02608](https://arxiv.org/abs/2608.02608)

arXiv:2608.02608v1 Announce Type: new
Abstract: The artificial intelligence industry has constructed a USD 300 billion centralized data center infrastructure to serve a workload, large language model inference, that does not architecturally require centralization. This paper articulates the central architectural inefficiency of contemporary AI infrastructure: the conflation of model training (irreducibly centralized, capital-intensive, one-time per model version) with model inference (parallelizable, latency-sensitive, recurring per query) on the same physical hardware. We propose the separation principle: intelligence is trained centrally and shipped as software; inference executes on hardware near the data source, at the edge. We quantify the energy implications at civilizational scale and show that a fully edge-resident inference architecture for one billion daily users saves approximately 19 TWh per year and 7.3 megatons of CO2 annually relative to current centralized practice. We specify two new device classes, the Personal AI Computer (PAC) and the Corporate AI Workstation (CAW), with concrete hardware tiers, memory bandwidth requirements, thermal envelopes, and software interfaces. We then describe a reference architectural stack of eight components addressing weight distribution, sovereignty-aware routing, thermal-adaptive quantization, multi-tenant resource management, federated network inference, cryptographic provenance, privacy-preserving telemetry, and distributed context window extension. Several components are the subject of pending United States patent applications by the first author and are presented here as candidate open architectural principles
