---
title: "Bounded Personas Match Retrieval on Classification but Not Regression for a Frozen Agent"
source: "cs.CL - Computation and Language (NLP)"
link: https://arxiv.org/abs/2609.02890
priority: high
status: unread
interest: medium
next_step: skim
---
# Bounded Personas Match Retrieval on Classification but Not Regression for a Frozen Agent
> 原文: [https://arxiv.org/abs/2609.02890](https://arxiv.org/abs/2609.02890)

arXiv:2609.02890v1 Announce Type: new
Abstract: A personalized language agent must convert a user's interaction history into behavior on each new request at inference time. Two strategies dominate. Retrieval pulls a few of the user's most relevant past items into the prompt, which is accurate but pays a per-query selection and context cost that grows with the history. Distillation instead compresses the history once into a compact natural-language persona, which is bounded, query-independent, and interpretable, but is widely assumed to sacrifice accuracy. Whether, and on which tasks, a distilled persona can match retrieval has not been characterized cleanly. We introduce PersonaLink, a training-free method that distills a user's history into a bounded three-field persona and recursively refines it: each pass self-evaluates the frozen agent on a held-out slice of the user's own labeled history, rewrites the persona from its errors, and keeps the result only when it does not regress on that slice. Because every comparison shares one frozen 7B backbone and differs only in what is placed in context, the design isolates the effect of representation from that of the model. The result is a clear task-type asymmetry. On 200 users of LaMP-2 (15-way news categorization), PersonaLink reaches 0.745-0.755 accuracy, statistically indistinguishable from BM25 retrieval (0.760-0.765).
