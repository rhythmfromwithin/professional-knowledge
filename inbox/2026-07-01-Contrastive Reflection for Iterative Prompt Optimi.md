---
interest: medium
link: https://arxiv.org/abs/2606.30840
next_step: skim
priority: high
slack_ts: '1782880928.600849'
source: cs.AI - Artificial Intelligence
status: unread
title: Contrastive Reflection for Iterative Prompt Optimization
---
# Contrastive Reflection for Iterative Prompt Optimization
> 原文: [https://arxiv.org/abs/2606.30840](https://arxiv.org/abs/2606.30840)

arXiv:2606.30840v1 Announce Type: new
Abstract: LLM agents are becoming central to information retrieval: they issue retrieval queries, synthesize answers, and increasingly serve as judges for IR evaluation. Improving the prompts that control these agents is an optimization problem, but in applied IR settings it often looks less like blind search and more like debugging. Engineers need to know which behavior failed, which nearby behavior still worked, what distinguishes the two, and whether a prompt edit improves held-out quality without introducing regressions.
We present Contrastive Reflection, an iterative prompt-optimization framework for agentic IR workflows. The framework starts from a task-centric quality definition: QA agents expose retrieval or reasoning traces, and grading agents expose dimension-level scores and rationales. These structured traces are used to identify error-anchored behavioral slices, add nearby successful examples from the same region, and ask a Teacher LLM to propose a targeted prompt edit. Candidate edits are accepted only when validation performance improves, optionally subject to regression checks. We instantiate the framework with a tree-based slice selector, but the contribution is the contrastive reflection loop rather than the tree itself.
On a public HotpotQA retrieval-augmented QA setup, one tree-selected contrastive repair improves held-out exact-match accuracy from 51.4% to 60.4%. Failure-only and random-evidence variants improve less and break more previously correct examples. A light instruction-only comparison places the method near modern prompt optimizers: MIPROv2 reaches 59.4% and GEPA 57.0%. The result is an interpretable optimization loop for IR agents, aimed at making prompt repair more inspectable and validation-driven.
