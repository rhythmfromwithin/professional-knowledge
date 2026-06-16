---
interest: medium
link: https://arxiv.org/abs/2606.13727
next_step: skim
priority: medium
slack_ts: '1781586972.826689'
source: cs.RO - Robotics
status: unread
title: Occupancy-Grounded Room Segmentation for Hierarchical 3D Scene Graphs
---
# Occupancy-Grounded Room Segmentation for Hierarchical 3D Scene Graphs
> 原文: [https://arxiv.org/abs/2606.13727](https://arxiv.org/abs/2606.13727)

arXiv:2606.13727v1 Announce Type: new
Abstract: Hierarchical 3D scene graphs (3DSGs) for indoor robots organize geometric and semantic information across spatial scales, with a room layer that connects object-level perception to room-scale reasoning. Existing systems construct this layer from different spatial substrates (\eg{} place clusters, wall planes, or segmentation outputs), and as a result, room nodes are not evaluated on a common geometric criterion. We present an occupancy-grounded 3DSG pipeline in which room nodes are anchored to tracked free-space regions derived from occupancy decomposition, giving each room an explicit polygonal footprint. We evaluate the pipeline on 12 Matterport3D scenes by matching predicted room polygons to annotated room instances and compare against Hydra, a representative state-of-the-art place-connectivity baseline. The results show that occupancy-grounded anchoring recovers substantially more room instances than place-connectivity construction, at the cost of lower precision, and that wall-accurate room boundaries remain an open problem for both methods. Code is available at https://github.com/crcz25/OccuSG.
