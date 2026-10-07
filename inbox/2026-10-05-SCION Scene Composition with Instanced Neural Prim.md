---
interest: medium
link: https://arxiv.org/abs/2610.02322
next_step: skim
priority: medium
slack_ts: '1791351179.520179'
source: cs.CV - Computer Vision
status: unread
title: 'SCION: Scene Composition with Instanced Neural Primitives'
---
# SCION: Scene Composition with Instanced Neural Primitives
> 原文: [https://arxiv.org/abs/2610.02322](https://arxiv.org/abs/2610.02322)

arXiv:2610.02322v1 Announce Type: new
Abstract: Real-world scenes are compositional: bricks, blades of grass, pebbles, and tree leaves recur across human-built and natural environments. Existing neural scene representations model these elements independently. Most 3D Gaussian Splatting and follow-up abstraction and compression methods treat each element as unique, fitting millions of independent Gaussians per scene. Prior methods like Splat and Replace fit template objects, but they require mostly manual selection of repeated elements. As a result, these representations store redundant parameters and provide weak manipulation handles for downstream tasks. We introduce SCION, a hier- archical compositional scene representation that replaces independent Gaussians with a compact vocabulary of reusable primitives and lightweight world-space instances that place transformed copies throughout the scene. We fit this represen- tation to multi-view captures via a joint optimization over discrete and continuous scene parameters, combining two-level densification over splats and instances with an adversarial loss that preserves detail across shared primitives. The recovered structure yields a compact, controllable representation while maintaining high quality even at 1.2 MB. SCION achieves rate-distortion favorable to existing Gaussian compression methods, and it enables instance-level scene editing and animation without retraining. Our results show that neural scene representations need not memorize scenes as independent primitives; they can discover reusable parts. Project webpage: https://light.princeton.edu/SCION
