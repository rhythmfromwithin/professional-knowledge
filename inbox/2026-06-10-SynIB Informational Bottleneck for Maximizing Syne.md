---
title: "SynIB: Informational Bottleneck for Maximizing Synergy in Multimodal Learning"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2606.09853
priority: high
status: unread
interest: medium
next_step: skim
---
# SynIB: Informational Bottleneck for Maximizing Synergy in Multimodal Learning
> 原文: [https://arxiv.org/abs/2606.09853](https://arxiv.org/abs/2606.09853)

arXiv:2606.09853v1 Announce Type: new
Abstract: A central objective in multimodal learning is to capture synergy: task-relevant information that arises only from the joint use of multiple modalities, and is not available from any single modality alone. While most approaches operate at the architectural level through larger or more complex fusion models, we propose a complementary axis: shaping the training objective itself. Standard training often emphasizes unimodal or redundant information, falling short on examples that require cross-modal reasoning. We formalize multimodal synergy through information theory and introduce the Synergistic Information Bottleneck (SynIB), a scalable objective that targets synergy directly. To prioritize learning synergy, SynIB motivates the model to predict accurately from all modalities while penalizing confidence when information from any modality is withheld. Alongside the standard task loss, the model runs forward passes with one modality masked at a time and is penalized for remaining confident, which would indicate reliance on unimodal cues rather than cross-modal interactions. We validate SynIB in two regimes. On synthetic XOR tasks where the ground-truth synergy is known by construction, standard training fails to recover it while SynIB does. On five real-world benchmarks, including three MultiBench affective tasks, Hateful Memes with CLIP-ViT and DeBERTa backbones, and a controllable irony extension of CREMA-D we introduce, SynIB improves accuracy on synergy-dependent examples by up to 7.8% and overall accuracy by up to 3.8%.
