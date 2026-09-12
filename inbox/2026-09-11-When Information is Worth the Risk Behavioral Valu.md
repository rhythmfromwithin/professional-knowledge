---
interest: medium
link: https://arxiv.org/abs/2609.10726
next_step: skim
priority: medium
slack_ts: '1789186434.561569'
source: cs.RO - Robotics
status: unread
title: 'When Information is Worth the Risk: Behavioral Valuation for Hazardous Robotic
  Exploration'
---
# When Information is Worth the Risk: Behavioral Valuation for Hazardous Robotic Exploration
> 原文: [https://arxiv.org/abs/2609.10726](https://arxiv.org/abs/2609.10726)

arXiv:2609.10726v1 Announce Type: new
Abstract: Hazardous robotic exploration requires robots to map spatial risks, such as unsafe terrain, radiation, fire, mines, or structural damage, while operating where collecting information can itself cause failure. A highly informative path may expose the robot to hazards, terminate execution, and prevent future observations. Hazardous exploration therefore requires deciding not only where uncertainty is largest, but when reducing it is worth the risk. This paper introduces a valuation-layer view of this problem. We keep the belief update, sensor model, physical risk model, and finite-horizon informative planner fixed, and change only the scalar objective used to rank feasible paths. Within this framework, we introduce a risk-augmented Behavioral Information objective based on Prelec probability weighting, yielding an interpretable family of conservative-to-aggressive information-risk valuations. Theoretically, we show that valuation parameters create switching boundaries between high-information/high-risk and lower-information/lower-risk paths, and induce a transformed Pareto-frontier structure over feasible exploration policies. Large-scale failure-truncated grid-world experiments show that valuation alone reshapes the information-risk frontier. Shannon information planning remains a strong raw-information baseline, while risk-aware objectives can reduce hazard exposure and robot losses by avoiding failures that truncate future sensing. Risk-augmented Behavioral valuation is Pareto-competitive with standard risk-aware baselines and provides interpretable conservative and intermediate regimes. These results support a framework in which robots reason not only about how much uncertainty an action reduces, but whether that reduction is worth the risk required to obtain it.
