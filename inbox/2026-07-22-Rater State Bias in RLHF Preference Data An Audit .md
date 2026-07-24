---
interest: medium
link: https://arxiv.org/abs/2607.16195
next_step: skim
priority: high
slack_ts: '1784863623.011139'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Rater State Bias in RLHF Preference Data: An Audit Framework'
---
# Rater State Bias in RLHF Preference Data: An Audit Framework
> 原文: [https://arxiv.org/abs/2607.16195](https://arxiv.org/abs/2607.16195)

arXiv:2607.16195v1 Announce Type: new
Abstract: We identify a structured confound in Reinforcement Learning from Human Feedback (RLHF). Pairwise preference labels are intended to reflect the compared outputs, but they may also reflect the rater's state during annotation. Under sustained stressful or distressing conditions, raters' preferences may shift over time. As a result, preference data can encode rater state alongside judgments about response quality. These shifts differ from ordinary disagreement or random label noise. They are state dependent, can be shared across annotators working under similar conditions, and can propagate through reward modeling and policy optimization. We therefore propose rater state shift as a plausible and testable source of structured bias in RLHF preference data. This paper develops a hypothesis and an audit framework for studying this source of bias. We define rater state shift, rater state confound, and correlated rater state bias. We also define survival level emotional authenticity as a measurable response pattern using lexical, pragmatic, discourse, and safety related features. We analyze how correlated rater state bias can survive aggregation and enter learned reward signals. We derive five falsifiable predictions and effect size thresholds for an initial audit. Finally, we present an audit protocol and pilot study plan that can be applied to publicly available instruction tuned models. We do not infer the training history of any specific deployed model. Our goal is to isolate a plausible and testable source of structured bias in RLHF preference data.
