---
interest: medium
link: https://arxiv.org/abs/2603.24736
next_step: skim
priority: high
slack_ts: '1774666227.135699'
source: cs.AI - Artificial Intelligence
status: unread
title: 'AutoSAM: an Agentic Framework for Automating Input File Generation for the
  SAM Code with Multi-Modal Retrieval-Augmented Generation'
---
# AutoSAM: an Agentic Framework for Automating Input File Generation for the SAM Code with Multi-Modal Retrieval-Augmented Generation
> 原文: [https://arxiv.org/abs/2603.24736](https://arxiv.org/abs/2603.24736)

arXiv:2603.24736v1 Announce Type: new
Abstract: In the design and safety analysis of advanced reactor systems, constructing input files for system-level thermal-hydraulics codes such as the System Analysis Module (SAM) remains a labor-intensive task. Analysts must extract and reconcile design data from heterogeneous engineering documents and manually translate it into solver-specific syntax. In this paper, we present AutoSAM, an agentic framework that automates SAM input file generation. The framework combines a large language model agent with retrieval-augmented generation over the solver's user guide and theory manual, together with specialized tools for analyzing PDFs, images, spreadsheets, and text files. AutoSAM ingests unstructured engineering documents, including system diagrams, design reports, and data tables, extracts simulation-relevant parameters into a human-auditable intermediate representation, and synthesizes validated, solver-compatible input decks. Its multimodal retrieval pipeline integrates scientific text extraction, vision-based figure interpretation, semantic embedding, and query answering. We evaluate AutoSAM on four case studies of increasing complexity: a single-pipe steady-state model, a solid-fuel channel with temperature reactivity feedback, the Advanced Burner Test Reactor core, and the Molten Salt Reactor Experiment primary loop. Across all cases, the agent produces runnable SAM models consistent with expected thermal-hydraulic behavior while explicitly identifying missing data and labeling assumed values. The framework achieves 100% utilization of structured inputs, about 88% extraction from PDF text, and 100% completeness in vision-based geometric extraction. These results demonstrate a practical path toward prompt-driven reactor modeling, in which analysts provide system descriptions and supporting documentation while the agent translates them into transparent, and executable, SAM simulations.
