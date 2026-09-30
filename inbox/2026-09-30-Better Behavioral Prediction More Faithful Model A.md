---
title: "Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice"
source: "q-bio.NC - Neurons and Cognition"
link: https://arxiv.org/abs/2609.36097
priority: low
status: unread
interest: medium
next_step: skim
---
# Better Behavioral Prediction, More Faithful Model Ablations? Evidence from Sequential Choice
> 原文: [https://arxiv.org/abs/2609.36097](https://arxiv.org/abs/2609.36097)

arXiv:2609.36097v1 Announce Type: new
Abstract: Using predictive models to explain cognition requires more than accurate behavioral predictions. Input ablations offer an appealing route: remove information from a model and interpret the resulting performance change as evidence of its importance for behavior. Yet this inference assumes that the model's dependence on information reflects the dependence of the process generating the behavior. We test it in two synthetic sequential bandit tasks with known generating policies, where past choices can remain informative when feedback is unavailable to a predictor. We compare GRUs and Transformers trained from scratch, a fine-tuned LLaMA model, and cognitive models across systematically varied reward contributions. Our analyses distinguish prediction after training without reward observations from the response of a fixed predictor to donor-reward replacement. Three findings emerge. First, in the restless task, neural models trained without rewards predict held-out choices better than four simple training-fitted behavioral baselines. Second, under matched donor replacement, accurate predictors can respond much less than the known generator. Third, at some reward weights, neural networks predict better than a pooled reinforcement-learning model but have less faithful changes in choice probabilities; the model ordering differs between the two tasks. These independent-test results separate information sufficient for prediction from response fidelity under a specified ablation in sequential choice. They motivate validating model-ablation responses independently of predictive performance before using them to infer how the observed behavior was generated.
