---
interest: medium
link: https://arxiv.org/abs/2607.07737
next_step: skim
priority: medium
slack_ts: '1783827432.489429'
source: cs.RO - Robotics
status: unread
title: 'SASGeo: Stability-Aware Semantic Map Localization for GNSS-Denied UAVs --
  A Framework and Synthetic Proof of Concept'
---
# SASGeo: Stability-Aware Semantic Map Localization for GNSS-Denied UAVs -- A Framework and Synthetic Proof of Concept
> 原文: [https://arxiv.org/abs/2607.07737](https://arxiv.org/abs/2607.07737)

arXiv:2607.07737v1 Announce Type: new
Abstract: GNSS-denied unmanned aerial vehicles require occasional absolute position fixes to bound the drift of visual-inertial odometry. Cross-view image retrieval can provide such fixes, but raw appearance is sensitive to season, illumination, viewpoint, map age, and sensor modality. We propose \sas, a semantic map-localization framework that represents the environment through persistent structures such as roads, buildings, waterways, railways, intersections, and field boundaries. The method combines semantic raster alignment, relational graph evidence, feature stability and geographic distinctiveness, explicit positive/contradictory/unknown observations, and integrity-aware rejection of ambiguous fixes. Unlike a broad architecture-only proposal, this paper specifies concrete weighting and decision models and reports a reproducible synthetic proof of concept. In 220 randomized retrieval trials with rotation, scale changes, partial crops, occlusion, simulated map changes, and hard semantic decoys, a global semantic descriptor achieved 58.6\% Recall@1, while spatial semantic matching variants achieved 94.5-95.5%. Wilson 95\% intervals separate the global descriptor from the spatial variants but overlap among the spatial variants, so the experiment supports semantic geometry rather than a definitive benefit from each proposed module. The preliminary experiment does not validate real-flight navigation; rather, it demonstrates that structured semantic geometry can discriminate locations under controlled cross-view perturbations and identifies the harder aliasing, map-aging, and rejection tests required next.
