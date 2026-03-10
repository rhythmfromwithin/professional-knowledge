---
title: "Hidden in the Metadata: Stealth Poisoning Attacks on Multimodal Retrieval-Augmented Generation"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2603.00172
priority: low
status: unread
interest: medium
next_step: skim
---
# Hidden in the Metadata: Stealth Poisoning Attacks on Multimodal Retrieval-Augmented Generation
> 原文: [https://arxiv.org/abs/2603.00172](https://arxiv.org/abs/2603.00172)

arXiv:2603.00172v1 Announce Type: new
Abstract: Retrieval-augmented generation (RAG) has emerged as a powerful paradigm for enhancing multimodal large language models by grounding their responses in external, factual knowledge and thus mitigating hallucinations. However, the integration of externally sourced knowledge bases introduces a critical attack surface. Adversaries can inject malicious multimodal content capable of influencing both retrieval and downstream generation. In this work, we present MM-MEPA, a multimodal poisoning attack that targets the metadata components of image-text entries while leaving the associated visual content unaltered. By only manipulating the metadata, MM-MEPA can still steer multimodal retrieval and induce attacker-desired model responses. We evaluate the attack across multiple benchmark settings and demonstrate its severity. MM-MEPA achieves an attack success rate of up to 91\% consistently disrupting system behaviors across four retrievers and two multimodal generators. Additionally, we assess representative defense strategies and find them largely ineffective against this form of metadata-only poisoning. Our findings expose a critical vulnerability in multimodal RAG and underscore the urgent need for more robust, defense-aware retrieval and knowledge integration methods.
