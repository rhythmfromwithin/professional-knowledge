---
title: "A Non-Destructive Methodological Framework for Modernizing Legacy Clinical Reporting Systems for AI-Driven Pharmacoinformatics: A SAS Case Study"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2605.13905
priority: low
status: unread
interest: medium
next_step: skim
---
# A Non-Destructive Methodological Framework for Modernizing Legacy Clinical Reporting Systems for AI-Driven Pharmacoinformatics: A SAS Case Study
> 原文: [https://arxiv.org/abs/2605.13905](https://arxiv.org/abs/2605.13905)

arXiv:2605.13905v1 Announce Type: new
Abstract: Drug development and pharmacovigilance are frequently bottlenecked by legacy clinical reporting pipelines. These monolithic systems encode regulatory-grade logic but resist AI integration by producing opaque output with no machine-readable intermediate layer. Existing modernization approaches force a choice between full rewrites and incremental refactoring that preserves structural barriers. We present a non-destructive methodological framework achieving AI-driven pharmacoinformatics readiness without altering legacy source code. A metadata layer--comprising a bridge map, a typed Intermediate Representation (IR), and an orchestrator--wraps existing components and re-exposes their outputs as structured data consumable by LLMs. It enables optional incremental consolidation, replacing selected legacy components with metadata-configured core routines while the remainder operates unchanged. Validated on a 558-component SAS reporting library (373,000 lines of code), the framework demonstrated immediate AI-readiness under coexistence mode, yielding machine-readable output. Where consolidation was elected, the modernized core achieved a 92% reduction in proprietary code. Parity validation on 14 report types from a Phase III study achieved cell-level parity of 80% or above on 11 reports (mean 82.7%, best 99.2%). A benchmark using CDISC CDISCPilot01 data achieved 100% parity across 5 reports. LLM experiments confirmed the IR enables automated pharmacovigilance, table summarization, and trial configuration generation. The framework offers a regulation-aware path to AI-integrated clinical reporting, accelerating drug development without interrupting regulatory submissions.
