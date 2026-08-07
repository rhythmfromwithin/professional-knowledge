---
interest: medium
link: https://arxiv.org/abs/2608.01646
next_step: skim
priority: low
slack_ts: '1786072104.400979'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: 'Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition'
---
# Spike-HTR: Spiking Neural Transformer for Handwritten Text Recognition
> 原文: [https://arxiv.org/abs/2608.01646](https://arxiv.org/abs/2608.01646)

arXiv:2608.01646v1 Announce Type: new
Abstract: Handwritten Text Recognition (HTR) is computationally imbalanced in two ways: most image pixels are background, and many width-axis sequence positions are blank-dominated. This creates a mismatch for Spiking Neural Networks (SNNs): handwriting is observed as a static image, whereas spiking computation unfolds over timesteps. We propose Spike-HTR, a hybrid spiking recognizer that controls both the number of spiking steps and the number of width positions processed by the deep sequence mixer. To make a static image suitable for short-horizon spiking inference, InkCoder converts it into a coarse-to-fine input stream, where early steps cover broad stroke regions and later steps emphasize sharper stroke details. To reduce sequence computation, a CTC-guided length reducer keeps likely character or uncertain positions and compresses long blank-dominated stretches before deep mixing. With $T{=}2$, Spike-HTR trains only on target data, decodes without language models or lexicons, and reaches validation/test CERs of 3.5/5.4, 2.3/2.5, and 4.2/3.9 on IAM, LAM, and READ2016. Codes are available at https://github.com/QomolangmaH/SpikeHTR.
