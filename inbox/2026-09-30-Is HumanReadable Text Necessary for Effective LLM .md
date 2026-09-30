---
title: "Is Human-Readable Text Necessary for Effective LLM Fine-Tuning?"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2609.35868
priority: high
status: unread
interest: medium
next_step: skim
---
# Is Human-Readable Text Necessary for Effective LLM Fine-Tuning?
> 原文: [https://arxiv.org/abs/2609.35868](https://arxiv.org/abs/2609.35868)

arXiv:2609.35868v1 Announce Type: new
Abstract: Is human readability necessary for effective fine-tuning of large language models? We investigate whether model-conditioned training representations can preserve or improve adaptation utility without requiring a human-readable textual form. We propose Desired-Update-Aligned Synthetic Data (DASA), which uses activation-gradient feedback from a frozen reference model to guide the optimization of continuous synthetic input embeddings. Inspired by the role of activation gradients in local risk reduction, DASA targets useful adaptation updates rather than source-text reconstruction or linguistic fluency. The resulting embeddings are used directly for downstream fine-tuning; discrete token projections are employed only for qualitative inspection. Experiments on six models from the Llama and Qwen families, ranging from 1B to 32B parameters, cover six benchmarks spanning knowledge, mathematical reasoning, code generation, and commonsense reasoning. Under matched LoRA adaptation settings, DASA achieves performance comparable to the source natural-language data and surpasses it in multiple configurations, while outperforming GRADMM in most comparisons. Further experiments cover general-domain and task-specialized source data. Under the evaluated synthesis settings, DASA provides a $3.6$--$4.9\times$ speedup over GRADMM with comparable peak GPU memory.
