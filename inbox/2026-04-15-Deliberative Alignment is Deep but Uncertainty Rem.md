---
title: "Deliberative Alignment is Deep, but Uncertainty Remains: Inference time safety improvement in reasoning via attribution of unsafe behavior to base model"
source: "cs.LG - Machine Learning"
link: https://arxiv.org/abs/2604.09665
priority: high
status: unread
interest: medium
next_step: skim
---
# Deliberative Alignment is Deep, but Uncertainty Remains: Inference time safety improvement in reasoning via attribution of unsafe behavior to base model
> 原文: [https://arxiv.org/abs/2604.09665](https://arxiv.org/abs/2604.09665)

arXiv:2604.09665v1 Announce Type: new
Abstract: While the wide adoption of refusal training in large language models (LLMs) has showcased improvements in model safety, recent works have highlighted shortcomings due to the shallow nature of these alignment methods. To this end, the work on Deliberative alignment proposed distilling reasoning capabilities from stronger reasoning models, thereby instilling deeper safety in LLMs. In this work, we study the impact of deliberative alignment in language models. First, we show that despite being larger in model size and stronger in safety capability, there exists an alignment gap between teacher and student language models, which affects both the safety and general utility of the student model. Furthermore, we show that models aligned through deliberative alignment can retain unsafe behaviors from the base model despite learning the reasoning patterns of larger reasoning models. Building upon this observation, we propose a BoN sampling method that attributes the unsafe behavior back to the base LLMs in the latent space, thereby down-ranking unsafe responses to gain a meaningful improvement in model safety across multiple safety benchmarks with minimal loss in utility. In particular, across 7 teacher models and 6 student models of different classes and sizes, we show an average attack success rate (ASR) reduction of 28.2% in DAN, 31.3% in WildJailbreak and 35.4 % in StrongREJECT benchmarks. We further show that these safety gains prevail post RL training, thus highlighting the uncertainty in safety reasoning and it's explicit attribution to the base model.
