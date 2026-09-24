---
interest: medium
link: https://arxiv.org/abs/2609.26811
next_step: skim
priority: high
slack_ts: '1790223784.332129'
source: cs.LG - Machine Learning
status: unread
title: 'The Drift Contract: Spectral Updates for Depth-Robust Local Learning'
---
# The Drift Contract: Spectral Updates for Depth-Robust Local Learning
> 原文: [https://arxiv.org/abs/2609.26811](https://arxiv.org/abs/2609.26811)

arXiv:2609.26811v1 Announce Type: new
Abstract: Local learning trains each layer with its own auxiliary loss and no global backward pass, which makes layer updates structurally parallel. Two problems have kept it marginal: accuracy degrades as depth grows, and hyperparameters are fragile. We apply Muon-style spectral update geometry (momentum orthogonalization with spectral step scaling) to per-layer local updates, an intersection not previously studied. On CIFAR-10 MLP benchmarks with local linear heads, a single step-size setting is the best value in our tested grids from width 128 to 2048 and from depth 12 to 48, while local Adam requires re-tuning along both axes and still collapses at depth 48 (31.3 percent re-tuned per depth, 19 percent with its depth-12 setting transferred, vs 42.7 percent for the spectral update at its unchanged setting). At five seeds and width 512 the spectral update leads local Adam by a clear margin (48.9 +/- 0.5 vs 46.6 +/- 0.3). Prospectively specified controls attribute the transfer and most of the depth robustness to the spectral geometry itself rather than to any step-size rule on top of it. We additionally formulate the step size as a drift contract, lr = epsilon / RMS(input), which bounds each layer's weight-induced pre-activation change per step, conditioned on its current input. The contract yields a small gain over the best fixed learning rate where that baseline is measured, makes the step size interpretable, and provides a per-layer, input-conditioned drift bound that standard optimizers do not offer. We report one negative result: with RMSNorm and weight decay in the trunk, the stability benefit of spectral updates accrues to global rather than local training, so the local advantage concentrates precisely where normalization is absent.
