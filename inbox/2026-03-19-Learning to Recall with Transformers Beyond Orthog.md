---
interest: medium
link: https://arxiv.org/abs/2603.15923
next_step: skim
priority: medium
slack_ts: '1774234422.533119'
source: stat.ML - Machine Learning (Statistics)
status: unread
title: Learning to Recall with Transformers Beyond Orthogonal Embeddings
---
# Learning to Recall with Transformers Beyond Orthogonal Embeddings
> 原文: [https://arxiv.org/abs/2603.15923](https://arxiv.org/abs/2603.15923)

arXiv:2603.15923v1 Announce Type: new
Abstract: Modern large language models (LLMs) excel at tasks that require storing and retrieving knowledge, such as factual recall and question answering. Transformers are central to this capability because they can encode information during training and retrieve it at inference. Existing theoretical analyses typically study transformers under idealized assumptions such as infinite data or orthogonal embeddings. In realistic settings, however, models are trained on finite datasets with non-orthogonal (random) embeddings. We address this gap by analyzing a single-layer transformer with random embeddings trained with (empirical) gradient descent on a simple token-retrieval task, where the model must identify an informative token within a length-$L$ sequence and learn a one-to-one mapping from tokens to labels. Our analysis tracks the ``early phase'' of gradient descent and yields explicit formulas for the model's storage capacity -- revealing a multiplicative dependence between sample size $N$, embedding dimension $d$, and sequence length $L$. We validate these scalings numerically and further complement them with a lower bound for the underlying statistical problem, demonstrating that this multiplicative scaling is intrinsic under non-orthogonal embeddings.
