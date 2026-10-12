---
title: "An Input-Dependent Readout Phase for Resonant Sequence Models"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2610.12496
priority: high
status: unread
interest: medium
next_step: skim
---
# An Input-Dependent Readout Phase for Resonant Sequence Models
> 原文: [https://arxiv.org/abs/2610.12496](https://arxiv.org/abs/2610.12496)

arXiv:2610.12496v1 Announce Type: new
Abstract: Sequence models with a fixed-size state avoid the quadratic cost of attention, but face a design choice. An input-dependent state transition gives content-dependent memory at the cost of FFT-based training, while a fixed transition keeps the O(T log T) convolutional path but reads memory the same way for every input. ResonatorLM, a recent model of the second kind, reads a bank of damped complex oscillators through a fixed learned phase per head. We make that readout phase a function of the current token, which adds input dependence to the read only, keeps the convolution exact, and costs 0.2 percent more parameters. An analysis of the untrained bank shows that phase does encode elapsed time, but an ordinary token falls below the background within 2-8 steps and no choice of damping extends linear reconstruction beyond about 16 tokens. In 6M-parameter character-level models on WikiText-2, the input-dependent phase matches the original at the training length and removes its failure beyond it: trained on 256 tokens and tested on 1024, perplexity falls from 12.81 to 3.76. We trace the failure to long-memory heads that accumulate more history than training exposed them to. The learned phase tracks the current character rather than distance and does not improve retrieval.
