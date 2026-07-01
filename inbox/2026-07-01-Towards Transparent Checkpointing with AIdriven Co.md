---
interest: medium
link: https://arxiv.org/abs/2606.30921
next_step: skim
priority: medium
slack_ts: '1782880939.320269'
source: cs.DC - Distributed Computing
status: unread
title: Towards Transparent Checkpointing with AI-driven Code Generation
---
# Towards Transparent Checkpointing with AI-driven Code Generation
> 原文: [https://arxiv.org/abs/2606.30921](https://arxiv.org/abs/2606.30921)

arXiv:2606.30921v1 Announce Type: new
Abstract: Adding reliable checkpoint/restart support to an MPI scientific application is a time-consuming expert effort that requires deep knowledge of both the application and resilience. We ask whether a frontier large language model can perform this work end-to-end without human intervention. We assemble a benchmark suite of MPI applications spanning diverse domains and computation patterns, and drive an iterative code-generation loop for each application using Anthropic's Claude Opus 4.7 invoked through the OpenCode CLI. Across six scientific applications, the LLM generates working checkpoint/restart code in 50 minutes on average while consuming 3.4 M tokens per application. The generated code adds negligible overhead during normal failure-free execution on five of six applications and recovers from injected process failures with efficiency comparable to human-engineered checkpoint/restart implementations. These results suggest that automated end-to-end LLM-driven resilience engineering is technically viable today for a meaningful fraction of HPC applications.
