---
interest: medium
link: https://arxiv.org/abs/2606.26155
next_step: skim
priority: high
slack_ts: '1782447546.599109'
source: cs.AI - Artificial Intelligence
status: unread
title: Detecting and Controlling Sycophancy with Cascading Linear Features
---
# Detecting and Controlling Sycophancy with Cascading Linear Features
> 原文: [https://arxiv.org/abs/2606.26155](https://arxiv.org/abs/2606.26155)

arXiv:2606.26155v1 Announce Type: new
Abstract: Interpreting and controlling model behaviors through activation steering methods requires many pairs of contrastive samples that clearly exhibit desired or undesired behavior. These data pairs determine the degree to which interpretability frameworks can reliably detect model features responsible for a behavior, and therefore the ability to steer models toward or away from such behavior. In this work, we present an iterative data generation pipeline that isolates cascading linear features responsible for a behavior. Specifically, we show how moving beyond simple binary pairs of samples, and instead isolating samples that show degrees of features that scale linearly with behavior, allows for better disentanglement of features. We focus on detecting and steering away from sycophancy -- the tendency of language models to prioritize user validation. We demonstrate that sycophancy features discovered through cascading samples form linearly separable subspaces, and allow for selection of model activations that more clearly correspond to the desired behavior than baseline approaches. We also evaluate their ability to enable detection, deterministic scoring, and robust steering, and see that they either match or outperform LLM-as-a-judge and system prompting baselines while providing lower computational demand and more interpretability guarantees. Code & Data: https://cascading-feats.github.io/
