---
interest: medium
link: https://arxiv.org/abs/2611.25105
next_step: skim
priority: medium
slack_ts: '1795328173.580479'
source: cs.RO - Robotics
status: unread
title: 'MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation'
---
# MAWAM: A Multi-Agent World-Action Model for Coordinated Manipulation
> 原文: [https://arxiv.org/abs/2611.25105](https://arxiv.org/abs/2611.25105)

arXiv:2611.25105v1 Announce Type: new
Abstract: Every move in a robot team changes the world in which its teammates must act. Coordinated manipulation therefore calls for predicting the team's actions together with the physical future they jointly create. We introduce MAWAM, a multi-agent world-action model that jointly generates each robot's future views and executable action chunks in a single sample. Built from a pretrained single-robot world-action backbone, MAWAM jointly denoises all robots' action and future-view tokens through cross-agent attention, while preserving a separate control interface for each robot. MAWAM achieves the highest success on all three real-robot tasks (laundry-bag collection, bath-towel folding, and umbrella handover), with 67.8% mean success, 18.9 percentage points above MA-VLA trained on the same demonstrations and cameras. In simulation, MAWAM reaches 90.3% mean success on eight tasks with teams of up to four arms. Ablations show that cross-agent attention and team-stage future-video supervision both improve coordinated control: without attention, a four-arm relay falls from 95.0% to 39.0%, and without this supervision, Place Food falls from 78.0% to 47.0%.
