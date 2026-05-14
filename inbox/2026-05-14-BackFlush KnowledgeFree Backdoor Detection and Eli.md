---
title: "BackFlush: Knowledge-Free Backdoor Detection and Elimination with Watermark Preservation in Large Language Models"
source: "cs.CR - Cryptography and Security"
link: https://arxiv.org/abs/2605.12529
priority: low
status: unread
interest: medium
next_step: skim
---
# BackFlush: Knowledge-Free Backdoor Detection and Elimination with Watermark Preservation in Large Language Models
> 原文: [https://arxiv.org/abs/2605.12529](https://arxiv.org/abs/2605.12529)

arXiv:2605.12529v1 Announce Type: new
Abstract: In recent trends, one can observe Large Language Models (LLMs) are exposed to backdoor attacks where vicious triggers added during training or model editing to elicit harmful outputs on specific input patterns while maintaining clean performance on normal inputs. Legitimate watermarks used as ownership signatures share similar mechanisms to backdoors, creating a critical challenge: detecting and eliminating unknown backdoors without compromising watermark integrity. Existing defenses require prior knowledge of triggers or their payloads, depend on clean reference models, or sacrifice model utility without preserving the watermark. To address these limitations we introduce BackFlush and its variants, a unified framework for backdoor detection and elimination while preserving watermarks. We establish two novel observations: Backdoor Flushing Phenomenon, where injecting and unlearning auxiliary data eliminates pre established backdoors, and Backdoor Susceptibility Amplification, enabling constant time detection independent of vocabulary size. BackFlush employs Rotation based Parameter Editing (RoPE) Unlearning, a technique that preserves watermarks while eliminating backdoors by rotating the embeddings. Comprehensive evaluation across diverse trigger types over different architectures demonstrates BackFlush achieves approximately 1%Attack Success Rate (ASR), approximately 99% clean accuracy (CACC), and preserved watermarking capabilities in the realm where no existing method simultaneously provides these alongside maintaining model utility comparable to clean baselines. Codes are available at https://github.com/JagadeeshAI/BackFlush IJCNN.git.
