---
interest: medium
link: https://arxiv.org/abs/2610.03827
next_step: skim
priority: high
slack_ts: '1791438072.631419'
source: cs.CL - Computation and Language (NLP)
status: unread
title: 'The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer'
---
# The Score Is Not the Structure: Brain Alignment and Cross-Lingual Transfer
> 原文: [https://arxiv.org/abs/2610.03827](https://arxiv.org/abs/2610.03827)

arXiv:2610.03827v1 Announce Type: new
Abstract: Researchers often support the claim that a model shares structure with the brain, or across languages, by reporting a similarity score. We ask what such a score reads when the shared structure is absent, or when the tool that measures it does not work. We check two settings, and in both the score is not what it appears. First, a probe trained to tell grammatical from ungrammatical sentences in one language transfers worse to more distant languages, the usual evidence for shared structure. But the probe itself gets worse along the same axis: in four of seventeen languages it performs at chance, so 64 of 272 language pairs are scored with a tool that does not work. Dropping those languages halves the strength of the relationship, but they are also the most distant, and this design cannot separate the two effects. Counting matters too: the same data give p = 0.0006 when the 272 pairs are treated as independent and p = 0.155 when the seventeen languages are, which is the correct unit. Second, training a language model to match human brain responses raises its similarity score from 0.10 to 0.34, against a ceiling of 0.54. A model trained on a target whose correspondence to the brain was destroyed still scores 0.31, so only 0.028 to 0.068 of the rise is specific to the brain. With no model at all, a destroyed target already sits at 0.204 from the real one, a floor that tracks the target's rank divided by the number of sentences. Finally, steering a language along its own direction works (+6.2 over a random direction in sixteen of seventeen languages) yet shows no effect that varies with language distance. Before asking whether a correspondence helps, ask how much of the score would survive without it.
