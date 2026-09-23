---
interest: medium
link: https://arxiv.org/abs/2609.22276
next_step: skim
priority: medium
slack_ts: '1790137534.297749'
source: cs.RO - Robotics
status: unread
title: 'D3DWA: Adaptive Weight and Prediction-Horizon for Dynamic Window Approach
  via Dueling Double Deep Q-Network'
---
# D3DWA: Adaptive Weight and Prediction-Horizon for Dynamic Window Approach via Dueling Double Deep Q-Network
> 原文: [https://arxiv.org/abs/2609.22276](https://arxiv.org/abs/2609.22276)

arXiv:2609.22276v1 Announce Type: new
Abstract: The Dynamic Window Approach (DWA) is widely used for local navigation, but its performance depends strongly on parameters that are typically fixed before navigation. In particular, the appropriate prediction horizon can vary with local free space: longer horizons support efficient motion in open areas, whereas shorter horizons help preserve feasible motions in narrow or cluttered regions. This paper proposes D3DWA, an adaptive DWA framework based on a Dueling Double Deep Q-Network (D3QN), which jointly selects the DWA evaluation weights and prediction horizon from a continuous navigation state at every control step while retaining DWA's trajectory generation and collision checking. In eight simulated environments, including unseen layouts, D3DWA reached every goal. Real-robot experiments further showed that D3DWA completed all three tested configurations, including a constrained case in which the weights-only variant timed out. These results demonstrate the benefit of jointly adapting the evaluation weights and prediction horizon. Additional material is available at https://mertcookimg.github.io/d3dwa/
