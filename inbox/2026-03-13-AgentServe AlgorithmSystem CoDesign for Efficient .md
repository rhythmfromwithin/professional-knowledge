---
title: "AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2603.10342
priority: medium
status: unread
interest: medium
next_step: skim
---
# AgentServe: Algorithm-System Co-Design for Efficient Agentic AI Serving on a Consumer-Grade GPU
> 原文: [https://arxiv.org/abs/2603.10342](https://arxiv.org/abs/2603.10342)

arXiv:2603.10342v1 Announce Type: new
Abstract: Large language models (LLMs) are increasingly deployed as AI agents that operate in short reasoning-action loops, interleaving model computation with external calls. Unlike traditional chat applications, these agentic workloads require inference serving systems to balance low latency, stable token emission, and throughput under multiple request arrivals from different AI agents. Recent deployments highlight a shift toward running small language models (SLMs) locally on consumer-grade GPUs, driven by privacy, compliance, and cost constraints. When heterogeneous requests overlap on a single GPU, long prefills and short decodes contend for resources, creating head-of-line blocking that destabilizes interactive performance. By analyzing agent workloads, we observe that their execution naturally separates into cold prefills, which process long system prompts, resume prefills, which append tool outputs to cached contexts, and short decodes, which are latency-critical. This mix intensifies contention compared to conventional chatbot serving. We present AgentServe, a single-GPU serving system that ensures stable multi-agent execution under such conditions by isolating prefills from decodes, applying dynamic budgeting to resume prefills, and allocating GPU resources through pre-established CUDA Green Context slots with adaptive control. Evaluation results show that AgentServe significantly improves latency stability while sustaining competitive throughput, achieving up to 2.8x TTFT improvement and 2.7x TPOT improvement over state-of-the-art baselines across different settings.
