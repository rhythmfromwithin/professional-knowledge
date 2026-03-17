---
interest: medium
link: https://arxiv.org/abs/2603.05604
next_step: skim
priority: medium
slack_ts: '1773715513.148959'
source: cs.CV - Computer Vision
status: unread
title: 'From Decoupled to Coupled: Robustness Verification for Learning-based Keypoint
  Detection with Joint Specifications'
---
# From Decoupled to Coupled: Robustness Verification for Learning-based Keypoint Detection with Joint Specifications
> 原文: [https://arxiv.org/abs/2603.05604](https://arxiv.org/abs/2603.05604)

arXiv:2603.05604v1 Announce Type: new
Abstract: Keypoint detection underpins many vision tasks, including pose estimation, viewpoint recovery, and 3D reconstruction, yet modern neural models remain vulnerable to small input perturbations. Despite its importance, formal robustness verification for keypoint detectors is largely unexplored due to high-dimensional inputs and continuous coordinate outputs. We propose the first coupled robustness verification framework for heatmap-based keypoint detectors that bounds the joint deviation across all keypoints, capturing their interdependencies and downstream task requirements. Unlike prior decoupled, classification-style approaches that verify each keypoint independently and yield conservative guarantees, our method verifies collective behavior. We formulate verification as a falsification problem using a mixed-integer linear program (MILP) that combines reachable heatmap sets with a polytope encoding joint deviation constraints. Infeasibility certifies robustness, while feasibility provides counterexamples, and we prove the method is sound: if it certifies the model as robust, then the keypoint detection model is guaranteed to be robust. Experiments show that our coupled approach achieves high verified rates and remains effective under strict error thresholds where decoupled methods fail.
