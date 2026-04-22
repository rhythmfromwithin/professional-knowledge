---
title: "CrossTraffic: An Open-Source Framework for Reproducible and Executable Transportation Analysis and Knowledge Management"
source: "cs.CY - Computers and Society"
link: https://arxiv.org/abs/2604.16316
priority: medium
status: unread
interest: medium
next_step: skim
---
# CrossTraffic: An Open-Source Framework for Reproducible and Executable Transportation Analysis and Knowledge Management
> 原文: [https://arxiv.org/abs/2604.16316](https://arxiv.org/abs/2604.16316)

arXiv:2604.16316v1 Announce Type: new
Abstract: Transportation engineering often relies on technical manuals and analytical tools for planning, design, and operations. However, the dissemination and management of these methodologies, such as those defined in the Highway Capacity Manual (HCM), remain fragmented. Computational procedures are often embedded within proprietary tools, updates are inconsistently propagated across platforms, and knowledge transfer is limited. These challenges hinder reproducibility, interoperability, and collaborative advancement in transportation analysis.
This paper introduces CrossTraffic, an open-source framework that treats transportation methodologies and regulatory knowledge as continuously deployable and verifiable software infrastructure. CrossTraffic provides an executable computational core for transportation analysis with cross-platform access through standardized interfaces. An ontology-driven knowledge graph encodes engineering rules and provenance and serves as a semantic validation layer for analytical workflows. A conversational interface further connects large language models to this validated execution environment through structured tool invocation, enabling natural-language access while preventing procedurally invalid analyses.
Experimental results show that knowledge-graph-constrained execution substantially improves numerical accuracy and methodological fidelity compared with context-only approaches, achieving near-zero numerical error (MAE<0.50) across multiple large language models and perfect detection of invalid analytical inputs in stress testing (F1~=~1.0). Its modular architecture supports the integration of additional transportation manuals and research models, providing a foundation for an open and collaborative transportation science ecosystem with a reproducible computational core. The system implementation is publicly available at https://github.com/crosstraffic.
