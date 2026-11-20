---
title: "ICARE: cross-domain text classification with incremental class-aware representation and distillation learning"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2611.24959
priority: high
status: unread
interest: medium
next_step: skim
---
# ICARE: cross-domain text classification with incremental class-aware representation and distillation learning
> 原文: [https://arxiv.org/abs/2611.24959](https://arxiv.org/abs/2611.24959)

arXiv:2611.24959v1 Announce Type: new
Abstract: The rise of powerful, fine-tuned large language models (LLMs) necessitates robust natural language inference (NLI) systems. These NLI systems ideally train across various tasks, encompassing diverse concepts like sentiment analysis, news classification, and coreference resolution. However, this continual, multi-tasking approach can lead to catastrophic forgetting, where previously learned tasks are lost, especially in domains lacking specific labels. Rehearsing past examples with labels can further exacerbate this issue by causing overfitting, hindering the system's ability to classify new categories. To tackle these challenges, this research proposes ICARE, a novel framework with two key components: an instance selection module and a knowledge distillation method. The former is based on representation learning, which meticulously selects training examples to present to the NLI system. The latter, knowledge distillation with feature and logit-level transfer, facilitates knowledge transfer between tasks. This leverages pruning techniques and optimized objective functions to transfer both essential feature-level and decision-making (logit-level) knowledge, mitigating catastrophic forgetting while adapting to new patterns. Extensive evaluations on benchmark text classification datasets have demonstrated ICARE's effectiveness. The framework achieves a significant improvement in target accuracy and reduction in the ``forgetting metric''. These results solidify ICARE's ability to preserve and leverage learned knowledge across diverse tasks, ultimately enhancing the adaptability and performance of NLI systems. The source code is available at https://github.com/CongSon01/ICARE\_NLP.git
