---
interest: medium
link: https://arxiv.org/abs/2606.24963
next_step: skim
priority: medium
slack_ts: '1782360758.029339'
source: cs.CV - Computer Vision
status: unread
title: Curvature-Guided Mixing for MLLM Adaptation
---
# Curvature-Guided Mixing for MLLM Adaptation
> 原文: [https://arxiv.org/abs/2606.24963](https://arxiv.org/abs/2606.24963)

arXiv:2606.24963v1 Announce Type: new
Abstract: Fine-tuning Multimodal Large Language Models (MLLMs) on specialized tasks often leads to catastrophic forgetting of their general capabilities. Existing model merging methods to combat this are often heuristic or use sub-optimal objectives. We propose CurvatureGuided Mixing (CGM), a theoretically grounded framework that merges pre-trained and fine-tuned models. CGM formulates a joint optimization objective and uses a second-order (Hessian) approximation of the loss landscapes to analytically derive an optimal, closed-form "soft mixing" ratio. This ratio intelligently blends parameters based on their relative task-specific curvatures. We also introduce CGM$\dagger$, a robust "hard mixing" variant that performs sparse parameter selection guided by a novel, curvature-aware score. Experiments on LLaVA-1.5 and Qwen2.5VL across multiple downstream tasks show that CGM and CGM$\dagger$ consistently improve the trade-off between task specialization and general knowledge retention over existing methods. Code is available at github.com/zzsyjl/CGM-ECCV-2026.
