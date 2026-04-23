---
interest: medium
link: https://arxiv.org/abs/2604.18792
next_step: skim
priority: low
slack_ts: '1776915213.043759'
source: cs.SE - Software Engineering
status: unread
title: 'Tractable Verification of Model Transformations: A Cutoff-Theorem Approach
  for DSLTrans'
---
# Tractable Verification of Model Transformations: A Cutoff-Theorem Approach for DSLTrans
> 原文: [https://arxiv.org/abs/2604.18792](https://arxiv.org/abs/2604.18792)

arXiv:2604.18792v1 Announce Type: new
Abstract: Model transformations are central to MDE, but formal verification is difficult because mainstream transformation languages are undecidable. DSLTrans was designed to be Turing-incomplete to improve verifiability, yet earlier verification based on path-condition enumeration still suffered exponential blow-up and did not scale to realistic cases.
We present a tractable verification workflow for DSLTrans and formalize when it is complete. The method combines three contributions: (i) a Cutoff Theorem proving that bounded model checking is complete for a precise DSLTrans fragment and positive existence/traceability properties, turning an infinite search into a finite computable bound; (ii) composable, soundness-preserving optimizations (per-class bounds, CEGAR-based fragment verification, and trace-aware dependency analysis) that reduce SMT encoding size; and (iii) a Z3-based implementation evaluated on realistic transformations from the ATL Zoo and related benchmarks.
On 29 concrete transformations and 899 properties spanning compiler lowering, schema translation, behavioral modeling, graph mapping, and stress tests, 552 properties are proved, 345 produce concrete counterexamples (including intentional negative and boundary cases), and only 2 remain undecided within timeout. For properties beyond the tractability budget, we introduce tractability-driven refinement (precondition specialization, postcondition decomposition, and transformation instrumentation), achieving up to 112x speedup while eliminating spurious counterexamples. The workflow is supported by a web IDE and a concrete execution engine for runtime validation.
