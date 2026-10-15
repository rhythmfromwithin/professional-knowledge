---
interest: medium
link: https://arxiv.org/abs/2610.19732
next_step: skim
priority: low
slack_ts: '1792037691.369629'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Controlling the latency in temporal coded spiking models for neuromorphic datasets
---
# Controlling the latency in temporal coded spiking models for neuromorphic datasets
> 原文: [https://arxiv.org/abs/2610.19732](https://arxiv.org/abs/2610.19732)

arXiv:2610.19732v1 Announce Type: new
Abstract: Exploiting temporal information in datasets with high temporal dependencies (such as spoken keyword recognition) by spiking models is still an open problem. Promising frameworks include Time-To-First coding (TTFS) and the inclusion of synaptic delays into learning. In TTFS, neurons are forced to spike at most once, forcing the network to found its learning on the spiking times of neurons rather than their spiking rate. Some models use the TTFS framework to directly compute the spiking time of Integrate-and-Fire (IF) or Leaky Integrate-and-Fire (LIF) neurons. However, most models built in the TTFS framework have not been tested against datasets containing temporal information. Little is known about the latency of these models on temporal datasets, where the latency is the time taken by the network to correctly classify a sample. In this work, we study the behaviour of Delay Neural Networks (DeNN) models, i.e. models that directly compute the spiking time of neurons by bypassing the membrane potential and thresholding mechanisms of spiking neurons. We show how to analytically control their latency, and empirically study the latency-accuracy tradeoff in a dynamic temporal dataset.
