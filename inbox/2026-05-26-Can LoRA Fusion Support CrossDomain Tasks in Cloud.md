---
interest: medium
link: https://arxiv.org/abs/2605.23913
next_step: skim
priority: medium
slack_ts: '1779941824.165439'
source: cs.DC - Distributed Computing
status: unread
title: Can LoRA Fusion Support Cross-Domain Tasks in Cloud-Edge Collaboration?
---
# Can LoRA Fusion Support Cross-Domain Tasks in Cloud-Edge Collaboration?
> 原文: [https://arxiv.org/abs/2605.23913](https://arxiv.org/abs/2605.23913)

arXiv:2605.23913v1 Announce Type: new
Abstract: Cloud-hosted large language models (LLMs) commonly rely on LoRA for domain adaptation, yet domain data are distributed across multiple edge devices and cannot be uploaded due to privacy constraints. This raises a fundamental question: how can knowledge from multiple private edges be integrated into a cloud LLM for cross-domain problem solving? A natural solution is to train LoRA adapters locally and fuse them in the cloud; however, existing pipelines rely on unrealistic assumptions that edge devices can host cloud-scale LLMs and are evaluated mainly on single-domain tasks. To address these limitations, we propose a prune-train-recover framework that enables local LoRA training on pruned models and privacy-preserving cloud integration. We further introduce MMLU-CD, a cross-domain benchmark that composes multiple domain samples into a single instance, enabling explicit evaluation of cross-domain problem solving. This allows us to ask a concrete question: Can existing LoRA fusion methods support cross-domain tasks in cloud-edge collaboration? Our empirical answer is negative. Existing LoRA fusion methods perform poorly on MMLU-CD, often underperforming the base LLM, revealing their inability to support cross-domain problem solving. We attribute this failure to parameter conflicts among LoRA adapters and propose a simple conflict-resolution module, LoRA-CR, which mitigates conflicting updates and improves LoRA fusion performance by up to 3.8%. These results identify conflict mitigation as a critical yet largely overlooked factor in cloud-edge LoRA fusion, warranting further investigation in future research.
