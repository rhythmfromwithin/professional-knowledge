---
interest: medium
link: https://arxiv.org/abs/2610.33044
next_step: skim
priority: medium
slack_ts: '1793164456.299459'
source: cs.CV - Computer Vision
status: unread
title: 'EKT-Router: Expert-Evidence Alignment for Embodied Vision-Language Models'
---
# EKT-Router: Expert-Evidence Alignment for Embodied Vision-Language Models
> 原文: [https://arxiv.org/abs/2610.33044](https://arxiv.org/abs/2610.33044)

arXiv:2610.33044v1 Announce Type: new
Abstract: Embodied vision-language models must answer questions from partial, evolving observations. Their success depends on both the reasoning capability selected and the evidence available to it. Expert routers adapt internal computation, while tool-augmented systems acquire external evidence; choosing these independently can leave a suitable expert without the evidence it needs. We introduce EKT-Router, a bounded framework that jointly selects a capability expert, optional knowledge, and perceptual tools. Outcome-derived signatures represent the overlapping strengths of General, Spatial Reasoning, and Spatiotemporal experts. A joint utility scores complete expert-evidence routes under a call budget. After acquisition, a packet verifier admits valid evidence with positive predicted expert-conditioned gain. The selected expert then answers once, reverting to the unchanged observation if all packets are rejected. Across 6 embodied QA benchmarks, EKT-Router achieves a mean score of 61.4, the highest among the compared systems, and averages 74.7 on 10 general vision-language benchmarks. With all external evidence disabled, question-conditioned expert selection alone improves over the best fixed expert by 1.75 points. Ablations show that learned routing is the dominant component and that knowledge and perception are complementary.
