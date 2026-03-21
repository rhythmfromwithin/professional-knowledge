---
interest: medium
link: https://arxiv.org/abs/2603.15641
next_step: skim
priority: low
slack_ts: '1774060656.293349'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Form Follows Function: Recursive Stem Model'
---
# Form Follows Function: Recursive Stem Model
> 原文: [https://arxiv.org/abs/2603.15641](https://arxiv.org/abs/2603.15641)

arXiv:2603.15641v1 Announce Type: cross
Abstract: Recursive reasoning models such as Hierarchical Reasoning Model (HRM) and Tiny Recursive Model (TRM) show that small, weight-shared networks can solve compute-heavy and NP puzzles by iteratively refining latent states, but their training typically relies on deep supervision and/or long unrolls that increase wall-clock cost and can bias the model toward greedy intermediate behavior. We introduce Recursive Stem Model (RSM), a recursive reasoning approach that keeps the TRM-style backbone while changing the training contract so the network learns a stable, depth-agnostic transition operator. RSM fully detaches the hidden-state history during training, treats early iterations as detached "warm-up" steps, and applies loss only at the final step. We further grow the outer recursion depth $H$ and inner compute depth $L$ independently and use a stochastic outer-transition scheme (stochastic depth over $H$) to mitigate instability when increasing depth. This yields two key capabilities: (i) $>20\times$ faster training than TRM while improving accuracy ($\approx 5\times$ reduction in error rate), and (ii) test-time scaling where inference can run for arbitrarily many refinement steps ($\sim 20,000 H\_{\text{test}} \gg 20 H\_{\text{train}}$), enabling additional "thinking" without retraining. On Sudoku-Extreme, RSM reaches 97.5% exact accuracy with test-time compute (within ~1 hour of training on a single A100), and on Maze-Hard ($30 \times 30$) it reaches ~80% exact accuracy in ~40 minutes using attention-based instantiation. Finally, because RSM implements an iterative settling process, convergence behavior provides a simple, architecture-native reliability signal: non-settling trajectories warn that the model has not reached a viable solution and can be a guard against hallucination, while stable fixed points can be paired with domain verifiers for practical correctness checks.
