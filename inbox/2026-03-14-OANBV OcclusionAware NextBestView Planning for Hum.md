---
title: "OA-NBV: Occlusion-Aware Next-Best-View Planning for Human-Centered Active Perception on Mobile Robots"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2603.11072
priority: medium
status: unread
interest: medium
next_step: skim
---
# OA-NBV: Occlusion-Aware Next-Best-View Planning for Human-Centered Active Perception on Mobile Robots
> 原文: [https://arxiv.org/abs/2603.11072](https://arxiv.org/abs/2603.11072)

arXiv:2603.11072v1 Announce Type: new
Abstract: We naturally step sideways or lean to see around the obstacle when our view is blocked, and recover a more informative observation. Enabling robots to make the same kind of viewpoint choice is critical for human-centered operations, including search, triage, and disaster response, where cluttered environments and partial visibility frequently degrade downstream perception. However, many Next-Best-View (NBV) methods primarily optimize generic exploration or long-horizon coverage, and do not explicitly target the immediate goal of obtaining a single usable observation of a partially occluded person under real motion constraints. We present Occlusion-Aware Next-Best-View Planning for Human-Centered Active Perception on Mobile Robots (OA-NBV), an occlusion-aware NBV pipeline that autonomously selects the next traversable viewpoint to obtain a more complete view of an occluded human. OA-NBV integrates perception and motion planning by scoring candidate viewpoints using a target-centric visibility model that accounts for occlusion, target scale, and target completeness, while restricting candidates to feasible robot poses. OA-NBV achieves over 90% success rate in both simulation and real-world trials, while baseline NBV methods degrade sharply under occlusion. Beyond success rate, OA-NBV improves observation quality: compared to the strongest baseline, it increases normalized target area by at least 81% and keypoint visibility by at least 58% across settings, making it a drop-in view-selection module for diverse human-centered downstream tasks.
