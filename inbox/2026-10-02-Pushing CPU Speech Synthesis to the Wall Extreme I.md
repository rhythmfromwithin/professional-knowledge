---
title: "Pushing CPU Speech Synthesis to the Wall: Extreme Inference Tuning under Serverless Architecture and Billing"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2610.00063
priority: medium
status: unread
interest: medium
next_step: skim
---
# Pushing CPU Speech Synthesis to the Wall: Extreme Inference Tuning under Serverless Architecture and Billing
> 原文: [https://arxiv.org/abs/2610.00063](https://arxiv.org/abs/2610.00063)

arXiv:2610.00063v1 Announce Type: new
Abstract: Instance-billed serverless platforms charge for CPU and memory over the lifetime of a warm instance, making idle inference state a direct serving cost. We present billing-aware neural text-to-speech (TTS) serving on serverless CPUs, optimizing CPU-seconds and GB-seconds rather than throughput or latency alone. Conventional runtimes are poorly suited to this setting: per-request parallelism causes CPU contention under concurrency, while warm instances retain gigabytes of billable inference and page-cache state.
We address these costs with request-sized concurrent inference, which bounds per-request CPU parallelism, and a reclaimable instance lifecycle, which releases inference state and page-cache memory after idle periods while retaining the server process and compile cache. On Kokoro-82M, our system achieves 2.71 audio-seconds per CPU-second versus 0.89 with ONNX Runtime defaults and reduces cost per audio-hour from $0.0631 with PyTorch to $0.0153, a 4.1x reduction. Idle billed memory falls from 8.7 GB to 1.33 GB, while restoration reaches first audio in 2.2 s versus 7.7 s for a PyTorch cold start. Under bursty traffic, lifecycle reclamation is essential for translating inference efficiency into lower serverless cost.
