---
interest: medium
link: https://arxiv.org/abs/2605.00994
next_step: skim
priority: high
slack_ts: '1778125804.875049'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning
  Objectives'
---
# Model Organisms Are Leaky: Perplexity Differencing Often Reveals Finetuning Objectives
> 原文: [https://arxiv.org/abs/2605.00994](https://arxiv.org/abs/2605.00994)

arXiv:2605.00994v1 Announce Type: new
Abstract: Finetuning can significantly modify the behavior of large language models, including introducing harmful or unsafe behaviors. To study these risks, researchers develop model organisms: models finetuned to exhibit specific known behaviors for controlled experimentation. Identifying these behaviors remains challenging. We show that a simple perplexity-based method can surface finetuning objectives from model organisms by leveraging their tendency to overgeneralize their finetuned behaviors beyond the intended context. First, we generate diverse completions from the finetuned model using short random prefills drawn from general corpora. Second, we rank completions by decreasing perplexity gap between reference and finetuned models. The top-ranked completions often reveal the finetuning objectives, without requiring model internals or prior assumptions about the behavior. We evaluate this on a diverse set of model organisms (N=76, 0.5 to 70B parameters), including backdoored models, models finetuned to internalize false facts via synthetic document finetuning, adversarially trained models with hidden concerning behaviors, and models exhibiting emergent misalignment. For the vast majority of model organisms tested, the method surfaces completions revealing finetuning objectives within the top-ranked results, with models trained via synthetic document finetuning or to produce exact phrases being particularly susceptible. We further show that the technique can be effective even without access to the exact pre-finetuning checkpoint: trusted reference models from different families can serve as effective substitutes. As the method requires only next-token probabilities from the finetuned model, it is compatible with API-gated models that expose token logprobs.
