---
title: "UniSpike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.23796
priority: low
status: unread
interest: medium
next_step: skim
---
# UniSpike: Accelerating Spiking Neural Networks on Neuromorphic Systems via Eliminating Address Redundancy
> 原文: [https://arxiv.org/abs/2605.23796](https://arxiv.org/abs/2605.23796)

arXiv:2605.23796v1 Announce Type: new
Abstract: Many-core neuromorphic systems accelerate Spiking Neural Networks (SNNs), yet their packet-based spike communication can spend substantial traffic and energy repeatedly transmitting destination addresses. This overhead is amplified by the small payload of spike packets: in representative workloads, duplicate address transmissions account for up to 49% of the total traffic. This paper presents UniSpike, a hardware-software co-design that removes address redundancy by aggregating spikes destined for the same core into compact packets. UniSpike combines destination-centric spike scheduling, lightweight runtime packet assembly hardware, and destination-aware SNN partitioning. Across diverse SNN workloads, UniSpike reduces traffic by 1.93$\times$ on average, delivering 1.77$\times$ speedup and 1.50$\times$ energy efficiency improvement over state-of-the-art designs.
