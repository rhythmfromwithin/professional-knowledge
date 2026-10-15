---
interest: medium
link: https://arxiv.org/abs/2604.08552
next_step: skim
priority: low
slack_ts: '1792037689.661469'
source: cs.DB - Databases
status: unread
title: Automated Standardization of Legacy Biomedical Metadata Using an Ontology-Constrained
  LLM Agent
---
# Automated Standardization of Legacy Biomedical Metadata Using an Ontology-Constrained LLM Agent
> 原文: [https://arxiv.org/abs/2604.08552](https://arxiv.org/abs/2604.08552)

arXiv:2604.08552v4 Announce Type: replace
Abstract: Descriptive scientific metadata in public repositories are often incomplete and inconsistent with community standards and ontologies, limiting data FAIRness. Large language models (LLMs) offer a promising approach to automatically standardizing such metadata when the LLM is provided with knowledge of the relevant standards in machine-actionable form (e.g., as metadata templates from systems such as the CEDAR Workbench). Entry of metadata standards through prompt engineering offers only fixed snapshots of the relevant standards, however, and it relies on an LLM's pretrained knowledge to interpret and satisfy constraints related to the standard. We evaluate whether giving an LLM access to metadata specifications and authoritative terminology at runtime improves automated metadata standardization. We present ARMS, a tool-augmented LLM agent that retrieves complete CEDAR metadata templates and dynamically queries authoritative biomedical terminology services at execution time. We compared ARMS with a prompt-based approach on 839 legacy metadata records from the Human BioMolecular Atlas Program (HuBMAP), using expert-standardized records as the reference standard. ARMS outperformed the prompt-based approach, increasing precision from 0.56 to 0.93 and recall from 0.51 to 0.85, with improvements across all field categories and assay types. The largest gains occurred for ontology-constrained fields, where precision increased from 0.36 to 0.92. Our findings show that access to appropriate metadata standards can substantially improve LLM-based standardization of legacy metadata. ARMS improves metadata standardization by giving LLMs runtime access to the authoritative resources that define valid metadata. Representation of metadata standards in machine-actionable form enhances the task of rectifying legacy metadata using LLM technology, especially when those standards can be queried dynamically.
