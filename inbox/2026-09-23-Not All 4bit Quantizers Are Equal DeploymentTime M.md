---
interest: medium
link: https://arxiv.org/abs/2609.25014
next_step: skim
priority: low
slack_ts: '1790223767.332289'
source: cs.CR - Cryptography and Security
status: unread
title: 'Not All 4-bit Quantizers Are Equal: Deployment-Time Mitigation of PII Leakage
  in Fine-Tuned Small Language Models'
---
# Not All 4-bit Quantizers Are Equal: Deployment-Time Mitigation of PII Leakage in Fine-Tuned Small Language Models
> 原文: [https://arxiv.org/abs/2609.25014](https://arxiv.org/abs/2609.25014)

arXiv:2609.25014v1 Announce Type: new
Abstract: Organizations fine-tune small language models on private data and then compress them to 4 bits for resource-efficient deployment. We show that the compression method also affects privacy. What separates the methods is not the bit width but whether they tune their rounding on a small sample of text, the calibration corpus. On our primary model, when each planted record's own opening text is used as the prompt, the two calibration-based methods we test, Activation-aware Weight Quantization (AWQ) and Gradient-based Post-Training Quantization (GPTQ), each reproduce none of the planted records, while the calibration-corpus-free GGUF Q4\_K\_M format reproduces 5.3% of them. Tracked across five open models with 0.5-7 billion parameters, AWQ leaks least at every size and in both families, with little accuracy loss at 3-7 billion. Controlled experiments associate the difference with calibration-induced rounding error in channels involved in rare-token prediction. Choosing the 4-bit method is therefore a deployment-time privacy decision, not only a question of speed and quality.
