---
interest: medium
link: https://arxiv.org/abs/2604.00085
next_step: skim
priority: high
slack_ts: '1775270911.419129'
source: cs.AI - Artificial Intelligence
status: unread
title: 'One Panel Does Not Fit All: Case-Adaptive Multi-Agent Deliberation for Clinical
  Prediction'
---
# One Panel Does Not Fit All: Case-Adaptive Multi-Agent Deliberation for Clinical Prediction
> 原文: [https://arxiv.org/abs/2604.00085](https://arxiv.org/abs/2604.00085)

arXiv:2604.00085v1 Announce Type: new
Abstract: Large language models applied to clinical prediction exhibit case-level heterogeneity: simple cases yield consistent outputs, while complex cases produce divergent predictions under minor prompt changes. Existing single-agent strategies sample from one role-conditioned distribution, and multi-agent frameworks use fixed roles with flat majority voting, discarding the diagnostic signal in disagreement. We propose CAMP (Case-Adaptive Multi-agent Panel), where an attending-physician agent dynamically assembles a specialist panel tailored to each case's diagnostic uncertainty. Each specialist evaluates candidates via three-valued voting (KEEP/REFUSE/NEUTRAL), enabling principled abstention outside one's expertise. A hybrid router directs each diagnosis through strong consensus, fallback to the attending physician's judgment, or evidence-based arbitration that weighs argument quality over vote counts. On diagnostic prediction and brief hospital course generation from MIMIC-IV across four LLM backbones, CAMP consistently outperforms strong baselines while consuming fewer tokens than most competing multi-agent methods, with voting records and arbitration traces offering transparent decision audits.
