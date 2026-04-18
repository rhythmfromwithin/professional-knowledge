---
title: "Geometrically Consistent Multi-View Scene Generation from Freehand Sketches"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.14302
priority: medium
status: unread
interest: medium
next_step: skim
---
# Geometrically Consistent Multi-View Scene Generation from Freehand Sketches
> 原文: [https://arxiv.org/abs/2604.14302](https://arxiv.org/abs/2604.14302)

arXiv:2604.14302v1 Announce Type: new
Abstract: We tackle a new problem: generating geometrically consistent multi-view scenes from a single freehand sketch. Freehand sketches are the most geometrically impoverished input one could offer a multi-view generator. They convey scene intent through abstract strokes while introducing spatial distortions that actively conflict with any consistent 3D interpretation. No prior method attempts this; existing multi-view approaches require photographs or text, while sketch-to-3D methods need multiple views or costly per-scene optimisation.
We address three compounding challenges; absent training data, the need for geometric reasoning from distorted 2D input, and cross-view consistency, through three mutually reinforcing contributions: (i) a curated dataset of $\sim$9k sketch-to-multiview samples, constructed via an automated generation and filtering pipeline; (ii) Parallel Camera-Aware Attention Adapters (CA3) that inject geometric inductive biases into the video transformer; and (iii) a Sparse Correspondence Supervision Loss (CSL) derived from Structure-from-Motion reconstructions.
Our framework synthesizes all views in a single denoising process without requiring reference images, iterative refinement, or per-scene optimization. Our approach significantly outperforms state-of-the-art two-stage baselines, improving realism (FID) by over 60% and geometric consistency (Corr-Acc) by 23%, while providing up to a 3.7$\times$ inference speedup.
