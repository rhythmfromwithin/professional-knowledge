---
interest: medium
link: https://arxiv.org/abs/2611.13681
next_step: skim
priority: low
slack_ts: '1794376039.248419'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'A Functional Preservation Score for Auditing Connectome Operations: Compression,
  Alignment, Transport, and Local-Rule Writing'
---
# A Functional Preservation Score for Auditing Connectome Operations: Compression, Alignment, Transport, and Local-Rule Writing
> 原文: [https://arxiv.org/abs/2611.13681](https://arxiv.org/abs/2611.13681)

arXiv:2611.13681v1 Announce Type: new
Abstract: We introduce the Functional Preservation Score (FPS), a null-normalised, behaviourally grounded measure of how much of a neural network's input-output function survives a structural operation, and use it to audit the operations underlying speculative "mind-migration" pipelines on public data that runs on a single laptop. Across five pre-registered studies on the C. elegans connectome, whole-brain calcium activity, and hippocampal replay, FPS yields two positive characterisations and a three-part negative. Low-bit quantisation of a real connectome exhibits a structure-dependent sparsity floor: uniform int4/ternary quantisation is forced to roughly 73%/98% effective sparsity because heavy-tailed integer synaptic weights round to zero, while mixed-precision protection of hub neurons lowers these floors to about 27%/32%. Decoded hippocampal replay sequences compress heavily yet remain identifiable at a cross-validated top-1 accuracy of 0.69 (95% CI [0.63, 0.74]; chance 0.125; permutation p < 1e-3) from latents of order 10-50 bits per event, and a bounded incremental store shows a graceful-versus-cliff capacity trade-off. The migration pipeline fails in simulation at each stage for largely independent reasons: the putative "identity payload" is not a functionally separable module (p >= 0.16 at every tested size); cross-individual functional transport via Gromov-Wasserstein collapses once the target's wiring is respected (fidelity 1.00 to 0.40, [0.31, 0.49], p < 1e-3) or alignment is imperfect (0.06, [0.00, 0.13]); and biologically plausible local plasticity cannot reach the function the target topology provably admits (gap 0.45, [0.27, 0.64], p < 1e-3, d = 2.0). We release FPS, the data loaders, and all operations as a toolkit. All results are at nematode / small-network scale and concern coherence in simulation, not the feasibility of reading or writing a living brain.
