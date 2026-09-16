---
title: "MechReason: Benchmarking Multi-Image Multi-Hop Reasoning in Mechanical Engineering"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2609.16012
priority: medium
status: unread
interest: medium
next_step: skim
---
# MechReason: Benchmarking Multi-Image Multi-Hop Reasoning in Mechanical Engineering
> 原文: [https://arxiv.org/abs/2609.16012](https://arxiv.org/abs/2609.16012)

arXiv:2609.16012v1 Announce Type: new
Abstract: Despite significant progress in general visual question answering and cross-modal understanding, multimodal large language models still face a pronounced gap in evaluation for complex reasoning within the mechanical engineering domain. Existing benchmarks predominantly focus on rudimentary tasks such as drawing recognition, CAD interpretation, or single-chart querying, falling short of assessing whether models can integrate multiple images, textual conditions, physical principles, and engineering constraints to perform multi-step reasoning when confronted with authentic, intricate mechanical problems. To address this, we introduce MechReason, a benchmark derived from real mechanical engineering papers, comprising 12k question-answer pairs with explicit reasoning-chain annotations and 21k visual materials spanning nine evidence types, including statistical charts, parameter tables, engineering drawings, microscopic images, simulation images, system architectures, real mechanical scene photos, CAD model images and manufacturing flowcharts. MechReason covers eight task types across four reasoning dimensions: explanation, prediction, design, and diagnosis. We devise a four-stage construction pipeline: we first extract core engineering claims and decompose their supporting evidence into premises, reasoning processes, conclusions, and corroborative evidence; we then generate shortcut-preventing questions by masking posterior verification information; finally, we apply multimodal quality validation to ensure task quality and multi-hop nature. Extensive experimental results demonstrate that MechReason is highly challenging, with even the most advanced models achieving only 62.89\% accuracy.
