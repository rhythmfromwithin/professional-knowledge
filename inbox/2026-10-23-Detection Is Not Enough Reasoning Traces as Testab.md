---
title: "Detection Is Not Enough: Reasoning Traces as Testable Program Hypotheses"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2610.30200
priority: low
status: unread
interest: medium
next_step: skim
---
# Detection Is Not Enough: Reasoning Traces as Testable Program Hypotheses
> 原文: [https://arxiv.org/abs/2610.30200](https://arxiv.org/abs/2610.30200)

arXiv:2610.30200v1 Announce Type: new
Abstract: When a language model is deployed, no reference solution exists, so the reasoning trace it writes is the only evidence for judging its answer. The reference-free substitutes each fail differently: self-assessment degrades the answer it was meant to protect, sampling agreement measures stability rather than correctness, and perturbation studies read the expected answer off a human-written template, grading a model rather than a trace. We ask how far a single trace can be verified with no reference solution, no judge model and no weight update, and find, for a frozen LLaMA-2-7B-chat on GSM8K, that detection is not what limits such a pipeline. Checking a trace against itself reaches an AUROC of 0.741 and stops there for a structural reason: two thirds of wrong traces state no false equation, having executed a mistaken plan correctly, and on wrong-plan failures the detector flags a wrong trace less often than a right one. A candidate-derived metamorphic probe exposes many of these failures: we abstract the trace into a program over the question's quantities, perturb one quantity, execute the program, and ask the model the rewritten question once, so every trace supplies its own test. Valid perturbations exist for 937 of 1,319 test questions (71.0%); among the 847 that also have a parseable first trace, supported traces are correct 60.6% of the time against a 31.6% base rate, although the probe also refutes 45.5% of correct traces. No tested policy yields a statistically significant improvement in accuracy. A flag earns its retry only when detector precision exceeds D/(R+D), where R and D are the rates at which a retry repairs a wrong trace and damages a correct one; our repair rate is so low that, at the same retry budget, even a perfect detector would recover an estimated 66 of 1,319 questions. Repair, not detection, is the open problem.
