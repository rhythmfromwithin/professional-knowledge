---
interest: medium
link: https://arxiv.org/abs/2606.07846
next_step: skim
priority: medium
slack_ts: '1780978309.669909'
source: cs.DC - Distributed Computing
status: unread
title: 'Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension
  Method'
---
# Cost-Aware Speculative Execution for LLM-Agent Workflows: An Integrated Five-Dimension Method
> 原文: [https://arxiv.org/abs/2606.07846](https://arxiv.org/abs/2606.07846)

arXiv:2606.07846v1 Announce Type: new
Abstract: LLM-agent workflows chain model calls and tool invocations, and spend most of their wall-clock time waiting on upstream operations before downstream ones can start. Speculative execution can reclaim that idle time by launching a downstream operation with a predicted upstream input, but here each speculation costs real money (per-token billing) and its success probability is hard to estimate and drifts over time. This paper presents a method organized around five design decisions: (D1) start a downstream operation before its upstream completes; (D2) price each speculation in real dollars at separate input and output rates; (D3) expose a single operator dial for latency versus cost; (D4) decide via an expected-value rule with a failure-weighted cost term and a preference-adjusted threshold; and (D5) estimate the success probability with a Bayesian Beta-Binomial posterior whose prior is keyed to a dependency-type taxonomy. Variants of these ideas appear in recent work; the combination, with every decision logged in dollars, is what is new. The rule fires only on edges passing an admissibility precondition (side-effect-free, idempotent, or stageable behind a commit barrier), since a wrong speculation is rolled back by re-execution, which refunds tokens but cannot un-send an irreversible side effect. We specify the runtime mechanics, a closed-form result that the rule self-limits as the upstream branching factor grows, a five-stage calibration pipeline (offline replay, shadow, canary, online calibration, drift-triggered kill-switch), and a workload-fit rubric over eight production archetypes. Contrast tables against the four closest published systems (DSP, Speculative Actions v2, Sherlock, B-PASTE) show differentiators on every dimension, and a synthetic validation suite confirms the predicted decision boundary, probability threshold, posterior recovery, and streaming-cancellation behavior.
