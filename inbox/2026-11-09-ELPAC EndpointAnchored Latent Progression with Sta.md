---
title: "ELPAC: Endpoint-Anchored Latent Progression with Stage-Varying Multimodal Coordination"
source: "stat.ML - Machine Learning (Statistics)"
link: https://arxiv.org/abs/2611.08541
priority: medium
status: unread
interest: medium
next_step: skim
---
# ELPAC: Endpoint-Anchored Latent Progression with Stage-Varying Multimodal Coordination
> 原文: [https://arxiv.org/abs/2611.08541](https://arxiv.org/abs/2611.08541)

arXiv:2611.08541v1 Announce Type: new
Abstract: Aging cohorts increasingly combine imaging, plasma, and cognitive measurements, but most subjects provide only a partially observed cross-sectional snapshot, leaving latent stage, progression subtype, and stage-varying multimodal coordination to be inferred jointly. Existing methods estimate the cohort-level aging process, model covariance under observed covariates, or fuse modalities for prediction. However, they rarely target the joint problem of endpoint-anchored staging and progression-resolved residual coordination across modalities, even though subject staging, subtype assignment, and multimodal interplay are mutually dependent. We introduce ELPAC, a Bayesian framework with two interlocking constructions. The first integrates subtype trajectories backward from clinically reliable endpoint groups along biologically structured velocity components encoding modality-specific monotone direction and optional sequential ordering priors. The second factorizes residual multimodal variation around the inferred stage axis into sparse coordination axes whose loadings and activations expose which multimodal patterns are operative in each subtype and when they emerge, with stage-resolved variation supplying the auxiliary structure for conditional identifiability. We use a scalable amortized variational inference scheme that enables joint posterior inference at cohort scale with single-pass deployment on new subjects. On synthetic data and a harmonized ADNI+NACC/SCAN Alzheimer's cohort, ELPAC demonstrates accurate latent-structure recovery, well-calibrated prediction intervals, and biologically interpretable multimodal coordination programs that differ by subtype.
