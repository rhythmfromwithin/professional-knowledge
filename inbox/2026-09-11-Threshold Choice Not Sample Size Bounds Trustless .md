---
title: "Threshold Choice, Not Sample Size, Bounds Trustless Verification of Nondeterministic Compound AI Workflows"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.10601
priority: low
status: unread
interest: medium
next_step: skim
---
# Threshold Choice, Not Sample Size, Bounds Trustless Verification of Nondeterministic Compound AI Workflows
> 原文: [https://arxiv.org/abs/2609.10601](https://arxiv.org/abs/2609.10601)

arXiv:2609.10601v1 Announce Type: new
Abstract: Compound AI pipelines chain LLM calls, retrievers, and tools and are nondeterministic: sampling, model updates, and volatile tool responses make one input yield different outputs across runs. Such pipelines increasingly run across edge, cloud, and orbital nodes owned by no single party, whose optimizations discard intermediate results before inspection. Verifying reproduction there means tolerating nondeterministic outputs, a node that may not report honestly, and intermittent access to any shared record; existing work addresses at most two at once. We give a protocol covering all three: it commits digests of each stage's inputs, outputs, and context under a policy digest pinning the metric and threshold, anchors them without trusting the executing node, defers under partition, and decides a challenge on the median of $k$ re-executions, with no quorum. Where that procedure breaks is the main result. On a synthetic HotpotQA pipeline a calibrated fixed threshold accepts 44 of 45 honest reproductions and rejects 104 of 105 divergent pairs, yet lets same-input fabrication through in 27 of 29 trials at k=5, more samples being no help since sampling sharpens an estimate without moving it. Holding that metric and this pipeline's re-execution spread fixed, the binding constraint is the threshold rather than the sample size: one derived per execution detects 19 of 29 where the best constant matched to the same zero honest rejections reaches 9, rejects no honest commitment at k=5 though 3 of 15 at k=3, and catches 11 of 15 of an attacker built against it, which has to aim at a target drawn only after its commitment exists. That rule is measured rather than deployed.
