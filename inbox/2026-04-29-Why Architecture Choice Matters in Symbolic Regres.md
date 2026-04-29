---
interest: medium
link: https://arxiv.org/abs/2604.23256
next_step: skim
priority: low
slack_ts: '1777434606.152339'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Why Architecture Choice Matters in Symbolic Regression
---
# Why Architecture Choice Matters in Symbolic Regression
> 原文: [https://arxiv.org/abs/2604.23256](https://arxiv.org/abs/2604.23256)

arXiv:2604.23256v1 Announce Type: new
Abstract: Symbolic regression discovers mathematical formulas from data. Some methods fix a tree of operators, assign learnable weights, and train by gradient descent. The tree's structure, which determines what operators and variables appear at each position, is chosen once and applied to every target. This paper tests whether that choice affects which targets are actually recovered. Three structures are compared, all sharing the same operator and target language but differing in how variables enter the tree; one is strictly more expressive. Across over 12,700 training runs, one structure recovers a target at 100% while another scores 0%, and the ranking reverses on a different target. Expressiveness guarantees that a solution exists in the search space, but not that gradient descent finds it: the most expressive structure fails on targets that a restricted alternative solves reliably. Switching the operator changes which targets succeed; reversing its gradient profile collapses recovery entirely. Balanced (non-chain) tree shapes are never recovered. These findings show that the optimization landscape, not expressiveness alone, determines what gradient-based symbolic regression recovers.
