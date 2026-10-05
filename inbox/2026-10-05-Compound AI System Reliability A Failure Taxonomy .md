---
title: "Compound AI System Reliability: A Failure Taxonomy and Resilience Pattern Catalog from 150 Production Incidents"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.02503
priority: low
status: unread
interest: medium
next_step: skim
---
# Compound AI System Reliability: A Failure Taxonomy and Resilience Pattern Catalog from 150 Production Incidents
> 原文: [https://arxiv.org/abs/2610.02503](https://arxiv.org/abs/2610.02503)

arXiv:2610.02503v1 Announce Type: new
Abstract: Deploying compound AI systems reliably and safely requires understanding failure modes that emerge at component boundaries, not within individual models. Cascading errors propagate across component boundaries, silent quality degradation evades standard monitoring, and coordination failures yield incorrect collective behavior from individually correct parts. We analyze 150 production incident reports from open-source compound AI projects and anonymized enterprise deployments to construct a taxonomy of 23 failure modes organized into five categories: retrieval failures, generation failures, tool failures, orchestration failures, and integration failures. For each category, we propose resilience patterns with measured effectiveness from controlled fault injection experiments. Circuit breakers reduce cascade propagation by 89%, output quality gates catch 73% of silent degradation before user impact, and component isolation reduces blast radius by 64%. Systems implementing three or more resilience patterns from our catalog reduce mean-time-to-recovery (MTTR) by 71% compared to unstructured monitoring baselines. We release the incident taxonomy and pattern catalog as a practitioner resource.
