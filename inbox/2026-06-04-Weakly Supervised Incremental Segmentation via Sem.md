---
interest: medium
link: https://arxiv.org/abs/2606.04060
next_step: skim
priority: medium
slack_ts: '1780548680.618549'
source: cs.CV - Computer Vision
status: unread
title: Weakly Supervised Incremental Segmentation via Semantic Anchors and Spatial
  Arbitration
---
# Weakly Supervised Incremental Segmentation via Semantic Anchors and Spatial Arbitration
> 原文: [https://arxiv.org/abs/2606.04060](https://arxiv.org/abs/2606.04060)

arXiv:2606.04060v1 Announce Type: new
Abstract: Weakly Incremental Learning for Semantic Segmentation (WILSS) suffers from the continuous introduction of noisy supervision, which progressively corrupts class-level representations, leading to severe feature drift and semantic corruption, thereby causing newly learned classes to overwrite old ones. To address these issues, we propose a drift-resilient WILSS approach, named SASA, designed to stabilize semantic learning via Semantic Anchors and Spatial Arbitration. Specifically, at the representation level, we introduce semantic anchors of learnable tokens as rigid class-level references to preserve long-term semantic identity. Complementary to this, an elastic residual adaptation facilitates controlled, instance-specific refinement, ensuring a stable yet flexible learning trajectory. At the supervision level, we develop a Spatial Label Arbitration mechanism that performs geometry-aware decisions to directly filter unreliable signals and enforce a strict "one object, one class" constraint. By synergistically stabilizing representations and improving supervision reliability, SASA effectively mitigates feature drift under weak supervision. Extensive experiments on standard benchmarks demonstrate that our approach consistently outperforms existing state-of-the-art methods, particularly in challenging multi-step incremental settings. The code is available at https://github.com/ZhonggaiWang/SASA.
