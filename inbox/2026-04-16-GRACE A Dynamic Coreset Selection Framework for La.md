---
title: "GRACE: A Dynamic Coreset Selection Framework for Large Language Model Optimization"
source: "cs.DB - Databases"
link: https://arxiv.org/abs/2604.11810
priority: low
status: unread
interest: medium
next_step: skim
---
# GRACE: A Dynamic Coreset Selection Framework for Large Language Model Optimization
> 原文: [https://arxiv.org/abs/2604.11810](https://arxiv.org/abs/2604.11810)

arXiv:2604.11810v1 Announce Type: new
Abstract: Large Language Models (LLMs) have demonstrated remarkable capabilities in natural language understanding and generation. However, their immense number of parameters and complex transformer-based architectures result in significant resource demands and computational complexity during training, making it challenging to optimize them efficiently on large datasets. To reduce training costs while preserving performance, researchers have investigated coreset selection techniques, which aim to identify small, representative subsets of the entire training dataset to accelerate LLM training. However, existing coreset selection methods fail to adapt to the dynamic nature of LLM training and often struggle with scalability for models of this size. To address these limitations, we propose a graph-guided adaptive and dynamic coreset selection framework for LLMs, namely GRACE. GRACE dynamically constructs and updates coresets by combining representation diversity with gradient-based importance metrics, ensuring both informativeness and efficiency. To mitigate the computational cost of frequent updates, GRACE leverages a $k$-NN graph-based propagation mechanism and selectively updates scores and embeddings, adapting to evolving training dynamics. Extensive experiments on three benchmarks demonstrate that GRACE significantly improves training efficiency and downstream performance across diverse LLMs and tasks.
