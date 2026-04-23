---
interest: medium
link: https://arxiv.org/abs/2604.18623
next_step: skim
priority: medium
slack_ts: '1776915199.052049'
source: cs.CV - Computer Vision
status: unread
title: 'Can We Build Scene Graphs, Not Classify Them? FlowSG: Progressive Image-Conditioned
  Scene Graph Generation with Flow Matching'
---
# Can We Build Scene Graphs, Not Classify Them? FlowSG: Progressive Image-Conditioned Scene Graph Generation with Flow Matching
> 原文: [https://arxiv.org/abs/2604.18623](https://arxiv.org/abs/2604.18623)

arXiv:2604.18623v1 Announce Type: new
Abstract: Scene Graph Generation (SGG) unifies object localization and visual relationship reasoning by predicting boxes and subject-predicate-object triples. Yet most pipelines treat SGG as a one-shot, deterministic classification problem rather than a genuinely progressive, generative task. We propose FlowSG, which recasts SGG as continuous-time transport on a hybrid discrete-continuous state: starting from a noised graph, the model progressively grows an image-conditioned scene graph through constraint-aware refinements that jointly synthesize nodes (objects) and edges (predicates). Specifically, we first leverage a VQ-VAE to quantize a scene graph (e.g., continuous visual features) into compact, predictable tokens; a graph Transformer then (i) predicts a conditional velocity field to transport continuous geometry (boxes) and (ii) updates discrete posteriors for categorical tokens (object features and predicate labels), coupling semantics and geometry via flow-conditioned message aggregation. Training combines flow-matching losses for geometry with a discrete-flow objective for tokens, yielding few-step inference and plug-and-play compatibility with standard detectors and segmenters. Extensive experiments on VG and PSG under closed- and open-vocabulary protocols show consistent gains in predicate R/mR and graph-level metrics, validating the mixed discrete-continuous generative formulation over one-shot classification baselines, with an average improvement of about 3 points over the state-of-the-art USG-Par.
