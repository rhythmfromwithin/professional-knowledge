---
title: "XNET: Intelligent Dynamic Sampling for High-Speed Network Security Monitoring"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2608.18349
priority: low
status: unread
interest: medium
next_step: skim
---
# XNET: Intelligent Dynamic Sampling for High-Speed Network Security Monitoring
> 原文: [https://arxiv.org/abs/2608.18349](https://arxiv.org/abs/2608.18349)

arXiv:2608.18349v1 Announce Type: new
Abstract: Growing network speeds, with 100GbE line rates becoming common in modern enterprise networks, pose challenges to operators and security applications, as they struggle to scale their operational efficiency accordingly, without relying on costly hardware, excessive sampling, or complex distributed deployments. Unintentional loss due to stochastic packet sampling often produces low-quality traffic, further risking missed detection of critical security incidents, particularly those hidden in typically low-rate traffic, such as APT/malware command-and-control communications. In this paper, we introduce XNET, a system that monitors traffic at line rate using commodity hardware and applies dynamic sampling to amplify the visibility of high security value traffic. XNET leverages Linux's XDP technology to process packets efficiently, classify them based on their security value, and sample them as per configured policies. The outcome is a reduced packet stream in which the security-relevant portion of the traffic is amplified at the expense of less interesting traffic segments. XNET is a highly flexible, scalable and dynamic system that can be adapted based on a network's needs. We deployed XNET in a large real-world network using only commodity hardware, where our results show that XNET can achieve up to 84% traffic reduction with no packet loss while increasing the visibility of otherwise negligible traffic fivefold. With controlled stress tests, we further demonstrate XNET's scalability up to 100Gbps. Additionally, we show that XNET sampling led to a detection rate of 99.6% in an IDS application.
