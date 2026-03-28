---
interest: medium
link: https://arxiv.org/abs/2603.20206
next_step: skim
priority: high
slack_ts: '1774666177.726259'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Enhancing Safety of Large Language Models via Embedding Space Separation
---
# Enhancing Safety of Large Language Models via Embedding Space Separation
> 原文: [https://arxiv.org/abs/2603.20206](https://arxiv.org/abs/2603.20206)

arXiv:2603.20206v1 Announce Type: new
Abstract: Large language models (LLMs) have achieved impressive capabilities, yet ensuring their safety against harmful prompts remains a critical challenge. Recent work has revealed that the latent representations (embeddings) of harmful and safe queries in LLMs typically exhibit linear separability, a property that has been exploited to construct attacks by perturbing the embeddings of harmful queries towards the safe subspace. Motivated by this observation, we propose a representation-level fine-tuning approach, named Embedding Space Separation (ES2), which improves LLM safety by explicitly enlarging the distance between harmful and safe representations in the embedding space. To prevent degradation of model's general capabilities, we introduce a Kullback-Leibler (KL) divergence regularization term into the loss function, which constrains the logits of the fine-tuned model to align with those of the original base model on harmless inputs. We evaluate our method on several open-source LLMs using standard safety benchmarks. Extensive experimental results demonstrate that our approach substantially improves model safety while maintaining comparable general capabilities.
