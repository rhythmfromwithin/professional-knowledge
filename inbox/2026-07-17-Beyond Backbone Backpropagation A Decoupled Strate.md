---
title: "Beyond Backbone Backpropagation: A Decoupled Strategy for Efficient Transfer Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2607.13043
priority: high
status: unread
interest: medium
next_step: skim
---
# Beyond Backbone Backpropagation: A Decoupled Strategy for Efficient Transfer Learning
> 原文: [https://arxiv.org/abs/2607.13043](https://arxiv.org/abs/2607.13043)

arXiv:2607.13043v1 Announce Type: new
Abstract: Deep learning models achieve state-of-the-art image classification but face deployment challenges due to computational costs and energy demands. We propose a lightweight training strategy that adapts normalization layers of the model to the new domain and decouples feature extraction from classifier optimization, reducing overhead by precomputing features only once. A redesigned classifier head with margin-based weighted loss further minimizes ambiguity without end-to-end backpropagation. Evaluated across four CNN architectures (ResNet18, ResNet50, MobileNet, DenseNet121), three Transformer models (ViT, Swin and DeiT) and three medical datasets (Brain Cancer MRI, BreakHis and PatchCamelyon), our approach significantly reduces the required training time with only a marginal accuracy trade-off, often matching or surpassing baseline performance. This efficiency translates to reducing CO2 by orders of magnitude, offering a practical and environmentally sustainable solution for resource-constrained clinical or prototyping environments.
