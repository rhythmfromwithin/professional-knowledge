---
interest: medium
link: https://arxiv.org/abs/2608.11402
next_step: skim
priority: medium
slack_ts: '1786674578.868689'
source: cs.DC - Distributed Computing
status: unread
title: An Event-Driven Cloud-Native Wearable Analytics Framework for Real-Time Clinical
  Workloads
---
# An Event-Driven Cloud-Native Wearable Analytics Framework for Real-Time Clinical Workloads
> 原文: [https://arxiv.org/abs/2608.11402](https://arxiv.org/abs/2608.11402)

arXiv:2608.11402v1 Announce Type: new
Abstract: Continuous physiological monitoring using consumer-grade wearables offers a transformative opportunity for clinical care and research, yet integration remains hindered by device heterogeneity, proprietary data formats, and strict regulatory requirements. We present an event-driven, cloud-native system designed to ingest, normalize, and analyze high-frequency vital signs from wearables at scale and without vendor lock-in. The system design proposes a multi-layered microservice architecture using cluster orchestration. Data acquisition is handled via a cross-platform mobile application that leverages native health frameworks, ensuring compatibility across fragmented device ecosystems. To address interoperability, we implement an event-driven transformation pipeline using stream processing engines and specialized services to map raw measurements to the FHIR standard for medical interoperability. Our novel dependency-aware FHIR minimization scheme reduces storage overhead while maintaining lossless resource reconstruction. Furthermore, the platform integrates a modular data analytics and machine learning layer based on a medallion lakehouse architecture, supporting the full machine learning lifecycle from real-time stream processing to model serving. Performance evaluation demonstrates that the ingestion pipeline sustains 50 full ingestion requests per second with median response times under 8 ms, satisfying the low-latency requirements for real-time patient monitoring. Our open-source implementation adheres to regulatory compliance standards through role-based access control and secure service-to-service communication, providing a robust foundation for deploying wearable-based monitoring in institutional healthcare settings for clinical decision support and research workloads.
