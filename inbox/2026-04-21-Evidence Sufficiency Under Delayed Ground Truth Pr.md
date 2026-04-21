---
interest: medium
link: https://arxiv.org/abs/2604.15740
next_step: skim
priority: medium
slack_ts: '1776742304.206259'
source: cs.CY - Computers and Society
status: unread
title: 'Evidence Sufficiency Under Delayed Ground Truth: Proxy Monitoring for Risk
  Decision Systems'
---
# Evidence Sufficiency Under Delayed Ground Truth: Proxy Monitoring for Risk Decision Systems
> 原文: [https://arxiv.org/abs/2604.15740](https://arxiv.org/abs/2604.15740)

arXiv:2604.15740v1 Announce Type: new
Abstract: Machine learning systems in fraud detection, credit scoring, and clinical risk assessment operate under delayed ground truth: outcome labels arrive days to months after the decision they evaluate. During this blind period, governance evidence degrades through mechanisms that neither drift detection methods nor governance frameworks adequately address. This paper formalizes an evidence sufficiency model with four dimensions (completeness, freshness, reliability, representativeness) and a decision-readiness gate that quantifies how label latency degrades evidence quality. The model maps three drift types to dimension-specific degradation trajectories. A complementary proxy indicator framework comprising seven measurement categories estimates sufficiency degradation without labels, with explicit coverage mapping and characterized blind spots per drift type. Evaluation on the IEEE-CIS Fraud Detection dataset (~590K transactions) with controlled drift injection shows that composite proxy monitoring detects covariate and mixed drift with 100% detection rate, while concept drift without feature change remains undetected -- consistent with the theoretical impossibility of unsupervised detection when P(X) is unchanged. Blind period simulation confirms monotone sufficiency degradation, with concept drift degrading fastest (S=0.242 at day 60 vs 0.418 for no-drift). The framework contributes a governance sufficiency monitoring instrument; its value lies in translating drift signals into auditable sufficiency assessments with characterized blind spots. Mapping sufficiency levels to governance actions requires deployment-specific calibration beyond this study's scope.
