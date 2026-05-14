---
title: "Driving Intents Amplify Planning-Oriented Reinforcement Learning"
source: "cs.RO - Robotics"
link: https://arxiv.org/abs/2605.12625
priority: medium
status: unread
interest: medium
next_step: skim
---
# Driving Intents Amplify Planning-Oriented Reinforcement Learning
> 原文: [https://arxiv.org/abs/2605.12625](https://arxiv.org/abs/2605.12625)

arXiv:2605.12625v1 Announce Type: new
Abstract: Continuous-action policies trained on a single demonstrated trajectory per scene suffer from mode collapse: samples cluster around the demonstrated maneuver and the policy cannot represent semantically distinct alternatives. Under preference-based evaluation, this caps best-of-N performance -- even oracle selection cannot recover what the sampling distribution does not contain. We introduce DIAL, a two-stage Driving-Intent-Amplified reinforcement Learning framework for preference-aligned continuous-action driving policies. In the first stage, DIAL conditions the flow-matching action head on a discrete intent label with classifier-free guidance (CFG), which expands the sampling distribution along distinct maneuver modes and breaks single-demonstration mode collapse. In the second stage, DIAL carries this expanded distribution into preference RL through multi-intent GRPO, which spans all intent classes within every preference group and prevents fine-tuning from re-collapsing around the currently preferred mode. Instantiated for end-to-end driving with eight rule-derived intents and evaluated on WOD-E2E: competitive Vision-to-Action (VA) and Vision-Language-Action (VLA) Supervised Finetuning (SFT) baselines plateau below the human-driven demonstration at best-of-128, with the strongest prior (RAP) capping at Rater Feedback Score (RFS) 8.5 even with best-of-64; intent-CFG sampling lifts this ceiling to RFS 9.14 at best-of-128, surpassing both the prior best (RAP 8.5) and the human-driven demonstration (8.13) for the first time; and multi-intent GRPO improves held-out RFS from 7.681 to 8.211, while every single-intent baseline peaks lower and degrades by training end. These results suggest that the bottleneck of preference RL on continuous-action policies trained from demonstrations is not only how to update the policy, but to expand and preserve the sampling distribution being optimized.
