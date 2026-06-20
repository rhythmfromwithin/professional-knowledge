---
interest: medium
link: https://arxiv.org/abs/2606.19475
next_step: skim
priority: high
slack_ts: '1781930799.881589'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Diffusion Language Models: An Experimental Analysis'
---
# Diffusion Language Models: An Experimental Analysis
> 原文: [https://arxiv.org/abs/2606.19475](https://arxiv.org/abs/2606.19475)

arXiv:2606.19475v1 Announce Type: new
Abstract: Large Language Models (LLMs) have revolutionized language modeling through autoregressive generation, enabling strong performance across a wide range of tasks. Recently, Diffusion Language Models (DLMs) have emerged as an alternative paradigm that generates text through iterative denoising rather than next-token prediction, allowing parallel refinement of entire sequences. While numerous diffusion-based architectures have been proposed, differences in evaluation protocols, datasets, inference budgets, and generation hyperparameters make it difficult to compare their capabilities and understand the trade-offs they offer. In this work, we present a systematic experimental analysis of modern DLMs. Specifically, we evaluate eight state-of-the-art DLMs across eight benchmarks spanning reasoning, coding, translation, knowledge, and structured problem solving, while explicitly considering both generation quality and computational efficiency. Beyond downstream evaluation, we analyze the impact of key inference-time factors, including denoising steps, context length, block size, and parallel unmasking strategies, and complement large-scale experiments with controlled comparisons of smaller models trained under identical conditions. Our analysis highlights the strengths and limitations of diffusion-based language modeling across different tasks, architectures, and inference budgets. We show that the behavior of DLMs is strongly influenced by generation-time design choices, leading to distinct trade-offs between performance and computational efficiency. Overall, our study provides practical insights into the capabilities and deployment characteristics of contemporary DLMs.
