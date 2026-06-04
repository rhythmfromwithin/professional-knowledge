---
title: "Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2606.04017
priority: low
status: unread
interest: medium
next_step: skim
---
# Neither Layer Alone: Epistemic Integrity Requires Hierarchical Joint Design for Long-Running AI Agents
> 原文: [https://arxiv.org/abs/2606.04017](https://arxiv.org/abs/2606.04017)

arXiv:2606.04017v1 Announce Type: new
Abstract: Long-running AI agents fail not only when inference fails or tools are underspecified, but when independently evolving model and harness layers change the semantics of belief, capability, and goal commitments across their boundary - a failure class this paper terms Interface Volatility. This paper argues that Agent Epistemic Integrity (AEI) must be treated as a first-class architectural constraint, achievable only through joint model-harness design organized around an explicit interface contract. The central claim is that the model-harness interface contract is the precondition for joint design; its operational form is a four-level hierarchy - goal validity, action-archetype sequencing, tool-instance selection, and invocation-level failure discrimination - that specifies what the boundary must preserve and what structured outputs the model must return for the contract to hold across levels. This reframes long-running agent design away from flat action loops and toward contract-preserving control over persistent state. Evaluation and training should therefore derive from the contract itself, testing whether belief, tool, and goal commitments hold across session boundaries and independent layer upgrades.
