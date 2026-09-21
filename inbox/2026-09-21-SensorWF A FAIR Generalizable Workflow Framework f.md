---
title: "SensorWF: A FAIR Generalizable Workflow Framework for Scientific Time-Series Analysis"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2609.21110
priority: medium
status: unread
interest: medium
next_step: skim
---
# SensorWF: A FAIR Generalizable Workflow Framework for Scientific Time-Series Analysis
> 原文: [https://arxiv.org/abs/2609.21110](https://arxiv.org/abs/2609.21110)

arXiv:2609.21110v1 Announce Type: new
Abstract: Scientific sensor data is foundational across disciplines including spacecraft engineering, clinical medicine, and atmospheric science. In each context, pipelines are constructed to ingest raw archives, assess data quality, perform feature engineering and semantic annotation, and record provenance. However, these pipelines are often implemented as monolithic, domain-specific scripts with implicit assumptions and limited reusability across fields. This work introduces SensorWF, a FAIR-annotated workflow framework for generalizable scientific time-series analysis. The framework features a five-module reusable core (M1-M5) with typed input/output contracts. A domain adapter pattern isolates all domain-specific logic within M1, enabling modules M2-M5 to operate identically across disciplines. Domain assumptions are encoded in a machine-readable component registry, enabling reuse across sensor domains without modifying the analytical core. SensorWF also generates runtime PROV-O/ProvONE provenance traces with SHA-256 checksums for all file-path entities and emits SSN/SOSA-aligned OWL ontologies as primary outputs. To assess generalizability, SensorWF is instantiated in three distinct scientific domains: spacecraft telemetry, ambulatory ECG, and atmospheric climate, with synthetic fault injection and multi-detector anomaly detection demonstrated as use-case extensions. Results show that a single codebase, parameterized solely through M1 adapters of approximately 170-500 lines each, supports analytical pipelines across domains with varying sampling rates, channel counts, and fault taxonomies. All code, the component registry, ontology artifacts, and datasets are made available as an open scientific object. Our codebase is publicly available at https://purl.archive.org/sensor-wf.
