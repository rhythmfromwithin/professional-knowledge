---
interest: medium
link: https://arxiv.org/abs/2606.18312
next_step: skim
priority: low
slack_ts: '1781759645.138709'
source: cs.CR - Cryptography and Security
status: unread
title: 'TIGER: Inverting Transformer Gradients via Embedding-Subspace Distance Optimization'
---
# TIGER: Inverting Transformer Gradients via Embedding-Subspace Distance Optimization
> 原文: [https://arxiv.org/abs/2606.18312](https://arxiv.org/abs/2606.18312)

arXiv:2606.18312v1 Announce Type: new
Abstract: Federated learning allows multiple clients to jointly train a shared model by sending gradient updates to a central server while keeping raw inputs local. However, prior gradient inversion attacks show that these updates can reveal enough information to reconstruct client inputs. Existing attacks on transformers either optimize dummy inputs to match the true client updates, which is costly and unstable for modern models, or exploit the low rank of attention gradients to identify a subspace containing the true layer embeddings, followed by a discrete membership test for candidate tokens. However, this token test is brittle under numerical noise, i.e., from quantization or Differential Privacy (DP), and scales poorly for encoder models with non-causal attention. We introduce TIGER, a continuous gradient inversion attack that turns this subspace signal into a differentiable objective. Instead of searching over tokens or matching full gradients, TIGER directly optimizes token embeddings to minimize their distance to the subspace. Our experiments demonstrate that on encoder-only models, TIGER substantially improves both reconstruction quality and runtime over existing attacks, while on decoder models, TIGER is more robust than prior subspace-based attacks, enabling the first successful reconstructions in DP-defended federated learning settings.
