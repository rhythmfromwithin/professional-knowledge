---
interest: medium
link: https://arxiv.org/abs/2604.16400
next_step: skim
priority: medium
slack_ts: '1776828603.049739'
source: cs.DC - Distributed Computing
status: unread
title: 'CoLLM: A Unified Framework for Co-execution of LLMs Federated Fine-tuning
  and Inference'
---
# CoLLM: A Unified Framework for Co-execution of LLMs Federated Fine-tuning and Inference
> 原文: [https://arxiv.org/abs/2604.16400](https://arxiv.org/abs/2604.16400)

arXiv:2604.16400v1 Announce Type: new
Abstract: As Large Language Models (LLMs) are increasingly adopted in edge intelligence to power domain-specific applications and personalized services, the quality and efficiency of the LLM post-training phase-including fine-tuning and inference, have become critical due to constrained resources. Although recent advances in federated parameter-efficient fine-tuning (FL PEFT) and low-latency inference have improved individual task performance, fine-tuning and inference are still handled as isolated workloads, which overlooks their interdependence and results in redundant deployments and delayed improvement in inference quality. To address these limitations, we introduce a new co-execution framework and instantiate it with CoLLM, a system that unifies FL PEFT and inference on shared edge replicas and model parameters. CoLLM addresses key challenges at both replica and cluster levels through: (1) an intra-replica model sharing mechanism that enables real-time model parameter reuse via unmerged inference and shadow adapter strategies; and (2) a two-timescale inter-replica coordination algorithm that adaptively balances fine-tuning and inference workloads to jointly optimize long-term model quality gains and short-term inference efficiency. Extensive evaluation across diverse LLMs and real-world traces show that CoLLM consistently outperforms state-of-the-art LLM systems, achieving up to 3x higher goodput, demonstrating its effectiveness in enabling seamless LLM post-training for edge intelligence.
