---
title: "Cloud Is Closer Than It Appears: Revisiting the Tradeoffs of Distributed Real-Time Inference"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.00005
priority: high
status: unread
interest: medium
next_step: skim
---
# Cloud Is Closer Than It Appears: Revisiting the Tradeoffs of Distributed Real-Time Inference
> 原文: [https://arxiv.org/abs/2605.00005](https://arxiv.org/abs/2605.00005)

arXiv:2605.00005v1 Announce Type: new
Abstract: The increasing deployment of deep neural networks (DNNs) in cyber-physical systems (CPS) enhances perception fidelity, but imposes substantial computational demands on execution platforms, posing challenges to real-time control deadlines. Traditional distributed CPS architectures typically favor on-device inference to avoid network variability and contention-induced delays on remote platforms. However, this design choice places significant energy and computational demands on the local hardware. In this work, we revisit the assumption that cloud-based inference is intrinsically unsuitable for latency-sensitive control tasks. We demonstrate that, when provisioned with high-throughput compute resources, cloud platforms can effectively amortize network and queueing delays, enabling them to match or surpass on-device performance for real-time decision-making. Specifically, we develop a formal analytical model that characterizes distributed inference latency as a function of the sensing frequency, platform throughput, network delay, and task-specific safety constraints. We instantiate this model in the context of emergency braking for autonomous driving and validate it through extensive simulations using real-time vehicular dynamics. Our empirical results identify concrete conditions under which cloud-based inference adheres to safety margins more reliably than its on-device counterpart. These findings challenge prevailing design strategies and suggest that the cloud is not merely a feasible option, but often the preferred inference location for distributed CPS architectures. In this light, the cloud is not as distant as traditionally perceived; in fact, it is closer than it appears.
