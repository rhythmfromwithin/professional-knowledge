---
title: "Engineering Verifiable Modularity in Transformers via Per-Layer Supervision"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2603.18029
priority: high
status: unread
interest: medium
next_step: skim
---
# Engineering Verifiable Modularity in Transformers via Per-Layer Supervision
> 原文: [https://arxiv.org/abs/2603.18029](https://arxiv.org/abs/2603.18029)

arXiv:2603.18029v1 Announce Type: new
Abstract: Transformers resist surgical control. Ablating an attention head identified as critical for capitalization produces minimal behavioral change because distributed redundancy compensates for damage. This Hydra effect renders interpretability illusory: we may identify components through correlation, but cannot predict or control their causal role. We demonstrate that architectural interventions can expose hidden modularity. Our approach combines dual-stream processing separating token and contextual representations, per-layer supervision providing independent gradient signal at each depth, and gated attention regularizing toward discrete activation patterns. When trained with per-layer supervision, models produce ablation effects 5 to 23 times larger than architecturally identical controls trained with standard objectives. This enables 4 times greater control leverage on targeted behaviors: scaling identified attention heads produces smooth, predictable changes in model output. The key finding is architectural. Without per-layer supervision, ablation damage concentrates near zero with low variance (Winograd standard deviation 0.63%). With per-layer supervision, effects spread widely (standard deviation 6.32%), revealing which predictions depend on which circuits. The larger variance is not measurement noise but the signature of unmasked modularity. We validate our approach through three components: engineered features that capture computational dynamics rather than vocabulary structure (validated by near-zero correlation with raw activation clustering), an architecture providing positive control for modularity, and causal experiments demonstrating functional reorganization where different tasks route through different attention heads. This es tablishes a methodology for transforming interpretability from passive observation to active control.
