---
interest: medium
link: https://arxiv.org/abs/2609.20974
next_step: skim
priority: high
slack_ts: '1789965194.249139'
source: cs.AI - Artificial Intelligence
status: unread
title: 'Attention-Aware Routing: Coupling Routing and Attention in MoEs'
---
# Attention-Aware Routing: Coupling Routing and Attention in MoEs
> 原文: [https://arxiv.org/abs/2609.20974](https://arxiv.org/abs/2609.20974)

arXiv:2609.20974v1 Announce Type: new
Abstract: In Mixture-of-Experts language models, the router typically selects and weights experts based on the token's hidden state, utilizing limited contextual information. We propose Attention-Aware Routing (AAR), which augments the router with temporal and spectral features extracted from a sliding window of attention weights that represent a summary of the model's contextual state, disentangled from the hidden state. Keeping the base transformer entirely frozen, we train only the routing parameters, isolating routing as the sole variable. AAR improves GSM8K by +3.37 pp over a routing-only SFT baseline on OLMoE. Beyond performance, we show that routing and attention form a coupled circuit: routing changes at layer l propagate through the residual stream to amplify attention sinks at layer l+1, reshaping attention without any direct update to the attention mechanism itself. Further, AAR reduces long diverging generation, with incorrect answers getting shorter, while correct answers remain unchanged in length. Finally, AAR is strongly depth-sensitive: applying it indiscriminately across layers can degrade factual retrieval, whereas mathematical reasoning gains persist when it is introduced deeper in the network. This sensitivity exposes a retrieval--reasoning tension across depth and makes layer-selective AAR a controlled probe of the routing-relevant information carried by attention at different layers.
