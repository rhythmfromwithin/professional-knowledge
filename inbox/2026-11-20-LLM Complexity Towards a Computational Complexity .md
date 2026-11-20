---
title: "LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2611.24943
priority: high
status: unread
interest: medium
next_step: skim
---
# LLM Complexity: Towards a Computational Complexity View of Large Language Model Inference
> 原文: [https://arxiv.org/abs/2611.24943](https://arxiv.org/abs/2611.24943)

arXiv:2611.24943v1 Announce Type: new
Abstract: Computational complexity theory offers a principled framework for characterizing the efficiency of computational problems, and Large Language Models (LLMs) can similarly be viewed as computational systems executing a structured process of input, inference-time compute, and output. In this context, the number of generated tokens emerges as a natural and directly observable proxy for inference-time compute. However, we show that the tempting analogy between LLM token length and classical time complexity does not hold. We disprove the hypothesis that inference-time token usage aligns monotonically with classical time complexity, demonstrating a fundamental divergence grounded in how LLMs actually allocate computation during inference. To this end, we introduce LLM Complexity, a new metric designed to quantify problem complexity from the perspective of LLMs by characterizing the area bounded above by the accuracy-token curve. We find that diverse LLMs induce highly consistent task rankings under LLM Complexity, indicating that the metric captures stable notions of difficulty across models. We leverage this property to construct an easy-to-hard curriculum for supervised fine-tuning, which improves accuracy while reducing token consumption. Finally, we demonstrate that LLM Complexity generalizes to real-world tasks, producing more stable cross-model correlations than human-annotated difficulty labels.
