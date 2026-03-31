---
title: "Semi-Automated Knowledge Engineering and Process Mapping for Total Airport Management"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2603.26076
priority: high
status: unread
interest: medium
next_step: skim
---
# Semi-Automated Knowledge Engineering and Process Mapping for Total Airport Management
> 原文: [https://arxiv.org/abs/2603.26076](https://arxiv.org/abs/2603.26076)

arXiv:2603.26076v1 Announce Type: new
Abstract: Documentation of airport operations is inherently complex due to extensive technical terminology, rigorous regulations, proprietary regional information, and fragmented communication across multiple stakeholders. The resulting data silos and semantic inconsistencies present a significant impediment to the Total Airport Management (TAM) initiative. This paper presents a methodological framework for constructing a domain-grounded, machine-readable Knowledge Graph (KG) through a dual-stage fusion of symbolic Knowledge Engineering (KE) and generative Large Language Models (LLMs).
The framework employs a scaffolded fusion strategy in which expert-curated KE structures guide LLM prompts to facilitate the discovery of semantically aligned knowledge triples. We evaluate this methodology on the Google LangExtract library and investigate the impact of context window utilization by comparing localized segment-based inference with document-level processing. Contrary to prior empirical observations of long-context degradation in LLMs, document-level processing improves the recovery of non-linear procedural dependencies.
To ensure the high-fidelity provenance required in airport operations, the proposed framework fuses a probabilistic model for discovery and a deterministic algorithm for anchoring every extraction to its ground source. This ensures absolute traceability and verifiability, bridging the gap between "black-box" generative outputs and the transparency required for operational tooling. Finally, we introduce an automated framework that operationalizes this pipeline to synthesize complex operational workflows from unstructured textual corpora.
