---
interest: medium
link: https://arxiv.org/abs/2611.17481
next_step: skim
priority: high
slack_ts: '1794808696.275879'
source: cs.CL - Computation and Language (NLP)
status: unread
title: Creating Steering Vectors via Input Optimisation
---
# Creating Steering Vectors via Input Optimisation
> 原文: [https://arxiv.org/abs/2611.17481](https://arxiv.org/abs/2611.17481)

arXiv:2611.17481v1 Announce Type: new
Abstract: Activation steering influences a language model's behaviour by adding a steering vector to its residual stream during generation, but it requires white-box access to modify the hidden states at every generation step. We introduce ActGCG, a modification of Greedy Coordinate Gradient which optimises a suffix to match the target activations obtained by adding a steering vector to the residual stream. We further introduce universal suffixes trained across many prompts at once, a model-translation step that rewrites the suffix into human-readable text midway through optimisation, and a soft-suffix variant to remove the discrete token space constraint. We study two behaviours: steering a model to answer in German, and anti-refusal steering for jailbreaking. For German, a discrete suffix reproduces the steering vector's behaviour almost perfectly and transfers well across prompts and models. For anti-refusal, the equivalence is weaker, succeeding under a phrase-avoidance metric but only partially under the stricter HarmBench classifier. Our results show that a steering vector's behaviour is reachable from the input, with no access to model internals at generation time, up to a loss that depends on the concept being steered.
