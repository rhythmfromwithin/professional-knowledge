---
title: "Fuzzing Microservices in Face of Intrinsic Uncertainties"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2603.02551
priority: low
status: unread
---
# Fuzzing Microservices in Face of Intrinsic Uncertainties
> 原文: [https://arxiv.org/abs/2603.02551](https://arxiv.org/abs/2603.02551)

arXiv:2603.02551v1 Announce Type: new
Abstract: The widespread adoption of microservices has fundamentally transformed how modern software systems are designed, deployed, operated and maintained. However, well-known microservice properties (e.g., dynamic scalability and decentralized control) introduce inherent and multi-dimensional uncertainties. These uncertainties span across inter-service interactions, runtime environments, and internal service logic, which manifest as nondeterministic behaviors, performance fluctuations, and unpredictable fault propagation. Existing approaches do not have sufficient support in capturing such uncertainties and their propagation in industrial microservice systems, and these approaches mostly focus on single-service testing. In this paper, we argue for a novel paradigm: ``uncertainty-driven'' and ``system-level'' microservice testing. We outline key research challenges, including the modeling and injection of uncertainties and their propagation, causal inference for fault localization, and multi-dimensional analyses and assessment of uncertainties and their impact on system quality. We propose an architecture for continuous uncertainty-driven and system-level microservice fuzzing, which integrates service virtualization, uncertainty simulation, adaptive test generation and optimization\revision{, and illustrate it with an e-commerce example we developed}. Our goal is to inspire the development of scalable and automated system-level testing methods that improve the dependability and resilience of industrial microservice systems, with the explicit consideration of uncertainties and their propagation.
