---
title: "TraCE: Trajectory-Aware Concepts for Explainable Video Understanding"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2611.07009
priority: medium
status: unread
interest: medium
next_step: skim
---
# TraCE: Trajectory-Aware Concepts for Explainable Video Understanding
> 原文: [https://arxiv.org/abs/2611.07009](https://arxiv.org/abs/2611.07009)

arXiv:2611.07009v1 Announce Type: new
Abstract: Video understanding models often rely on motion, yet their explanations can obscure which motion sources support a prediction. We identify motion-source under-specification as a limitation of existing video XAI: region-centric explanations can be source-ambiguous, while motion vocabularies restricted to single-person pose sequences are source-incomplete. We propose TraCE (Trajectory-Aware Concepts for Explainable Video Understanding), a concept-based framework that discovers source-flexible motion concepts by clustering optical-flow trajectories from training videos. These concepts represent dynamic evidence from people, objects, and interactions, while object and scene concepts account for static context. The resulting typed trajectory/object/scene interface supports class prediction for action recognition and question-conditioned concept matching for video question answering (VQA). We evaluate TraCE across five random seeds on six benchmarks: NTU RGB+D Mutual, Chiral SSv2, UCF-101, KTH, TOMATO, and STAR. Relative to non-interpretable baselines, TraCE maintains competitive task performance, with an average accuracy drop of 1.0 points for action recognition and a nominal gain of 0.4 points for VQA. Motion perturbation and concept-removal tests provide complementary evidence of directional semantic alignment and decision faithfulness, while sample-level interventions illustrate targeted model debugging. Our project page is available at https://leewooil.github.io/TraCE\_project\_page/.
