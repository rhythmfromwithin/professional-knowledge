---
title: "Navigating Epistemic Parity in LLM Agents: A Benchmark for Cross-Source Conflict Resolution Between Memory and Procedural Skills"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.33128
priority: low
status: unread
interest: medium
next_step: skim
---
# Navigating Epistemic Parity in LLM Agents: A Benchmark for Cross-Source Conflict Resolution Between Memory and Procedural Skills
> 原文: [https://arxiv.org/abs/2610.33128](https://arxiv.org/abs/2610.33128)

arXiv:2610.33128v1 Announce Type: new
Abstract: Production LLM agents increasingly run episodic memory pipelines and procedural skill modules (e.g., SKILL.md files) in tandem. Both are injected into the same context region with no defined precedence, so they can issue contradictory instructions that no instruction hierarchy resolves, a condition we term epistemic parity. We introduce a benchmark for measuring how LLM agents adjudicate such cross-source conflicts. We (i) develop a four-way taxonomy of memory-skill contradictions (factual, format, procedural, permission); (ii) instantiate 52 scenarios under a tripartite test-case anatomy (memory injection, skill injection, ambiguous user task), scored almost entirely by deterministic checkers over tool-call payloads and output structure; and (iii) run each scenario under three context conditions to isolate positional bias, measure the efficacy of an explicit precedence directive, and classify disclosure behavior, quantifying silent adjudication: resolving a conflict without telling the user. Across 1,383 runs on three open-weight models, neither source wins uniformly: resolution depends jointly on conflict type, model, and injection order. Moving the skill block nearer the task raises its win rate in all six factual and procedural cells (sign test, p = 0.031) but reverses for format conflicts, indicating that adjudication tracks token placement rather than source semantics. An explicit "skill takes absolute precedence" directive raises skill compliance on the two stronger models yet leaves 3-10% residual non-compliance, and moves the smallest model's factual and procedural resolution in the wrong direction. Most consequentially, in 98.8% of runs where the agent acted through a tool call it emitted no accompanying text at all, and 89% of all runs disclosed nothing about the contradiction: silent adjudication is the default. Code, scenarios, and raw outputs are public.
