---
interest: medium
link: https://arxiv.org/abs/2609.09184
next_step: skim
priority: medium
slack_ts: '1789013733.709489'
source: cs.CV - Computer Vision
status: unread
title: Evidence-Order Calibration for Selective Visual Reasoning under Progressive
  Loss of Question-Critical Evidence
---
# Evidence-Order Calibration for Selective Visual Reasoning under Progressive Loss of Question-Critical Evidence
> 原文: [https://arxiv.org/abs/2609.09184](https://arxiv.org/abs/2609.09184)

arXiv:2609.09184v1 Announce Type: new
Abstract: Vision-language model (VLM) confidence may change in aggregate when visual evidence is degraded while remaining structurally inconsistent within individual examples. We study answer-level reliability along five-step, question-conditioned evidence-loss trajectories. Using a frozen Qwen2.5-VL-3B-Instruct model, we construct 176 accepted GQA-derived trajectories (880 masking conditions) by progressively masking scene-graph-localized question-critical regions. Native sequence confidence has an evidence monotonicity violation rate (EMVR) of 0.436, and 92.0% of trajectories contain at least one adjacent violation. A matched non-critical-region control shows that full critical masking reduces accuracy by 28.2 percentage points, compared with 0.6 points for equally sized non-critical masks; the paired difference is 27.6 points (95% CI [20.0, 34.7]). We train a lightweight post-hoc reliability head on frozen hidden states, sequence confidence, and entropy. Adding evidence-order supervision to binary cross-entropy (BCE) reduces masking EMVR from 0.330 to 0.303 (paired difference -0.027, 95% CI [-0.044, -0.010]). The same mask-trained objective reduces EMVR from 0.449 to 0.402 on held-out question IDs under unseen local Gaussian blur (difference -0.0468, 95% CI [-0.0739, -0.0199]). AUROC, Brier, and AURC differences between the two learned heads are statistically inconclusive, and native confidence remains stronger for selective-risk ranking. The results separate evidence-order consistency from conventional correctness discrimination rather than establishing generic confidence superiority.
