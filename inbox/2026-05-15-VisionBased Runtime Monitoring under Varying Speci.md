---
interest: medium
link: https://arxiv.org/abs/2605.13923
next_step: skim
priority: high
slack_ts: '1778817957.037299'
source: cs.LG - Machine Learning
status: unread
title: Vision-Based Runtime Monitoring under Varying Specifications using Semantic
  Latent Representations
---
# Vision-Based Runtime Monitoring under Varying Specifications using Semantic Latent Representations
> 原文: [https://arxiv.org/abs/2605.13923](https://arxiv.org/abs/2605.13923)

arXiv:2605.13923v1 Announce Type: new
Abstract: We study certified runtime monitoring of past-time signal temporal logic (ptSTL) from visual observations under partial observability. The monitor must infer safety-relevant quantities from images and provide finite-sample guarantees, while being \emph{reusable}: once trained and calibrated, it should certify any formula in a target fragment without per-formula retraining. For fragments induced by a finite dictionary of temporal atoms, we prove that the \emph{semantic basis}, the vector of atom robustness scores, is the minimum prediction target within the class of monotone, 1-Lipschitz reusable interfaces: any formula is evaluated by a deterministic decoder derived from the parse tree, and a single conformal calibration pass certifies the entire fragment with no union bound. We also introduce a \emph{rolling prediction monitor} that predicts only current predicate values and reconstructs temporal history online; this is easier to learn but grows conservative at long horizons. On a pedestrian-crossroad benchmark, rolling achieves tighter certified bounds at short horizons while the semantic-basis monitor is up to 4-times tighter at long horizons. We validate the presented monitors on real-world Waymo driving data, where both monitors satisfy the conformal coverage guarantee empirically.
