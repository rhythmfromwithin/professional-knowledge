---
title: "Evolved Spiking Neural Networks for EEG Seizure Detection: Calcium Dynamics and Delay Mechanics"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2611.03841
priority: low
status: unread
interest: medium
next_step: skim
---
# Evolved Spiking Neural Networks for EEG Seizure Detection: Calcium Dynamics and Delay Mechanics
> 原文: [https://arxiv.org/abs/2611.03841](https://arxiv.org/abs/2611.03841)

arXiv:2611.03841v1 Announce Type: new
Abstract: Neuroevolution can discover compact network designs that are hard to specify by hand. The EONS framework evolves the topology, weights, thresholds and delays of neuromorphic spiking networks without gradients. We tested whether giving integrate-and-fire (IF) neurons an activity-dependent calcium current (Ca-IF neurons) improves evolved networks for EEG seizure detection, with calcium parameters fixed, shared across a network, or evolved for each neuron. On 10 held-out CHB-MIT patients never seen in training, per-neuron calcium raised the record-level Matthews correlation coefficient (MCC) from 0.592 to 0.726 over 20 independent runs (p = 0.008) and lowered the false-alarm rate from 0.17 to 0.10. Fixed or per-network calcium gave no significant benefit. IF networks with evolved synaptic delays of 1-3 ticks gave a similar gain (p = 0.005), whereas axonal delays did not. On Siena, with unchanged settings, per-neuron calcium gained +0.096 MCC over IF in one patient-disjoint split (p = 0.011) and +0.059 in the other (p = 0.052). These results suggest that calcium and delays may make the evolutionary search more effective, and motivate testing on more data and in neuromorphic hardware.
