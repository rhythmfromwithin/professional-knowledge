---
title: "Local Synaptic Rules Can Implement a SIGReg Gradient Without Backpropagation"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2607.21622
priority: low
status: unread
interest: medium
next_step: skim
---
# Local Synaptic Rules Can Implement a SIGReg Gradient Without Backpropagation
> 原文: [https://arxiv.org/abs/2607.21622](https://arxiv.org/abs/2607.21622)

arXiv:2607.21622v1 Announce Type: new
Abstract: We prove that two canonical local synaptic learning rules, the potentiation arm of spike-timing-dependent plasticity (STDP$^+$) and homeostatic plasticity (instantiated here via flashlight granule-cell-like neurons), together can implement the exact gradient of a SIGReg-like self-supervised learning objective. The equivalence requires no gradient calculations, no global error signals, no weight transport, and no label information: the only inputs are pre- and post-synaptic firing rates, local firing statistics, and the temporal contiguity of natural sensory streams. On a synthetic clustering task designed to probe whether class structure can be recovered from temporal ordering of inputs alone, ordered presentation raised cluster separation (CSR) to 2.49 while random ordering left it near baseline (0.83), a roughly threefold ($\approx 3.5\sigma$) separation attributable solely to input ordering. On temporally ordered MNIST, a two-layer network trained entirely with these rules achieved 87.3% linear-probe accuracy, showing that the mechanism functions end-to-end.
