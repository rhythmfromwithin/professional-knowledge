---
interest: medium
link: https://arxiv.org/abs/2606.11231
next_step: skim
priority: medium
slack_ts: '1781153111.760519'
source: cs.CV - Computer Vision
status: unread
title: 'CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object
  Detection'
---
# CFCamo: A Counterfactual Detect-or-Abstain Framework for Camouflaged Object Detection
> 原文: [https://arxiv.org/abs/2606.11231](https://arxiv.org/abs/2606.11231)

arXiv:2606.11231v1 Announce Type: new
Abstract: Vision-language reinforcement learning has recently shown strong target-present localization for camouflaged object detection (COD). Yet localization is only one side of the decision: when the agent faces an ordinary image with no camouflaged target, will it still claim that a camouflaged object exists? Standard COD training and evaluation data are positive-only, so agents optimized under this setting can acquire an over-detect bias, a task-specific form of object hallucination that standard COD evaluation leaves unmeasured. To quantify this target-absent behavior, we construct Counterfactual COD (CF-COD), a paired benchmark that removes the camouflaged target from each held-out COD evaluation image while preserving a plausible background. CF-COD evaluates whether a model detects the target on the original image and abstains on the target-absent counterfactual, summarized by Pair Accuracy (PA). We further introduce CFCamo, a paired counterfactual framework for COD with abstention. For training, CFCamo optimizes a Qwen3-VL-4B-Instruct agent with Counterfactual Sequence Policy Optimization (CSPO), which samples paired original-counterfactual rollouts and uses a Counterfactual Paired Reward (CPR) to couple original-image detection with counterfactual abstention. On CAMO-test, CFCamo improves S\_alpha by +3.7 pp over the prior RL-based COD baseline; across CF-COD, it reaches 80.0-90.8% PA. Ablations show that removing counterfactual coupling reduces PA to 1.4-5.2% despite strong target-present COD scores, showing that target-present evaluation alone does not characterize detect-or-abstain behavior. Overall, these results indicate that CFCamo improves COD agents by coupling target-present detection with target-absent abstention, rather than merely strengthening target-present localization. Code and data are available at https://github.com/suhang2000/CFCamo.
