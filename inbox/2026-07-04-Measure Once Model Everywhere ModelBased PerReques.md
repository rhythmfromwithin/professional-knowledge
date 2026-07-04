---
interest: medium
link: https://arxiv.org/abs/2607.01246
next_step: skim
priority: medium
slack_ts: '1783136971.032849'
source: cs.CY - Computers and Society
status: unread
title: 'Measure Once, Model Everywhere: Model-Based Per-Request Resource Consumption
  for HTTP'
---
# Measure Once, Model Everywhere: Model-Based Per-Request Resource Consumption for HTTP
> 原文: [https://arxiv.org/abs/2607.01246](https://arxiv.org/abs/2607.01246)

arXiv:2607.01246v1 Announce Type: new
Abstract: Recent proposals for HTTP-based sustainability disclosure focus on \textbf{what} environmental information should be transmitted at the protocol boundary, for example through response headers, but leave open the practical question of \textbf{how} such per-request values can be generated in realistic deployments. This paper addresses that implementation gap. We present a model-based approach for estimating resource consumption and $CO\_2e$ per HTTP request without requiring fine-grained production power telemetry. The approach benchmarks endpoints offline under controlled conditions, derives compact endpoint-specific energy models from observable request features, and evaluates these models online at the HTTP server boundary. We implement this mechanism as an nginx extension that loads a JSON model registry and emits per-request metadata for energy, grid intensity, embodied emissions, and total request-level impact. We show that heterogeneous request classes can be represented with constant, linear, and piecewise models, and that the same approach extends to endpoints whose dominant cost driver is only visible at the application layer through inputs such as token counts. Our evaluation indicates that the approach is operationally feasible and introduces only low runtime overhead.
