---
title: "Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.05642
priority: medium
status: unread
interest: medium
next_step: skim
---
# Runway Characters: Serving a 57B Video Diffusion Transformer for Real-Time Conversation
> 原文: [https://arxiv.org/abs/2611.05642](https://arxiv.org/abs/2611.05642)

arXiv:2611.05642v1 Announce Type: new
Abstract: Conversational video characters must generate video as fast as it plays, for one user at a time: at 24 fps, a sustained 166.7 ms per four-frame chunk at batch size one, with only a few chunks of buffering. We describe the system behind Runway Characters, which serves a $\approx$57B-parameter autoregressive video diffusion transformer (four denoising passes per chunk) at 704$\times$1088 and 24 fps on four H100 GPUs with a voice agent in the loop. Each chunk takes 240 attention calls, each reading a 5,788-slot KV cache in which only 757 tokens are new, and 29% of the original step was whole-cache work repeated in every call. We move that work to write time (a ring cache, RoPE and FP8 quantization applied once per write, and a delta rotation when positions reset), fuse the tensor-parallel all-reduce into the FP8 GEMM with in-switch reduction, and give the decoder that turns latents into video frames its own GPU. Without the fused kernel, our optimizations cut the diffusion step from 240.9 to 159.3 ms (1.51$\times$, 24.5 fps sustained) with no detected degradation in lip-sync scores; the fused kernel, rolled back once in production and since re-enabled, reaches 147.4 ms (1.63$\times$, 43% of FP8 peak). In seven weeks of production the worker averaged above 23.5 fps in 99.5% of sessions that streamed for at least a second, and our pipeline takes 0.49 s of a 2.1 s median conversational turn. On the same GPUs, the two open-source real-time video systems we benchmarked, at four denoising passes, miss real time or add over a second of latency (one by estimate), at a third to half of our resolution.
