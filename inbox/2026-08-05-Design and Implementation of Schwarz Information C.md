---
title: "Design and Implementation of Schwarz Information Criterion-Aided Intelligent Decentralized Resource Allocation in Dynamic LoRa Networks"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2608.00409
priority: medium
status: unread
interest: medium
next_step: skim
---
# Design and Implementation of Schwarz Information Criterion-Aided Intelligent Decentralized Resource Allocation in Dynamic LoRa Networks
> 原文: [https://arxiv.org/abs/2608.00409](https://arxiv.org/abs/2608.00409)

arXiv:2608.00409v1 Announce Type: new
Abstract: This paper proposes a lightweight distributed learning method for selecting transmission parameters in Long-Range (LoRa) networks that adapts to dynamically changing communication environments. In the proposed method, the Thompson Sampling (TS) is adopted for transmission parameter selection, whereas the Schwarz Information Criterion (SIC) is employed for environmental change detection. TS is a reinforcement learning approach that effectively balances exploration and exploitation by updating parameters based on probability distributions. Additionally, it demonstrates stable performance even with a small number of trials, thereby making it well-suited for LoRa end devices (EDs) with limited memory capacity and computational resources. Furthermore, to address the issue that TS-based methods strongly depend on past learning histories and therefore adapt slowly to abrupt changes in communication environments, a statistical change detection mechanism based on the SIC is integrated into our proposed method. SIC is adopted because it can detect environmental changes with low computational cost and is suitable for implementation on resource-constrained LoRa EDs. When a change in the communication environment is detected by SIC, the learning history of TS is reset, thereby enabling rapid re-learning under new environmental conditions. Moreover, to achieve fully distributed communication parameter selection while enhancing transmission reliability and energy efficiency, the proposed method relies solely on Acknowledgment (ACK) feedback and the selected transmission parameters. Experimental results demonstrate that the proposed method improves the transmission success rate from 64.0% to 71.1% and increases energy efficiency from 293.9 bit/J to 328.3 bit/J compared with the conventional Upper Confidence Bound (UCB)1-tuned scheme under high-density dynamic LoRa networks.
