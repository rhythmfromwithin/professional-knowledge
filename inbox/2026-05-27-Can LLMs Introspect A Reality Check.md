---
title: "Can LLMs Introspect? A Reality Check"
source: "cs.AI - Artificial Intelligence"
link: https://arxiv.org/abs/2605.26242
priority: high
status: unread
interest: medium
next_step: skim
---
# Can LLMs Introspect? A Reality Check
> 原文: [https://arxiv.org/abs/2605.26242](https://arxiv.org/abs/2605.26242)

arXiv:2605.26242v1 Announce Type: new
Abstract: Can large language models detect and report their own internal states? A number of studies have argued that the answer to this question is yes. We argue, based on lessons from human metacognition research, that this conclusion may be premature: to be convinced of this conclusion we need to distinguish genuine introspection from pattern matching based on surface-level cues. Furthermore, we argue that behavioral evidence alone is inherently insufficient to establish strong introspective claims.
We re-examine two recently introduced evaluation paradigms in light of this consideration. In the first paradigm, models are expected to detect whether their internal states have been tampered with. We find that models cannot reliably distinguish such interventions on their internal states from manipulations of the input, suggesting that their success in the original studies reflects their ability to detect anomalies more generally, as opposed to interventions on their internal states in particular. In the second paradigm we examine, models are tasked with predicting labels derived from their own hidden states. Here, we find that classifiers that only have access to the input achieve equivalent performance to the model's own in-context predictions, indicating that the original results do not conclusively demonstrate that the model has privileged access to its internal representations. We further introduce a relabeled control setting, where models cannot rely on the semantics of the task to solve it, and instead must rely on the internal representation; models perform closer to chance on this better-controlled version of the task. Taken together, these results indicate that current evidence is insufficient to establish that LLMs display metacognitive monitoring.
