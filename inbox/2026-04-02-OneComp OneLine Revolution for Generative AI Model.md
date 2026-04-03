---
interest: medium
link: https://arxiv.org/abs/2603.28845
next_step: skim
priority: high
slack_ts: '1775185072.474509'
source: cs.LG - Machine Learning
status: unread
title: 'OneComp: One-Line Revolution for Generative AI Model Compression'
---
# OneComp: One-Line Revolution for Generative AI Model Compression
> 原文: [https://arxiv.org/abs/2603.28845](https://arxiv.org/abs/2603.28845)

arXiv:2603.28845v1 Announce Type: new
Abstract: Deploying foundation models is increasingly constrained by memory footprint, latency, and hardware costs. Post-training compression can mitigate these bottlenecks by reducing the precision of model parameters without significantly degrading performance; however, its practical implementation remains challenging as practitioners navigate a fragmented landscape of quantization algorithms, precision budgets, data-driven calibration strategies, and hardware-dependent execution regimes. We present OneComp, an open-source compression framework that transforms this expert workflow into a reproducible, resource-adaptive pipeline. Given a model identifier and available hardware, OneComp automatically inspects the model, plans mixed-precision assignments, and executes progressive quantization stages, ranging from layer-wise compression to block-wise refinement and global refinement. A key architectural choice is treating the first quantized checkpoint as a deployable pivot, ensuring that each subsequent stage improves the same model and that quality increases as more compute is invested. By converting state-of-the-art compression research into an extensible, open-source, hardware-aware pipeline, OneComp bridges the gap between algorithmic innovation and production-grade model deployment.
