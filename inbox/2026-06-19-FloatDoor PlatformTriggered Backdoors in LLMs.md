---
interest: medium
link: https://arxiv.org/abs/2606.19535
next_step: skim
priority: low
slack_ts: '1781847259.318739'
source: cs.CR - Cryptography and Security
status: unread
title: 'FloatDoor: Platform-Triggered Backdoors in LLMs'
---
# FloatDoor: Platform-Triggered Backdoors in LLMs
> 原文: [https://arxiv.org/abs/2606.19535](https://arxiv.org/abs/2606.19535)

arXiv:2606.19535v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly deployed in sensitive settings such as software engineering, where their outputs directly shape downstream artifacts. Recent work has shown that an identical model can produce measurably different outputs depending on the deployment platform, a consequence of non-associative floating-point arithmetic and divergent kernel implementations. We study the security implications of this platform-dependent variability and uncover a novel attack surface on LLM deployments. We introduce FloatDoor, the first input-independent, platform-triggered backdoor attack against generative LLMs. The compromised model exhibits adversary-chosen behavior when served on a target platform and is otherwise benign. FloatDoor is realized through two lightweight LoRA adapters, one that amplifies inter-platform numerical divergence and one that binds the resulting platform signature to a malicious downstream task, while leaving aggregate model utility largely intact. FloatDoor exploits a pronounced time-of-check, time-of-use gap between model auditing and serving. We demonstrate FloatDoor on Qwen3-4B across a broad range of deployment targets, including NVIDIA GPUs, Google TPUs, AWS Graviton, and Alibaba Yitian-710. As a final case study, we show that FloatDoor reliably induces exploitable code vulnerabilities on a chosen target platform. Our results establish a new class of attacks on LLM deployments and underscore the pressing need for trusted model supply chains in sensitive, LLM-powered applications.
