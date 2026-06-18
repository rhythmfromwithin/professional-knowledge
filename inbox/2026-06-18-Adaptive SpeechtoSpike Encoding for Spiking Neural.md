---
interest: medium
link: https://arxiv.org/abs/2606.19039
next_step: skim
priority: low
slack_ts: '1781759639.138029'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Adaptive Speech-to-Spike Encoding for Spiking Neural Networks
---
# Adaptive Speech-to-Spike Encoding for Spiking Neural Networks
> 原文: [https://arxiv.org/abs/2606.19039](https://arxiv.org/abs/2606.19039)

arXiv:2606.19039v1 Announce Type: new
Abstract: The mismatch between continuous acoustic signals and discrete event-driven processing remains a fundamental bottleneck for neuromorphic speech processing. Current systems typically rely on fixed spike encoders, forcing downstream Spiking Neural Networks (SNNs) to compensate for non-adaptive input representations. To address this, we present a learnable residual speech-to-spike encoder jointly trained end-to-end with a Recurrent Leaky Integrate-and-Fire (R-LIF) backbone. We validate this approach on the Google Speech Commands v2 (GSC-v2) benchmark, achieving up to 94.97% accuracy. Notably, the learned encoder remains highly parameter-efficient with a compact 35k-parameter variant that reaches 89.8%, matching or exceeding prior baselines that require an order of magnitude more parameters. Our encoder-focused analysis, including linear probing and gradient-residual inspection, indicates that the encoder does not target faithful signal reconstruction but instead learns task-aligned spike representations that enhance class separability. Finally, we benchmark bio-inspired, hardware-friendly credit assignment by comparing Direct Feedback Alignment (DFA) with surrogate-gradient BPTT under identical architectures and training conditions. We find that DFA reaches 91.5% accuracy, quantifying the performance trade-off of bio-inspired learning rules for modern neuromorphic audio.
