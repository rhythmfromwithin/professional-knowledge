---
title: "Falsifiable Release Gates for Self-Improving Systems"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2607.13070
priority: low
status: unread
interest: medium
next_step: skim
---
# Falsifiable Release Gates for Self-Improving Systems
> 原文: [https://arxiv.org/abs/2607.13070](https://arxiv.org/abs/2607.13070)

arXiv:2607.13070v1 Announce Type: new
Abstract: Safety claims on self-improving agent runtimes are almost always self-graded: a policy file, a guardrail, or a README commitment. We describe falsifiable release gates, and a methodology to build and validate such systems, such that every new capability must pass a pre-specified, machine-verifiable acceptance suite before it ships, and a fixed set of standing invariants is preserved at each gate. I think we applied the method in the Antahkarana, an open runtime, via seven gates from basic observability into a self governing loop that suggests changes to its own policy. no action goes to an effector without a safety-critical property capability token minted by a control ring is exhaustively machine-checked over the one million recorded reachable state space of a bounded model and re-checked against execution traces. A purposely broken model gives the shortest counterexample, so the checker has teeth, is apparent. The self-enhancement loop is positively Constrained: the entire write surface is policy rules, tightening changes. may auto-apply loosening changes always require a human merge and a proposal autoclosed is one that mispredicts its own effect; We publish the acceptance measured results for all the seven gates, define precisely the scope of each claim (a bounded of the coordination skeleton (not the learned components) and free the runtime, either command line tools and the gate suite, so the results reproduce, and gates can run against other agent frameworks. Reviewers may repeat the single command central non-bypass in seconds.
