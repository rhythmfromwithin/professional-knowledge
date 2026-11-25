---
interest: medium
link: https://arxiv.org/abs/2611.27322
next_step: skim
priority: low
slack_ts: '1795593782.589409'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Spiking Neural Networks Incrementally Track Firing-Rate Networks
---
# Spiking Neural Networks Incrementally Track Firing-Rate Networks
> 原文: [https://arxiv.org/abs/2611.27322](https://arxiv.org/abs/2611.27322)

arXiv:2611.27322v1 Announce Type: new
Abstract: Understanding how spiking neural networks (SNNs) efficiently process data streams is key to (i) studying how biological brains conserve energy for lifelong predictions and (ii) enabling efficient continuous AI inference. In this work, we propose a theory on how an SNN incrementally tracks its corresponding firing-rate network, a continuous-valued neural network (ANN). We prove that the output of a discrete SNN continuously tracks the instantaneous ANN output implicitly determined by the SNN input. Based on this principle, we develop LIF-Stream, a conversion framework for efficient SNN inference over unbounded data streams. It enables the converted SNN to reuse its prior activation state and compute only the activation updates between frames, thereby reducing the average number of time steps needed per frame. Specifically, LIF-Stream controls the SNN to continuously track the reference ANN output, which gives a high-accuracy prediction for every frame. Evaluation on three large-scale streaming inference benchmarks with distinct modalities shows that LIF-Stream achieves the best efficiency-accuracy trade-off compared to high-accuracy SNN techniques.
