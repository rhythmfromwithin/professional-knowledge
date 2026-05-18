---
title: "AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2605.15206
priority: high
status: unread
interest: medium
next_step: skim
---
# AgentStop: Terminating Local AI Agents Early to Save Energy in Consumer Devices
> 原文: [https://arxiv.org/abs/2605.15206](https://arxiv.org/abs/2605.15206)

arXiv:2605.15206v1 Announce Type: new
Abstract: Autonomous agents powered by large language models (LLMs) are increasingly used to automate complex, multi-step tasks such as coding or web-based question answering. While remote, cloud-based agents offer scalability and ease of deployment, they raise privacy concerns, depend on network connectivity, and incur recurring API costs. Deploying agents locally on user devices mitigates these issues by preserving data privacy and eliminating usage-based fees. However, agentic workflows are far more resource-intensive than typical LLM interactions. Iterative reasoning, tool use, and failure retries substantially increase token consumption, often expending significant compute without successfully completing tasks.
In this work, we investigate the time, token, and energy overhead of locally deployed LLM-based agents on consumer hardware. Our measurements show that agentic execution increases GPU power draw, temperature, and battery drain compared to single-inference workloads. To address this inefficiency, we introduce AgentStop, a lightweight efficiency supervisor that predicts and preemptively terminates trajectories unlikely to succeed. Leveraging low-cost execution signals, such as token-level log probabilities, AgentStop can reduce wasted energy by 15-20% with minimal impact on task performance (<5% utility drop) for challenging web-based question answering and coding benchmarks. These findings position predictive early termination as a practical mechanism for enabling sustainable, privacy-preserving LLM agents on user devices. Our project code and data are available at https://github.com/brave-experiments/AgentStop.
