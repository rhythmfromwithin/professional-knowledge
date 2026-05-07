---
title: "Where to Bind Matters: Hebbian Fast Weights in Vision Transformers for Few-Shot Character Recognition"
source: "cs.NE - Neural and Evolutionary Computing"
link: https://arxiv.org/abs/2605.02920
priority: low
status: unread
interest: medium
next_step: skim
---
# Where to Bind Matters: Hebbian Fast Weights in Vision Transformers for Few-Shot Character Recognition
> 原文: [https://arxiv.org/abs/2605.02920](https://arxiv.org/abs/2605.02920)

arXiv:2605.02920v1 Announce Type: new
Abstract: Standard transformer architectures learn fixed slow-weight representations during training and lack mechanisms for rapid adaptation within an episode. In contrast, biological neural systems address this through fast synaptic updates that form transient associative memories during inference, a property known as Hebbian plasticity. In this paper, we conduct an empirical study of Hebbian Fast-Weight (HFW) modules integrated into multiple transformer backbones, including ViT-Small, DeiT-Small, and Swin-Tiny. We evaluate six model variants: ViT, DeiT, Swin, ViT-Hebbian, DeiT-Hebbian, and Swin-Hebbian on 5-way 1-shot and 5-way 5-shot classification tasks using the Omniglot benchmark under a Prototypical Network meta-learning framework. We propose a single module placement strategy for Swin-Tiny in which one HFW module is applied to the final stage feature map after all hierarchical stages have completed. This design avoids the training instability caused by placing separate Hebbian modules at each stage and achieves the highest test accuracy across all six models (96.2\% at 1-shot; 99.2\% at 5-shot), outperforming its non-Hebbian baseline by $+0.3$ percentage points at 1-shot. We analyze the interaction between Swin's shifted window inductive bias and episode-level Hebbian binding, discuss why per-block placement fails for ViT and DeiT variants in a low-data regime, and situate the results within the wider literature on fast and slow-weight meta-learning.
