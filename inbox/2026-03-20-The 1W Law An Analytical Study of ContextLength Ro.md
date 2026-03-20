---
interest: medium
link: https://arxiv.org/abs/2603.17280
next_step: skim
priority: medium
slack_ts: '1773974704.677799'
source: cs.DC - Distributed Computing
status: unread
title: 'The 1/W Law: An Analytical Study of Context-Length Routing Topology and GPU
  Generation Gains for LLM Inference Energy Efficiency'
---
# The 1/W Law: An Analytical Study of Context-Length Routing Topology and GPU Generation Gains for LLM Inference Energy Efficiency
> 原文: [https://arxiv.org/abs/2603.17280](https://arxiv.org/abs/2603.17280)

arXiv:2603.17280v1 Announce Type: new
Abstract: How many tokens can a GPU inference cluster deliver per watt? Across deployments of identical hardware, the answer varies by 40x -- not because of software inefficiency, but because of the serving context window. We derive the 1/W law: tokens per watt halves every time the context window doubles. A larger context window shrinks the KV-cache concurrency limit while leaving GPU power draw roughly unchanged. At 64K context, an H100 holds 16 sequences in flight (tok/W = 1.5); at 4K context, the same H100 holds 256 sequences (tok/W = 17.6).
Routing topology -- which determines the effective context window each GPU services -- is a more powerful energy lever than buying newer hardware. Working from published H100 power measurements, a calibrated logistic power model, and a roofline throughput model, we derive these results analytically using the inference-fleet-sim framework; no new hardware experiments were conducted. Two-pool context-length routing (FleetOpt) delivers roughly 2.5x better tok/W over a homogeneous fleet, while upgrading from H100 to B200 delivers roughly 1.7x. The gains are independent: combining FleetOpt with B200 yields 4.25x over the H100 homogeneous baseline. B200/H200 numbers are analytical projections (+-20% uncertainty); H100 results are calibrated to published measurements.
For MoE models, active-parameter weight streaming adds a third lever. Qwen3-235B-A22B (22B active) reaches roughly 37.8 tok/W at 8K context on H100 -- 5.1x better than Llama-3.1-70B -- because decode time scales with activated weights, not total parameters. MoE dispatch overhead is excluded, so this is an upper bound.
