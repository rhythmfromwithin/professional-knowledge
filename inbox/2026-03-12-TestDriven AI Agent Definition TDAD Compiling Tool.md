---
interest: medium
link: https://arxiv.org/abs/2603.08806
next_step: skim
priority: low
slack_ts: '1773888801.528199'
source: cs.SE - Software Engineering
status: unread
title: 'Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral
  Specifications'
---
# Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications
> 原文: [https://arxiv.org/abs/2603.08806](https://arxiv.org/abs/2603.08806)

arXiv:2603.08806v1 Announce Type: new
Abstract: We present Test-Driven AI Agent Definition (TDAD), a methodology that treats agent prompts as compiled artifacts: engineers provide behavioral specifications, a coding agent converts them into executable tests, and a second coding agent iteratively refines the prompt until tests pass. Deploying tool-using LLM agents in production requires measurable behavioral compliance that current development practices cannot provide. Small prompt changes cause silent regressions, tool misuse goes undetected, and policy violations emerge only after deployment. To mitigate specification gaming, TDAD introduces three mechanisms: (1) visible/hidden test splits that withhold evaluation tests during compilation, (2) semantic mutation testing via a post-compilation agent that generates plausible faulty prompt variants, with the harness measuring whether the test suite detects them, and (3) spec evolution scenarios that quantify regression safety when requirements change. We evaluate TDAD on SpecSuite-Core, a benchmark of four deeply-specified agents spanning policy compliance, grounded analytics, runbook adherence, and deterministic enforcement. Across 24 independent trials, TDAD achieves 92% v1 compilation success with 97% mean hidden pass rate; evolved specifications compile at 58%, with most failed runs passing all visible tests except 1-2, and show 86-100% mutation scores, 78% v2 hidden pass rate, and 97% regression safety scores. The implementation is available as an open benchmark at https://github.com/f-labs-io/tdad-paper-code.
