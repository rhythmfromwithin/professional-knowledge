---
title: "Fly Whiskers Meet LiDAR: Robust Navigation under Sensor Failure"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2611.03897
priority: low
status: unread
interest: medium
next_step: skim
---
# Fly Whiskers Meet LiDAR: Robust Navigation under Sensor Failure
> 原文: [https://arxiv.org/abs/2611.03897](https://arxiv.org/abs/2611.03897)

arXiv:2611.03897v1 Announce Type: new
Abstract: We extend FLYNN, a leaky integrator recurrent network wired on the Drosophila melanogaster connectome, with a 32-ray 2D LiDAR interface that requires no learned fusion layer beyond a scalar input gain. A 270 degree frontal scan at 8 m range is injected as inverted proximity into the 37 BM Vib head-bristle neurons. Across 24 paired comparisons in a four- state vision matrix with LiDAR on or off, FLYNN-LiDAR has 17 significant wins, 5 nonsignificant comparisons, and 2 significant losses against three LiDAR-capable baselines. Both losses are to MobileNet with the left eye off. With full vision, FLYNN- LiDAR reaches 96.6% success. Under total vision loss, the scan raises success from 45.2% to 64.6%; the baselines reach 44.6% to 56.6% with the scan on. Under out of distribution textures, it is the only LiDAR-capable model whose success improves with the scan (44.2% to 58.4%); both CNNs score 0%, and SmallWorld declines from 26.8% to 7.4%. Under periodic vision dropout, FLYNN-LiDAR achieves 93.6% and 89.6% success at 25% and 50% duty with fewer collisions. Profiling the evaluated forward paths gives 3.93M multiply accumulate operations per step; EfficientNet and MobileNet require 4.60x and 2.94x as many. Final- state analysis shows near-linear sensory superposition (cosine 0.9955).
