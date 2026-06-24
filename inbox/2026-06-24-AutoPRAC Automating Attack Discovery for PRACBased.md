---
interest: medium
link: https://arxiv.org/abs/2606.23905
next_step: skim
priority: low
slack_ts: '1782274335.024989'
source: cs.CR - Cryptography and Security
status: unread
title: 'AutoPRAC: Automating Attack Discovery for PRAC-Based Rowhammer Defenses using
  Model Checkers'
---
# AutoPRAC: Automating Attack Discovery for PRAC-Based Rowhammer Defenses using Model Checkers
> 原文: [https://arxiv.org/abs/2606.23905](https://arxiv.org/abs/2606.23905)

arXiv:2606.23905v1 Announce Type: new
Abstract: Per-Row Activation Counting (PRAC) in DDR5 is a specification to mitigate Rowhammer attacks by tracking activations per row and triggering mitigative refreshes when needed. However, the security of PRAC designs is currently evaluated using human-crafted attack patterns and we lack formal verification of their security properties, or automated techniques to detect implementation flaws. In this work, we present AutoPRAC, the first automated technique to test the security of PRAC-based defenses using model checkers. AutoPRAC models PRAC implementations as bounded state machines and checks security-critical safety properties against a worst-case oracle attacker. If a property is violated, the framework produces a concrete counterexample trace corresponding to a successful attack. Using AutoPRAC, we uncover a previously unreported flaw in MOAT, a state-of-the-art PRAC defense, in its counter-reset policy that allows up to 34 activations to go undetected above the Rowhammer threshold. Our results demonstrate that AutoPRAC can automatically discover subtle security flaws in Rowhammer mitigations and serves as an early-stage design aid for attack discovery on PRAC designs.
