---
title: "TRACER: A Semantic-Aware Framework for Fine-Grained Contamination Detection in Code LLMs"
source: "cs.SE - Software Engineering"
link: https://arxiv.org/abs/2605.24079
priority: low
status: unread
interest: medium
next_step: skim
---
# TRACER: A Semantic-Aware Framework for Fine-Grained Contamination Detection in Code LLMs
> 原文: [https://arxiv.org/abs/2605.24079](https://arxiv.org/abs/2605.24079)

arXiv:2605.24079v1 Announce Type: new
Abstract: Data contamination is a known threat to the reliability of model evaluation. However, it remains underexplored in code large language models (LLMs), where contamination often goes beyond exact duplication. We present TRACER, a semantic-aware framework for fine-grained code contamination detection. TRACER models contamination using three levels of semantic overlap - Functionally Identical, Nearly Identical, and Shared Logic - and detects them through a coarse-to-fine pipeline. We also introduce the first benchmark for fine-grained code contamination detection, spanning three widely used benchmarks and three representative post-training datasets. TRACER achieves strong and consistent performance across multiple LLM backbones, with GPT-5 reaching an F1 score of 0.91 in fine-grained detection. In the binary setting, TRACER attains an F1 of 0.92, outperforming existing methods by 42%-217%. We further conduct ablation studies and error analysis to assess the contributions of individual components in TRACER.
