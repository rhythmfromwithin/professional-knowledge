---
title: "GAIDE: Graph-based Attention Masking for Spatial- and Embodiment-aware Motion Planning"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.04463
priority: medium
status: unread
interest: medium
next_step: skim
---
# GAIDE: Graph-based Attention Masking for Spatial- and Embodiment-aware Motion Planning
> 原文: [https://arxiv.org/abs/2603.04463](https://arxiv.org/abs/2603.04463)

arXiv:2603.04463v1 Announce Type: new
Abstract: Sampling-based motion planning algorithms are widely used for motion planning of robotic manipulators, but they often struggle with sample inefficiency in high-dimensional configuration spaces due to their reliance on uniform or hand-crafted informed sampling primitives. Neural informed samplers address this limitation by learning the sampling distribution from prior planning experience to guide the motion planner towards planning goal. However, existing approaches often struggle to encode the spatial structure inherent in motion planning problems. To address this limitation, we introduce Graph-based Attention Masking for Spatial- and Embodiment-aware Motion Planning (GAIDE), a neural informed sampler that leverages both the spatial structure of the planning problem and the robotic manipulator's embodiment to guide the planning algorithm. GAIDE represents these structures as a graph and integrates it into a transformer-based neural sampler through attention masking. We evaluate GAIDE against baseline state-of-the-art sampling-based planners using uniform sampling, hand-crafted informed sampling, and neural informed sampling primitives. Evaluation results demonstrate that GAIDE improves planning efficiency and success rate.
