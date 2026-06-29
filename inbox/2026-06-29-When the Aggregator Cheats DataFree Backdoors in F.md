---
interest: medium
link: https://arxiv.org/abs/2606.27511
next_step: skim
priority: low
slack_ts: '1782708436.824629'
source: cs.CR - Cryptography and Security
status: unread
title: 'When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA
  Systems'
---
# When the Aggregator Cheats: Data-Free Backdoors in Federated LLM-based QA Systems
> 原文: [https://arxiv.org/abs/2606.27511](https://arxiv.org/abs/2606.27511)

arXiv:2606.27511v1 Announce Type: new
Abstract: Large Language Model (LLM)-based question-answering (QA) systems are increasingly deployed in sensitive domains such as healthcare, mental health counseling, and legal consultation. Federated learning (FL) enables collaborative training without sharing raw client data, for which locally trained models are aggregated at a central server (i.e., a cloud service provider) to obtain a global model. In this paper, we explore the potential vulnerability where a malicious aggregator, who may collude with a third-party vendor, stealthily implants advertisement-type backdoors into federated QA models, without ever accessing client data. The attacker's goals are twofold: (1) preserve clean QA fidelity (i.e., the poisoned model behaves like a clean model on non-triggered queries); and (2) generate highly natural, contextually relevant responses with target advertisements when a trigger appears. Achieving these two goals simultaneously is highly challenging, as naive backdoor injection without knowledge about private data may degrade model's clean performance or fail to inject the target. Motivated by this, we propose to leverage clients' uploaded gradients during training, and develop a two-stage framework for data-free and stealthy poisoning: (1) recover representative training samples from client gradients, and (2) construct poisoning datasets utilizing recovered samples and trigger phrases to inject backdoors into the global model. Experiments across representative QA datasets and LLM families under full fine-tuning and LoRA settings demonstrate that, our method achieves nearly 100% Attack Success Rate (ASR) while incurring negligible degradation on clean tasks. Crucially, reconstructing only 5-20% of gradients suffices to mount a reliable attack, exposing a practical blind spot in the pipeline of federated training of QA LLMs.
