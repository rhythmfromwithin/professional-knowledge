---
interest: medium
link: https://arxiv.org/abs/2611.05448
next_step: skim
priority: medium
slack_ts: '1794029935.472849'
source: cs.RO - Robotics
status: unread
title: 'Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language
  World Model'
---
# Jev with Foresight: Safe Language-Guided Autonomous Driving via a Language World Model
> 原文: [https://arxiv.org/abs/2611.05448](https://arxiv.org/abs/2611.05448)

arXiv:2611.05448v1 Announce Type: new
Abstract: Large language models understand passengers' driving commands, but as driving agents they reason in generated text for seconds and must infer each action's consequences implicitly from the scene. We present Jev-AD, which pairs Jev, a typed decision model that answers predefined questions with probabilities, not generated text, with a language world model that predicts for every candidate action how nearby vehicles move over the next two seconds. Code turns these predictions into foreseen consequences, which Jev compares instead of inferring them from coordinates. In simulated highway merging (500 car-episodes), this foresight lowers the same decision model's collision rate from 26.0% to 2.4% at 0.25 seconds per decision, and Jev-AD achieves the passenger's intent in 93% of free-form command trials. In 500 replayed real-world NGSIM episodes, foresight lowers the collision rate from 48.2% to 2.8%, and the world model, learned from this traffic, foresees 93% of dangerous actions. Project page: https://ys-qu.github.io/jev-ad-website.
