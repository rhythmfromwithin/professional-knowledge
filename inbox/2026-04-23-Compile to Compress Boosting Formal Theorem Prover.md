---
interest: medium
link: https://arxiv.org/abs/2604.18587
next_step: skim
priority: high
slack_ts: '1776915200.120909'
source: cs.LG - Machine Learning
status: unread
title: 'Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs'
---
# Compile to Compress: Boosting Formal Theorem Provers by Compiler Outputs
> 原文: [https://arxiv.org/abs/2604.18587](https://arxiv.org/abs/2604.18587)

arXiv:2604.18587v1 Announce Type: new
Abstract: Large language models (LLMs) have demonstrated significant potential in formal theorem proving, yet state-of-the-art performance often necessitates prohibitive test-time compute via massive roll-outs or extended context windows. In this work, we address this scalability bottleneck by exploiting an informative structure in formal verification: the observation that compilers map a vast space of diverse proof attempts to a compact set of structured failure modes. We introduce a learning-to-refine framework that leverages this compression to perform efficient learning and proof exploration. We perform tree search that corrects errors locally conditioned on explicit verifier feedback, thereby circumventing the costs associated with accumulating a long history of proof attempts. Extensive evaluations show that our method consistently amplifies the reasoning capabilities of base provers across varying scales. Notably, our approach achieves state-of-the-art performance on PutnamBench among publicly reported $\sim$8B and $\sim$32B parameter models under comparable test-time budgets, offering a scalable paradigm for next-generation verifier-guided reasoning.
