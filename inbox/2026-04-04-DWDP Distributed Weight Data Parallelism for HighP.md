---
title: "DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2604.01621
priority: medium
status: unread
interest: medium
next_step: skim
---
# DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72
> 原文: [https://arxiv.org/abs/2604.01621](https://arxiv.org/abs/2604.01621)

arXiv:2604.01621v1 Announce Type: new
Abstract: Large language model (LLM) inference increasingly depends on multi-GPU execution, yet existing inference parallelization strategies require layer-wise inter-rank synchronization, making end-to-end performance sensitive to workload imbalance. We present DWDP (Distributed Weight Data Parallelism), an inference parallelization strategy that preserves data-parallel execution while offloading MoE weights across peer GPUs and fetching missing experts on demand. By removing collective inter-rank synchronization, DWDP allows each GPU to progress independently. We further address the practical overheads of this design with two optimizations for split-weight management and asynchronous remote-weight prefetch. Implemented in TensorRT-LLM and evaluated with DeepSeek-R1 on GB200 NVL72, DWDP improves end-to-end output TPS/GPU by 8.8% at comparable TPS/user in the 20-100 TPS/user serving range under 8K input sequence length and 1K output sequence length.
