---
title: "Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.19329
priority: low
status: unread
interest: medium
next_step: skim
---
# Goedel-Code-Prover: Hierarchical Proof Search for Open State-of-the-Art Code Verification
> 原文: [https://arxiv.org/abs/2603.19329](https://arxiv.org/abs/2603.19329)

arXiv:2603.19329v1 Announce Type: new
Abstract: Large language models (LLMs) can generate plausible code but offer limited guarantees of correctness. Formally verifying that implementations satisfy specifications requires constructing machine-checkable proofs, a task that remains beyond current automation. We propose a hierarchical proof search framework for automated code verification in Lean~4 that decomposes complex verification goals into structurally simpler subgoals before attempting tactic-level proving. Central to our approach is a principled decomposition score that combines constructive justification with structural effectiveness. Crucially, this score serves as both the training reward and the inference-time ranking criterion, ensuring strict alignment between optimization and deployment. We train Goedel-Code-Prover-8B, a single unified policy for both decomposition and completion, via supervised initialization followed by hybrid reinforcement learning, where a continuous decomposition reward drives planning exploration while supervised replay stabilizes proof generation. On three Lean-based code verification benchmarks comprising 427 tasks, our 8B-parameter model achieves a 62.0\% prove success rate, a 2.6$\times$ improvement over the strongest baseline, surpassing neural provers up to 84$\times$ larger. We further observe consistent inference-time scaling: success rates improve monotonically with search iterations and sampling budget, with our trained model achieving greater efficiency than frontier off-the-shelf models of comparable scale.
