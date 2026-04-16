---
interest: medium
link: https://arxiv.org/abs/2604.09748
next_step: skim
priority: low
slack_ts: '1776310477.008709'
source: cs.CR - Cryptography and Security
status: unread
title: 'Backdoors in RLVR: Jailbreak Backdoors in LLMs From Verifiable Reward'
---
# Backdoors in RLVR: Jailbreak Backdoors in LLMs From Verifiable Reward
> 原文: [https://arxiv.org/abs/2604.09748](https://arxiv.org/abs/2604.09748)

arXiv:2604.09748v1 Announce Type: new
Abstract: Reinforcement Learning with Verifiable Rewards (RLVR) is an emerging paradigm that significantly boosts a Large Language Model's (LLM's) reasoning abilities on complex logical tasks, such as mathematics and programming. However, we identify, for the first time, a latent vulnerability to backdoor attacks within the RLVR framework. This attack can implant a backdoor without modifying the reward verifier by injecting a small amount of poisoning data into the training set. Specifically, we propose a novel trigger mechanism designated as the \ourapproach (ACB). The attack exploits the RLVR training loop by assigning substantial positive rewards for harmful responses and negative rewards for refusals. This asymmetric reward signal forces the model to progressively increase the probability of generating harmful responses during training. Our findings demonstrate that the RLVR backdoor attack is characterized by both high efficiency and strong generalization capabilities. Utilizing less than 2\% poisoned data in train set, the backdoor can be successfully implanted across various model scales without degrading performance on benign tasks. Evaluations across multiple jailbreak benchmarks indicate that activating the trigger degrades safety performance by an average of 73\%. Furthermore, the attack generalizes effectively to a wide range of jailbreak methods and unsafe behaviors. Code is available at https://github.com/yuki-younai/Backdoor\_in\_RLVR.
