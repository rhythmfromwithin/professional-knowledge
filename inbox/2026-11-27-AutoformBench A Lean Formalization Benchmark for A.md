---
title: "AutoformBench: A Lean Formalization Benchmark for Advanced Mathematics"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2611.33165
priority: high
status: unread
interest: medium
next_step: skim
---
# AutoformBench: A Lean Formalization Benchmark for Advanced Mathematics
> 原文: [https://arxiv.org/abs/2611.33165](https://arxiv.org/abs/2611.33165)

arXiv:2611.33165v1 Announce Type: new
Abstract: AI systems are increasingly capable of producing machine-checked Lean proofs of advanced mathematical results. Real mathematical formalization, however, is not isolated theorem proving: it requires building the definitions and intermediate lemmas that connect a result to a formal library. Existing evaluations often provide isolated theorem statements in settings where much of this supporting theory is already available in Mathlib. We introduce AutoformBench, a benchmark of 341 Lean 4 formalization tasks drawn from 24 advanced mathematical sources. Lean-experienced mathematicians formalized and audited each target statement, leaving the corresponding Lean proof to the evaluated agent. Each problem is embedded in a broader mathematical development: agents receive the informal proof but must translate it into Lean while constructing the missing definitions, intermediate lemmas, and supporting infrastructure. We compare the performance of frontier models on these problems. We find a largely shared difficulty frontier: success depends less on mathematical domain than on models' ability to construct missing formal infrastructure. Data and code at https://github.com/facebookresearch/autoformbench
