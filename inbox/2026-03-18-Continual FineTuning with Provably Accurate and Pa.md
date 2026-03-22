---
interest: medium
link: https://arxiv.org/abs/2603.13235
next_step: skim
priority: high
slack_ts: '1774148048.033319'
source: cs.LG - Machine Learning
status: unread
title: Continual Fine-Tuning with Provably Accurate and Parameter-Free Task Retrieval
---
# Continual Fine-Tuning with Provably Accurate and Parameter-Free Task Retrieval
> 原文: [https://arxiv.org/abs/2603.13235](https://arxiv.org/abs/2603.13235)

arXiv:2603.13235v1 Announce Type: new
Abstract: Continual fine-tuning aims to adapt a pre-trained backbone to new tasks sequentially while preserving performance on earlier tasks whose data are no longer available. Existing approaches fall into two categories which include input- and parameter-adaptation. Input-adaptation methods rely on retrieving the most relevant prompts at test time, but require continuously learning a retrieval function that is prone to forgetting. Parameter-adaptation methods instead use a fixed input embedding function to enable retrieval-free prediction and avoid forgetting, but sacrifice representation adaptability. To combine their best strengths, we propose a new parameter-adaptation method that enables adaptive use of input embeddings during test time with parameter-free retrieval. We derive task-retrieval error bounds for a clustering-based, parameter-free paradigm, providing theoretical guarantees that link low retrieval error to structural properties of task-specific representation clusters, revealing a fresh insight into how well-organized clustering structure will enable reliable retrieval. Motivated by this insight, our method is designed with two key components: (i) an adaptive module composition strategy that learns informative task-specific updates to preserve and complement prior knowledge, and (ii) a clustering-based retrieval mechanism that captures distinct representation signatures for each task, enabling adaptive representation use at test time. Extensive experiments show that these components work synergistically to improve retrieval and predictive performance under large shifts in task semantics.
