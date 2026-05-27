---
title: "BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.26182
priority: high
status: unread
interest: medium
next_step: skim
---
# BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization
> 原文: [https://arxiv.org/abs/2605.26182](https://arxiv.org/abs/2605.26182)

arXiv:2605.26182v1 Announce Type: new
Abstract: Generating physically buildable brick structures from 3D shapes requires more than geometric reconstruction: the output must also satisfy discrete part constraints and structural stability. Existing brick generation methods either rely on heuristic optimization, which can break down when the target 3D shape does not admit a feasible structure under predefined constraints, or generate brick sequences without explicitly modeling the underlying 3D geometry and assembly relations. In this work, we present BrickAnything, a geometry-conditioned autoregressive framework for generating buildable brick structures from diverse 3D representations. BrickAnything uses point clouds as a unified geometric interface and predicts brick sequences that reconstruct the target shape under assembly constraints. To model structural dependencies among bricks, we introduce a structure-aware tree tokenization, which represents brick structures through local attachment relations. This formulation makes sequence generation more consistent with the physical construction process, and reduces invalid intermediate states. We further introduce preference-based alignment post-training, validity-constrained decoding and adaptive rollback to improve buildability objectives such as stability and geometric fidelity. Extensive experiments demonstrate that BrickAnything produces geometrically faithful and physically realizable brick structures, and that the proposed tokenization effectively reduces rollback and regeneration compared with conventional ordering strategies.
