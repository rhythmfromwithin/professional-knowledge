---
title: "UniMark: Unified Adaptive Multi-bit Watermarking for Autoregressive Image Generators"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2604.11843
priority: medium
status: unread
interest: medium
next_step: skim
---
# UniMark: Unified Adaptive Multi-bit Watermarking for Autoregressive Image Generators
> 原文: [https://arxiv.org/abs/2604.11843](https://arxiv.org/abs/2604.11843)

arXiv:2604.11843v1 Announce Type: new
Abstract: Invisible watermarking for autoregressive (AR) image generation has recently gained attention as a means of protecting image ownership and tracing AI-generated content. However, existing approaches suffer from three key limitations: (1) they embed only zero-bit watermarks for binary verification, lacking the ability to convey multi-bit messages; (2) they rely on static codebook partitioning strategies that are vulnerable to security attacks once the partition is exposed; and (3) they are designed for specific AR architectures, failing to generalize across diverse AR paradigms. We propose \method{}, a training-free, unified watermarking framework for autoregressive image generators that addresses all three limitations. \method{} introduces three core components: \textbf{Adaptive Semantic Grouping (ASG)}, which dynamically partitions codebook entries based on semantic similarity and a secret key, ensuring both image quality preservation and security; \textbf{Block-wise Multi-bit Encoding (BME)}, which divides the token sequence into blocks and encodes different bits across blocks with error-correcting codes for reliable message transmission; and \textbf{a Unified Token-Replacement Interface (UTRI)} that abstracts the watermark embedding process to support both next-token prediction (e.g., LlamaGen) and next-scale prediction (e.g., VAR) paradigms. We provide theoretical analysis on detection error rates and embedding capacity. Extensive experiments on three AR models demonstrate that \method{} achieves state-of-the-art performance in image quality (FID), watermark detection accuracy, and multi-bit message extraction, while maintaining robustness against cropping, JPEG compression, Gaussian noise, blur, color jitter, and random erasing attacks.
