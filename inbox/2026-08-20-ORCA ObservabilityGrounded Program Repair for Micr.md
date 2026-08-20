---
title: "ORCA: Observability-Grounded Program Repair for Microservice Incidents"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2608.17018
priority: low
status: unread
interest: medium
next_step: skim
---
# ORCA: Observability-Grounded Program Repair for Microservice Incidents
> 原文: [https://arxiv.org/abs/2608.17018](https://arxiv.org/abs/2608.17018)

arXiv:2608.17018v1 Announce Type: new
Abstract: Microservice failures are often diagnosed from operational telemetry. However, automated program repair systems usually start from issue reports, localized code context, or failing tests. This mismatch leaves a gap between telemetry-based diagnosis and patch generation. We present ORCA, an observability-grounded APR pipeline for microservice incidents. ORCA first distills the differences in paired failure and reference telemetry into a fault signature, then uses the signature to identify candidate code and deployment-configuration locations. Repair graph agents and an Exploration agent generate unified-diff patch candidates from these locations. ORCA evaluates generated patches with a Telemetry-Grounded Patch Verifier that separates patch validity, syntactic and semantic correctness, test-oracle integrity, and telemetry replay. On a 575-case benchmark, ORCA outperforms all evaluated baselines in terms of cost-effectiveness. Results show that operational telemetry can be transformed from diagnostic evidence into actionable repair context: paired telemetry supports repair-oriented localization, while repair graph agents convert localized code and configuration evidence into constrained patch-generation context for the LLM. Telemetry-grounded verification then exposes repair outcomes that issue- or test-only evaluation would miss.
