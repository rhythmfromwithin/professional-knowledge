---
title: "4DGS-JEPA: Temporally Compositional Joint-Embedding Prediction for Dynamic Gaussian Splatting"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2609.25036
priority: high
status: unread
interest: medium
next_step: skim
---
# 4DGS-JEPA: Temporally Compositional Joint-Embedding Prediction for Dynamic Gaussian Splatting
> 原文: [https://arxiv.org/abs/2609.25036](https://arxiv.org/abs/2609.25036)

arXiv:2609.25036v1 Announce Type: new
Abstract: Dynamic Gaussian Splatting provides an explicit representation of evolving 3D scenes, but existing approaches are primarily optimized for reconstruction, future-state generation, or rendering rather than for learning reusable predictive dynamics. We propose 4DGS-JEPA, a Gaussian-native joint-embedding predictive architecture for causal multi-horizon prediction over dynamic Gaussian scenes. The model uses a hierarchical scene-, motion-group-, and Gaussian-level representation together with a horizon-conditioned transition operator that supports both direct prediction and recursive rollout. Its central principle is temporal composition: different chronological transition paths reaching the same future endpoint should produce compatible predictive states. Endpoint and multi-horizon path supervision anchor these predictions to future target embeddings, while a selective geometry decoder and geometry-level composition ground the learned dynamics in consistent group motion and Gaussian geometry without requiring complete future appearance reconstruction. We further introduce a hybrid correspondence mechanism that combines persistent canonical identity with residual optimal-transport matching under reordering and topology change. We characterize zero-loss path agreement and finite-error rollout accumulation theoretically. Three controlled experiments provide mechanism-level evidence that temporal composition reduces latent path dependence while retaining predictive accuracy, geometry-level composition improves consistency of decoded motion, and hybrid correspondence preserves reliable identity while remaining robust when correspondence becomes ambiguous. Together, 4DGS-JEPA provides a predictive, temporally compositional formulation of dynamic Gaussian worlds.
