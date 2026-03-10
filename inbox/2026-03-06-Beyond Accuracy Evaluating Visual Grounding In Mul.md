---
title: "Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2603.03437
priority: medium
status: unread
interest: medium
next_step: skim
---
# Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning
> 原文: [https://arxiv.org/abs/2603.03437](https://arxiv.org/abs/2603.03437)

arXiv:2603.03437v1 Announce Type: new
Abstract: Recent work shows that text-only reinforcement learning with verifiable rewards (RLVR) can match or outperform image-text RLVR on multimodal medical VQA benchmarks, suggesting current evaluation protocols may fail to measure causal visual dependence. We introduce a counterfactual evaluation framework using real, blank, and shuffled images across four medical VQA benchmarks: PathVQA, PMC-VQA, SLAKE, and VQA-RAD. Beyond accuracy, we measure Visual Reliance Score (VRS), Image Sensitivity (IS), and introduce Hallucinated Visual Reasoning Rate (HVRR) to detect cases where models generate visual claims despite producing image-invariant answers. Our findings reveal that RLVR improves accuracy while degrading visual grounding: text-only RLVR achieves negative VRS on PathVQA (-0.09), performing better with mismatched images, while image-text RLVR reduces image sensitivity to 39.8% overall despite improving accuracy. On VQA-RAD, both variants achieve 63% accuracy through different mechanisms: text-only RLVR retains 81% performance with blank images, while image-text RLVR shows only 29% image sensitivity. Models generate visual claims in 68-74% of responses, yet 38-43% are ungrounded (HVRR). These findings demonstrate that accuracy-only rewards enable shortcut exploitation, and progress requires grounding-aware evaluation protocols and training objectives that explicitly enforce visual dependence.
