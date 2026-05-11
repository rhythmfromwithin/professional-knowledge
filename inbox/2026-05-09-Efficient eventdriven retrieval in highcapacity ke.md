---
interest: medium
link: https://arxiv.org/abs/2605.05978
next_step: skim
priority: low
slack_ts: '1778472598.559419'
source: cs.NE - Neural and Evolutionary Computing
status: unread
title: Efficient event-driven retrieval in high-capacity kernel Hopfield networks
---
# Efficient event-driven retrieval in high-capacity kernel Hopfield networks
> 原文: [https://arxiv.org/abs/2605.05978](https://arxiv.org/abs/2605.05978)

arXiv:2605.05978v1 Announce Type: new
Abstract: High-capacity associative memory models, such as Kernel Logistic Regression (KLR) Hopfield networks, have demonstrated strong storage capabilities but typically rely on computationally expensive synchronous updates. This reliance poses a bottleneck for deployment on energy-efficient, event-driven neuromorphic hardware. In this paper, we investigate the asynchronous retrieval dynamics of KLR Hopfield networks. We show empirically that, under appropriately tuned kernel parameters, asynchronous sequential updates exhibit trajectories that are statistically indistinguishable from those of synchronous dynamics, while maintaining high recall accuracy within the tested regime for random patterns. Furthermore, we find that the asynchronous network achieves empirical storage capacities approaching $P/N \approx 30$ in static random pattern regimes, exceeding classical limits. To evaluate computational efficiency, we analyze the total number of state transitions (bit flips) required for error correction. The results show that the network converges using a number of events close to the initial Hamming distance from the target pattern, without observable spurious oscillations. These findings suggest that the large-margin attractors induced by KLR learning create a smooth energy landscape suited for sparse, event-driven computation, providing a basis for scalable and low-power associative memory on neuromorphic architectures.
