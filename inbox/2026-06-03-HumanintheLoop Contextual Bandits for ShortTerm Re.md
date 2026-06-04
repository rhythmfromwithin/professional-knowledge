---
interest: medium
link: https://arxiv.org/abs/2606.02595
next_step: skim
priority: high
slack_ts: '1780548663.579619'
source: cs.LG - Machine Learning
status: unread
title: 'Human-in-the-Loop Contextual Bandits for Short-Term Rental Dynamic Pricing:
  Structural Equivalence of Historical Warm-Up and Approval-Gated Live Learning'
---
# Human-in-the-Loop Contextual Bandits for Short-Term Rental Dynamic Pricing: Structural Equivalence of Historical Warm-Up and Approval-Gated Live Learning
> 原文: [https://arxiv.org/abs/2606.02595](https://arxiv.org/abs/2606.02595)

arXiv:2606.02595v1 Announce Type: new
Abstract: Dynamic pricing in short-term rental (STR) markets presents a distinctive challenge for online learning algorithms: pricing decisions carry significant financial risk, operators require explainability, and market feedback is sparse (one booking outcome per listed night). We introduce the Human-in-the-Loop Gated Bandit (HITL-GB) framework, in which a contextual bandit algorithm generates price recommendations but a human agent retains authority to accept, modify, or reject each recommendation before it is applied. We show that under this approval constraint, historical pricing data -- collected under a prior deterministic policy -- is structurally equivalent to on-policy warm-up data for initialising the bandit's posterior, bypassing the weeks-to-months cold-start period that renders pure online bandit learning impractical in sparse-feedback markets. We formalise the approval-gated reward signal, derive a regularised ridge-regression warm-up procedure from historical episodes, and validate the approach on real STR production data (anonymised urban market, 2 rooms, April 2022 -- April 2026, 1,461 nightly pricing episodes). Our warm-up procedure compresses effective cold-start from ~150 episodes to ~30 episodes when initialising agents from the Hierarchical Factored Thompson Sampling (HF-TS) family. We further argue that the structural equivalence result is domain-agnostic: any high-stakes domain where human approval is legally or operationally required -- including clinical drug dosing, credit origination, content moderation, and radiological diagnosis -- satisfies the same conditions and benefits from the same warm-up strategy. In regulated industries, mandatory human oversight is thus a statistical asset rather than a deployment constraint.
