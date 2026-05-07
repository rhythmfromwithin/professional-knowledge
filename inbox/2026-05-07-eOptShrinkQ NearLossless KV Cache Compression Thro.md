---
title: "eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.02905
priority: high
status: unread
interest: medium
next_step: skim
---
# eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization
> 原文: [https://arxiv.org/abs/2605.02905](https://arxiv.org/abs/2605.02905)

arXiv:2605.02905v1 Announce Type: new
Abstract: We show that the key-value (KV) cache in transformer attention heads admits a natural decomposition into a low-rank \emph{shared context} component and a full-rank \emph{per-token} residual, well described by the spiked random matrix model. This observation leads to eOptShrinkQ, a two-stage compression pipeline: optimal singular value shrinkage (eOptShrink) automatically extracts the shared structure, and the residual -- which satisfies the \emph{thin shell property} with delocalized coordinates -- is quantized by TurboQuant~\citep{zandieh2025turboquant}, a recently proposed per-vector scalar quantizer with near-optimal distortion guarantees. By restoring the isotropy that scalar quantization assumes, spectral denoising eliminates the need for both outlier handling and dedicated inner product bias correction, freeing those bits for improved reconstruction.
The theoretical grounding in random matrix theory provides three guarantees: automatic rank selection via the BBP phase transition, provably near-zero inner product bias on the residual, and coordinate delocalization ensuring near-optimal quantization distortion. Experimentally, we validate eOptShrinkQ on Llama-3.1-8B and Ministral-8B across three levels: per-head MSE and inner product fidelity, where eOptShrinkQ saves nearly one bit per entry over TurboQuant at equivalent quality; end-to-end on LongBench (16 tasks), where eOptShrinkQ at $\sim$2.2 bits per entry outperforms TurboQuant at 3.0 bits; and multi-needle retrieval, where eOptShrinkQ at 2.2 bits closely matches or exceeds uncompressed FP16, suggesting that spectral denoising can act as a beneficial regularizer for retrieval-intensive tasks.
