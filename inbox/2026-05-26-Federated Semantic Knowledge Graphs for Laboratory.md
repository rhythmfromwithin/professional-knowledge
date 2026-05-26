---
title: "Federated Semantic Knowledge Graphs for Laboratory Workflows: A Structured Expert Elicitation Methodology Demonstrated Through Bioanalytical Workflow Twins"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2605.23985
priority: low
status: unread
interest: medium
next_step: skim
---
# Federated Semantic Knowledge Graphs for Laboratory Workflows: A Structured Expert Elicitation Methodology Demonstrated Through Bioanalytical Workflow Twins
> 原文: [https://arxiv.org/abs/2605.23985](https://arxiv.org/abs/2605.23985)

arXiv:2605.23985v1 Announce Type: new
Abstract: Laboratory workflows in pharmaceutical and biomedical research encode substantial tacit knowledge -- expert judgment about failure conditions, decision branching logic, and contextual dependencies -- that remains inaccessible to protocol documents, sensor streams, and existing biomedical ontologies. We present a repeatable structured expert elicitation methodology and federated Semantic Knowledge Graph (SKG) architecture for capturing and querying this knowledge, demonstrated through deployment at the Biochemical and Cellular Pharmacology Department of Genentech. Knowledge is elicited via the Protocol Intelligence Co-pilot, a purpose-built AI interview agent that applies structured elicitation lenses to surface tacit procedural knowledge with expert-assigned confidence scores, producing graph representations across three tiers: program-level decision milestones, assay protocol knowledge, and physical execution infrastructure. Separately constructed subgraphs, exemplified by immunoassay (ELISA), quantitative mass spectrometry (LC-MS/PRM), and laboratory automation, are aligned through a shared upper ontology and queried as a single federated graph. Evaluation demonstrates seven query types structurally unavailable from any individual data source, including a cross-subgraph traversal that identifies automation-masked silent failures -- conditions where execution logs report success while scientific validity is compromised. Critically, the MASKED\_BY graph relationship encodes a class of laboratory risk invisible to current informatics platforms -- the structural gap that prevents existing systems from reasoning about scientific validity. This architecture provides the semantic world model that AI laboratory agents currently lack: a queryable representation of where workflows fail silently, where human judgment is irreplaceable, and which execution assets mask rather than detect failure.
