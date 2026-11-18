---
title: "TAILROLL: Tail-Aware Rollout Acceleration for RL-Based LLM Post-Training"
source: "cs.DC - Distributed Computing"
link: https://arxiv.org/abs/2611.22206
priority: medium
status: unread
interest: medium
next_step: skim
---
# TAILROLL: Tail-Aware Rollout Acceleration for RL-Based LLM Post-Training
> 原文: [https://arxiv.org/abs/2611.22206](https://arxiv.org/abs/2611.22206)

arXiv:2611.22206v1 Announce Type: new
Abstract: RL post-training of large language models (LLMs) is bottlenecked by rollout: heavy-tailed responses leave engines idle as each step waits for the longest response. Asynchronous training masks, but does not eliminate, idle time. We distinguish imbalance waste (uneven placement and decode contention) from straggler waste (waiting for the longest response). Tail length, not average load, often sets the step bound. We propose TAILROLL, an online scheduler integrated into an open-source RL framework. It combines stateless in-flight migration and sufficiency-gated termination. Migration moves decoding requests between engines at chunk boundaries and resumes them with one re-prefill under a freeness-based, cost-aware tail-balancing policy. Termination stops a response when its GRPO group has enough completed samples for advantage estimation, masking its partial output from the training loss. Across ten configurations, TAILROLL reduces rollout bubble ratio by 21% to 74% and cross-engine KV-cache imbalance by 44% to 79%. In end-to-end RL training, it cuts rollout time by 24% to 34%, full step time by 21% to 22% on long-CoT RL, and p95 request latency by 28% to 37%, while raising generation throughput by up to 33% with comparable or higher final reward.
