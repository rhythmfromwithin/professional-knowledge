---
interest: medium
link: https://arxiv.org/abs/2605.24111
next_step: skim
priority: medium
slack_ts: '1779941826.337199'
source: cs.RO - Robotics
status: unread
title: 'MASt3R-Nav: WayPixel Navigation in Relative 3D Maps'
---
# MASt3R-Nav: WayPixel Navigation in Relative 3D Maps
> 原文: [https://arxiv.org/abs/2605.24111](https://arxiv.org/abs/2605.24111)

arXiv:2605.24111v1 Announce Type: new
Abstract: Visual navigation ability is strongly tied to its underlying representation of the world. Unlike classical 3D maps that require globally-consistent geometry, image- or object-relative topological graphs almost entirely do away with geometric understanding. But, this comes at the cost of navigation capability, often limiting it to merely teach-and-repeat. In this work, we propose a novel map representation in the form of pixel-relative connectivity, which is geometrically accurate but does not require global geometric consistency. Inspired by recent progress in 3D grounded image matching, we construct a map from an image sequence through inter-image connectivity based on pixel correspondences in the relative 3D coordinate systems of individual image pairs. We then use this pixel-level graph to perform global path planning by approximating and sparsifying intra-image pixel connectivity. Through this, we derive a ''WayPixel Costmap'' representation and train a controller conditioned on it to predict a trajectory rollout. We show that this dense pixel-level costmap based on relative geometry is a more accurate conditioning variable for control prediction than its image- and object-level counterparts. This enables a highly capable navigation system, as validated on four types of navigation tasks in the simulator and through real world demonstrations.
