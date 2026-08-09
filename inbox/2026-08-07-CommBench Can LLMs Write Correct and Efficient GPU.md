---
interest: medium
link: https://arxiv.org/abs/2608.04450
next_step: skim
priority: medium
slack_ts: '1786241596.971629'
source: cs.DC - Distributed Computing
status: unread
title: 'CommBench: Can LLMs Write Correct and Efficient GPU Communication Code?'
---
# CommBench: Can LLMs Write Correct and Efficient GPU Communication Code?
> 原文: [https://arxiv.org/abs/2608.04450](https://arxiv.org/abs/2608.04450)

arXiv:2608.04450v1 Announce Type: new
Abstract: Training and serving large language models (LLMs) rely heavily on high-performance GPU communication, yet implementing efficient GPU communication primitives requires deep expertise in GPU architectures, networking hardware, and distributed communication patterns, making them particularly challenging for code generation models. We present CommBench, a comprehensive benchmark for GPU communication programming, consisting of over 100 expert-curated tasks spanning point-to-point communication, collective operations, expert-parallel communication, compute--communication fusion, and communication utility functions, with reference implementations either written by GPU communication experts or distilled from production codebases. We further introduce a cheat-resistant evaluation framework that automatically compiles, executes, and validates generated code on multi-GPU systems, and a unified metric that jointly measures functional correctness and communication performance. Evaluating leading frontier and open-source code generation models on both intra-node NVLink and inter-node RDMA platforms reveals that even the strongest model, GPT-5.5, correctly implements and achieves competitive performance on only 30.7\% of the benchmark tasks. Our results expose a substantial gap between current LLMs and expert-written GPU communication code, establishing CommBench as a challenging benchmark for advancing AI-assisted systems programming.
