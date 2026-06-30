---
interest: medium
link: https://arxiv.org/abs/2606.28439
next_step: skim
priority: low
slack_ts: '1782792824.664679'
source: cs.CR - Cryptography and Security
status: unread
title: 'PLAA: Packet-level Adversarial Attacks in Network Traffic Detection'
---
# PLAA: Packet-level Adversarial Attacks in Network Traffic Detection
> 原文: [https://arxiv.org/abs/2606.28439](https://arxiv.org/abs/2606.28439)

arXiv:2606.28439v1 Announce Type: new
Abstract: Deep neural networks (DNNs) are widely applied in Network-based Intrusion Detection System (NIDS) due to their high accuracy. However, DNNs are highly susceptible to adversarial attacks, which generate malicious traffic to evade NIDS detection. Existing approaches often adapt adversarial attacks from computer vision (CV) tasks to the NIDS domain, overlooking the fundamental differences between CV and NIDS. This results in two major issues: 1) The generated network traffic may become invalid, 2) The generated traffic may lose its original attack semantics. To address these issues, this paper proposes an adversarial attack specifically designed for NIDS. Instead of directly generating flow-level features, our approach incrementally generates packet-level features to construct adversarial traffic. During the generation process, the semantic integrity of the traffic is monitored at each stage, effectively avoiding the issues of invalid traffic and semantic loss observed in existing methods. We evaluate our attack algorithm against current NIDS models using the CIC-UNSW-NB15, CIC-DDoS2019, and CIC-IDS-2017 datasets. The proposed method achieves an average evasion success rate of 92.78%, while ensuring that the generated adversarial traffic remains semantically consistent with the original malicious traffic.
