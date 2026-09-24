---
interest: medium
link: https://arxiv.org/abs/2609.25082
next_step: skim
priority: high
slack_ts: '1790223764.095549'
source: cs.LG - Machine Learning
status: unread
title: 'Federating Quantum and Classical Computing: A Privacy-Preserving Hybrid Approach'
---
# Federating Quantum and Classical Computing: A Privacy-Preserving Hybrid Approach
> 原文: [https://arxiv.org/abs/2609.25082](https://arxiv.org/abs/2609.25082)

arXiv:2609.25082v1 Announce Type: new
Abstract: Quantum machine learning (QML) is increasingly recognized as one of the most promising near-term applications of quantum computing, viewed as a next-frontier candidate beyond purely classical approaches. Hybrid quantum-classical models operationalize this potential by embedding a parameterized quantum circuit within a model where all other components remain classical-a design already applied to chemistry simulation, financial modeling, and image classification. However, their deployment in privacy-sensitive, multi-party settings is constrained by the need to avoid centralizing raw data and by the requirement that modern quantum circuits remain parameter-efficient to stay trainable at scale.
In this paper, we address these constraints by evaluating federated learning (FL) as a means of combining a hybrid quantum-classical active party with a classical passive party, using Sherpa.ai's Blind Vertical FL (SBVFL) protocol to avoid centralizing raw data, while drastically reducing communication. We construct the split multiplicative periodic parity (SMPP) benchmark, following common QML design practice. On this task, our simulations show that SBVFL raises accuracy from 0.7227 to 0.8757 compared to local training, closely approaching non-private centralized accuracy, and that the hybrid quantum-classical model achieves this with substantially fewer trainable parameters than the classical neural networks and random forest alternatives. These results show that FL enables high-performing, privacy-preserving quantum-classical collaboration without centralizing raw data.
