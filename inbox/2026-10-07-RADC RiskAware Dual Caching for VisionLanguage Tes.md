---
title: "RADC: Risk-Aware Dual Caching for Vision-Language Test-Time Adaptation"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2610.06932
priority: medium
status: unread
interest: medium
next_step: skim
---
# RADC: Risk-Aware Dual Caching for Vision-Language Test-Time Adaptation
> 原文: [https://arxiv.org/abs/2610.06932](https://arxiv.org/abs/2610.06932)

arXiv:2610.06932v1 Announce Type: new
Abstract: Cache-based test-time adaptation (TTA) for vision-language models is often hindered by background bias in global representations and unreliable entropy-based cache admission under representation variations. To address these limitations, we propose RADC, which enhances prototype learning through reliable dual caching. RADC introduces a Semantic Foreground Cache that aggregates category-consistent spatial evidence from CLIP representations, yielding foreground prototypes that complement the global cache while mitigating background interference. To reliably manage both caches, Gaussian Risk Admission models multi-view representations as diagonal Gaussian distributions and jointly considers class separation and feature uncertainty to prioritize reliable cache candidates. RADC integrates zero-shot logits with complementary global- and foreground-cache predictions for robust inference. Extensive experiments on cross-domain and out-of-distribution benchmarks demonstrate consistent state-of-the-art performance.
