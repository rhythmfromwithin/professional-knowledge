---
title: "STEP: A Modular Silent Trial Engine for Operational Evaluation of Digital Pathology AI in Routine Workflow"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.28708
priority: low
status: unread
interest: medium
next_step: skim
---
# STEP: A Modular Silent Trial Engine for Operational Evaluation of Digital Pathology AI in Routine Workflow
> 原文: [https://arxiv.org/abs/2608.28708](https://arxiv.org/abs/2608.28708)

arXiv:2608.28708v1 Announce Type: new
Abstract: Prospective silent trials provide an important bridge between retrospective validation of artificial intelligence (AI) models and their use in clinical care by evaluating model performance and operational reliability on live clinical data without influencing patient management. In computational pathology, conducting silent trials requires integration across laboratory information systems, digital pathology infrastructure, computational resources, and model inference pipelines, and these workflows are often implemented using application-specific software. We developed the Silent Trial Engine for Pathology (STEP), a reusable software platform for orchestrating prospective silent trials of computational pathology AI models across heterogeneous clinical and computational environments. STEP separates common trial orchestration from institution-specific data access and compute infrastructure through modular adapter interfaces. The platform supports scheduled case discovery, per-slide inference submission, deterministic idempotency, failure recovery, result and ancillary-data ingestion, persistent trial and run state, and audit logging, with compute adapters supporting local execution and high-performance computing environments using LSF and Slurm. STEP was deployed at three institutions to support prospective silent evaluation of EAGLE, an AI model for predicting EGFR mutation status from hematoxylin and eosin-stained whole-slide images. By separating trial-level workflow logic from site-specific integrations, STEP enables a common execution framework to operate across heterogeneous pathology environments while maintaining durable and auditable trial state. This approach may reduce duplicated engineering effort and facilitate systematic real-world evaluation of computational pathology AI before interventional clinical deployment.
