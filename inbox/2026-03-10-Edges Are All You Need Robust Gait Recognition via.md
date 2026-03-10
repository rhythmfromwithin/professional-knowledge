---
title: "Edges Are All You Need: Robust Gait Recognition via Label-Free Structure"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.05537
priority: medium
status: unread
interest: medium
next_step: skim
---
# Edges Are All You Need: Robust Gait Recognition via Label-Free Structure
> 原文: [https://arxiv.org/abs/2603.05537](https://arxiv.org/abs/2603.05537)

arXiv:2603.05537v1 Announce Type: new
Abstract: Gait recognition is a non-intrusive biometric technique for security applications, yet existing studies are dominated by silhouette- and parsing-based representations. Silhouettes are sparse and miss internal structural details, limiting discriminability. Parsing enriches silhouettes with part-level structures, but relies heavily on upstream human parsers (e.g., label granularity and boundary precision), leading to unstable performance across datasets and sometimes even inferior results to silhouettes. We revisit gait representations from a structural perspective and describe a design space defined by edge density and supervision form: silhouettes use sparse boundary edges with weak single-label supervision, while parsing uses denser cues with strong semantic priors. In this space, we identify an underexplored paradigm: dense part-level structure without explicit semantic labels, and introduce SKETCH as a new visual modality for gait recognition. Sketch extracts high-frequency structural cues (e.g., limb articulations and self-occlusion contours) directly from RGB images via edge-based detectors in a label-free manner. We further show that label-guided parsing and label-free sketch are semantically decoupled and structurally complementary. Based on this, we propose SKETCHGAIT, a hierarchically disentangled multi-modal framework with two independent streams for modality-specific learning and a lightweight early-stage fusion branch to capture structural complementarity. Extensive experiments on SUSTech1K and CCPG validate the proposed modality and framework: SketchGait achieves 92.9% Rank-1 on SUSTech1K and 93.1% mean Rank-1 on CCPG.
