---
title: "Extracting ODRL Policies from Business Process Models: A Graph Traversal Approach to Compliance-by-Extraction"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2608.02607
priority: low
status: unread
interest: medium
next_step: skim
---
# Extracting ODRL Policies from Business Process Models: A Graph Traversal Approach to Compliance-by-Extraction
> 原文: [https://arxiv.org/abs/2608.02607](https://arxiv.org/abs/2608.02607)

arXiv:2608.02607v1 Announce Type: new
Abstract: Organisations maintain large corpora of process models expressed in the Business Process Model and Notation (BPMN), yet the normative content encoded in those models, the obligations, permissions, and prohibitions that govern participant behaviour, remains inaccessible to policy infrastructure. The Open Digital Rights Language (ODRL) is the emerging lingua franca of machine-readable policy, but authoring ODRL at scale is slow, expert-intensive work, and generation by large language models introduces well-documented risks of structural invalidity. We present a pipeline that resolves this gap by extracting ODRL policies automatically from BPMN XML, grounded in the observation that BPMN control flow encodes deontic modalities by construction. The pipeline traverses the BPMN process graph, classifies each task as an odrl:Duty or odrl:Permission via a reachability check, and introduces a novel treatment of intermediate catch events as odrl:Prohibition rules with lifting constraints, capturing waiting semantics that prior approaches have dropped. The result is a compliance-by-extraction approach in which auditable, interoperable ODRL policies are derived directly from the process models organisations already maintain. The implementation and a live demonstration are available at https://github.com/manabcodes/bpmn2odrl and https://bpmn.linkeddata.es/.
