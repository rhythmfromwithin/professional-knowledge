---
title: "Private Computation Space: Experience with Trusted Multi-Cluster Federated Learning for Agriculture"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2609.01667
priority: low
status: unread
interest: medium
next_step: skim
---
# Private Computation Space: Experience with Trusted Multi-Cluster Federated Learning for Agriculture
> 原文: [https://arxiv.org/abs/2609.01667](https://arxiv.org/abs/2609.01667)

arXiv:2609.01667v1 Announce Type: new
Abstract: Artificial Intelligence has shown to help improve agricultural practices, yet adoption remains limited: 69% of U.S. farmers have privacy concerns with sharing their data, and these concerns must be addressed before adoption is widespread. While Federated Learning has been demonstrated to protect privacy at scale for other sectors, deploying a system for agriculture comes with its own set of challenges; the problem necessitates a system that can protect farmer data and identities while preserving model utility, runs on commodity hardware, and is resilient to fragile rural infrastructure. To address these concerns, we introduce the Private Computation Space (PCS), a deployed, open-source Machine Learning system to provision and process farmer data securely. We design a system tailored to an agricultural setting, with multi-cluster orchestration for reliability in rural areas with asynchronous Federated Learning (FL), Differential Privacy (DP), and Trusted Execution Environments (TEEs), to allow farms to participate in the framework while keeping their data private. We evaluate the system on two deployed workloads: monitoring nitrogen with living plant sensors in NY for six months and predicting evapotranspiration from weather stations in CA for ten months. Our evaluation finds a Dice Similarity Coefficient (DSC) of 0.71 and $R^2$ accuracy of 0.84 for the respective workloads, improving the worst single-site model accuracy by 22.4% and 9.1%, respectively, while preserving privacy.
