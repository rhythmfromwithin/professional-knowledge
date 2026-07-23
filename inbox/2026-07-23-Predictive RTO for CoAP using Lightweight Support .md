---
title: "Predictive RTO for CoAP using Lightweight Support Vector Regression in Internet of Things"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2607.18273
priority: medium
status: unread
interest: medium
next_step: skim
---
# Predictive RTO for CoAP using Lightweight Support Vector Regression in Internet of Things
> 原文: [https://arxiv.org/abs/2607.18273](https://arxiv.org/abs/2607.18273)

arXiv:2607.18273v1 Announce Type: new
Abstract: Internet of Things (IoT) networks require lightweight application layer messaging, and CoAP is an option because it supports REST-style interactions over UDP on constrained devices. However, CoAP congestion control still depends on fixed heuristics, including binary exponential backoff (BEB) and RTT-based mechanisms such as CoCoA and CoCoA+, which do not adapt well to dynamic and lossy wireless links. This paper proposes prCoAP, a lightweight data-driven approach that replaces heuristic Retransmission Timeout (RTO) selection with a per-attempt linear Support Vector Regression (SVR) ensemble for direct RTO prediction from node-observable features. The model runs on-device on low-end microcontrollers and operates within strict memory and energy budgets. The framework also includes a calibrated Random Forest drop classifier that identifies likely-to-fail transactions in later retransmission attempts and terminates them early to reduce channel occupancy. We evaluate the approach using a discrete-event simulator implementing IEEE 802.15.4 and RFC 7252 and validate it against the FIT IoT-LAB testbed. Our experiments confirm that the proposed linear SVR achieves 97.25% PDR, outperforming standard CoAP under the evaluated conditions. We also evaluate a kernel SVR variant; while it improves regression fit (R2 0.84 vs. 0.63), the linear SVR provides better system-level efficiency, achieving comparable PDR with lower energy overhead.
