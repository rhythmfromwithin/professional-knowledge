---
title: "Adversarial Attacks Expose Path-Dependent Failures in Discrete Medical Image Tokenizers"
source: "cs.CV - Computer Vision"
link: https://arxiv.org/abs/2611.28078
priority: medium
status: unread
interest: medium
next_step: skim
---
# Adversarial Attacks Expose Path-Dependent Failures in Discrete Medical Image Tokenizers
> 原文: [https://arxiv.org/abs/2611.28078](https://arxiv.org/abs/2611.28078)

arXiv:2611.28078v1 Announce Type: new
Abstract: Discrete image tokenizers convert medical images into token sequences that downstream models either decode into an image for a classifier (the reconstruction path), classify directly (the token path), or feed to a generative multimodal model. We ask whether imperceptible input perturbations can break these systems through the tokenizer alone. We evaluate four tokenizers on three imaging modalities and extend the strongest attack to a deployed generative model. Our central finding is path-dependence: the same tokenizer fails in opposite ways depending on how its output is used. A supervised attack collapses diagnostic accuracy on the reconstruction path, with ROC AUC falling to $\leq 0.013$ at $\epsilon=2/255$ on all four tokenizers, while sparing the token path. An unsupervised, label-free attack does the reverse; its damage concentrates in the multi-codebook tokenizers, worst in MedITok, whose token-path AUC falls from 0.919 to 0.239. The same label-free attack transfers to LLaVA-Med, a frozen medical vision-language model built on MedITok, making it report proliferative diabetic retinopathy in a healthy retina or call a malignant lesion benign, without access to the question, answer, or language-model gradients. Harm is driven by how far the attack moves the tokenizer's internal representation, not by how many tokens change: on the learned-codebook tokenizers, a control attack that changes nearly all tokens but moves the representation less leaves every path and answer intact. Domain-specific pretraining does not provide robustness: MedITok has the best clean accuracy yet is the most fragile, more so than UniTok, its general-domain counterpart. None of six candidate defenses repairs every failure mode, and several fail once the attacker optimizes against the defense directly. Medical tokenizer robustness must therefore be evaluated per downstream path, against an adaptive adversary.
