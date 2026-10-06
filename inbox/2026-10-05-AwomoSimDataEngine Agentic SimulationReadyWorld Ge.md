---
interest: medium
link: https://arxiv.org/abs/2610.02274
next_step: skim
priority: medium
slack_ts: '1791266334.912519'
source: cs.RO - Robotics
status: unread
title: 'Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation'
---
# Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation
> 原文: [https://arxiv.org/abs/2610.02274](https://arxiv.org/abs/2610.02274)

arXiv:2610.02274v1 Announce Type: new
Abstract: Generating useful robot-training data requires more than visually plausiblescenes: objects must support interaction, placements must remain physicallyvalid, and tasks must admit repeatable execution. We present\textbf{Awomo-SimDataEngine}, an agentic system that connects asset and scenegeneration to robot demonstration synthesis. Shared asset services providerigid and articulated objects, including structure-grounded part and jointgeneration with ISArt. Scene generation supports two complementary routes:Unravel reconstructs editable scenes from images, while SimForge buildssingle-room and multi-room environments from text. A graph-native harnesscoordinates construction, validation, andbounded repair, routing failures to the responsible module while retainingunaffected scene state. PolicyForge binds validated worlds to tasks and robotembodiments to produce replayable demonstrations. Evaluations cover assetgeometry, scene quality, and downstream policy learning. On MuJoCo-basedLIBERO-Plus, co-training with Isaac Sim demonstrations improves the overallsuccess rate of a World-Action Model (WAM) from $77.17\%$ to $89.43\%$. Goal and spatialsuccess improve by $31.66$ and $6.25$ percentage points, respectively.These results support the utility of the generated data for cross-simulatorpolicy training, with more limited gains on long-horizon tasks.
