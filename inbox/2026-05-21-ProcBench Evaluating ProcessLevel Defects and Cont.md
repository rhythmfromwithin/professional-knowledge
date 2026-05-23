---
interest: medium
link: https://arxiv.org/abs/2605.20251
next_step: skim
priority: low
slack_ts: '1779508588.674379'
source: cs.SE - Software Engineering
status: unread
title: 'ProcBench: Evaluating Process-Level Defects and Control Preservation in LLM
  Coding Agents'
---
# ProcBench: Evaluating Process-Level Defects and Control Preservation in LLM Coding Agents
> 原文: [https://arxiv.org/abs/2605.20251](https://arxiv.org/abs/2605.20251)

arXiv:2605.20251v1 Announce Type: new
Abstract: Existing benchmarks for LLM coding agents mainly evaluate final outcomes, such as task completion, compilation success, and test pass rates. While these metrics are useful for measuring end-task capability, they provide limited visibility into how an execution unfolds and often miss recurrent process-level failures that arise during multi-step operation. We present ProcBench, a benchmark-oriented framework for evaluating coding-agent trajectories through process defects and control preservation. ProcBench organizes execution failures into a reusable ontology, standardizes heterogeneous logs into a unified trajectory representation, and reports calibrated risk-based scorecards instead of relying only on final outcomes. We instantiate ProcBench on an annotated set of 200 trajectories and apply it across three coding-agent benchmarks: AndroidBench, TerminalBench, and SWE-bench-Verified. Our results suggest that ProcBench can be instantiated with useful reliability, that calibration improves the empirical interpretability of defect findings relative to direct thresholding, and that process-aware scorecards provide diagnostic distinctions beyond conventional outcome-based evaluation. We also discuss limitations, including annotation dependence, partial observability for some defect classes, and the need for broader external validation.
