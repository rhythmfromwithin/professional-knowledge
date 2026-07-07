---
interest: medium
link: https://arxiv.org/abs/2607.02551
next_step: skim
priority: medium
slack_ts: '1783397054.186349'
source: cs.CV - Computer Vision
status: unread
title: 'DELTAVID: Enhancing Fine-Grained Spatiotemporal Perception with Cross-Video
  Differences'
---
# DELTAVID: Enhancing Fine-Grained Spatiotemporal Perception with Cross-Video Differences
> 原文: [https://arxiv.org/abs/2607.02551](https://arxiv.org/abs/2607.02551)

arXiv:2607.02551v1 Announce Type: new
Abstract: Video multimodal large language models have made strong progress on open-ended video understanding, but they still lack precise local spatiotemporal perception. When two videos share almost the same global semantics and differ only in a short time span or a small region, current models often fail to find the change and provide reliable evidence. We propose DELTAVID, a verifiable proxy-task framework that enhances fine-grained spatiotemporal perception with cross-video differences. The key idea is to turn cross-video spot-the-difference into a trainable perception signal, where a model identifies local changes, judges temporal boundaries, and organizes spatial evidence by comparing similar videos. To make this signal scalable to train and reliable to evaluate, we further introduce DELTAVID-10K and DELTAVID-Bench, which convert controllable local differences in real videos into evidence-labeled training and test samples. Experiments show that DELTAVID substantially improves performance on cross-video difference understanding and transfers the learned local evidence ability to general video understanding benchmarks, including MMVU, MLVU, Video-MME, VideoHolmes, VideoMMMU, LVBench, TempCompass, and LongVideoBench. These results show that cross-video differences are not only an effective way to diagnose fine-grained perception failures, but also a scalable proxy supervision that moves Video MLLMs from coarse semantic understanding toward fine-grained spatiotemporal evidence reasoning.
